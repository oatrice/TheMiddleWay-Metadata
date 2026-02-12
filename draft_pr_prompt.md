# PR Draft Prompt

You are an AI assistant helping to create a Pull Request description.
    
TASK: [Feature] Onboarding: Welcome Screen & "Authentic Wisdom" Introduction
ISSUE: {
  "title": "[Feature] Onboarding: Welcome Screen & \"Authentic Wisdom\" Introduction",
  "number": 11,
  "body": ""
}

GIT CONTEXT:
COMMITS:
0e83429 docs(onboarding): add feature planning documentation for v0.8.0
befb066 docs(roadmap): prioritize user authentication as top priority
0b28a84 ✨ feat(onboarding): Implement welcome screen and intro flow

STATS:
.luma_state.json                                   |  16 +-
 CHANGELOG.md                                       |   7 +
 ROADMAP.md                                         |  34 +-
 VERSION                                            |   2 +-
 code_review.md                                     |  94 +++++-
 create_ios_assets.py                               |  68 ++++
 .../analysis.md                                    | 258 +++++++++++++++
 .../antigravity1/implementation_plan.md            |  79 +++++
 .../antigravity1/task.md                           |  29 ++
 .../antigravity1/walkthrough.md                    |  48 +++
 .../plan.md                                        | 159 ++++++++++
 .../spec.md                                        |  98 ++++++
 .../specs/sbe_issue-11.md                          |  54 ++++
 prompt_android.txt                                 | 347 +++++++++------------
 prompt_backend.txt                                 | 347 +++++++++------------
 prompt_frontend.txt                                | 347 +++++++++------------
 prompt_ios.txt                                     | 347 +++++++++------------
 17 files changed, 1538 insertions(+), 796 deletions(-)

KEY FILE DIFFS:
diff --git a/create_ios_assets.py b/create_ios_assets.py
new file mode 100644
index 0000000..4d09bd7
--- /dev/null
+++ b/create_ios_assets.py
@@ -0,0 +1,68 @@
+import os
+import shutil
+import json
+
+# Configuration
+SOURCE_DIR = "/Users/oatrice/.gemini/antigravity/brain/c183d02e-5e38-4deb-8507-6431ec20a2f5"
+TARGET_DIR = "Platforms/iOS/TheMiddleWay/Resources/Assets.xcassets"
+
+# Map source filename to asset name
+ASSETS = {
+    "onboarding_welcome_logo_1770896268486.png": "onboarding_welcome",
+    "onboarding_authentic_wisdom_1770896292368.png": "onboarding_wisdom",
+    "onboarding_discover_path_1770896310277.png": "onboarding_path",
+    "onboarding_daily_practice_1770896329650.png": "onboarding_practice"
+}
+
+def create_imageset(source_path: str, asset_name: str) -> None:
+    imageset_dir = os.path.join(TARGET_DIR, f"{asset_name}.imageset")
+    os.makedirs(imageset_dir, exist_ok=True)
+
+    # Copy file (using 3x for simplicity as High Res, or 2x, or Universal)
+    target_file = "image.png"
+    shutil.copy(source_path, os.path.join(imageset_dir, target_file))
+
+    # Create Contents.json
+    contents = {
+        "images": [
+            {
+                "filename": target_file,
+                "idiom": "universal",
+                "scale": "1x"
+            },
+            {
+                "filename": target_file,
+                "idiom": "universal",
+                "scale": "2x"
+            },
+            {
+                "filename": target_file,
+                "idiom": "universal",
+                "scale": "3x"
+            }
+        ],
+        "info": {
+            "author": "xcode",
+            "version": 1
+        }
+    }
+    
+    with open(os.path.join(imageset_dir, "Contents.json"), "w") as f:
+        json.dump(contents, f, indent=2)
+
+    print(f"Created {asset_name}.imageset")
+
+def main() -> None:
+    if not os.path.exists(TARGET_DIR):
+        print(f"Target directory {TARGET_DIR} does not exist.")
+        return
+
+    for src_file, asset_name in ASSETS.items():
+        src_path = os.path.join(SOURCE_DIR, src_file)
+        if os.path.exists(src_path):
+            create_imageset(src_path, asset_name)
+        else:
+            print(f"Source file not found: {src_path}")
+
+if __name__ == "__main__":
+    main()


PR TEMPLATE:


INSTRUCTIONS:
1. Generate a comprehensive PR description in Markdown format.
2. If a template is provided, fill it out intelligently.
3. If no template, use a standard structure: Summary, Changes, Impact.
4. Focus on 'Why' and 'What'.
5. Do not include 'Here is the PR description' preamble. Just the body.
6. IMPORTANT: Always use FULL URLs for links to issues and other PRs (e.g., https://github.com/owner/repo/issues/123), do NOT use short syntax (e.g., #123) to ensuring proper linking across platforms.
