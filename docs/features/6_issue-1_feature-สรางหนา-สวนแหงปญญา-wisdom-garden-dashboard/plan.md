# Implementation Plan: 🌿 Wisdom Garden Dashboard

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Draft

## 1. Architecture & Design
The implementation will follow a component-based, state-driven architecture. A central state holder (ViewModel/Hook) at the screen level will manage the application's state, including the selected week, language, and all practice data. UI components will be stateless, receiving data and callbacks as props, ensuring a predictable and testable data flow.

For this initial phase, all data will be mocked and bundled with the application as per NFR-4. The development will proceed in three distinct phases: Web Mock UI, followed by full Android and iOS implementations.

### Component View
> [!IMPORTANT]
> **Platform Scope Policy:**
> - **Web**: Mock UI only for this phase. (React/Vue/Svelte)
> - **Android**: Full implementation with production-ready code and tests. (Jetpack Compose)
> - **iOS**: Full implementation with production-ready code and tests. (SwiftUI)
>
> **Development Order:** Web Mock UI FIRST → Android Full Implementation SECOND → iOS Full Implementation THIRD.

- **Modified Components**:
  - None. This is a new feature.

- **New Components**:
  - `WisdomGardenScreen`: The main container screen that holds all other components and manages the overall state.
  - `AppHeader`: A reusable header component containing the language switcher and week selector.
  - `LanguageSwitcher`: A button to toggle between 'TH' and 'EN'.
  - `WeekSelector`: A component to display and select weeks 1-8.
  - `WisdomGardenVisualization`: Displays the tree/flower graphic and the score. It will react to score changes.
  - `PracticeChecklist`: A scrollable list that renders `PracticeCategory` sections.
  - `PracticeCategory`: A header component for a group of practices (e.g., "Giving").
  - `PracticeCard`: A component for an individual practice item, containing the description and an interactive checkbox.

- **Dependencies**:
  - **Web**: No new external libraries needed. Standard React/Vue/Svelte setup.
  - **Android/iOS**: No new external libraries are anticipated. Standard UI toolkits (Compose/SwiftUI) are sufficient.

### Data Model Changes
We will define new data structures to represent the practice data. This data will be hardcoded in a mock data source file.

```typescript
// Shared data structure concept (will be adapted for each platform)

// Represents a single practice item
interface PracticeItem {
  id: string;
  title: { en: string; th: string };
  points: number;
  isCompleted: boolean;
}

// Represents a category of practices
interface PracticeCategory {
  id: string;
  title: { en: string; th: string };
  items: PracticeItem[];
}

// Represents the entire state for a given week
interface WeeklyData {
  weekNumber: number;
  categories: PracticeCategory[];
  // Calculated properties
  currentScore: number;
  maxScore: number;
}
```

---

## 2. Step-by-Step Implementation

### Phase 1: Web Mock UI (React)

#### Step 1: Project Scaffolding & Data Modeling
- **Description**: Set up a basic React project structure. Define the data models in TypeScript and create a mock data service that provides hardcoded data for all 8 weeks.
- **Files**:
  - `src/models/practice.ts`: Define `PracticeItem`, `PracticeCategory`, `WeeklyData` interfaces.
  - `src/data/mockData.ts`: Create and export an array of `WeeklyData` for weeks 1-8.
  - `src/services/i18n.ts`: Create a simple translation service with JSON objects for 'en' and 'th' strings.
- **Verification**:
  - Run the project without errors.
  - Unit test the mock data service to ensure it returns data in the correct format.

#### Step 2: Build Static UI Components
- **Description**: Create the visual components for the dashboard. These components will be stateless and receive all data via props. The tree visualization will be a set of static images (e.g., `tree-0.svg`, `tree-1.svg`, etc.) representing different growth stages.
- **Files**:
  - `src/components/AppHeader.tsx`
  - `src/components/WeekSelector.tsx`
  - `src/components/LanguageSwitcher.tsx`
  - `src/components/WisdomGardenVisualization.tsx`
  - `src/components/PracticeChecklist.tsx`
  - `src/components/PracticeCard.tsx`
