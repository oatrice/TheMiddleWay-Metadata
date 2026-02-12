# Implementation Plan: Weekly Practices & Checklist Page (ห้องปฏิบัติธรรม)

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Draft

## 1. Architecture & Design
*High-level technical approach.*

The "Weekly Practices" page will be implemented as a new, self-contained feature module. It will follow a reactive, component-based architecture. A central state management service will be responsible for handling user progress, ensuring data integrity (NFR3) and persistence (FR4). This service will act as the single source of truth for checklist completion status, which can be consumed by both this new page and the existing Dashboard.

Practice data will be loaded from the provided CSV files by a dedicated data service, which will parse and cache the data for efficient access.

### Component View
> [!IMPORTANT]
> **Platform Scope Policy:**
> - **Web**: Mock UI only for this phase. A static, non-interactive version will be created to establish the visual layout.
> - **Android**: Full implementation with production-ready code and tests.
> - **iOS**: Full implementation with production-ready code and tests.
>
> **Development Order:** Web Mock UI FIRST → Android Full Implementation SECOND → iOS Full Implementation THIRD.

- **Modified Components**:
    - `AppNavigator`: To add a new route and tab bar/menu entry for the "ห้องปฏิบัติธรรม" page.
    - `DashboardPage`: Will be modified later to read from the new `PracticeStateService` to ensure progress consistency. This is out of scope for the initial build of this feature but is a key architectural consideration.

- **New Components**:
    - `WeeklyPracticesPage`: The main screen container component. It will orchestrate the other components and manage the currently selected week state.
    - `WeekSelector`: A horizontal list or segmented control component that displays buttons for Week 1 to Week 8. Emits an event when a new week is selected.
    - `ProgressSummary`: A component that displays the progress bar and the "X/Y Completed" text. It will receive the total and completed counts as props.
    - `PracticeChecklist`: A virtualized/recycling list view to display the practice items for the selected week, ensuring smooth scrolling (NFR2).
    - `PracticeItem`: A card component for a single practice. It will display the practice text, category tag, and a custom checkbox. It will manage its own visual state (checked/unchecked) based on props and emit events on user interaction.

- **New Services / Utilities**:
    - `PracticeDataService`: A singleton service responsible for fetching, parsing, and caching the practice data from the weekly CSV files. It will provide a method like `getPracticesForWeek(weekNumber)`.
    - `PracticeStateService`: A singleton service that manages the user's progress. It will:
        - Load the completion state from the device's local storage on app startup.
        - Provide methods like `isPracticeComplete(week, practiceId)`, `togglePracticeStatus(week, practiceId)`.
        - Persist any changes back to local storage immediately.
        - Expose the progress state reactively so that UI components can subscribe to changes.
    - `FeedbackService`: A utility to handle non-visual feedback (sound effects, haptics) in a platform-agnostic way.

### Data Model Changes
```typescript
// Represents a single practice item parsed from CSV
interface Practice {
  id: string;       // A unique identifier, e.g., "week1_item3"
  week: number;     // The week this practice belongs to (1-8)
  category: 'Giving' | 'Ethics' | 'Meditation' | 'Wisdom'; // Enum for categories
  description: string; // The text of the practice, e.g., "สวดมนต์ทำวัตรเช้า"
}

// Structure for storing user progress in LocalStorage.
// A simple JSON object where keys are week numbers and values are arrays of completed practice IDs.
// Example: { "1": ["week1_item1", "week1_item5"], "3": ["week3_item2"] }
type PracticeProgress = {
  [weekNumber: number]: string[];
};

// State managed by PracticeStateService
interface AppState {
  practiceProgress: PracticeProgress;
  lastSelectedWeek: number;
}
```

---

## 2. Step-by-Step Implementation

