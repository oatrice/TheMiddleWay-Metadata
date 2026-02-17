# Implementation Plan: User Authentication & Sync

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Draft

## 1. Architecture & Design
This plan outlines the implementation of a user authentication and data synchronization system using **Firebase** (Authentication & Cloud Firestore) as the Backend-as-a-Service (BaaS) platform. This choice provides a robust, real-time sync engine (Firestore) and comprehensive authentication support (Google, Apple, Email Link), addressing the cross-platform synchronization requirements effectively.

The client-side application will interact with Firebase via the `firebase` modular SDK. A new set of services and UI components will be created to manage authentication state and handle data synchronization between LocalStorage and Firestore.

### Component View

-   **Modified Components**:
    -   `ProgressTracker`: The existing logic that manages user progress will be modified to interact with the new `ProgressSyncService`.

-   **New Components**:
    -   **Backend (Firebase Project)**:
        -   **Authentication**: Configuration for Google, Apple, and Email (Magic Link) providers.
        -   **Firestore Database**: NoSQL database with `users` and `user_progress` collections, secured by Firestore Security Rules.
    -   **Frontend (Client Application)**:
        -   `lib/firebase.ts`: Firebase App initialization.
        -   `services/auth.service.ts`: Service to handle Firebase Authentication (signInWithPopup, isSignInWithEmailLink, etc.).
        -   `services/progress.service.ts`: Service to handle Firestore CRUD operations and offline persistence.
        -   `store/user.store.ts`: Global state management for user session and profile.
        -   `pages/login.vue` (or `.tsx`): Login page with "Deep Cosmos" theme.
        -   `pages/profile.vue` (or `.tsx`): Profile page.
        -   `components/SignUpPrompt.vue`: Non-intrusive sign-up prompt.

-   **Dependencies**:
    -   `firebase`: The official Firebase JS SDK.

### Data Model (Firestore)

**Collection: `users`** (Document ID: `uid`)
```json
{
  "email": "user@example.com",
  "displayName": "User Name",
  "photoURL": "https://...",
  "providerId": "google.com",
  "createdAt": "Timestamp"
}
```

**Collection: `user_progress`** (Document ID: `uid`)
```json
{
  "points": 70,
  "meditationMinutes": 1500,
  "streak": 5,
  "progressData": { ... }, // Extended JSON data
  "updatedAt": "Timestamp"
}
```

**Security Rules**:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /user_progress/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

---

## 2. Step-by-Step Implementation

### Step 1: Firebase Setup
-   **Description**: Initialize the Firebase project and enable necessary services.
-   **Tasks**:
    1.  Create a project on [console.firebase.google.com](https://console.firebase.google.com).
    2.  Enable **Authentication**:
        -   Turn on **Google** provider.
        -   Turn on **Apple** provider (requires Apple Developer Account).
        -   Turn on **Email/Passwordless** (Magic Link).
    3.  Enable **Cloud Firestore**:
        -   Create database in production mode.
        -   Apply the Security Rules defined above.
    4.  Get Firebase Config object (apiKey, authDomain, etc.) and add to environment variables (`.env`).

### Step 2: Frontend Integration
-   **Description**: Install SDK and set up auth service.
-   **Tasks**:
    1.  `npm install firebase`.
    2.  Create `lib/firebase.ts` to initialize `initializeApp`.
    3.  Implement `services/auth.service.ts`:
        -   `loginWithGoogle()`: `signInWithPopup(auth, googleProvider)`
        -   `loginWithApple()`: `signInWithPopup(auth, appleProvider)`
        -   `sendMagicLink(email)`: `sendSignInLinkToEmail(auth, email, actionCodeSettings)`
        -   `finishMagicLinkLogin(url)`: `signInWithEmailLink(auth, email, url)`
        -   `logout()`: `signOut(auth)`

### Step 3: UI Implementation (Deep Cosmos Theme)
-   **Description**: Create Login and Profile pages matching the new dark theme.
-   **Tasks**:
    1.  **Login Page**: Minimalist, dark background (Deep Cosmos), Auth buttons (Google, Apple, Email).
    2.  **Profile Page**: User info, Logout button.
    3.  **SignUp Prompt**: "Save your progress to the cloud" banner.

### Step 4: Data Sync Logic
-   **Description**: Sync LocalStorage <-> Firestore.
-   **Tasks**:
    1.  **Initial Migration**:
        -   On `auth.onAuthStateChanged`: if `user` exists and it is the **first login** (check if Firestore doc exists or via flag), read `LocalStorage`.
        -   If `LocalStorage` has data, write to `user_progress/{uid}` in Firestore.
    2.  **Continuous Sync**:
        -   Use `onSnapshot` (real-time listener) on `user_progress/{uid}`.
        -   When data changes in Firestore -> Update Store/LocalStorage (as cache).
        -   When user updates progress locally -> Write to Firestore (if online).

### Step 5: Testing & SBE Scenarios
-   **Description**: Verify against SBE scenarios.
-   **Tasks**:
    1.  **Scenario 1 (Migration)**: Test guest with data -> Login -> Data in Firestore.
    2.  **Scenario 2 (New Device)**: Login on new browser -> Data fetched from Firestore.
    3.  **Scenario 3 (Error)**: Test invalid Magic Link.

## 3. Verification
-   [ ] Firebase Auth users created.
-   [ ] Firestore documents created/updated.
-   [ ] LocalStorage syncs correctly.
-   [ ] UI matches "Deep Cosmos" theme.