- **Verification**:
  - Use Storybook or a similar tool to render each component with mock data.
  - Verify that components match the design specified in NFR-1 (colors, layout).
  - Verify responsiveness on mobile and desktop viewport sizes.

#### Step 3: Implement Screen State & Interactivity
- **Description**: Create the main `WisdomGardenScreen` component. Use React hooks (`useState`, `useContext`) to manage the current week, language, and the user's progress data. Wire up the event handlers (`onClick`, `onChange`) to update the state.
- **Files**:
  - `src/screens/WisdomGardenScreen.tsx`:
    - Manage state for `selectedWeek` and `currentLanguage`.
    - Fetch data from `mockData.ts` based on `selectedWeek`.
    - Implement the `handleCheckItem` function which updates the completion status of a practice item.
    - Calculate `currentScore` and pass it down to child components.
    - Pass state and handlers down to the static components.
- **Verification**:
  - Manually test the full user journey as described in the spec.
  - Tapping a checkbox updates the score and the tree image.
  - Changing the week in the `WeekSelector` re-renders the entire dashboard with the correct data.
  - Toggling the language switch updates all text.

### Phase 2: Android Full Implementation (Jetpack Compose)

#### Step 4: Android Data & ViewModel Setup
- **Description**: Translate the data models into Kotlin data classes. Create a `WisdomGardenViewModel` to manage the UI state using `StateFlow` or `MutableState`. Implement the business logic for calculating scores and updating practice item status.
- **Files**:
  - `.../data/model/Practice.kt`: Define `PracticeItem`, `PracticeCategory`, `WeeklyData` data classes.
  - `.../data/repository/PracticeRepository.kt`: A class that provides the hardcoded mock data.
  - `.../ui/wisdomgarden/WisdomGardenViewModel.kt`:
    - Expose UI state via `StateFlow`.
    - Include functions like `selectWeek(week: Int)`, `togglePractice(itemId: String)`, `setLanguage(lang: String)`.
- **Verification**:
  - Unit test the `WisdomGardenViewModel`.
  - Verify that `togglePractice` correctly updates the score.
  - Verify that `selectWeek` correctly loads the data for the selected week.

#### Step 5: Android UI Implementation with Jetpack Compose
- **Description**: Build the UI screens and components using Jetpack Compose, mirroring the structure from the web mock. Connect the Composables to the `WisdomGardenViewModel` to observe state changes and call its functions.
- **Files**:
  - `.../ui/wisdomgarden/WisdomGardenScreen.kt`: The main Composable function that observes the ViewModel.
  - `.../ui/wisdomgarden/composables/AppHeader.kt`
  - `.../ui/wisdomgarden/composables/WisdomGardenVisualization.kt`
  - `.../ui/wisdomgarden/composables/PracticeChecklist.kt`
  - `.../ui/wisdomgarden/composables/PracticeCard.kt`
  - `res/values/strings.xml` & `res/values-th/strings.xml`: For i18n.
- **Verification**:
  - Run the app on an emulator or device.
  - The UI should render correctly with the initial state from the ViewModel.
  - Manually verify the layout matches the design.

#### Step 6: Android Interactivity & Animations
- **Description**: Implement the user interactions and animations. Checkbox taps should call the ViewModel function. Use Compose's animation APIs (`animate*AsState`) to create smooth transitions for score updates and tree growth.
- **Files**:
  - Modify `.../ui/wisdomgarden/composables/*.kt` files to add `onClick` modifiers and animations.
- **Verification**:
  - Manually test the full user journey on a device.
  - Confirm that checking an item triggers a smooth score update and a subtle tree growth animation.
  - Confirm that the checkbox interaction provides immediate visual feedback.

### Phase 3: iOS Full Implementation (SwiftUI)

#### Step 7: iOS Data & ViewModel Setup
- **Description**: Create Swift `structs` for the data models. Develop a `WisdomGardenViewModel` as an `ObservableObject` to manage the UI state using `@Published` properties.
- **Files**:
  - `Models/Practice.swift`: Define `PracticeItem`, `PracticeCategory`, `WeeklyData` structs.
  - `Data/PracticeStore.swift`: A class or struct to provide the mock data.
  - `ViewModels/WisdomGardenViewModel.swift`: The `ObservableObject` managing the app's state.