### Step 1: Data Layer Foundation
- **Description**: Create the core services for managing practice data and user progress state. This step involves no UI work but is critical for all subsequent steps.
- **Code**:
    - **Create `services/PracticeDataService`**:
        - Implement logic to read and parse all 8 `week_N.csv` files. The CSVs should be bundled as assets within the mobile apps.
        - Create a method `getPracticesForWeek(week: number): Promise<Practice[]>`.
        - Add in-memory caching to avoid re-parsing files.
    - **Create `services/PracticeStateService`**:
        - Implement `loadProgress()` and `saveProgress()` methods that interact with the device's local storage (`SharedPreferences` on Android, `UserDefaults` on iOS).
        - Implement `togglePracticeStatus(week: number, practiceId: string)`. This method will update the in-memory state and trigger `saveProgress()`.
        - Implement `getProgressForWeek(week: number): { completed: number, total: number }`.
        - Expose the state reactively (e.g., using `StateFlow` on Android, `Combine` on iOS).
- **Tests**:
    - **Unit Tests for `PracticeDataService`**:
        - Verify that CSV parsing is correct for a sample file.
        - Verify `getPracticesForWeek` returns the correct data and handles invalid week numbers.
    - **Unit Tests for `PracticeStateService`**:
        - Verify that `togglePracticeStatus` correctly adds and removes practice IDs.
        - Verify that `saveProgress` and `loadProgress` correctly serialize/deserialize the state to a mock storage interface.

### Step 2: UI Scaffolding and Navigation
- **Description**: Create the main page and its sub-components as stateless UI elements. Set up navigation to the new page.
- **Code**:
    - **Create `screens/WeeklyPracticesPage`**:
        - Create the basic layout containing placeholders for the `WeekSelector`, `ProgressSummary`, and `PracticeChecklist`.
    - **Create `components/WeekSelector`**:
        - Renders buttons for "Week 1" through "Week 8".
        - Takes the `currentWeek` and an `onSelectWeek` callback as props.
    - **Create `components/ProgressSummary`**:
        - Renders a progress bar and text. Takes `completed` and `total` numbers as props.
    - **Create `components/PracticeChecklist` and `components/PracticeItem`**:
        - `PracticeChecklist` renders a list of `PracticeItem` components.
        - `PracticeItem` is a simple card displaying mock text, a category tag, and a checkbox.
    - **Modify `navigation/AppNavigator`**:
        - Add the `WeeklyPracticesPage` to the app's navigation stack.
        - Add a link in the main menu or tab bar.
- **Verification**:
    - Manually navigate to the new "ห้องปฏิบัติธรรม" page.
    - Verify that the page loads and displays the static, placeholder components correctly.

### Step 3: Wire Up State and Data to UI
- **Description**: Connect the UI components to the data services. The page should now display real data and respond to week selection.
- **Code**:
    - **In `WeeklyPracticesPage`**:
        - Instantiate and use `PracticeDataService` and `PracticeStateService`.
        - Manage a state variable for the `selectedWeek`, defaulting to the current week or the last selected week from `PracticeStateService`.
        - When `selectedWeek` changes, call `PracticeDataService.getPracticesForWeek()` to get the list of practices.
        - Pass the practice list to `PracticeChecklist`.
        - Pass the `selectedWeek` to `WeekSelector` and update the state via its `onSelectWeek` callback.
        - Calculate progress using `PracticeStateService` and pass the counts to `ProgressSummary`.
- **Verification**:
    - The page should now display the correct list of practices for the default week.
    - Tapping on the `WeekSelector` (e.g., "Week 3") should update the checklist and progress summary below to show the data for Week 3.
    - The last selected week should be remembered when navigating away and back to the page.

### Step 4: Implement Checklist Interaction and Persistence
- **Description**: Enable the core functionality of checking and un-checking items and ensure the state persists.
- **Code**:
    - **In `PracticeItem`**:
        - Add an `onToggle` callback prop.
        - When the user taps the checkbox, call the `onToggle` callback with the `practice.id`.
        - Add props for `isComplete` and apply visual styles (strikethrough, dimming) based on this prop.
    - **In `PracticeChecklist` / `WeeklyPracticesPage`**:
        - For each `PracticeItem`, pass the `onToggle` handler which calls `PracticeStateService.togglePracticeStatus(selectedWeek, practiceId)`.
        - For each `PracticeItem`, determine its `isComplete` status by querying `PracticeStateService`.
        - Because the service's state is reactive, the UI should update automatically when the state changes (e.g., progress bar, item style).
