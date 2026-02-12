Closes: https://github.com/mdwmediaworld072/TheMiddleWay/issues/2

### Summary

This pull request lays the foundational groundwork for the **"ห้องปฏิบัติธรรม" (Weekly Practices & Checklist)** feature, as detailed in Issue #2. It focuses on establishing a comprehensive plan and updating project documentation before implementation begins.

The core of this PR is the creation of detailed planning documents, including analysis, implementation strategies, specifications, and user walkthroughs for the new feature. This ensures that the development process is guided by a clear and well-defined roadmap.

Additionally, the project's state has been updated to reflect that Issue #2 is now the active focus, and the version has been bumped to `0.7.0` to mark this significant planning milestone.

### Key Changes

*   **📝 Feature Documentation:** Added a complete suite of planning documents for the "Weekly Practices & Checklist" feature under `docs/features/7_issue-2...`. This includes:
    *   `analysis.md`: Requirement analysis, user stories, and impact assessment.
    *   `implementation_plan.md`: A step-by-step guide for frontend and backend development.
    *   `plan.md` & `spec.md`: Detailed feature specifications and technical requirements.
    *   `task.md` & `walkthrough.md`: Breakdown of development tasks and expected user flow.
*   **⚙️ Project State Update:** Modified `.luma_state.json` to set Issue #2 as the `active_issue`, officially kicking off its development cycle.
*   **📈 Version Bump:** Updated `VERSION` and `CHANGELOG.md` to `0.7.0` to signify the release of the new feature documentation.
*   **🤖 AI Prompt Enhancement:** Updated `prompt_*.txt` files to include the context and requirements of the new checklist feature, ensuring future AI-assisted development is aligned.
*   **🧪 New Test Cases:** Added relevant, edge-case test suggestions to `code_review.md` specifically for the new feature, focusing on state persistence and data integrity.