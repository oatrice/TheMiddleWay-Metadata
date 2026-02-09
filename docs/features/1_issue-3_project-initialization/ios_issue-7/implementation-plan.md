# iOS: Implementation Plan

สร้างโปรเจค iOS ด้วย SwiftUI สำหรับแอป "The Middle Way" ที่มี Design System แบบ Warm Modern Sanctuary

---

## Proposed Changes

### Core Configuration

#### [NEW] iOS Project Initialization
- สร้างโปรเจค Xcode พร้อม:
  - iOS 17.0+ deployment target
  - SwiftUI
  - Swift 5.9+

---

### Design System

#### [NEW] AppColors.swift
- สร้าง custom colors:
  - `ivory: Color(hex: "#FCF9F6")` (Background)
  - `sage: Color(hex: "#8B9D83")` (Primary Accent)
  - `slate: Color(hex: "#2D3748")` (Text)
  - `sand: Color(hex: "#F3F0ED")` (Surface/Cards)

#### [NEW] AppTypography.swift
- Typography styles:
  - `largeTitle` - System Serif
  - `headline` - System Serif
  - `body` - System Sans
  - `caption` - System Sans

---

### Project Structure

#### [NEW] Directory Hierarchy
```
TheMiddleWay/
├── Sources/
│   ├── App/
│   │   ├── TheMiddleWayApp.swift
│   │   └── ContentView.swift
│   ├── Core/
│   │   └── Theme/
│   │       ├── AppColors.swift
│   │       └── AppTypography.swift
│   └── Features/
│       └── Home/
│           └── HomeView.swift
└── Resources/
    └── Assets.xcassets/
```

---

### Initial Shell

#### [NEW] ContentView.swift
- TabView พร้อม NavigationStack
- 4 tabs: Home, Library, Courses, Profile
- ใช้ SF Symbols

#### [NEW] HomeView.swift
- Welcome Card
- Quick Actions section
- Recent Activity section

---

## Verification Plan

### Manual Verification
1. **เปิดใน Xcode** และกด `Cmd + R`
2. **รันบน Simulator** (iOS 17+)
3. **ตรวจสอบ**:
   - พื้นหลังสี Ivory (#FCF9F6)
   - TabView อยู่ด้านล่าง
   - มี 4 tabs: Home, Library, Courses, Profile
   - UI ตรงกับ Web และ Android
