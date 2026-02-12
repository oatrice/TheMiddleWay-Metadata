# Changelog

## [0.7.0] - 2026-02-12

### Added
- **Feature Planning (Weekly Practices Checklist):**
  - Added comprehensive documentation for the upcoming "Weekly Practices Checklist" feature.
  - Includes detailed analysis, implementation plan, specifications, and a pending features report to guide development.

## [0.6.0] - 2026-02-12

### Added
- **Wisdom Garden Dashboard (All Platforms):** logic and UI implementation for the Wisdom Garden feature.
  - **Android:**
    - Full implementation of `WisdomGardenScreen` with `WisdomTree` (visualization), `WeekSelector`, and `PracticeChecklist`.
    - Room Database integration for persisting weekly progress and scores.
    - **Auto-seeding logic:** Database automatically populates with 8 weeks of initial data on first launch via `RoomDatabase.Callback`.
  - **Web:**
    - `WisdomGardenVisualization` component with dynamic tree growth stages.
    - Interactive `PracticeChecklist` with immutable state management.
    - Dynamic `maxScore` calculation based on actual practice items.
- **Test Plan:** Created `TEST_PLAN.md` incorporating rigorous test cases from code reviews (Persistence, Localization, Workflows).

### Fixed
- **Android Compilation:** Resolved critical issue with `toggleTheme` signature mismatch in `MainViewModel`.
- **Android Architecture:** Refactored `WisdomGardenScreen` to properly separate ViewModel injection using `WisdomGardenRoute` wrapper.
- **Android UI:** Restored high-fidelity Bottom Navigation with custom theming in `MainScreenBackup`.
- **Web Logic:** Fixed `maxScore` being hardcoded to 70 (now dynamically calculated to 40).
- **Web State Mutation:** Fixed anti-pattern in `handleCheckItem` by implementing proper immutable state updates.
- **CI/CD (iOS):** Fixed `auto-tag.yml` workflow to correctly strip quotes from `MARKETING_VERSION` and strictly validate unique project files to prevent ambiguity.

### Changed
- **Documentation:** Updated `code_review.md` findings and resolutions.

## [0.5.0] - 2026-02-11

### Added

- **CSV Ingestion Documentation:** Introduced comprehensive planning for the CSV data ingestion feature, including analysis, technical specifications, and test data fixtures.
- **Backend Architecture:** Finalized and documented the Go backend architecture.
- **CI:** Implemented a GitHub Actions workflow to automatically create and push Git tags when the `VERSION` file is updated.
- **Deployment Documentation:** Created `DEPLOYMENT_URLS.md` to provide a central reference for application links for QA and users.
- **Code Review:** Added a formal `code_review.md` report with initial suggestions for CSV testing.

### Changed

- **Project Roadmap:** Updated `ROADMAP.md` to prioritize the CSV data ingestion feature.
- **Developer Prompts:** Overhauled prompts for Android, iOS, Backend, and Frontend to align with new architectural decisions and improve development guidance.

### Fixed

- **Documentation:** Removed a reference to a missing screenshot in a feature testing guide.

## [0.4.0] - 2026-02-11

### Added

- **Persistence Layer Documentation:** Introduced comprehensive documentation for the persistence layer, including analysis, planning, and technical specifications.
- **Code Review Process:** Added a formal code review report to identify and track key issues, starting with the `UserProgress` data schema.
- **Feature Testing Guide:** Created a dedicated testing guide for the Light/Dark theme feature.
- **CI:** Implemented a new GitHub Actions workflow to automatically create and push Git tags when the `VERSION` file is updated.
- **Documentation:** Created `DEPLOYMENT_URLS.md` to provide a central reference for application links for QA and users.

### Changed

- **Project Roadmap:** Updated `ROADMAP.md` to reflect progress on CI/CD and to outline the development plan towards v0.2.0.
- **Testing Guide:** Refined the main `TESTING_GUIDE.md` to better support development builds.
- **Developer Prompts:** Overhauled and simplified developer prompts for Android, iOS, and Frontend to streamline the development process.
- **Documentation:** Updated the persistence layer testing guide by removing a reference to a missing screenshot.

## [0.3.0] - 2026-02-10

### Added

- **Design System Foundation:** Implemented the foundational colors and typography, establishing the core visual identity for the project.
- **Development Workflow & Documentation:**
  - Introduced structured templates for feature analysis, planning, and specifications to streamline development.
  - Added a comprehensive `TESTING_GUIDE.md` with manual testing steps for Light/Dark theme functionality.
  - Created `THEME_OVERVIEW.md` to document the Light/Dark mode implementation details.
  - Added a `code_review.md` report to track and document critical issues.

### Changed

- **Roadmap:** Updated `ROADMAP.md` to restructure the v0.2.0 milestone, prioritizing architecture and theme implementation.
- **Developer Prompts:** Standardized and enhanced prompt templates for all platforms (Android, iOS, Frontend, Backend) to improve development consistency and clarity.

### Fixed

- **Documentation:** Corrected formatting issues with truncated headers in various documentation files.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.2.0] - 2026-02-09

### Added

- **Android Platform Initialized (v0.1.0)**
  - Jetpack Compose with Material 3
  - Hilt dependency injection
  - Room database configuration
  - Material Icons Extended
  - HomeScreen with Welcome Card, Quick Actions, Recent Activity
  - Bottom Navigation with 4 tabs

- **iOS Platform Initialized (v0.1.0)**
  - SwiftUI with iOS 17+ target
  - MVVM architecture
  - AppColors and AppTypography matching design system
  - HomeView with full UI components
  - TabView navigation with 4 tabs

### Changed

- Updated README with platform status table and quick start guides
- All platforms now share consistent "Warm Modern Sanctuary" design system

---

## [0.1.1] - 2026-02-06

### Changed

- Moved feature documentation to root `docs/features/`.
- Promoted `README.md`, `ROADMAP.md`, `CHANGELOG.md` to repository root.
- Updated root README to describe multi-platform structure.

---

## [0.1.0] - 2026-02-05

### Added

- **Initial Project Setup**
  - Next.js 16.1.6 with App Router and TypeScript
  - Tailwind CSS v4 for styling
  - Framer Motion for animations
  - Lucide React for iconography

- **Design System (Warm Modern Sanctuary)**
  - Custom color palette: Ivory, Sage, Slate, Sand
  - Typography: Playfair Display (headings) + Inter (body)
  - Custom border-radius: `rounded-pill` (40px), `rounded-card` (1rem)
  - Mobile-first responsive configuration

- **Folder Structure**
  - `/components/ui` - Atomic components
  - `/components/layout` - Navigation and headers
  - `/lib` - Utility functions
  - `/hooks` - Custom React hooks

- **Initial Shell**
  - Root layout with Google Fonts
  - Mobile Navigation Bar (fixed bottom) with 4 tabs
  - Dashboard placeholder page
  - Library, Courses, Profile placeholder pages

### Technical Details

- Viewport configured for mobile-first with safe-area support
- Static page generation for all routes
- ESLint configuration included
