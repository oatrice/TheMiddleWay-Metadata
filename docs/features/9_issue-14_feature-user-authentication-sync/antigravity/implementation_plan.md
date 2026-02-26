# Implementation Plan: API-Centric Architecture & Network Switcher

## Goal
To transition the application to a fully API-centric architecture, removing direct Firestore dependencies from clients and implementing a flexible environment switcher for backend URLs across all platforms (Web, Android, iOS).

## Key Architectural Decisions
1. **Remove Direct Client-to-Firestore Communication**: All clients will exclusively communicate with the Go backend API. The Go backend is solely responsible for interacting with the database.
2. **Dynamic Network Environment Switcher**: Replaced the binary (Firestore/API) toggles with a multi-state environment switcher.

## Client Implementations

### 1. Web Platform (Next.js)
- **Removal**: Removed `firebase/firestore` imports and code from `useWisdomGarden.ts`.
- **Store**: Updated `useDevSettingsStore.ts` to manage `apiEnvironment` (`render`, `local`, `custom`) and `customApiUrl`.
- **UI**: Added a custom `DevSettingsToggle` in the Profile page using Radio buttons to select the network environment.

### 2. Android Platform (Kotlin / Jetpack Compose)
- **Removal**: Deleted `FirestoreWisdomGardenRepository` and `HybridWisdomGardenRepository`.
- **Store**: Added `apiEnvironment` and `customApiUrl` state management to the `DataStore` via `PersistenceRepository`.
- **Injection**: Added an `Interceptor` in `NetworkModule.kt` to dynamically intercept and rewrite the Retrofit base URL on every request based on the selected environment.
- **UI**: Added Radio buttons to `ProfileScreen` for environment selection.

### 3. iOS Platform (Swift / SwiftUI)
- **Removal**: Deleted `FirestoreWisdomGardenRepository.swift`.
- **Store**: Updated `DevSettingsViewModel` to utilize an `ApiEnvironment` enum backed by `@AppStorage`.
- **Injection**: Refactored `WisdomGardenViewModel` to strictly initialize the `NetworkWisdomGardenRepository`. The repository reads the base URL dynamically from the ViewModel.
- **UI**: Replaced the Toggle in `DevSettingsView` with a `Picker` controlling the API Environment.

## Backend Implementations
- Resolving CORS issues (`gin-contrib/cors`) for `PATCH` requests.
- Deploying the Go API to Render.com connected to the unified Neon Postgres database.
