# Walkthrough - Wisdom Garden UI Refactor

The **Wisdom Garden** feature has been refactored to separate the "Viewing" experience from the "Doing" experience.

## Changes Made
- **Dashboard (`/`)**: Now displays a **Read-Only** checklist and the Wisdom Garden tree. Added a "Go to Practice Room" button.
- **Weekly Practices (`/weekly-practices`)**: A new dedicated page for checking off practices.
- **State Management**: Implemented `useWisdomGarden` hook to sync data between pages using `localStorage`.

## Verification Steps

### 1. Verify Read-Only Dashboard
1.  Navigate to the home page (`http://localhost:3000`).
2.  Try to click on any checklist item.
    - [ ] **Expected:** Item should NOT toggle. Cursor should be default (not pointer).
3.  Observe the "Wisdom Garden" tree visualization.

### 2. Verify Interactive Practice Room
1.  Click the **"Go to Practice Room"** button.
2.  You should be navigated to `/weekly-practices`.
3.  Click on an unchecked item (e.g., "Morning Meditation").
    - [ ] **Expected:** Item becomes checked. Points are added.
4.  Click on a checked item.
    - [ ] **Expected:** Item becomes unchecked. Points are deducted.
5.  Refresh the page.
    - [ ] **Expected:** The item states persist.

### 3. Verify Data Sync
1.  Check an item in the **Practice Room** (e.g., ensure "Offering alms" is checked).
2.  Click **"Back to Dashboard"** (or use browser back).
3.  Look at the checklist on the Dashboard.
    - [ ] **Expected:** "Offering alms" should be shown as checked (visual only).
4.  Check the total score/tree visualization.
    - [ ] **Expected:** Score reflects the changes made in the Practice Room.

### 4. Verify Week Selection
1.  Change the week using the Week Selector (e.g., select Week 2).
2.  Verify the checklist resets or shows data for Week 2.
3.  Go back to Dashboard and select Week 2.
    - [ ] **Expected:** Data matches Week 2 in Practice Room.

## Identified Gaps & Next Steps
We have identified several features from the original specifications (Issue 1 & 2) that were not implemented in this iteration.
Please refer to [Pending Features Report](pending_features_report.md) for a detailed list to create new GitHub issues.
- Language Switcher (FR-1.1)
- Category Tags on Practice Cards (FR-2)
- Weekly Progress Summary (FR-5)
- Haptic & Sound Feedback (FR-6)
