# Implementation Plan: iOS Feature Parity

## Goal
Bring the iOS application to feature parity with Web and Android by implementing:
1.  **User Authentication**: Firebase Auth with Google Sign-In.
2.  **Wisdom Garden Sync**: Support for both Firestore-based sync and Authenticated API calls.
3.  **Developer Settings**:- [x] Test switching between API and Firestore mode
- [x] Verify data sync between iOS and Web/Android
-   **Certificates**: Ensure iOS Bundle ID matches Firebase Console and GoogleService-Info.plist.
-   **Dependencies**: Need to add `Firebase/Auth` and `Firebase/Firestore` via Swift Package Manager.

## Proposed Changes

### 1. Firebase Setup
#### [MODIFY] `TheMiddleWay/Sources/App/TheMiddleWayApp.swift`
-   Import `FirebaseCore`.
-   Add `FirebaseApp.configure()` in `init` or `AppDelegate` adapter.

#### [NEW] `TheMiddleWay/Sources/Core/Auth/AuthService.swift`
-   Implement `AuthService` class to handle:
    -   `signInWithGoogle()`
    -   `signOut()`
    -   `currentUser` state publishing.
    -   `getAuthToken()` for API calls.

### 2. Wisdom Garden Repository
#### [MODIFY] `TheMiddleWay/Sources/Features/WisdomGarden/Data/NetworkWisdomGardenRepository.swift`
-   Inject `AuthService`.
-   Add `Authorization: Bearer <token>` header to all requests.

#### [NEW] `TheMiddleWay/Sources/Features/WisdomGarden/Data/FirestoreWisdomGardenRepository.swift`
-   Implement `WisdomGardenRepository` protocol using `FirebaseFirestore`.
-   Logic:
    -   `getWeeklyData`: Listen to `users/{uid}/weekly_practices/{week}`.
    -   Fallback: specific fetching of `master_weeks/{week}` if user data missing.
    -   `togglePractice`: Update local optimistic state then write to Firestore.

#### [MODIFY] `TheMiddleWay/Sources/Features/WisdomGarden/ViewModels/WisdomGardenViewModel.swift`
-   Inject a `RepositoryFactory` or switching logic based on Dev Settings.

### 3. Developer Settings
#### [NEW] `TheMiddleWay/Sources/Features/Settings/DevSettingsViewModel.swift`
-   `@Published var useApiMode: Bool`.
-   Persist preference in `UserDefaults`.

## Verification Plan
### Manual Verification
1.  **Auth**:
    -   Tap "Sign in with Google".
    -   Verify user is logged in and sees Profile.
2.  **API Mode (Go Backend)**:
    -   Enable "Use API Mode" in settings.
    -   Toggle an item -> Verify Backend Log (Audit Log) & Firestore update (via backend sync).
3.  **Firestore Mode**:
    -   Disable "Use API Mode".
    -   Toggle an item -> Verify immediate Firestore update.
    -   Toggle an item -> Verify immediate Firestore update.

### 4. Code Review Fixes
#### Backend
- [ ] **Security**: Remove `service-account.json` and add to `.gitignore`.
- [ ] **Config**: Fix `.env.local` syntax.
- [ ] **Middleware**: Use `c.Request.Context()` in `AuthMiddleware`.
- [ ] **Health Check**: Dynamic DB type response.

#### iOS
- [ ] **Logic**: Fix `extractWeekFromID` to handle `w1_i1` format.
- [ ] **Error Handling**: Propagate errors in `NetworkWisdomGardenRepository`.

#### Android
- [ ] **Optimization**: Use `flatMapLatest` in `WisdomGardenViewModel`.
- [ ] **State**: Observe `authRepository.currentUser` in `AuthViewModel`.

#### Web
- [ ] **Refactor**: Fix `require` import in `ProfilePage`.
- [ ] **Content**: Static date for Policy pages.