- **Verification**:
    - Tapping a practice item's checkbox marks it as complete, applies the visual style, and updates the progress bar.
    - Tapping a completed item reverts it to the incomplete state and updates the progress bar.
    - Close and reopen the app. The previously checked items should remain checked.
    - Navigate to another page and return. The state should be preserved.

### Step 5: Add Final Polish and Feedback
- **Description**: Implement the non-visual feedback and ensure the UI meets all non-functional requirements.
- **Code**:
    - **Create `services/FeedbackService`**:
        - Implement `triggerSuccess()` which plays a subtle sound and/or triggers a haptic vibration.
    - **In `WeeklyPracticesPage`**:
        - When handling the `onToggle` event from a `PracticeItem`, if the item is being marked as complete, call `FeedbackService.triggerSuccess()`.
    - **In `PracticeItem` / CSS**:
        - Review and confirm that tap targets for checkboxes are sufficiently large (e.g., by making the entire list item tappable).
    - **In `PracticeChecklist`**:
        - Ensure it uses a performant list view (`RecyclerView` on Android, `UICollectionView` or `List` with SwiftUI) to handle scrolling smoothly.
- **Verification**:
    - A sound or haptic feedback occurs when checking an item.
    - The list scrolls smoothly without any jank.
    - The UI is clean, readable, and easy to interact with on a mobile device.

---

## 3. Verification Plan
*How will we verify success?*

> [!IMPORTANT]
> **Android Build Policy**: MUST use scripts in `Android/scripts/` (e.g., `build_android.sh`) instead of direct `./gradlew` to ensure correct JDK version (Java 21).

### Automated Tests
- [ ] **Unit Tests**:
    - `PracticeDataService`: Verify correct parsing of sample CSV data.
    - `PracticeStateService`: Verify state logic (toggling, saving, loading) with a mocked storage dependency.
- [ ] **Component/Widget Tests**:
    - `ProgressSummary`: Given props `completed=3` and `total=10`, verify it displays "3/10" and the progress bar is at 30%.
    - `PracticeItem`: Verify that passing `isComplete=true` applies the correct visual styling (e.g., strikethrough).
- [ ] **Integration Tests**:
    - A test for the `WeeklyPracticesPage` that simulates tapping a week, checking an item, and verifies that both the `PracticeStateService` was called and the `ProgressSummary` UI updated correctly.

### Manual Verification
- [ ] **FR1 (Week Selector)**:
    - [ ] The page displays a selector for Weeks 1 through 8.
    - [ ] Tapping "Week 5" updates the list to show practices for Week 5.
    - [ ] Navigate away and back; the page should still be on "Week 5".
- [ ] **FR2 (Checklist Display)**:
    - [ ] The list of practices for the selected week is displayed correctly.
    - [ ] Each item shows a colored category tag (e.g., "🎁 Giving").
- [ ] **FR3 (Checklist Interaction)**:
    - [ ] Tapping an unchecked item's checkbox marks it as checked.
    - [ ] Tapping a checked item's checkbox marks it as unchecked.
- [ ] **FR4 (State Persistence)**:
    - [ ] Check 3 items in Week 2.
    - [ ] Force-close and reopen the app.
    - [ ] Navigate to Week 2. The same 3 items must still be checked.
- [ ] **FR5 (Weekly Progress Summary)**:
    - [ ] When viewing a week with 12 items and 0 are checked, the summary shows "0/12".
    - [ ] After checking 4 items, the summary updates to "4/12" and the progress bar visually reflects this.
- [ ] **FR6 (User Feedback)**:
    - [ ] Checking an item triggers a subtle sound or haptic feedback.
    - [ ] Checked items are visually distinct (dimmed/strikethrough).
- [ ] **NFRs (Usability/Performance)**:
    - [ ] The list scrolls smoothly on a device.
    - [ ] Switching between weeks is instantaneous.
    - [ ] All checkboxes and interactive elements are easy to tap with a finger.