# Implementation Plan: Onboarding - Welcome Screen & "Authentic Wisdom" Introduction

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Draft

## 1. Architecture & Design
The implementation will introduce a dedicated onboarding module responsible for handling the first-time user experience. The application's entry point will be modified to include a routing mechanism that checks a persistent flag (`hasCompletedOnboarding`). If the flag is not set, the user is directed to the new onboarding flow. Otherwise, they proceed directly to the main application screen.

The onboarding flow itself will be managed by a dedicated Activity (Android) / View (iOS) that orchestrates two main states: the initial Welcome Screen and the multi-page Introduction Carousel. A `ViewModel` will manage the state (e.g., current page index) and user interactions (next, skip, finish). The `hasCompletedOnboarding` flag will be managed via a simple Repository pattern that abstracts `SharedPreferences` (Android) and `UserDefaults` (iOS).

### Component View
> [!IMPORTANT]
> **Platform Scope Policy:**
> - **Web**: Mock UI only for this phase.
> - **Android**: Full implementation with production-ready code and tests.
> - **iOS**: Full implementation with production-ready code and tests.
>
> **Development Order:** Web Mock UI FIRST → Android Full Implementation SECOND → iOS Full Implementation THIRD.

- **Modified Components**:
    - `MainActivity.kt` / `MainView.swift`: To incorporate the initial routing logic that decides whether to show the onboarding flow or the main app screen.
- **New Components**:
    - **Persistence**:
        - `OnboardingRepository`: A class to abstract the reading/writing of the `hasCompletedOnboarding` boolean flag from the device's persistent storage.
    - **State Management**:
        - `OnboardingViewModel`: A view model to hold the state of the onboarding flow, including the list of intro slides, the current page index, and to handle user actions.
    - **UI (Android)**:
        - `OnboardingActivity.kt`: The main activity to host the entire onboarding flow.
        - `WelcomeFragment.kt`: A fragment for the initial welcome screen.
        - `IntroCarouselFragment.kt`: A fragment containing a `ViewPager2` to display the introduction slides.
        - `IntroSlideFragment.kt`: A reusable fragment to display the content of a single introduction slide.
        - `layout/activity_onboarding.xml`, `layout/fragment_welcome.xml`, `layout/fragment_intro_carousel.xml`, `layout/fragment_intro_slide.xml`: Associated layout files.
    - **UI (iOS - SwiftUI)**:
        - `OnboardingView.swift`: The main view that conditionally displays either the `WelcomeView` or the `IntroCarouselView`.
        - `WelcomeView.swift`: A view for the initial welcome screen.
        - `IntroCarouselView.swift`: A view containing a `TabView` with `PageTabViewStyle` to create the swipeable carousel.
        - `IntroSlideView.swift`: A reusable view for the content of a single introduction slide.
- **Dependencies**:
    - **Android**: `androidx.viewpager2:viewpager2` for the carousel implementation.
    - **iOS**: No new external dependencies. Native SwiftUI components (`TabView`, `UserDefaults`) will be used.

### Data Model Changes
```python
# A simple data structure to represent the content of each intro slide.
# This will be defined in Kotlin (data class) and Swift (struct).

class IntroSlide:
    title: String
    body: String
    # A placeholder for the associated visual asset name
    image_asset_name: String 
```

---

## 2. Step-by-Step Implementation

### Step 1: Persistence Layer for Onboarding Status
- **Goal**: Create a repository to manage the `hasCompletedOnboarding` flag in persistent storage.
- **Android**:
    - **Code**: Create `data/repository/OnboardingRepository.kt`. It will use `SharedPreferences` to get and set a boolean value.
    - **Tests**: Create `OnboardingRepositoryTest.kt`. Write unit tests to verify that the flag can be written and read correctly.
- **iOS**:
    - **Code**: Create `Services/OnboardingService.swift`. It will use `UserDefaults` to get and set a boolean value.
    - **Tests**: Create `OnboardingServiceTests.swift`. Write unit tests to verify the service logic.
- **Verification**: All unit tests for the repository/service pass.

### Step 2: Onboarding ViewModels and Data Structures
- **Goal**: Define the data for the intro slides and create the ViewModel to manage the onboarding state.
- **Android**:
    - **Code**:
        - Create `model/IntroSlide.kt` data class.
        - Create `ui/onboarding/OnboardingViewModel.kt`. It will hold a list of `IntroSlide` objects, the current page index, and expose functions like `onNextClicked()`, `onSkipClicked()`, `onFinishOnboarding()`.
    - **Tests**: Create `OnboardingViewModelTest.kt`. Unit test the logic for page navigation and state changes.
- **iOS**:
    - **Code**:
        - Create `Models/IntroSlide.swift` struct.
        - Create `ViewModels/OnboardingViewModel.swift`. This `ObservableObject` will publish the current page, the slide data, and handle user intent functions.
    - **Tests**: Create `OnboardingViewModelTests.swift` to test the state management logic.
- **Verification**: All ViewModel unit tests pass.

### Step 3: Build Reusable UI for a Single Intro Slide
- **Goal**: Create the visual component for one slide of the "Authentic Wisdom" introduction.
- **Android**:
    - **Code**:
        - Create `layout/fragment_intro_slide.xml` with `ImageView`, `TextView` for title, and `TextView` for body.
        - Create `ui/onboarding/IntroSlideFragment.kt` to bind the `IntroSlide` data to the layout.
