# Specification: 📝 สร้างหน้า "ห้องปฏิบัติธรรม" (Weekly Practices & Checklist)

## 1. Overview

This document specifies the requirements for a new feature: the "Weekly Practices" page, referred to in Thai as "ห้องปฏิบัติธรรม" (Practice Room). This page will serve as the primary interface for users to view and track their assigned spiritual practices for each week. It is designed to be a focused "action" area, separating the task of recording progress from the "Dashboard" page ("สวนแห่งปัญญา"), which is dedicated to viewing overall results. The goal is to create a clean, simple, and encouraging user experience for daily and weekly engagement.

## 2. User Goal

As a practitioner, I want a dedicated page to see my list of practices for any given week and easily check them off as I complete them. This will help me stay focused on my current tasks, feel a sense of accomplishment, and keep my progress accurately recorded without the distractions of the main dashboard.

## 3. User Journey

1.  **Accessing the Page**: The user navigates from the main menu or tab bar to the "ห้องปฏิบัติธรรม" (Weekly Practices) page.
2.  **Viewing Practices**: By default, the page displays the checklist of practices for the current week (e.g., Week 1). A progress bar at the top immediately shows the user their completion status for this week (e.g., "3/10 Completed").
3.  **Selecting a Week**: The user can tap on the week selector at the top of the page (e.g., "Week 2", "Week 3") to view the practices for a different week. The checklist and progress bar below update instantly to reflect the selected week's content and saved progress.
4.  **Completing a Practice**: The user reads a practice item in the list. After completing it in real life, they tap the checkbox next to it.
5.  **Receiving Feedback**: Upon tapping, the system provides immediate feedback:
    *   The checkbox is filled (✅).
    *   The list item's text is dimmed or struck through.
    *   A subtle sound effect or haptic feedback (on mobile) occurs.
    *   The progress bar at the top updates to reflect the new count (e.g., from "3/10" to "4/10").
6.  **Un-doing a Practice**: If the user taps a completed item by mistake, they can tap it again. The item reverts to its original, un-completed state, and the progress bar updates accordingly.
7.  **Persistent State**: The user navigates away to the Dashboard and then returns to the "Weekly Practices" page. All their previously checked items remain checked, exactly as they left them.

## 4. Functional Requirements

| ID | Requirement | Details |
| :--- | :--- | :--- |
| **FR1** | **Week Selector** | - A component at the top of the screen shall allow users to select any week from Week 1 to Week 8.<br>- Selecting a week must dynamically update the checklist content and progress bar to show the data for that specific week.<br>- The system must remember and display the last selected week when the user returns to the page. |
| **FR2** | **Checklist Display** | - The system must fetch and display a list of practices for the selected week from the specified data source (CSV files).<br>- Each practice item must be displayed in its own card for clarity.<br>- Each item must display a colored category tag/badge (e.g., 🎁 Giving, 🛡️ Ethics) corresponding to its category in the data source. |
| **FR3** | **Checklist Interaction** | - Each practice item must have a tappable checkbox.<br>- Tapping an unchecked item marks it as "complete".<br>- Tapping a checked item marks it as "incomplete" (toggle functionality). |
| **FR4** | **State Persistence** | - The completion status (checked/unchecked) of every practice for all weeks must be saved locally on the user's device (e.g., using LocalStorage).<br>- This state must persist even if the user closes and reopens the application or navigates to other pages. |
| **FR5** | **Weekly Progress Summary** | - A progress bar must be displayed at the top of the checklist area.<br>- The bar must visually represent the ratio of completed tasks to total tasks for the currently selected week.<br>- A text label must accompany the bar, showing the exact numbers (e.g., "8/10 Completed"). |
| **FR6** | **User Feedback** | - When a user checks an item, the UI for that item must visually change (e.g., text becomes dimmed, a strikethrough is applied).<br>- When a user checks an item, the system should provide non-visual feedback, such as a subtle sound effect or haptic feedback on supported devices. |

## 5. Non-Functional Requirements

| ID | Requirement | Details |
| :--- | :--- | :--- |
| **NFR1** | **Usability** | - The UI must be clean, uncluttered, and easy to read.<br>- All interactive elements, especially checkboxes, must have large enough tap targets to be easily used on mobile devices (finger-friendly). |
| **NFR2** | **Performance** | - The list of practices must scroll smoothly, even if a week contains a large number of items.<br>- Switching between weeks should feel instantaneous with no noticeable lag. |
| **NFR3** | **Data Integrity** | - The state of the checklist on this page must be the source of truth. The Dashboard page must read from this same global state to ensure consistency in progress reporting across the application. |

