# Implementation Plan: User Sync API & Firestore Complete Removal

## Goal
To completely eliminate the `firebase/firestore` dependency from the Web, Android, and iOS clients by migrating the `users` profile data storage to the Go Backend API. Clients will now sync their profile data via a new backend endpoint.

## Backend Implementations

#### [NEW] `internal/model/user.go`
- Define the `User` struct matching the old Firestore schema:
  - `ID` (string, primary key, maps to Firebase UID)
  - `Email` (string)
  - `DisplayName` (string, nullable)
  - `PhotoURL` (string, nullable)
  - `Provider` (string)
  - `CreatedAt` (timestamp)
  - `LastLoginAt` (timestamp)

#### [NEW] `internal/repository/user_repo.go`
- Implement `SyncUser(ctx context.Context, user *model.User) error`
- Use an `INSERT ... ON CONFLICT (id) DO UPDATE` query to create or update the user's `last_login_at`, `email`, `display_name`, and `photo_url`.

#### [NEW] `internal/handler/auth_handler.go`
- Implement `SyncUser` handler.
- Reads the validated user ID from the `AuthMiddleware`.
- Accepts a JSON payload: `{ email, displayName, photoURL, provider }`.
- Calls `userRepo.SyncUser`.

#### [MODIFY] `cmd/server/main.go`
- Add database migration step: `CREATE TABLE IF NOT EXISTS users (...)`
- Register `POST /api/v1/auth/sync` under the protected route group (requires Bearer token).

---

## Client Implementations (Firestore Removal)

### 1. Web Platform
#### [MODIFY] `services/auth.service.ts`
- **Delete:** All `firebase/firestore` imports (`doc`, `setDoc`, `getDoc`, etc.).
- **Update:** `createUserDocument(user)`: Change it to call `POST /api/v1/auth/sync` using `fetch`.
- **Remove:** `export const db` from `lib/firebase.ts`.
- **Remove:** `firebase/firestore` from `package.json` assuming it's unneeded.

### 2. Android Platform
#### [MODIFY] `AuthRepository.kt` or equivalent auth data source
- Update the login success flow to hit `WisdomGardenApi.syncUser()` with the Firebase User profile data.
- **Delete:** The `com.google.firebase:firebase-firestore` dependency in `/app/build.gradle.kts` to guarantee no accidental usage.

### 3. iOS Platform
#### [MODIFY] `AuthenticationViewModel.swift` or equivalent
- Update the login success flow to hit a new `NetworkAuthRepository.syncUser()` endpoint.
- **Delete:** Remove `FirebaseFirestore` from SPM (`Package.swift`) or Xcode project dependencies.

---

## Verification Plan

### Automated Tests
- Call the `POST /api/v1/auth/sync` endpoint via `curl` with a valid Bearer token and verify it creates/updates the record in the Neon database.

### Manual Verification
1. Login to the Web app using Google.
2. Verify no Firestore network calls are made in the browser DevTools.
3. Verify the user record appears correctly in the Neon Postgres `users` table with the updated `last_login_at`.
4. Verify Android and iOS builds succeed without Firestore dependencies.
