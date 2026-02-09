# Android: Implementation Plan

สร้างโปรเจค Android ด้วย Jetpack Compose และ Material 3 สำหรับแอป "The Middle Way" ที่มี Design System แบบ Warm Modern Sanctuary

---

## Proposed Changes

### Core Configuration

#### [NEW] Android Project Initialization
- สร้างโปรเจค Android พร้อม:
  - Kotlin 2.1.10
  - Jetpack Compose
  - Material 3
  - Gradle 8.7.3

#### [NEW] Dependencies Installation
- `Hilt` - สำหรับ dependency injection
- `Room` - สำหรับ local database
- `Navigation Compose` - สำหรับ navigation
- `Material Icons Extended` - สำหรับ icons

---

### Design System

#### [NEW] Color.kt
- สร้าง custom colors:
  - `Ivory: Color(0xFFFCF9F6)` (Background)
  - `Sage: Color(0xFF8B9D83)` (Primary Accent)
  - `Slate: Color(0xFF2D3748)` (Text)
  - `Sand: Color(0xFFF3F0ED)` (Surface/Cards)

#### [NEW] Theme.kt
- สร้าง Material 3 ColorScheme
- ตั้งค่า StatusBar color ให้ตรงกับ background
- Light mode only

---

### Project Structure

#### [NEW] Directory Hierarchy
```
app/src/main/java/com/oatrice/themiddleway/
├── MainActivity.kt
├── TheMiddleWayApp.kt
├── ui/
│   ├── navigation/
│   │   └── BottomNavItem.kt
│   ├── screens/
│   │   ├── MainScreen.kt
│   │   └── home/
│   │       └── HomeScreen.kt
│   └── theme/
│       ├── Color.kt
│       ├── Theme.kt
│       └── Type.kt
```

---

### Initial Shell

#### [NEW] MainScreen.kt
- Scaffold พร้อม BottomNavigationBar
- 4 tabs: Home, Library, Courses, Profile
- ใช้ Material Icons

#### [NEW] HomeScreen.kt
- Welcome Card
- Quick Actions section (4 buttons)
- Recent Activity section

---

## Verification Plan

### Automated Testing
```bash
# ทดสอบว่า build สำเร็จ
./gradlew assembleDebug

# Install และรัน
./gradlew installDebug
```

### Manual Verification
1. **รันบน emulator หรือ device**
2. **ตรวจสอบ**:
   - พื้นหลังสี Ivory (#FCF9F6)
   - Bottom Navigation อยู่ด้านล่าง
   - มี 4 tabs: Home, Library, Courses, Profile
   - UI ตรงกับ Web และ iOS
