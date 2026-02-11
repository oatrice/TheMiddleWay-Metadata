# The Middle Way - Roadmap

แผนพัฒนาแอปพลิเคชัน "The Middle Way" สำหรับการเรียนรู้และ mindfulness

**อัปเดตล่าสุด:** 2026-02-11

---

## 🎯 Release Strategy

### Versioning (Semantic Versioning)
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

### Current Versions
| Platform | Version | Tag | Status |
|----------|---------|-----|--------|
| Web | 0.4.0 | `v0.4.0` | 🔄 Foundation (Vercel Deploy ✅) |
| Android | 0.3.1 | `v0.3.1` | 🔄 Foundation (CI ✅) |
| iOS | 0.3.1 | `v0.3.1` | 🔄 Foundation (CI ✅) |
| Backend | 0.1.0 | — | 🔄 Foundation (CI ✅) |

---

## 🚀 Milestones

### 📌 [v0.1.0 - Project Scaffolding](https://github.com/oatrice/TheMiddleWay-Metadata/releases/tag/v0.1.0) ✅ RELEASED
**Released:** 2026-02-09

| ID | Title | Status |
|---|---|---|
| [#3](https://github.com/oatrice/TheMiddleWay-Metadata/issues/3) | [Setup] Project Scaffolding: React + Tailwind CSS | ✅ Complete |
| [#4](https://github.com/oatrice/TheMiddleWay-Metadata/issues/4) | [Setup] Android Project Scaffolding | ✅ Complete |
| [#7](https://github.com/oatrice/TheMiddleWay-Metadata/issues/7) | [Setup] iOS Project Scaffolding | ✅ Complete |

---

### 📌 [v0.2.0 - Foundation](https://github.com/oatrice/TheMiddleWay-Metadata/milestone/1) 🔄 IN PROGRESS
**Target:** 2026-02-16 | **Issues:** 5 open, 5 closed

| Priority | ID | Title | Status |
|----------|---|---|---|
| 1 | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | Implement Light/Dark Theme Support (Warm Modern vs Deep Cosmos) | ✅ Complete |
| 2 | [#14](https://github.com/oatrice/TheMiddleWay-Metadata/issues/14) | [Design] Design System Implementation | ✅ Complete |
| 3 | [#15](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15) | [Infrastructure] Persistence Layer: LocalStorage/UserDefaults/DataStore | ✅ Complete |
| 4 | [#16](https://github.com/oatrice/TheMiddleWay-Metadata/issues/16) | [Data] CSV Data Ingestion & Logic | ✅ Complete |
| 5 | [#12](https://github.com/oatrice/TheMiddleWay-Metadata/issues/12) | [Architecture] iOS SPM Modularization | 🔲 Todo |
| 6 | [#11](https://github.com/oatrice/TheMiddleWay-Metadata/issues/11) | [Architecture] Android Multi-Module Setup | 🔲 Todo |
| 7 | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) | [DevOps] CI/CD Pipeline Setup | ✅ Complete |
| 8 | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) | [DevOps] Automated Testing Framework | 🔲 Todo |
| 9 | [#18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18) | [DevOps] iOS TestFlight Setup & Distribution | 🔲 Todo |
| 10 | [#20](https://github.com/oatrice/TheMiddleWay-Metadata/issues/20) | [DevOps] Android CI/CD & Automated APK Build | 🔲 Todo |
| 11 | [#24](https://github.com/oatrice/TheMiddleWay-Metadata/issues/24) | [Quality] Epic: Observability & Reliability | 🔲 Todo |
| 12 | [#21](https://github.com/oatrice/TheMiddleWay-Metadata/issues/21) | [Quality][Android] Logging + Crashlytics + LeakCanary | 🔲 Todo |
| 13 | [#22](https://github.com/oatrice/TheMiddleWay-Metadata/issues/22) | [Quality][iOS] Logging + Crashlytics | 🔲 Todo |
| 14 | [#23](https://github.com/oatrice/TheMiddleWay-Metadata/issues/23) | [Quality][Web] Logging + Monitoring | 🔲 Todo |

---

### 📌 [v0.3.0 - Core Features](https://github.com/oatrice/TheMiddleWay-Metadata/milestone/2)
**Target:** 2026-02-28

| Priority | ID | Title | Status |
|----------|---|---|---|
| 1 | [#1](https://github.com/mdwmediaworld072/TheMiddleWay/issues/1) | 🌿 สวนแห่งปัญญา (Wisdom Garden Dashboard) | 🔲 Todo |
| 2 | [#2](https://github.com/mdwmediaworld072/TheMiddleWay/issues/2) | 📝 ห้องปฏิบัติธรรม (Weekly Practices & Checklist) | 🔲 Todo |
| 3 | [#12](https://github.com/mdwmediaworld072/TheMiddleWay/issues/12) | Navigation System: Bottom Tab Bar & Week Navigation | 🔲 Todo |
| 4 | [#11](https://github.com/mdwmediaworld072/TheMiddleWay/issues/11) | Onboarding: Welcome Screen & "Authentic Wisdom" Introduction | 🔲 Todo |
| 5 | [#28](https://github.com/oatrice/TheMiddleWay-Metadata/issues/28) | [Feature] Category Management UI: CRUD for 11 Core Categories | 🔲 Todo |
| 6 | [#27](https://github.com/oatrice/TheMiddleWay-Metadata/issues/27) | [Feature] Multi-format Data Import: Excel & JSON | 🔲 Todo |
| 7 | [#29](https://github.com/oatrice/TheMiddleWay-Metadata/issues/29) | [Feature] Data Deletion & Cleanup: Remove/Archive Ingested Content | 🔲 Todo |

---

### 📌 v0.4.0 - Enhanced UX
**Target:** 2026-03-15

| Priority | ID | Title | Status |
|----------|---|---|---|
| 1 | [#7](https://github.com/mdwmediaworld072/TheMiddleWay/issues/7) | Bilingual Support (i18n): EN/TH Toggle Framework | 🔲 Todo |
| 2 | [#17](https://github.com/oatrice/TheMiddleWay-Metadata/issues/17), [#13](https://github.com/mdwmediaworld072/TheMiddleWay/issues/13) | [Animation] Micro-interactions & Motion Design | 🔲 Todo |
| 3 | [#8](https://github.com/mdwmediaworld072/TheMiddleWay/issues/8) | The Wisdom Wheel: Radial Progress Chart Visualization | 🔲 Todo |

---

### 📌 v0.5.0 - Premium Features
**Target:** 2026-03-31

| Priority | ID | Title | Status |
|----------|---|---|---|
| 1 | [#9](https://github.com/mdwmediaworld072/TheMiddleWay/issues/9) | Audio Library: Meditation Players for Urban Lifestyles | 🔲 Todo |
| 2 | [#10](https://github.com/mdwmediaworld072/TheMiddleWay/issues/10) | AI Dhamma: Soft-bubble Chat Interface | 🔲 Todo |
| 3 | [#14](https://github.com/mdwmediaworld072/TheMiddleWay/issues/14) | 🔐 User Authentication & Sync | 🔲 Todo |
| 4 | [#30](https://github.com/oatrice/TheMiddleWay-Metadata/issues/30) | [Future] Admin UI for Content Management (iOS/Android) | 🔲 Todo |

---

### 📌 [v1.0.0 - Production](https://github.com/oatrice/TheMiddleWay-Metadata/milestone/3)
**Target:** 2026-04-30

| Priority | ID | Title | Status |
|----------|---|---|---|
| 1 | - | App Store / Play Store Submission | 🔲 Todo |
| 2 | [#5](https://github.com/oatrice/TheMiddleWay-Metadata/issues/5) | Vercel Production Deployment | 🔲 Todo |
| 3 | [#6](https://github.com/oatrice/TheMiddleWay-Metadata/issues/6) | GoDaddy Domain Configuration | 🔲 Todo |

---

## 🔧 DevOps & Infrastructure

### CI/CD Pipeline
| Platform | Tool | Auto-Tag | Status | Issue |
|----------|------|----------|--------|-------|
| Web | GitHub Actions + Vercel | ✅ `v0.4.0` | ✅ Configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) |
| Backend | GitHub Actions (Go CI) | ✅ (VERSION file) | ✅ Configured | — |
| Android | GitHub Actions (APK Artifact) | ✅ `v0.3.1` | ✅ Configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9), [#20](https://github.com/oatrice/TheMiddleWay-Metadata/issues/20) |
| iOS | GitHub Actions (Build only) | ✅ `v0.3.1` | ✅ Configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9), [#18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18) |

### Automated Testing
| Type | Tool | Status | Issue |
|------|------|--------|-------|
| Web Unit Tests | Jest + RTL | 🔲 Not configured | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) |
| Android Unit Tests | JUnit + Mockito | 🔲 Not configured | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) |
| iOS Unit Tests | XCTest | 🔲 Not configured | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) |
| E2E Tests | Playwright | 🔲 Not configured | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) |

---

## 📋 Issue Categories

- `[Setup]` - Project scaffolding and configuration
- `[Design]` - UI/UX and design system
- `[Feature]` - New functionality
- `[Data]` - Data handling and logic
- `[Infrastructure]` - Backend, persistence, APIs
- `[DevOps]` - CI/CD, testing, deployment
- `[Animation]` - Motion and interactions
- `[Architecture]` - Code structure, modularization
- `[UI/UX]` - User interface improvements
- `[Quality]` - Logging, monitoring, crashlytics
- `[Process]` - Development workflow and tracking

---

## 📝 Notes

- **Mobile-first approach** สำหรับทุก feature
- **Design System ที่กำหนดไว้** ใช้อย่างสม่ำเสมอ (Bright Sky / Deep Cosmos)
- **TDD (Test-Driven Development)** สำหรับ core logic
- **Cross-platform consistency** - Web, Android, iOS ต้องมี UI/UX เหมือนกัน
- **Testing Guide** — ดูที่ [TESTING_GUIDE.md](./TESTING_GUIDE.md)
- **Feature Docs** — ดูที่ [docs/features/](./docs/features/)

---

## 🔗 Quick Links

| Resource | Link |
|----------|------|
| 📊 **Kanban Board** | [Project #8](https://github.com/users/oatrice/projects/8) |
| 📦 **Releases** | [All Releases](https://github.com/oatrice/TheMiddleWay-Metadata/releases) |
| 🎯 **Milestones** | [All Milestones](https://github.com/oatrice/TheMiddleWay-Metadata/milestones) |
| 🌐 **Web Repo** | [TheMiddleWay-Web](https://github.com/oatrice/TheMiddleWay-Web) |
| 📱 **Android Repo** | [TheMiddleWay-Android](https://github.com/oatrice/TheMiddleWay-Android) |
| 🍎 **iOS Repo** | [TheMiddleWay-IOS](https://github.com/oatrice/TheMiddleWay-IOS) |
| ⚙️ **Backend Repo** | [TheMiddleWay-Backend](https://github.com/oatrice/TheMiddleWay-Backend) |
| 🌍 **Web (Vercel)** | [the-middle-way-web.vercel.app](https://the-middle-way-web.vercel.app) |
| 📋 **Testing Guide** | [TESTING_GUIDE.md](./TESTING_GUIDE.md) |
