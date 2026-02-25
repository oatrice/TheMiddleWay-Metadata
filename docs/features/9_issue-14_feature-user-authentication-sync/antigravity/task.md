# Task: Issue #14 - User Authentication & Sync (MVP Complete)

- [ ] **Infrastructure Setup** <!-- id: 0 -->
    - [x] Create Firebase Project (ID: `the-middle-way-auth`) <!-- id: 1 -->
    - [ ] Initialize Authentication (Google ONLY) (Apple/Magic Link moved to separate issues) <!-- id: 2 -->
    - [x] Initialize Configure Firestore & Security Rules <!-- id: 3 -->
    - [x] Update Environment Variables (`.env`) for Web, Android, iOS <!-- id: 4 -->

- [ ] **Web Implementation (Next.js)** <!-- id: 5 -->
    - [x] Install Firebase SDK & Zustand <!-- id: 6 -->
    - [x] Implement `auth.service.ts` <!-- id: 7 -->
    - [x] Implement `progress.service.ts` (Sync Logic - Partially in AuthService) <!-- id: 8 -->
    - [x] Create Login Page (Deep Cosmos Theme) <!-- id: 9 -->
    - [x] Create Profile Page (Auth Protected) <!-- id: 10 -->
    - [ ] Implement `SignUpPrompt` Component <!-- id: 11 -->
    - [x] **Refine Auth UX** <!-- id: 21 -->
        - [x] Guest Mode (Login Bypass) <!-- id: 22 -->
        - [x] Nav Bar Profile/Sign-In Logic <!-- id: 23 -->
        - [x] Legal Pages (Terms & Privacy) <!-- id: 24 -->
        - [x] Finalize Login Page Style (Sky Blue) <!-- id: 26 -->

- [ ] **Mobile Implementation** <!-- id: 12 -->
    - [x] **Android**: Setup Firebase & Auth UI (Google Auth) <!-- id: 13 -->
        - [x] Implement User Sync to Firestore <!-- id: 27 -->
    - [ ] **iOS**: Setup Firebase & Auth UI (Google Auth) <!-- id: 14 -->
        - [x] Add Firebase SDK via SPM <!-- id: 49 -->
        - [x] Configure `FirebaseApp` in `TheMiddleWayApp` <!-- id: 50 -->
        - [x] Implement Google Sign-In Logic & UI <!-- id: 51 -->
    - [x] **iOS**: Wisdom Garden Feature Parity <!-- id: 52 -->
        - [x] [iOS] Update `WisdomGardenViewModel` to use new Repository
        - [x] [iOS] Verify Parity (Check if data syncs with Web/Android)
        - [ ] [Bug] Fix API/Firestore Switching requiring restart (Issue created): 53 -->
        - [x] Fix Backend Toggle Route (404 Error) <!-- id: 56 -->
        - [x] Implement `FirestoreWisdomGardenRepository` <!-- id: 54 -->
        - [x] Implement Dev Settings (Toggle API/Firestore) <!-- id: 55 -->

- [x] **Wisdom Garden Data Sync** <!-- id: 28 -->
    - [x] **Web**: Connect `useWisdomGarden` to Firestore <!-- id: 29 -->
    - [x] **Android**: Implement `FirestoreWisdomGardenRepository` <!-- id: 30 -->
- [ ] **Parallel Backend Alignment** <!-- id: 31 -->
    - [x] **Go**: Update `internal/model/practice.go` to match Firestore Schema <!-- id: 32 -->
    - [x] **Go**: Implement `SeedData` with Real Content (from `wisdom-garden-data.ts`) <!-- id: 33 -->
    - [x] **Go/Script**: Create Master Data Seeder (Push to Firestore & SQLite) (Admin Tool) <!-- id: 34 -->

- [ ] **Refinements & Bug Fixes**
    - [x] **Android**: Fix Loading State & Guest Mode <!-- id: 35 -->
    - [x] **Android**: Add Guest Mode Toast for Practice Room <!-- id: 36 -->
    - [ ] **Web**: Add Guest Mode Toast for Practice Room & Fix Persistence Error <!-- id: 37 -->

- [ ] **Future / Backlog Tasks** <!-- id: 18 -->
    - [ ] Implement Apple Sign-in (Issue #43) <!-- id: 19 -->
    - [ ] Implement Email/Magic Link (Issue #44) <!-- id: 20 -->
    - [ ] Implement Login History Log (Issue #45) <!-- id: 25 -->
    - [ ] Implement PWA for Full Offline Support (Web) <!-- id: 35 -->

- [ ] **Data Migration & Testing** <!-- id: 15 -->
    - [ ] Implement Merge Logic (Union by Session ID) <!-- id: 16 -->
    - [ ] Verify SBE Scenarios <!-- id: 17 -->

- [ ] **Dev Tools**
    - [x] **Web**: Implement Dev Settings Toggle (Firestore/API) <!-- id: 39 -->
    - [x] **Android**: Implement Dev Settings Toggle (Firestore/API) <!-- id: 40 -->

- [ ] **Backend Scaling (Neon & Multi-tenancy)**
    - [x] **Models**: Add UserID to WeeklyData, Category, PracticeItem <!-- id: 41 -->
    - [x] **Auth**: Implement Firebase Auth Middleware <!-- id: 42 -->
    - [x] **Repository**: Update logic for UserID & Lazy Copy (Master -> User) <!-- id: 43 -->
    - [x] **Database**: Switch from SQLite to Postgres (Neon) <!-- id: 44 -->
    - [x] **Config**: Setup Environment Variables (.env) <!-- id: 45 -->
    - [x] **Audit Logs**: Implement RDBMS Audit Logging (Stdout + DB) <!-- id: 48 -->

- [ ] **Security & Cleanup**
    - [x] **Secrets**: Rotate all keys (Neon, Firebase) & Enforce Env Vars (See Issue #48) <!-- id: 46 -->
    - [x] **Documentation**: Update Backend README with DB Switch Instructions <!-- id: 47 -->

- [x] **Code Review Fixes (Luma)** <!-- id: 60 -->
    - [x] **Backend**: Security & Best Practices <!-- id: 61 -->
        - [x] Remove `service-account.json` & Update `.gitignore` <!-- id: 62 -->
        - [x] Fix `.env.local` syntax <!-- id: 63 -->
        - [x] Fix Auth Middleware Context usage <!-- id: 64 -->
        - [x] Fix Health Check DB Type <!-- id: 65 -->
    - [x] **iOS**: Critical Logic & Error Handling <!-- id: 66 -->
        - [x] Fix ID Parsing in `FirestoreWisdomGardenRepository` <!-- id: 67 -->
        - [x] Fix Error Propagation in `NetworkWisdomGardenRepository` <!-- id: 68 -->
    - [x] **Android**: Memory Leaks & State <!-- id: 69 -->
        - [x] Fix `WisdomGardenViewModel` Race Condition <!-- id: 70 -->
        - [x] Fix `AuthViewModel` Stale State <!-- id: 71 -->
    - [x] **Web**: Anti-patterns <!-- id: 72 -->
        - [x] Fix `ProfilePage` imports <!-- id: 73 -->
        - [x] Fix Policy Page dynamic dates <!-- id: 74 -->