- **iOS**:
    - **Code**: Create `Views/Onboarding/IntroSlideView.swift`. This SwiftUI view will take an `IntroSlide` object and display its contents.
- **Verification**:
    - The component can be previewed in Android Studio Layout Editor and SwiftUI Previews.
    - All elements are correctly laid out and support dynamic font sizes.
    - Content descriptions are added for accessibility.

### Step 4: Assemble the Welcome and Carousel Screens
- **Goal**: Build the main onboarding screen, including the initial welcome view and the multi-page carousel.
- **Android**:
    - **Code**:
        - Create `layout/fragment_welcome.xml` and `ui/onboarding/WelcomeFragment.kt`.
        - Create `layout/fragment_intro_carousel.xml` containing a `ViewPager2` and navigation buttons (`Next`, `Back`, `Skip`, etc.).
        - Create `ui/onboarding/IntroCarouselFragment.kt` to manage the `ViewPager2` adapter and UI controls.
        - Create `OnboardingActivity.kt` and `layout/activity_onboarding.xml` to host and navigate between `WelcomeFragment` and `IntroCarouselFragment`.
- **iOS**:
    - **Code**:
        - Create `Views/Onboarding/WelcomeView.swift`.
        - Create `Views/Onboarding/IntroCarouselView.swift` using a `TabView` with `.page` style. It will contain the navigation and skip buttons.
        - Create `Views/Onboarding/OnboardingView.swift` to manage the display logic between the `WelcomeView` and `IntroCarouselView`.
- **Verification**:
    - The onboarding flow can be launched in isolation.
    - The user can transition from the Welcome screen to the carousel.
    - Swiping and using "Next"/"Back" buttons correctly navigates through the slides.
    - UI controls (`Skip`, `Next`, final CTA) are visible and correctly change based on the current slide.

### Step 5: Implement Routing and Final Navigation
- **Goal**: Wire up the app's entry point to check the onboarding status and handle the completion of the flow.
- **Android**:
    - **Code**:
        - In `MainActivity.kt` (or the app's splash/launch activity), inject `OnboardingRepository`. Before setting the main content view, check `repository.hasCompletedOnboarding()`. If `false`, start `OnboardingActivity` and `finish()` the current activity.
        - In `OnboardingViewModel.kt`, on `onSkipClicked()` or `onFinishOnboarding()`, call the repository to set the flag to `true`.
        - In `OnboardingActivity.kt`, observe the ViewModel's "finished" state, and upon completion, launch `MainActivity` and `finish()` the onboarding activity.
- **iOS**:
    - **Code**:
        - In `TheMiddleWayApp.swift` (the main `@main` struct), use the `OnboardingService` to check the flag. Conditionally present `OnboardingView` or the main `ContentView`.
        - In `OnboardingViewModel.swift`, when the skip or finish actions are triggered, call the service to set the flag to `true`. This state change will cause the main app view to redraw, dismissing the onboarding flow.
- **Verification**:
    - A fresh install of the app shows the onboarding flow.
    - Completing the flow and restarting the app goes directly to the main screen.
    - Skipping the flow and restarting the app goes directly to the main screen.

---

## 3. Verification Plan
*How will we verify success?*

> [!IMPORTANT]
> **Android Build Policy**: MUST use scripts in `Android/scripts/` (e.g., `build_android.sh`) instead of direct `./gradlew` to ensure correct JDK version (Java 21).

### Automated Tests
- [ ] **Unit Tests**: `OnboardingRepositoryTest` verifies correct reading/writing of the completion flag.
- [ ] **Unit Tests**: `OnboardingViewModelTest` verifies state transitions (page changes, button visibility logic).

### Manual Verification
- [ ] **Scenario 1: Full Onboarding Flow**
    - [ ] **GIVEN** a fresh app install.
    - [ ] **WHEN** the app is opened, **THEN** the "Welcome Screen" is displayed.
    - [ ] **WHEN** "Get Started" is tapped, **THEN** Intro Screen 1 is displayed with "Next" and "Skip" buttons.
    - [ ] **WHEN** "Next" is tapped, **THEN** Intro Screen 2 is displayed with "Back", "Next", and "Skip" buttons.
    - [ ] **WHEN** "Next" is tapped on the second-to-last screen, **THEN** the final intro screen is displayed with a "Begin Your Journey" button.
    - [ ] **WHEN** "Begin Your Journey" is tapped, **THEN** the user is navigated to the main app screen.
    - [ ] **WHEN** the app is closed and reopened, **THEN** it opens directly to the main app screen.
- [ ] **Scenario 2: Skip Onboarding Flow**
    - [ ] **GIVEN** a fresh app install.
    - [ ] **WHEN** the app is opened and the user navigates to any intro screen.
    - [ ] **WHEN** "Skip" is tapped, **THEN** the user is immediately navigated to the main app screen.
    - [ ] **WHEN** the app is closed and reopened, **THEN** it opens directly to the main app screen.
- [ ] **Non-Functional Requirements**
    - [ ] Verify screen transitions are smooth and without jank on a mid-range test device.
    - [ ] Verify UI elements are visually aligned with design specifications.
    - [ ] Verify accessibility by enabling TalkBack (Android) / VoiceOver (iOS) and navigating the entire flow using only screen reader controls.