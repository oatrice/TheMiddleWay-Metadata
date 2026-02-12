# Implementation Plan: Onboarding Feature

> **Status**: Review Required
> **Goal**: Implement a cross-platform Onboarding flow (Web, Android, iOS) introduing "Authentic Wisdom".

## 1. Backend Tradeoff Analysis

### Design Conclusion
**Decision**: Use **Client-Side Storage Only** (Approach A) for this phase.
**Reasoning**: Onboarding occurs *before* authentication. Syncing state to a backend would require complexity (e.g., Device ID tracking or post-login reconciliation) that outweighs the value for a simple "seen/not seen" flag.

### Detail Analysis

| Feature | **Approach A: Client-Side Only** (Chosen) | **Approach B: Backend Sync** |
| :--- | :--- | :--- |
| **Logic Location** | Local Storage / SharedPrefs / UserDefaults | API + DB (User Profile) |
| **User Experience** | Immediate, works offline. | Requires network. |
| **Cross-Device** | No. (Must watch again on new device) | Yes. (Synced after login) |
| **Complexity** | 🟢 Low | 🔴 High (Requires Logic for Pre-login state) |
| **Privacy** | 🟢 High (No data sent) | 🟡 Generic (Data associated with user/device) |
| **Cost/Effort** | 🟢 Minimal | 🔴 Medium (Backend + DB changes) |

---

## 2. Shared Assets (Generated)

Use these assets for the slides across all platforms.

| Slide | Asset Name | Description | Path |
| :--- | :--- | :--- | :--- |
| **1. Welcome** | `welcome_logo` | App Logo & Zen Theme | `onboarding_welcome_logo_1770896268486.png` |
| **2. Authentic Wisdom** | `authentic_wisdom` | Glowing Book/Light | `onboarding_authentic_wisdom_1770896292368.png` |
| **3. Discover Path** | `discover_path` | Philosophy/Science/Art | `onboarding_discover_path_1770896310277.png` |
| **4. Daily Practice** | `daily_practice` | Meditation/Nature | `onboarding_daily_practice_1770896329650.png` |

**Action**: Copy these files to the respective asset directories of each platform during implementation.

---

## 3. Web Implementation Plan (Level B)

> **Goal**: Fully interactive UI with LocalStorage persistence.

### Components
1.  **`hooks/useOnboarding.ts`**:
    *   Manage state: `isCompleted` (boolean).
    *   Effect: Read from `localStorage.getItem('onboarding_completed')` on mount.
    *   Action: `completeOnboarding()` sets `localStorage` and updates state.
2.  **`components/onboarding/OnboardingLayout.tsx`**:
    *   Main container handling the transition between Onboarding and Main App.
3.  **`components/onboarding/WelcomeScreen.tsx`**:
    *   Show `welcome_logo`.
    *   "Get Started" button -> triggers Slide 1.
4.  **`components/onboarding/IntroductionCarousel.tsx`**:
    *   Slides logic (Authentic Wisdom -> Discover -> Daily Practice).
    *   "Next", "Back", "Skip" buttons.
    *   Final "Begin Journey" -> calls `completeOnboarding()`.

### Verification (Web)
*   **Manual**:
    1.  Open app -> See Welcome Screen.
    2.  Refresh -> Still Welcome Screen.
    3.  Click "Skip" -> See Main App.
    4.  Refresh -> See Main App (Persistent).
    5.  Clear LocalStorage -> See Welcome Screen again.

---

## 4. Mobile Implementation Updates

### Android (Jetpack Compose)
*   **Data Layer**: Use `DataStore` (Preferences) instead of raw `SharedPreferences` for modern best practices.
*   **UI**: Use `HorizontalPager` for the carousel.
*   **Assets**: Place generated PNGs in `res/drawable-xxhdpi`.

### iOS (SwiftUI)
*   **Data Layer**: `ref: AppStorage` wrapper for `UserDefaults`.
*   **UI**: `TabView` with `.tabViewStyle(.page)`.
*   **Assets**: Add PNGs to `Assets.xcassets`.