- **Verification**:
  - Write unit tests for the `WisdomGardenViewModel` using `XCTest`.

#### Step 8: iOS UI Implementation with SwiftUI
- **Description**: Build the UI using SwiftUI Views, mirroring the component structure. The main `WisdomGardenView` will observe the `WisdomGardenViewModel` using `@StateObject`.
- **Files**:
  - `Views/WisdomGardenView.swift`: The main container view.
  - `Views/Subviews/AppHeaderView.swift`
  - `Views/Subviews/WisdomGardenVisualizationView.swift`
  - `Views/Subviews/PracticeChecklistView.swift`
  - `Views/Subviews/PracticeCardView.swift`
  - `en.lproj/Localizable.strings` & `th.lproj/Localizable.strings`: For i18n.
- **Verification**:
  - Run the app in the Xcode simulator.
  - Verify the UI renders correctly and matches the design.

#### Step 9: iOS Interactivity & Animations
- **Description**: Connect user interactions (e.g., `Button` actions, `onTapGesture`) to the ViewModel's methods. Use SwiftUI's `withAnimation` block to animate state changes for the score and tree graphic.
- **Files**:
  - Modify `Views/Subviews/*.swift` files to add interactivity and animations.
- **Verification**:
  - Manually test the full user journey in the simulator and on a physical device.
  - Confirm animations are smooth and provide the "instant gratification" feedback described in the spec.

---

## 3. Verification Plan
*How will we verify success?*

> [!IMPORTANT]
> **Android Build Policy**: MUST use scripts in `Android/scripts/` (e.g., `build_android.sh`) instead of direct `./gradlew` to ensure correct JDK version (Java 21).

### Automated Tests
- [ ] **Unit Tests (ViewModel Logic)**:
  - `WisdomGardenViewModelTests.kt` (Android)
  - `WisdomGardenViewModelTests.swift` (iOS)
  - **Coverage**:
    - Test score calculation when an item is checked/unchecked.
    - Test that selecting a new week loads the correct data set.
    - Test that the maximum score is calculated correctly.
- [ ] **UI Tests (Snapshot/Component Tests)**:
  - `WisdomGardenScreenTest.kt` (Android): Verify the screen renders correctly for different states (e.g., week 1 vs. week 8, 0% score vs. 100% score).
  - `WisdomGardenViewTests.swift` (iOS): Similar snapshot tests for the SwiftUI view.

### Manual Verification
The following checklist should be completed for the Web Mock, Android, and iOS implementations.

- [ ] **FR-1 (Header & Navigation)**:
  - [ ] Verify the language switcher toggles all text between Thai and English.
  - [ ] Verify the selected language persists during the session.
  - [ ] Verify the week selector (1-8) is visible and functional.
  - [ ] Verify selecting a week updates the entire dashboard (score, tree, checklist).
  - [ ] Verify the currently selected week is visually highlighted.
- [ ] **FR-2 (Wisdom Garden Visualization)**:
  - [ ] Verify the tree/flower graphic is displayed.
  - [ ] Verify the tree's growth state corresponds to the current score (e.g., 0/70 = seed, 70/70 = full bloom).
  - [ ] Verify the score is displayed in the format `[Current Score] / [Max Score]`.
- [ ] **FR-3 (Daily Practices Checklist)**:
  - [ ] Verify practice items are grouped correctly under their category headers.
  - [ ] Verify tapping a checkbox marks it as complete and triggers a visual feedback animation.
  - [ ] Verify tapping a completed checkbox un-marks it.
  - [ ] Verify checking/un-checking an item immediately updates the score and tree graphic in real-time.
- [ ] **NFR-1 & NFR-2 (Design & Responsiveness)**:
  - [ ] Verify the color palette ("Deep Zen Blue", "Saffron Orange") is used correctly.
  - [ ] Verify the layout adapts correctly to both mobile portrait and desktop/tablet screen sizes.
- [ ] **NFR-3 (User Experience)**:
  - [ ] Verify all animations (score change, tree growth) are smooth and not jarring.