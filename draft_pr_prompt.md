# PR Draft Prompt

You are an AI assistant helping to create a Pull Request description.
    
TASK: [Design] Design System Implementation: Colors (#0A192F, #F59E0B) and Typography
ISSUE: {
  "title": "[Design] Design System Implementation: Colors (#0A192F, #F59E0B) and Typography",
  "number": 4
}

GIT CONTEXT:
COMMITS:
af2beec feat: [Design] Design System Implementation: Colors (#0A...
d128e28 docs: add v0.3.0 changelog and Bright Sky design system documentation
8d5f450 refactor: use relative path for Luma dependency
02c95af docs: Add Luma code review report documenting critical issues
b22b8a6 docs: add theme overview documentation for light/dark modes
8eca302 docs: update testing guide with platform status and deployment details
4ab4541 docs: restructure testing guide with installation steps and simplified tests
3f62e63 docs: add manual testing guide for Light/Dark theme features
67ddca8 docs(roadmap): restructure v0.2.0 milestone with architecture and theme issues
4a5540b docs: fix truncated headers and standardize prompt templates
16c5d69 docs: add Android dev prompt template and update platform rollout plan
b0d2912 ✨ feat(design-system): Implement foundational colors and typography

STATS:
.luma_state.json                                   |  23 ++
 CHANGELOG.md                                       |  20 ++
 README.md                                          |  51 +--
 ROADMAP.md                                         |  28 +-
 TESTING_GUIDE.md                                   | 205 ++++++++++++
 THEME_OVERVIEW.md                                  | 135 ++++++++
 .../analysis.md                                    | 250 ++++++++++++++
 .../code_review.md                                 | 100 ++++++
 .../plan.md                                        | 215 ++++++++++++
 .../spec.md                                        | 100 ++++++
 .../specs/sbe_issue-4.md                           |  55 ++++
 .../light-dark-theme.md                            | 168 ++++++++++
 .../screenshots/android_dark.png                   | Bin 0 -> 131911 bytes
 .../screenshots/android_light.png                  | Bin 0 -> 131050 bytes
 .../screenshots/ios_dark.png                       | Bin 0 -> 274498 bytes
 .../screenshots/ios_light.png                      | Bin 0 -> 298502 bytes
 .../screenshots/web_dark.png                       | Bin 0 -> 189682 bytes
 .../screenshots/web_light.png                      | Bin 0 -> 186158 bytes
 docs/templates/analysis_template.md                | 244 ++++++++++++++
 docs/templates/feature_spec_template.md            | 366 +++++++++++++++++++++
 docs/templates/plan_template.md                    |  55 ++++
 prompt_android.txt                                 | 354 ++++++++++++++++++++
 prompt_backend.txt                                 | 354 ++++++++++++++++++++
 prompt_frontend.txt                                | 354 ++++++++++++++++++++
 prompt_ios.txt                                     | 354 ++++++++++++++++++++
 run_guided_workflow.py                             |  36 ++
 26 files changed, 3430 insertions(+), 37 deletions(-)

KEY FILE DIFFS:
diff --git a/run_guided_workflow.py b/run_guided_workflow.py
new file mode 100644
index 0000000..61968e9
--- /dev/null
+++ b/run_guided_workflow.py
@@ -0,0 +1,36 @@
+import sys
+import os
+
+# Add path to Luma using a relative path for portability
+# This assumes the 'Luma' project is in a sibling directory to this script's parent directory.
+script_dir = os.path.dirname(os.path.abspath(__file__))
+luma_path = os.path.abspath(os.path.join(script_dir, '..', 'Luma'))
+sys.path.insert(0, luma_path)
+
+# Mock simple-term-menu just in case actions.py uses it inside
+# Wait, actions.py uses simple-term-menu inside interactive functions?
+# action_guided_workflow calls interactive functions like action_refine_issue
+from luma_core.state_manager import load_state, save_state
+from luma_core.config import PROJECTS
+import luma_core.actions as actions
+
+def run_workflow() -> None:
+    project_key = "6"
+    project = PROJECTS[project_key]
+    
+    # Load state
+    state_path = project["path"]
+    state = load_state(state_path)
+    state.project_key = project_key
+    
+    print(f"🚀 Starting Guided Workflow for Issue #{state.active_issue.number}")
+    
+    # Run the workflow action
+    # This will still be interactive in terms of prompts, but bypasses the menu
+    actions.action_guided_workflow(state, project)
+    
+    # Save state
+    save_state(state, state_path)
+
+if __name__ == "__main__":
+    run_workflow()

PR TEMPLATE:


INSTRUCTIONS:
1. Generate a comprehensive PR description in Markdown format.
2. If a template is provided, fill it out intelligently.
3. If no template, use a standard structure: Summary, Changes, Impact.
4. Focus on 'Why' and 'What'.
5. Do not include 'Here is the PR description' preamble. Just the body.
6. IMPORTANT: Always use FULL URLs for links to issues and other PRs (e.g., https://github.com/owner/repo/issues/123), do NOT use short syntax (e.g., #123) to ensuring proper linking across platforms.
