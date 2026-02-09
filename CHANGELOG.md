# Changelog

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
