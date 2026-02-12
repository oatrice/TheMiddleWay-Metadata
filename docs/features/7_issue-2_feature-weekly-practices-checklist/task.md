# Task Checklist: Wisdom Garden Android Implementation

## Data Layer & Repository (TDD)
- [x] Create Data Models (`PracticeItem`, `PracticeCategory`, `WeeklyData`)
- [x] Implement `WisdomGardenRepository` with Mock Data
    - [x] Create Repository Interface
    - [x] Create Mock Implementation matching Web's data structure
- [x] Implement `WisdomGardenViewModel`
    - [x] Expose `weeklyData` StateFlow
    - [x] Implement `toggleItem` function (immutable update simulation)

## UI Implementation (Jetpack Compose)
- [x] Create `PracticeChecklist` Component (Reusable)
    - [x] Support `readOnly` mode
    - [x] Support `onCheck` callback
- [x] Create `WeeklyPracticesScreen` (Interactive Practice Room)
    - [x] Display interactive checklist
    - [x] Add "Back to Dashboard" navigation
- [x] Refactor `WisdomGardenScreen` (Dashboard)
    - [x] Make Checklist Read-Only
    - [x] Add "Go to Practice Room" button
    - [x] Show identifying Toast on read-only click

## Backend Implementation (Go)
- [x] **Models**: Create `internal/model/practice.go`
    - [x] Struct `Practice` (ID, Week, Category, Title, Points, IsCompleted)
    - [x] *Decision*: Create `Practice` model with seeding logic.
- [x] **Repository**: Create `internal/repository/practice_repo.go`
    - [x] `GetPracticesByWeek(week int) ([]Practice, error)`
    - [x] `TogglePractice(id string, completed bool) (*Practice, error)`
    - [x] Seed data logic
- [x] **Handler**: Create `internal/handler/practice_handler.go`
    - [x] `GetWeeklyPractices` (GET /api/v1/wisdom-garden/weeks/:week)
    - [x] `TogglePractice` (POST /api/v1/wisdom-garden/practices/:id/toggle)
    - [x] Aggregation logic for `WeeklyData` response
- [x] **Router**: Register routes in `cmd/server/main.go`
- [x] **Verification**:
    - [x] Test endpoints with `curl`

## Android Network Integration
- [x] Add Dependencies (Retrofit, OkHttp, Gson)
- [x] Create `WisdomGardenApi` Interface
- [x] Implement `NetworkWisdomGardenRepository` with caching/optimistic updates
- [x] Setup `NetworkModule` (DI) and bind `NetworkWisdomGardenRepository`
- [x] Configure Network Security for localhost (10.0.2.2)

## iOS Implementation (SwiftUI)
- [x] **Data Layer**
    - [x] Create `PracticeItem` and `WeeklyData` Structs (Codable)
    - [x] Implement `NetworkWisdomGardenRepository` (URLSession)
- [x] **ViewModel**
    - [x] Create `WisdomGardenViewModel` (ObservableObject)
    - [x] Implement `fetchWeeklyData` and `togglePractice`
- [x] **UI Components**
    - [x] `WisdomGardenScreen` (Main View) - Integrated into ContentView
    - [x] `AppHeader` (Title & Theme Toggle) - Use NavigationBar
    - [x] `WeekSelector` (Horizontal Scroll)
    - [x] `WisdomTree` (Visualization)
    - [x] `PracticeChecklist` & `PracticeCard`
- [x] **Navigation**
    - [x] Implement Dashboard (Read-only) -> Practice Room (Interactive) flow
- [x] **Verification**
    - [x] Verify functionality in Simulator (Localhost connection)

## Navigation
- [x] Add `WeeklyPractices` route to Navigation Graph (Implemented via local state in WisdomGardenRoute)
- [x] Connect Dashboard -> Practice Room -> Dashboard

## Verification
- [x] Verify Android Build (./gradlew assembleDebug)
- [x] Verify Backend API (curl)
- [x] Verify Read-Only Dashboard behavior (Manual)
- [x] Verify Interactive Practice Room behavior (Manual)
- [x] Verify Interactive Practice Room behavior (Manual)
- [x] Verify State Sync (updates in Practice Room reflect on Dashboard) (Manual)

## Code Review Refactoring
- [x] **Android**
    - [x] Fix Race Condition in `NetworkWisdomGardenRepository`
    - [x] Security: Enable Minification & Split Network Config (Debug/Release)
    - [x] CI: Skip Release workflow on PRs
- [x] **Backend**
    - [x] Fix Non-deterministic Category Order (Sort Keys)
    - [x] Return 404 for `RecordNotFound` in Toggle
- [x] **iOS**
    - [x] Implement Caching in `loadWeeklyData`
