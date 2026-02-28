# SBE: User Authentication and Progress Synchronization

> 📅 Created: 2026-02-17
> 🔗 Issue: https://github.com/mdwmediaworld072/TheMiddleWay/issues/14

---

## Feature: User Authentication and Progress Synchronization

To prevent data loss and enable cross-device access, users can sign up or log in to their accounts. Upon the first login, any existing meditation progress from the browser's local storage is migrated to their cloud-based account. Subsequent logins will synchronize the progress, ensuring the user's data is always up-to-date, regardless of the device they use.

### Scenario: Happy Path - First-time login with existing local data

**Given** a guest user has meditation progress stored in their browser's LocalStorage
**When** the user successfully signs up for the first time using a supported authentication provider
**Then** a new user account is created, their local progress is migrated to their cloud account, and the local data is cleared

#### Examples

| localProgress | authProvider | expectedCloudProgress |
|---|---|---|
| `{"meditationMinutes": 70, "streak": 5}` | Google | `{"meditationMinutes": 70, "streak": 5}` |
| `{"meditationMinutes": 1250, "streak": 32}` | Apple ID | `{"meditationMinutes": 1250, "streak": 32}` |
| `{"meditationMinutes": 15, "streak": 1}` | Magic Link (Email) | `{"meditationMinutes": 15, "streak": 1}` |
| `{"meditationMinutes": 0, "streak": 0}` | Google | `{"meditationMinutes": 0, "streak": 0}` |

### Scenario: Edge Case - Returning user logs in on a new device

**Given** a registered user has meditation progress saved in their cloud account
**And** they are using a new device with empty LocalStorage
**When** the user successfully logs into their account
**Then** their cloud progress is fetched and synchronized to the new device's LocalStorage

#### Examples

| userEmail | cloudProgress | initialLocalProgress | expectedFinalLocalProgress |
|---|---|---|---|
| `s.jittaseno@example.com` | `{"meditationMinutes": 1500, "streak": 45}` | `null` | `{"meditationMinutes": 1500, "streak": 45}` |
| `jane.doe@icloud.com` | `{"meditationMinutes": 200, "streak": 10}` | `{}` | `{"meditationMinutes": 200, "streak": 10}` |
| `user@themiddleway.app` | `{"meditationMinutes": 9999, "streak": 108}` | `null` | `{"meditationMinutes": 9999, "streak": 108}` |

### Scenario: Error Handling - Attempting to log in with an invalid Magic Link

**Given** a user has requested a Magic Link to their email address
**When** the user clicks on a link that is expired, already used, or has an invalid token
**Then** the system should display a clear error message on the login page and not log the user in

#### Examples

| linkStatus | userAction | expectedErrorMessage |
|---|---|---|
| Expired | Clicks link after 20 minutes | "This login link has expired. Please request a new one." |
| Already Used | Clicks the same link a second time | "This login link has already been used. Please request a new one if you need to log in again." |
| Invalid Token | Clicks a manually altered link | "Invalid or malformed login link. Please try again." |