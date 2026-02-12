import os
import sys

# Path to publisher.py
luma_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'Luma'))
publisher_path = os.path.join(luma_path, 'luma_core', 'agents', 'publisher.py')

if not os.path.exists(publisher_path):
    print(f"Error: Could not find publisher.py at {publisher_path}")
    sys.exit(1)

with open(publisher_path, 'r') as f:
    content = f.read()

# 1. Inject Screenshot Logic
target_str = '            template_content = f.read()'
injection_code = """
    # B2. Check for Screenshots
    import glob
    feature_id = str(state.get('issue_data', {}).get('number', ''))
    screenshots_info = ""
    
    if feature_id:
        # Search for docs/features/*{feature_id}*
        search_pattern = os.path.join(target_dir, "docs", "features", f"*{feature_id}*")
        matches = glob.glob(search_pattern)
        
        if matches:
            feature_path = matches[0]
            screenshots_dir = os.path.join(feature_path, "screenshots")
            if not os.path.exists(screenshots_dir):
                 try:
                     os.makedirs(screenshots_dir, exist_ok=True)
                 except: pass
            
            # Check for files
            def get_images():
                pngs = glob.glob(os.path.join(screenshots_dir, "*.png"))
                jpgs = glob.glob(os.path.join(screenshots_dir, "*.jpg"))
                jpegs = glob.glob(os.path.join(screenshots_dir, "*.jpeg"))
                return pngs + jpgs + jpegs

            all_screens = get_images()
            
            # Interactive wait if empty
            if not all_screens and not state.get('auto_approve', False):
                print(f"\\n📸 No screenshots found in: {screenshots_dir}")
                print("   Please add screenshots now to help the LLM write a better PR description.")
                inp = input("   Press Enter after adding screenshots (or 's' to skip)...").strip().lower()
                if inp != 's':
                    all_screens = get_images()
            
            if all_screens:
                screenshots_info = "\\nSCREENSHOTS_AVAILABLE:\\n"
                screenshots_info += "The following screenshots are available. Please EMBED them in the PR description using markdown like `![Description](relative/path/to/image.png)` or `<img src=\\"relative/path/to/image.png\\" width=\\"300\\" />`. Pick the most relevant ones.\\n"
                for s in all_screens:
                    rel_path = os.path.relpath(s, target_dir)
                    screenshots_info += f"- {rel_path}\\n"
"""

if target_str in content:
    content = content.replace(target_str, target_str + injection_code)
    print("Injected screenshot logic.")
else:
    print("Error: Could not find target string for injection.")
    sys.exit(1)

# 2. Update Prompt
prompt_target = 'GIT CONTEXT:\n{git_stats}\n\nPR TEMPLATE:'
prompt_replacement = 'GIT CONTEXT:\n{git_stats}\n{screenshots_info}\n\nPR TEMPLATE:'

if prompt_target in content:
    content = content.replace(prompt_target, prompt_replacement)
    print("Updated prompt template.")
else:
    print("Error: Could not find prompt target string.")
    # Fallback to loose match if whitespace differs
    loose_target = 'GIT CONTEXT:\n{git_stats}'
    if loose_target in content:
         content = content.replace(loose_target, loose_target + '\n{screenshots_info}')
         print("Updated prompt template (loose match).")
    else:
         sys.exit(1)

# Write back
with open(publisher_path, 'w') as f:
    f.write(content)

print(f"Successfully patched {publisher_path}")
