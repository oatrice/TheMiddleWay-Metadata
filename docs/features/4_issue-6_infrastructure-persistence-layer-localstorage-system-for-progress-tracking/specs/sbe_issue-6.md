# SBE: Local Storage Progress Persistence

> 📅 Created: 2026-02-10
> 🔗 Issue: https://github.com/mdwmediaworld072/TheMiddleWay/issues/6

---

## Feature: Local Storage Progress Persistence

To ensure users don't lose their progress between sessions, the application saves and retrieves their progress data using the browser's local storage. This allows for a seamless experience when they return to the application.

### Scenario: Happy Path - Successfully retrieving saved progress

**Given** the user's progress data is saved in local storage
**When** the application starts and attempts to load progress
**Then** the application state is updated with the loaded progress data

#### Examples

| input_progress_data_in_storage                                                   | expected_loaded_state                                                            |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `{ "currentPath": "Mindfulness", "completedChapters": ["Intro", "Breathing"] }`    | `{ "currentPath": "Mindfulness", "completedChapters": ["Intro", "Breathing"] }`    |
| `{ "currentPath": "Stoicism", "completedChapters": [] }`                           | `{ "currentPath": "Stoicism", "completedChapters": [] }`                           |
| `{ "currentPath": "Ethics", "completedChapters": ["Chapter1", "Chapter2"] }`       | `{ "currentPath": "Ethics", "completedChapters": ["Chapter1", "Chapter2"] }`       |
| `{ "currentPath": "Beginner", "completedChapters": ["Lesson1"] }`                  | `{ "currentPath": "Beginner", "completedChapters": ["Lesson1"] }`                  |

### Scenario: Edge Case - First-time user with no saved progress

**Given** the user has no progress data in local storage
**When** the application starts and attempts to load progress
**Then** the application state is initialized with a default starting progress

#### Examples

| input_storage_value | expected_initial_state                                             |
|---------------------|--------------------------------------------------------------------|
| `(not set)`         | `{ "currentPath": "Introduction", "completedChapters": [] }`       |
| `null`              | `{ "currentPath": "Introduction", "completedChapters": [] }`       |
| `""` (empty string) | `{ "currentPath": "Introduction", "completedChapters": [] }`       |
| `undefined`         | `{ "currentPath": "Introduction", "completedChapters": [] }`       |

### Scenario: Error Handling - Loading corrupted or invalid data

**Given** the local storage contains malformed or invalid progress data
**When** the application attempts to load the progress
**Then** the application should revert to the default starting progress and log a warning

#### Examples

| input_corrupted_data          | expected_outcome                                                              |
|-------------------------------|-------------------------------------------------------------------------------|
| `"{'invalid': 'json'}"`       | `Revert to default state and log "Failed to parse progress data"`             |
| `"just a string"`             | `Revert to default state and log "Failed to parse progress data"`             |
| `"{ \"unexpectedKey\": true }"` | `Revert to default state and log "Invalid progress data schema"`              |
| `12345`                       | `Revert to default state and log "Invalid progress data schema"`              |