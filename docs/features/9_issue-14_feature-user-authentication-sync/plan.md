# Implementation Plan: User Authentication & Sync

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Completed (Shifted to API Architecture)

## 1. Architecture & Design
This plan outlines the implementation of a user authentication and data synchronization system using **Firebase Authentication** for identity management and a Custom **Go Backend / PostgreSQL** as the Single Source of Truth for user profiles and progress. 

**IMPORTANT**: We NO LONGER USE FIREBASE FIRESTORE. All client applications MUST communicate with the Go Backend REST API for data synchronization. Do NOT import or use `firebase/firestore` or any Firestore client libraries.

### Component View

-   **Backend (Go / PostgreSQL)**:
    -   `POST /api/v1/auth/sync`: Endpoint to create/update the user profile using the Firebase ID Token.
    -   `Neon` database provides the scalable backend storage infrastructure.
-   **Frontend (Client Application)**:
    -   `lib/firebase.ts` (or equivalent): Firebase App initialization (Auth only).
    -   `services/auth.service.ts`: Service to handle Firebase Authentication and call the Backend API to sync user data.
    -   `ProgessSyncService`: Refactored to communicate with the REST API.

### Data Flow
1. User logs in via Firebase Auth (Google, Apple, etc.)
2. Client receives the Firebase `IdToken` and User Profile info.
3. Client posts the data + token to `POST /api/v1/auth/sync`.
4. Backend verifies the token using Firebase Admin SDK and upserts the user into the `users` PostgreSQL table.

---

## 2. Step-by-Step Implementation

### Step 1: Firebase Setup
-   **Description**: Initialize the Firebase project and enable only necessary services.
-   **Tasks**:
    1.  Create a project on [console.firebase.google.com](https://console.firebase.google.com).
    2.  Enable **Authentication**:
        -   Turn on **Google** provider.
    3.  **DO NOT ENABLE CLOUD FIRESTORE**.

### Step 2: Backend API Integration
-   **Tasks**:
    1. Create `syncUserToBackend(user)` method.
    2. Fetch `POST /api/v1/auth/sync` with `Authorization: Bearer <token>`.

### Step 3: Frontend Integration
-   **Description**: Install SDK and set up auth service.
-   **Tasks**:
    1.  Create `lib/firebase.ts` to initialize Firebase App (Auth only).
    2.  Implement `services/auth.service.ts`:
        -   `loginWithGoogle()`
        -   `logout()`

### Step 4: UI Implementation
-   **Description**: Create Login and Profile pages.
-   **Tasks**:
    1.  **Login Page**: Minimalist, Support OAuth buttons.
    2.  **Profile Page**: User info, Logout button.

### Step 5: Removing Legacy Firestore Code
-   **Tasks**:
    1. Ensure no `Firestore` calls exist in Web, Android, iOS.
    2. Ensure the build does not depend on `firebase-firestore`.

## 3. Verification
-   [x] Firebase Auth users created.
-   [x] PostgreSQL (`users` table) records created/updated automatically.
-   [x] No Firestore dependencies left in the clients.