# Task: Code Review Fixes

- [x] **Backend**: Security & Best Practices
    - [x] Remove `service-account.json` & Update `.gitignore`
    - [x] Fix `.env.local` syntax
    - [x] Fix Auth Middleware Context usage
    - [x] Fix Health Check DB Type

- [x] **iOS**: Critical Logic & Error Handling
    - [x] Fix ID Parsing in `FirestoreWisdomGardenRepository`
    - [x] Fix Error Propagation in `NetworkWisdomGardenRepository`

- [x] **Android**: Memory Leaks & State
    - [x] Fix `WisdomGardenViewModel` Race Condition
    - [x] Fix `AuthViewModel` Stale State

- [x] **Web**: Anti-patterns
    - [x] Fix `ProfilePage` imports
    - [x] Fix Policy Page dynamic dates