## 6. Specification by Example (SBE)

### Scenario 1: User completes their first two practices for the week

**Given** the user is on the "ห้องปฏิบัติธรรม" page and has selected "Week 1".
**And** the progress for Week 1 is "0/12".

**When** the user taps the checkbox for "สวดมนต์ทำวัตรเช้า" (Morning Chanting).
**And then** taps the checkbox for "แผ่เมตตาให้ตนเอง" (Radiating Loving-Kindness to Self).

**Then** the system will:
1.  Mark both items as complete with a visual change (e.g., strikethrough).
2.  Update the weekly progress bar and text to "2/12 Completed".
3.  Save the completion state for these two items for Week 1.
4.  If the user navigates to the Dashboard and returns, these two items will remain checked.

**Example Data:**

**Initial State (Week 1):**
| Practice | Category | Status |
| :--- | :--- | :--- |
| สวดมนต์ทำวัตรเช้า | 🧘 Meditation | `[ ]` Unchecked |
| แผ่เมตตาให้ตนเอง | 🧘 Meditation | `[ ]` Unchecked |
| ให้ทานคนยากไร้ | 🎁 Giving | `[ ]` Unchecked |
| ... (9 more items) | ... | `[ ]` Unchecked |
*Progress Bar: 0/12*

**Final State (Week 1):**
| Practice | Category | Status |
| :--- | :--- | :--- |
| ~~สวดมนต์ทำวัตรเช้า~~ | 🧘 Meditation | `[✅]` Checked |
| ~~แผ่เมตตาให้ตนเอง~~ | 🧘 Meditation | `[✅]` Checked |
| ให้ทานคนยากไร้ | 🎁 Giving | `[ ]` Unchecked |
| ... (9 more items) | ... | `[ ]` Unchecked |
*Progress Bar: 2/12*

---

### Scenario 2: User switches weeks and then un-checks a task

**Given** the user has completed 5 practices in "Week 3" and is currently viewing that page.
**And** the progress for Week 3 is "5/10".

**When** the user taps the "Week 4" selector.
**And then** taps the "Week 3" selector to return.
**And then** taps on the already-checked item "รักษาศีล 5" (Observe the 5 Precepts) to un-check it.

**Then** the system will:
1.  Correctly display the checklist for Week 4 (with its own saved progress).
2.  Upon returning, correctly display the checklist for Week 3 with its 5 items checked.
3.  Revert the "รักษาศีล 5" item to its unchecked state.
4.  Update the Week 3 progress bar and text from "5/10" down to "4/10".

**Example Data:**

**Initial State (Week 3):**
| Practice | Category | Status |
| :--- | :--- | :--- |
| ~~รักษาศีล 5~~ | 🛡️ Ethics | `[✅]` Checked |
| ~~นั่งสมาธิ 15 นาที~~ | 🧘 Meditation | `[✅]` Checked |
| ... (3 more checked) | ... | `[✅]` Checked |
| ... (5 more unchecked) | ... | `[ ]` Unchecked |
*Progress Bar: 5/10*

**Final State (Week 3):**
| Practice | Category | Status |
| :--- | :--- | :--- |
| รักษาศีล 5 | 🛡️ Ethics | `[ ]` Unchecked |
| ~~นั่งสมาธิ 15 นาที~~ | 🧘 Meditation | `[✅]` Checked |
| ... (3 more checked) | ... | `[✅]` Checked |
| ... (5 more unchecked) | ... | `[ ]` Unchecked |
*Progress Bar: 4/10*

## 7. Out of Scope

-   **Locking future weeks**: For this initial version, all weeks (1-8) will be accessible from the start. The logic to lock weeks until the previous one is completed is out of scope.
-   **Adding custom practices**: Users cannot add their own practice items to the list. The list is predefined by the weekly CSV data.
-   **Detailed statistics or notes**: This page is only for checking items off. It will not include features for adding notes, timers, or viewing historical completion data (that is the role of the Dashboard).

## 8. Acceptance Criteria

1.  [ ] The page displays a week selector for Weeks 1 through 8.
2.  [ ] Selecting a week from the selector updates the checklist below to show the correct practices for that week.
3.  [ ] Each practice item in the list displays a category tag with a distinct color.
4.  [ ] Tapping a checkbox on an item successfully toggles its state between "complete" and "incomplete".
5.  [ ] A progress bar and text label (e.g., "X/Y") at the top of the page accurately reflect the number of completed items for the currently viewed week.
6.  [ ] The completion status of all items is saved and persists after the user navigates to another page and returns, or closes and reopens the app.
7.  [ ] A non-visual feedback (sound or haptic) is triggered upon checking an item.