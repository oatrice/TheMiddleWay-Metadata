# Implementation Plan - Wisdom Garden Android

Mirror the Web implementation: Separation of "Viewing" (Dashboard) and "Doing" (Practice Room).

## Architecture
- **MVVM**: ViewModel holds the `WeeklyData` state.
- **Repository**: Provides data (Mock/Local Room).
- **UI**: Jetpack Compose.

## Proposed Changes

### 1. Data Layer
#### [NEW] Data Models
- `data/model/PracticeItem.kt`: id, title, points, isCompleted
- `data/model/PracticeCategory.kt`: id, title, items
- `data/model/WeeklyData.kt`: weekNumber, categories

### 2. Repository
#### [NEW] WisdomGardenRepository
- Interface: `getWeeklyData(week: Int): Flow<WeeklyData>`, `toggleItem(week: Int, itemId: String)`
- Implementation: `MockWisdomGardenRepository` (Hardcoded similar to Web's `wisdom-garden-data.ts`)

### 3. ViewModel
#### [MODIFY] WisdomGardenViewModel
- Expose `uiState` with `WeeklyData`.
- Function `togglePractice(itemId: String)` -> calls Repository.

### 4. UI Components
#### [NEW] `Checklist` Components
- `ui/wisdomgarden/components/PracticeCard.kt`:
    - Props: `item`, `onCheck`, `readOnly`
    - Logic: If `readOnly`, click shows Toast/Warning.
- `ui/wisdomgarden/components/PracticeChecklist.kt`:
    - Renders categories & items.

#### [MODIFY] WisdomGardenScreen (Dashboard)
- Use `PracticeChecklist` with `readOnly = true`.
- Add Button: "Go to Practice Room".

#### [NEW] WeeklyPracticesScreen (Practice Room)
- Route: `weekly_practices`
- Use `PracticeChecklist` with `readOnly = false`.
- Back button to Dashboard.

## Verification Plan

### Automated Tests
- [x] Run `./gradlew assembleDebug` (Android)
- [x] Backend `go build` and `curl` tests.

### Manual Verification
- [x] Android: Verified Read-only Dashboard and Interactive Checkbox.
- [x] Backend: Verified API endpoints.
- [ ] iOS: Verify similar behavior in Simulator.

## Phase 4: iOS Implementation (SwiftUI)

### Architecture
- **MVVM**: `WisdomGardenViewModel` -> `WisdomGardenScreen`.
- **Repository**: `NetworkWisdomGardenRepository` using `URLSession`.
- **UI**: SwiftUI Components mirroring Android/Web.

### Steps
1.  **Data**: Define `Codable` structs matching Backend JSON.
2.  **Repo**: Implement network calls to `http://localhost:8080`.
3.  **UI**: Build `WisdomGardenScreen` with `WeekSelector`, `WisdomTree`, and `PracticeChecklist`.
4.  **Navigation**: Implement Read-only Dashboard and Interactive Practice Room.k items toggle state.
    - Check score updates.
3.  **Sync**:
    - Return to Dashboard -> verify state reflects changes.
