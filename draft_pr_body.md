Closes https://github.com/mdwmediaworld072/TheMiddleWay/issues/1

### Summary

This Pull Request introduces the **"สวนแห่งปัญญา" (Wisdom Garden)**, the core dashboard experience for the application. It provides users with a serene and visual way to track their progress in daily practices through a growing "Wisdom Tree" and an interactive weekly checklist.

This foundational feature is implemented across both Web and Android platforms, complete with data persistence on mobile, establishing the main user-facing interface of the app.

### What's New

#### 🌿 Feature: Wisdom Garden Dashboard

*   **Visual Progress Tracker:** A central UI component displays a "Wisdom Tree" that grows and flourishes based on the user's accumulated score from their practices.
*   **Interactive Practice Checklist:** Users can check off daily practices, which are grouped by categories like "Giving" (ทาน) and "Ethics" (ศีล). Checking an item provides immediate feedback and updates the total score.
*   **Week Selector:** A navigation element allows users to seamlessly view their progress and checklists for different weeks (1-8).
*   **Cross-Platform UI:** The dashboard has been implemented for both Web (React) and Android, ensuring a consistent and responsive user experience.

#### 🛠️ Technical Implementation & Fixes

*   **Android:**
    *   Integrated **Room Database** for persisting all weekly progress and scores locally on the device.
    *   Implemented an **auto-seeding mechanism** that populates the database with 8 weeks of initial practice data on the first launch.
    *   Refactored the screen architecture using a `WisdomGardenRoute` wrapper for clean and correct ViewModel injection.
*   **Web:**
    *   Fixed a critical logic bug where the `maxScore` was hardcoded; it is now dynamically calculated based on the available practice items for the week.
    *   Corrected a state management anti-pattern by implementing proper immutable state updates in the checklist handler (`handleCheckItem`).
*   **CI/CD:**
    *   Hardened the iOS `auto-tag.yml` workflow to correctly strip quotes from version strings and strictly validate project file paths to prevent ambiguity.

#### 📝 Documentation & Project Updates

*   **Test Plan:** Added a new, comprehensive `TEST_PLAN.md` based on code review feedback, covering critical edge cases.
*   **Changelog & Version:** Updated `CHANGELOG.md` with a detailed entry for `v0.6.0` and bumped the project version.
*   **Roadmap:** Revised `ROADMAP.md` to reflect the completion of this key feature and reprioritize upcoming work.
*   **Screenshots:** Added screenshots for light and dark modes across Web, Android, and iOS to the `docs/` directory.

### Screenshots

*Light Mode (Web)* ![web_light](https://github.com/mdwmediaworld072/TheMiddleWay/assets/12345/some-image-hash-web-light) 

*Dark Mode (Android)* ![android_dark](https://github.com/mdwmediaworld072/TheMiddleWay/assets/12345/some-image-hash-android-dark) 

### How to Test

1.  Launch the application (Web or Android).
2.  The "Wisdom Garden" dashboard should be the main screen.
3.  Verify the layout matches the design (tree visualization on top, checklist below).
4.  Click on a checkbox in the "Daily Practices Checklist".
    *   **Expected:** The item should be marked as complete, and the score (e.g., `1/40`) should update instantly. The tree visualization may also change.
5.  Use the "Week Selector" at the top to switch between different weeks.
    *   **Expected:** The checklist and score should update to reflect the data for the selected week.
6.  Verify the page is responsive and displays correctly on both desktop and mobile screen sizes.