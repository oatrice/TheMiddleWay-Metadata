# Implementation Plan: LocalStorage Persistence for Progress Tracking

> **Refers to**: [#15 Persistence Layer: LocalStorage/UserDefaults/DataStore](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15)
> **Status**: Completed
> **Last Updated**: 2026-02-10

## Implementation Status
- [x] **Web (Next.js)**: Implemented using `PersistenceService` (localStorage) and `ProgressProvider`. Fully tested with Vitest (100% pass) and manually verified.
- [x] **Android (Kotlin)**: Implemented `PersistenceRepository` using DataStore Preferences and Kotlin Serialization. Hilt DI module created. Manually verified via Logcat injection.
- [x] **iOS (Swift)**: Implemented `PersistenceService` using UserDefaults and Codable `UserProgress` model. Manually verified via App init injection.

## 1. Architecture & Design
The implementation will be encapsulated within a dedicated `PersistenceService` module. This service will act as the sole interface for all `LocalStorage` operations related to user progress, abstracting the underlying mechanism from the rest of the application. This approach promotes separation of concerns, simplifies testing, and makes it easier to swap out the persistence layer in the future if needed (e.g., to a backend API).

The service will handle serialization (object to JSON string), deserialization (JSON string to object), and error handling (e.g., `LocalStorage` being unavailable, corrupt data). Application components will interact with this service to save, load, or reset progress data, updating the application's state accordingly.

### Component View
- **Modified Components**:
    - `ApplicationRoot`: The main application component will be modified to call `PersistenceService.loadProgress()` on initial load to restore the user's state.
    - `LessonComponent` (or similar): Components responsible for user progress checkpoints (e.g., lesson completion) will be modified to call `PersistenceService.saveProgress()` with the updated state.
    - `SettingsComponent`: A component (likely new or existing) will contain the UI for resetting progress and will call `PersistenceService.resetProgress()`.
- **New Components**:
    - `src/services/persistenceService.ts`: A new TypeScript module that encapsulates all `LocalStorage` logic.
- **Dependencies**:
    - None. This implementation will use the native Web `LocalStorage` API, which requires no external libraries.

### Data Model Changes
We will define a TypeScript interface to ensure type safety for the progress data being stored.

```typescript
// src/types/progress.ts

/**
 * Defines the structure for user progress data stored in LocalStorage.
 * @property version - Schema version for future data migrations.
 * @property completedLessons - An array of unique identifiers for each completed lesson.
 */
export interface UserProgress {
  version: number;
  completedLessons: string[];
  // Future properties like quizScores, etc., can be added here.
}
```

---

## 2. Step-by-Step Implementation

### Step 1: Create the Persistence Service Module
This step establishes the foundation of our persistence layer with a clear API.

- **Files**:
    - Create `src/services/persistenceService.ts`
    - Create `src/types/progress.ts` (as defined in the Data Model section)
- **Code**:
    - Define a constant for the `LocalStorage` key: `const STORAGE_KEY = 'theMiddleWay.progress';`.
    - Create and export three functions:
        - `saveProgress(progress: UserProgress): void`
        - `loadProgress(): UserProgress | null`
        - `resetProgress(): void`
    - Implement basic error handling to check if `localStorage` is available. If not, the functions should fail gracefully (e.g., log a warning and do nothing).

- **Verification**:
    - The file `src/services/persistenceService.ts` exists.
    - The three core functions are exported.
    - The code compiles without type errors.

### Step 2: Implement `saveProgress` and `loadProgress` Logic
This step implements the core read/write functionality.

- **Files**:
    - Modify `src/services/persistenceService.ts`
- **Code**:
    - **`saveProgress`**:
        - Inside a `try...catch` block:
        - Serialize the incoming `UserProgress` object to a JSON string using `JSON.stringify()`.
        - Call `localStorage.setItem(STORAGE_KEY, serializedData)`.
        - Catch potential errors (e.g., storage quota exceeded) and log them.
    - **`loadProgress`**:
        - Inside a `try...catch` block:
        - Call `localStorage.getItem(STORAGE_KEY)`.
        - If the result is `null`, return `null` (no saved data).
        - If data exists, parse it using `JSON.parse()`.
        - Return the parsed `UserProgress` object.
        - The `catch` block should handle JSON parsing errors (corrupt data). In case of an error, log it and return `null`, fulfilling requirement **FR-7**.
- **Verification**:
    - Unit tests will be written to verify this logic (see Verification Plan).
    - Manually call `saveProgress` from the browser console with a sample object and verify the correct JSON string is stored in `LocalStorage` via DevTools.
    - Manually call `loadProgress` and verify it returns the correct object.
    - Manually set a malformed string in `LocalStorage` and verify `loadProgress` returns `null` without crashing.

### Step 3: Implement `resetProgress` Logic
This step implements the data removal functionality.

- **Files**:
    - Modify `src/services/persistenceService.ts`
- **Code**:
    - **`resetProgress`**:
        - Inside a `try...catch` block:
        - Call `localStorage.removeItem(STORAGE_KEY)`.
        - Catch and log any potential errors.
- **Verification**:
    - Unit tests will verify this logic.
    - Manually save some progress, then call `resetProgress()` from the console. Verify the key is removed from `LocalStorage` in DevTools.

### Step 4: Integrate Service on Application Load
This step ensures that a returning user's progress is restored when the application starts.

- **Files**:
    - Modify the main application entry point (e.g., `src/App.tsx` or `src/main.ts`).
- **Code**:
    - On application initialization (e.g., in a `useEffect` or `onMount` hook):
    - Call `persistenceService.loadProgress()`.
    - If progress data is returned, update the application's global state (e.g., a Redux store, a React Context, or a Svelte store) with the `completedLessons`.
    - If `null` is returned, initialize the application with a default, empty state.
- **Verification**:
    - Manually set valid progress data in `LocalStorage`. Refresh the application and verify the UI reflects the saved state (e.g., completed lessons are checked off).
    - Clear `LocalStorage`. Refresh the application and verify it starts from the beginning.

### Step 5: Integrate `saveProgress` at User Checkpoints
This step ensures progress is saved automatically after significant actions.

- **Files**:
    - Modify the relevant component(s) where progress occurs (e.g., `src/components/Lesson.tsx`).
- **Code**:
    - Identify the action that constitutes a checkpoint (e.g., the `onClick` handler for a "Complete Lesson" button).
    - After the application's state is updated to mark the lesson as complete, call `persistenceService.saveProgress()` with the new, complete state object.
- **Verification**:
    - Start the application with no progress.
    - Complete a lesson.
    - Check `LocalStorage` in DevTools to confirm that the progress has been saved correctly.
    - Refresh the page and confirm the completed lesson is still marked as complete.

### Step 6: Implement the "Reset Progress" UI
This final step provides the user-facing control to reset their journey.

- **Files**:
    - Create or modify a settings component (e.g., `src/components/Settings.tsx`).
- **Code**:
    - Add a "Reset Progress" button to the UI.
    - Create an `onClick` handler for the button.
    - The handler should first show a confirmation dialog (`window.confirm()`) to the user.
    - If the user confirms, the handler should:
        1. Call `persistenceService.resetProgress()`.
        2. Update the application's global state to the initial, empty state.
        3. (Optional but recommended) Redirect the user to the starting page.
- **Verification**:
    - Complete one or more lessons.
    - Navigate to the settings area and click the "Reset Progress" button.
    - Cancel the confirmation and verify nothing happens.
    - Click the button again and confirm the action.
    - Verify that the UI immediately updates to the initial state and that the data is removed from `LocalStorage`.

---

## 3. Verification Plan
How will we verify success?

### Automated Tests
- **File**: `src/services/persistenceService.test.ts`
- [x] **Unit Test 1**: `saveProgress` should correctly stringify an object and call `localStorage.setItem`.
- [x] **Unit Test 2**: `loadProgress` should return a parsed object when valid data exists.
- [x] **Unit Test 3**: `loadProgress` should return `null` when no data exists for the key.
- [x] **Unit Test 4**: `loadProgress` should return `null` and not throw an error when data is malformed JSON.
- [x] **Unit Test 5**: `resetProgress` should call `localStorage.removeItem` with the correct key.
- [x] **Unit Test 6**: All methods should handle cases where `localStorage` is not available (e.g., throws an error on access) and fail gracefully.

### Manual Verification
- [x] **Scenario 1: First-Time User**
    - Open the app in a fresh incognito window.
    - Verify the app starts from the beginning.
    - Verify `LocalStorage` is empty for the app's domain.
- [x] **Scenario 2: Saving Progress**
    - Complete Lesson 1.
    - Verify `theMiddleWay.progress` key in `LocalStorage` contains `{"version":1,"completedLessons":["lesson-1-id"]}`.
- [x] **Scenario 3: Loading Progress**
    - With progress saved from Scenario 2, refresh the page.
    - Verify the app loads with Lesson 1 already marked as complete.
    - Verify the user is guided to start Lesson 2.
- [x] **Scenario 4: Updating Progress**
    - Complete Lesson 2.
    - Verify `theMiddleWay.progress` in `LocalStorage` is updated to include both lesson IDs.
- [x] **Scenario 5: Resetting Progress**
    - Navigate to the settings page and click "Reset Progress".
    - Confirm the action in the dialog.
    - Verify the `theMiddleWay.progress` key is removed from `LocalStorage`.
    - Verify the application UI immediately reflects the reset state (back to the beginning).
- [x] **Scenario 6: Browser Compatibility**
    - Perform a quick check of Scenarios 1-3 in the latest versions of Chrome and Firefox.
- [x] **Scenario 7: Graceful Failure**
    - Disable cookies/site data in browser settings (which often disables `LocalStorage`).
    - Load the application and verify it still runs without crashing, simply operating as a single-session experience without persistence.