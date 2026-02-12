# SBE: Weekly Practices & Checklist Page

> 📅 Created: 2026-02-12
> 🔗 Issue: https://github.com/mdwmediaworld072/TheMiddleWay/issues/2

---

## Feature: Weekly Practices & Checklist Page

This feature provides a dedicated 'Practice Room' for users to view and complete their weekly spiritual practices. It includes a week selector, a categorized checklist, and a progress bar to track completion for the selected week. User progress is saved locally to ensure data persistence.

### Scenario: Happy Path - Completing and Saving a Practice Item

**Given** the user is viewing the checklist for a specific week with some items already completed
**When** the user taps on an incomplete practice item
**Then** the item is visually marked as complete (e.g., dimmed with a strikethrough), the weekly progress bar updates, and the new state is saved and persists even after navigating away and returning.

#### Examples

| selected_week | initial_progress | tapped_item | expected_visual_state | expected_progress_bar | persistence_check |
| :------------ | :--------------- | :-------------------------------- | :------------------------ | :-------------------- | :---------------------------------------------- |
| Week 1        | "2/10"           | "สวดมนต์ทำวัตรเช้า" (Morning Chanting) | Dimmed with strikethrough | "3/10"                | State remains after navigating to Dashboard and back |
| Week 3        | "0/8"            | "นั่งสมาธิ 15 นาที" (15-min Meditation) | Dimmed with strikethrough | "1/8"                 | State remains after closing and reopening the app |
| Week 5        | "7/12"           | "แผ่เมตตา" (Spreading Loving-Kindness) | Dimmed with strikethrough | "8/12"                | State remains after navigating to Week 6 and back |
| Week 8        | "9/10"           | "รักษาศีล 5" (Observing 5 Precepts) | Dimmed with strikethrough | "10/10"               | State remains after navigating to Dashboard and back |

### Scenario: Edge Case - Switching Between Weeks with Saved Progress

**Given** the user has completed a number of practices in one week
**When** the user selects a different week from the week selector
**Then** the checklist and progress bar correctly display the data for the newly selected week, and the progress for the previous week is preserved when they switch back.

#### Examples

| initial_week | initial_week_progress | action_switch_to | new_week_progress | action_switch_back_to | expected_restored_progress |
| :----------- | :-------------------- | :--------------- | :---------------- | :-------------------- | :------------------------- |
| Week 1       | "5/10"                | Week 2           | "0/9"             | Week 1                | "5/10"                     |
| Week 4       | "8/8"                 | Week 5           | "1/12"            | Week 4                | "8/8"                      |
| Week 7       | "3/10"                | Week 1           | "5/10"            | Week 7                | "3/10"                     |
| Week 2       | "4/9"                 | Week 8           | "0/10"            | Week 2                | "4/9"                      |

### Scenario: Edge Case - Toggling a Practice Item On and Off

**Given** a user has already marked a practice item as complete
**When** the user taps on that same completed item again
**Then** the item's visual state reverts to incomplete, the weekly progress bar decreases accordingly, and this un-checked state is saved.

#### Examples

| selected_week | initial_progress | tapped_item_to_uncheck | expected_visual_state | expected_progress_bar |
| :------------ | :--------------- | :----------------------------------- | :-------------------- | :-------------------- |
| Week 1        | "6/10"           | "สวดมนต์ทำวัตรเย็น" (Evening Chanting) | Normal (not dimmed)   | "5/10"                |
| Week 3        | "1/8"            | "นั่งสมาธิ 15 นาที" (15-min Meditation) | Normal (not dimmed)   | "0/8"                 |
| Week 6        | "9/11"           | "ฟังธรรม" (Listen to Dhamma Talk) | Normal (not dimmed)   | "8/11"                |

### Scenario: Error Handling - Practice Data Fails to Load

**Given** the user is on the "Weekly Practices" page
**When** the user selects a week for which the practice data (e.g., from a CSV file) is missing or corrupted
**Then** the application displays a user-friendly error message instead of the checklist, and the progress bar is hidden or shows an error state.

#### Examples

| selected_week | data_source_state | expected_ui_element | expected_error_text |
| :------------ | :------------------ | :------------------ | :--------------------------------------------------------------------- |
| Week 5        | Missing file      | Error Message       | "ไม่สามารถโหลดข้อมูลการปฏิบัติของสัปดาห์นี้ได้" (Could not load practices for this week.) |
| Week 7        | Corrupted data    | Error Message       | "ข้อมูลการปฏิบัติของสัปดาห์นี้เสียหาย" (Practice data for this week is corrupted.) |
| Week 9        | Non-existent week | Error Message       | "ไม่พบข้อมูลสำหรับสัปดาห์ที่เลือก" (Data not found for the selected week.) |