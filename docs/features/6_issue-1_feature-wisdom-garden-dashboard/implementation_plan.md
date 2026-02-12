# Implementation Plan - Wisdom Garden Dashboard (Web Mock UI)

## Goal Description
Implement the "Wisdom Garden" (สวนแห่งปัญญา) dashboard as the main landing page of the application. This dashboard visualizes the user's spiritual progress as a growing tree and provides a weekly checklist of practices. This phase focuses on the Web Mock UI using React/Next.js and hardcoded data.

## User Review Required
> [!IMPORTANT]
> This implementation will **replace** the current content of `app/page.tsx`. The existing "Welcome Back" dashboard will be overwritten by the new Wisdom Garden design.

## Proposed Changes

### Data & Models
#### [NEW] [wisdom-garden.ts](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/lib/types/wisdom-garden.ts)
- Define interfaces: `PracticeItem`, `PracticeCategory`, `WeeklyData`.

#### [NEW] [wisdom-garden-data.ts](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/lib/data/wisdom-garden-data.ts)
- Export mock data for 8 weeks containing practice categories and items.

### Components
#### [NEW] [components/features/wisdom-garden](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/components/features/wisdom-garden)
Create new directory for feature-specific components:
- `AppHeader.tsx`: Container for controls.
- `WeekSelector.tsx`: Selector for weeks 1-8.
- `WisdomGardenVisualization.tsx`: Tree growth visualization based on score.
- `PracticeChecklist.tsx`: List of practice categories.
- `PracticeCategory.tsx`: Section header for practices.
- `PracticeCard.tsx`: Individual practice item with checkbox.

### Pages
#### [BACKUP] [app/page.backup.tsx](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/app/page.backup.tsx)
- Backup existing `app/page.tsx` as `app/page.backup.tsx`. The existing dashboard (Library, Courses links) will be useful for future features.

#### [MODIFY] [app/page.tsx](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/app/page.tsx)
- Replace existing content with `WisdomGardenScreen` logic.
- Manage state for `selectedWeek` and `weeklyData`. (Language support deferred to future issue)
- Implement `handleCheckItem` to update local state and score.

## Verification Plan

### Automated Tests
- Run `npm run dev` to verify the application builds and runs without errors.
- (Optional) Add unit tests for `handleCheckItem` logic if complex.
- [x] Run `./gradlew :app:assembleDebug` to ensure compilation.
- [x] Verified fix for `clickable` Indication runtime crash.

### Manual Verification
1.  **Open the app**: Verify the "Wisdom Garden" dashboard loads by default.
2.  **Week Selection**: Click week numbers (1-8) and verify content updates (score, tree stage, checklist).
3.  **Checklist Interaction**:
    - Click a checkbox on a practice item.
    - Verify the item is marked as completed.
    - Verify the score increases immediately.
    - Verify the tree visualization updates (if score crosses a threshold).
4.  **Responsiveness**: Check layout on both mobile and desktop views.

### Phase 2: Android Implementation (Jetpack Compose)

#### Step 1: Data Layer & Domain
- **Description**: Define data classes and a repository to provide mock data.
- **Files**:
    - `com.oatrice.themiddleway.data.model.PracticeItem`: Data class.
    - `com.oatrice.themiddleway.data.model.WeeklyData`: Data class.
    - `com.oatrice.themiddleway.data.repository.WisdomGardenRepository`: Interface and Mock Implementation.
    - `com.oatrice.themiddleway.di.AppModule`: Provide Repository via Hilt.

#### Step 2: ViewModel
- **Description**: Manage state for the Wisdom Garden screen.
- **Files**:
    - `com.oatrice.themiddleway.ui.wisdomgarden.WisdomGardenViewModel`: Holds `uiState` (week, score, checklist).

#### Step 3: UI Components
- **Description**: Create Compose/Material3 components matching the Web Mock UI.
- **Files**:
    - `com.oatrice.themiddleway.ui.wisdomgarden.WisdomGardenScreen`: Main screen.
    - `com.oatrice.themiddleway.ui.wisdomgarden.components.AppHeader`: Header (No Language Switcher).
    - `com.oatrice.themiddleway.ui.wisdomgarden.components.WeekSelector`: Horizontal pager or list for weeks.
    - `com.oatrice.themiddleway.ui.wisdomgarden.components.WisdomTree`: Visualization of the tree.
    - `com.oatrice.themiddleway.ui.wisdomgarden.components.PracticeChecklist`: Recyclable list of items.

#### Step 4: Navigation
- **Description**: Add the new screen to the navigation graph.
- **Files**:
    - `com.oatrice.themiddleway.ui.navigation.AppNavigation`: Add `WisdomGarden` route and set as start destination.

### Navigation
- [x] Update `MainActivity` to set `WisdomGardenScreen` as the start destination.
- [x] Verify build success.

## Verification Result
- Android Build: **SUCCESS** (`./gradlew assembleDebug`)
- Android features: Read-only Dashboard, Interactive Practice Room, Network Integration.
- Backend Status: **COMPLETE** (Go, Clean Architecture, SQLite)

## Phase 3: Backend Implementation (Go)

### Architecture
- **Clean Architecture**: `cmd` -> `internal/handler` -> `internal/service` -> `internal/repository` -> `internal/model`.
- **Database**: SQLite with GORM.
- **API**: REST endpoints for getting weekly data (`GET`) and toggling practices (`POST`).

### Key Components
- `internal/model/practice.go`: `Practice` struct with ID (UUID), Week, Category, Title, Points, IsCompleted.
- `internal/repository/practice_repo.go`: `PracticeRepository` with logic to fetch by week and toggle status. Includes **Seeding Logic** for initial data.
- `internal/handler/practice_handler.go`: Aggregates flat practice list into `WeeklyData` hierarchy (Categories -> Items) for frontend consumption.
- `cmd/server/main.go`: Registers `/api/v1/wisdom-garden` routes.

## Phase 4: iOS Implementation (SwiftUI)

### Goal
Implement the Wisdom Garden feature on iOS, achieving parity with the Android and Web implementations.

### Steps
1.  **Data Layer**:
    - Create `PracticeItem` and `WeeklyData` structs (`Codable`).
    - Create `WisdomGardenRepository` protocol.
    - Implement `NetworkWisdomGardenRepository` using `URLSession` to connect to Backend (`http://localhost:8080`).
    - *Note*: iOS Simulator uses `localhost` directly to access Mac's ports.

2.  **ViewModel**:
    - Create `WisdomGardenViewModel` (`ObservableObject`).
    - Expose `weeklyData` (`Published`).
    - Implement `togglePractice(id)` method.

3.  **UI Components** (SwiftUI):
    - `WisdomGardenScreen.swift`: Main view with `NavigationView`? Or custom navigation state.
    - `AppHeader.swift`: Title and Theme Toggle.
    - `WeekSelector.swift`: Horizontal scroll or simple HStack for week numbers.
    - `WisdomTree.swift`: Image/View representing tree growth.
    - `PracticeChecklist.swift`: List of categories and items.
    - `PracticeCard.swift`: Individual row with checkbox.

4.  **Navigation**:
    - Implement the "Read-only Dashboard" -> "Interactive Practice Room" flow if following Android's latest pattern.
    - Or keep it simple if iOS patterns differ (e.g. standard NavigationLink). *Decision: Follow Android's "Dashboard + Practice Room" specific flow for consistency.*

### Verification
- Run via Xcode Simulator.
- Verify connection to backend (ensure Server is running).
- Verify Checkbox state persistence.
