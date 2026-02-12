# Pending Features Report

The following features were specified in the original requirements for **Issue 1 (Wisdom Garden Dashboard)** and **Issue 2 (Weekly Practices Checklist)** but were not implemented in the current iteration.

They are now tracked as new GitHub issues in the **Metadata** repository for future development.

## 1. Language Switcher (FR-1.1)
- **Status:** Created Issue [#37](https://github.com/oatrice/TheMiddleWay-Metadata/issues/37)
- **Source:** Issue 1 Spec
- **Description:** A toggle button in the header to switch the UI language between Thai (TH) and English (EN).
- **Requirement:**
    - Located in the top-right corner of the header.
    - Persists the user's language preference across sessions.
    - Updates all text content dynamically.

## 2. Category Tags on Practice Cards (FR-2)
- **Status:** Created Issue [#36](https://github.com/oatrice/TheMiddleWay-Metadata/issues/36)
- **Source:** Issue 2 Spec
- **Description:** Visual badges or tags on each practice card to indicate its category (e.g., "Giving", "Ethics", "Meditation").
- **Requirement:**
    - Each practice card must display a category tag.
    - Tags should have distinct colors corresponding to the category.
    - Helps users quickly identify the type of practice.

## 3. Weekly Progress Summary (FR-5)
- **Status:** Created Issue [#35](https://github.com/oatrice/TheMiddleWay-Metadata/issues/35)
- **Source:** Issue 2 Spec
- **Description:** A visual progress bar and text label at the top of the checklist area on the "Weekly Practices" page.
- **Requirement:**
    - Displays a progress bar representing the ratio of completed tasks to total tasks for the selected week.
    - Includes a text label showing the exact count (e.g., "8/10 Completed").
    - Updates instantly as items are checked/unchecked.

## 4. Haptic & Sound Feedback (FR-6)
- **Status:** Created Issue [#34](https://github.com/oatrice/TheMiddleWay-Metadata/issues/34)
- **Source:** Issue 2 Spec
- **Description:** Non-visual feedback when a user completes a practice item.
- **Requirement:**
    - **Haptic Feedback:** A subtle vibration when checking an item (on supported mobile devices).
    - **Sound Effect:** A gentle, satisfying sound upon completion.
    - Should be toggleable or respect system silent/do-not-disturb modes (implicit best practice).
