# Walkthrough - Wisdom Garden UI Refactor

The **Wisdom Garden** feature has been refactored to separate the "Viewing" experience from the "Doing" experience.

## Changes Made
- **Dashboard (`/`)**: Now displays a **Read-Only** checklist and the Wisdom Garden tree. Added a "Go to Practice Room" button.
- **Weekly Practices (`/weekly-practices`)**: A new dedicated page for checking off practices.
- **State Management**: Implemented `useWisdomGarden` hook to sync data between pages using `localStorage`.

### iOS Implementation (SwiftUI)
- **Architecture**: MVVM with `WisdomGardenViewModel` and `NetworkWisdomGardenRepository`.
- **UI**: 
    - `WisdomGardenView` as the main Home tab (Read-Only Dashboard).
    - `WeeklyPracticesView` for interactive practice (Practice Room).
    - `WeekSelectorView` for navigation between 8 weeks (Available on both screens).
    - `WisdomTreeVisualizationView` dynamic tree growth.
    - `PracticeChecklistView` for toggling items (Supports read-only mode).
- **Network**: 
    - Uses `URLSession` to connect to `http://localhost:8080`.
    - **Note**: Ensure `App Transport Security` allows Arbitrary Loads if testing on Simulator.
- **Features**:
    - **Separate Practice Room**: Dashboard is read-only; interaction happens in `WeeklyPracticesView`.
    - **Consistent Layout**: "Go to Practice Room" button placed between Tree and Checklist, matching Android.

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

### Android Implementation
- **Dashboard Refactor**:
    - Updated `WisdomGardenScreen` to be a read-only dashboard.
    - Added "Go to Practice Room" button.
    - Implemented read-only mode for `PracticeChecklist` with toast warnings.
- **Practice Room**:
    - Created `WeeklyPracticesScreen` for interactive checking.
    - Implemented local state navigation in `WisdomGardenRoute`.
- **Verification**:
    - Validated data models against Web.
    - Verified build functionality with `./gradlew assembleDebug`.
    - **Fixes**:
        - Changed "Go to Practice Room" button color to `Primary` (was Pink/PrimaryContainer).
        - Fixed Checkbox state issue by adding `key(item.id)` to `PracticeChecklist` loop.
    - **Network Integration**:
        - Switched from `RoomWisdomGardenRepository` to `NetworkWisdomGardenRepository`.
        - Configured Retrofit to connect to `http://10.0.2.2:8080/api/v1/` (Emulator localhost).
        - Added Internet permission and Network Security Config.

### Backend Implementation (Go)
- **Architecture**:
    - **Model**: Created `Practice` struct in `internal/model/practice.go`.
    - **Repository**: Created `PracticeRepository` in `internal/repository/practice_repo.go` with seeding logic.
    - **Handler**: Created `PracticeHandler` in `internal/handler/practice_handler.go` to aggregate data into `WeeklyData` format.
    - **API**: Registered `/api/v1/wisdom-garden` routes in `cmd/server/main.go`.
- **Verification**:
    - Verified `GET /api/v1/wisdom-garden/weeks/1` returns correct JSON structure.
    - Verified `POST /api/v1/wisdom-garden/practices/:id/toggle` updates completion status.

## Gaps & Next Steps
- **Backend**: Current implementation uses SQLite with a single table. Needs `UserPractice` table for multi-user support.
- **Data Persistence**: Android and iOS apps are now connected to the Backend API.

[Link to Pending Features Report](file:///Users/oatrice/.gemini/antigravity/brain/6b38fc57-9139-4a1f-9e31-687b961945ca/pending_features_report.md) for a detailed list to create new GitHub issues.
- Language Switcher (FR-1.1)
- Category Tags on Practice Cards (FR-2)
- Weekly Progress Summary (FR-5)
- Haptic & Sound Feedback (FR-6)
