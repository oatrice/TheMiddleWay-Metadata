Closes: [Link to the full issue URL, e.g., https://github.com/owner/repo/issues/11]

### Summary

This pull request introduces the initial version of the user onboarding experience. It implements a welcome screen and a multi-step introductory flow that explains the app's core concept of "Authentic Wisdom." This provides new users with a warm, informative welcome before they proceed to authentication, setting the stage for their journey with the application.

### Key Changes

*   **✨ Onboarding Flow Implementation:** A new multi-screen UI has been added for first-time users, guiding them through the app's value proposition. The flow includes:
    *   A main "Welcome" screen.
    *   An introduction to "Authentic Wisdom."
    *   Screens highlighting key features like "Discover Your Path" and "Daily Practice."

*   **🎨 New Image Assets:** New illustrations have been added to support each step of the onboarding process, creating a visually engaging experience.

*   **🛠️ iOS Asset Generation Script:** A new helper script, `create_ios_assets.py`, has been created to automate the process of converting source PNGs into properly structured `.imageset` bundles for the iOS project. This streamlines the asset pipeline and reduces manual effort in Xcode.

*   **📝 Comprehensive Documentation:** This feature was developed with a documentation-first approach. This PR includes:
    *   Detailed feature planning and specification documents.
    *   Implementation plans and analysis.
    *   Updates to the project `ROADMAP.md` to reflect this completed work.

### Screenshots

*(Please add screenshots or a GIF of the new onboarding flow below)*

[Insert GIF or screenshots here]