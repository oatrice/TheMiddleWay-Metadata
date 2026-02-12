# Walkthrough: Onboarding Feature

> **Status**: Implementation Complete (Ready for Review)
> **Goal**: Introduce "Authentic Wisdom" via a cross-platform onboarding flow.

## 1. Web Implementation (Level B)
- **Concept**: Interactive Mock UI with Client-Side Persistence.
- **Key Files**:
    - `hooks/useOnboarding.ts`: Manages `localStorage` state.
    - `components/onboarding/OnboardingScreen.tsx`: Carousel UI using Framer Motion.
    - `app/page.tsx`: Conditionally renders Onboarding or Main Dashboard.
- **Verification**:
    1. Open Web App.
    2. See "Welcome" screen.
    3. Swipe/Click Next through 3 slides.
    4. Click "Begin Journey".
    5. Refresh page -> Should see Main Dashboard (persisted).

## 2. Android Implementation
- **Concept**: Jetpack Compose with DataStore (Modern Android).
- **Key Files**:
    - `data/repository/OnboardingRepository.kt`: DataStore implementation.
    - `ui/viewmodel/OnboardingViewModel.kt`: Handles completion logic.
    - `ui/onboarding/OnboardingScreen.kt`: `HorizontalPager` UI.
    - `MainActivity.kt`: Checks `isOnboardingCompleted` state flow.
- **Assets**: Copied to `app/src/main/res/drawable/`.
- **Verification**:
    1. Launch App.
    2. Experience smooth Pager transition.
    3. Click "Skip" or complete flow.
    4. Restart App -> Should go straight to Home.

## 3. iOS Implementation
- **Concept**: SwiftUI with UserDefaults.
- **Key Files**:
    - `OnboardingService.swift`: `@AppStorage` wrapper.
    - `OnboardingView.swift`: `TabView` with `PageTabViewStyle`.
    - `TheMiddleWayApp.swift`: Root view switching logic.
- **Assets**: Generated `.imageset` folders in `Assets.xcassets`.
- **Verification**:
    1. Launch App (Simulator/Device).
    2. Swipe through pages.
    3. Tap "Begin Journey".
    4. Restart App -> Should see Content View.

## 4. Backend Strategy
- **Decision**: Deferred to Issue #4 ([Feature] Sync Onboarding Status API).
- **Current State**: Client-side storage only. No API calls made during onboarding.
