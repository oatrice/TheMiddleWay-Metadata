# Issue #13: Light/Dark Theme Support

**Date:** 2026-02-10  
**Status:** 🔄 In Progress (Web ✅ | Android ✅ | iOS ✅)  
**Issue:** [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13)  
**Milestone:** [v0.2.0 - Foundation](https://github.com/oatrice/TheMiddleWay-Metadata/milestone/1)

---

## Summary

ระบบสลับธีมระหว่าง **Bright Sky (Light)** และ **Deep Cosmos (Dark)** ทุก platform  
ผู้ใช้สลับธีมผ่านปุ่ม toggle ที่ header — ระบบจำค่าที่เลือกไว้แม้ปิดแอปแล้วเปิดใหม่

---

## 🎨 Color Palettes

### ☀️ Bright Sky (Light Mode) — Default

| Token | Hex | ตัวอย่าง | ใช้กับ |
|-------|-----|---------|-------|
| Sky White | `#EFF6FF` | 🟦 | Background |
| Bright Blue | `#2563EB` | 🔵 | Primary / Accent |
| Sky Surface | `#DBEAFE` | 🔷 | Cards / Surface |
| Deep Blue | `#1E3A5F` | 🔹 | Text Primary |
| Blue Gray | `#64748B` | ⬜ | Text Secondary |
| Sky Border | `#BFDBFE` | ⬜ | Borders |

### 🌙 Deep Cosmos (Dark Mode)

| Token | Hex | ตัวอย่าง | ใช้กับ |
|-------|-----|---------|-------|
| Navy | `#0A192F` | 🟫 | Background |
| Amber | `#F59E0B` | 🟡 | Primary / Accent |
| Slate Dark | `#1E293B` | ⬛ | Cards / Surface |
| Ivory | `#F8FAFC` | ⬜ | Text Primary |
| Slate Light | `#94A3B8` | ⬜ | Text Secondary |
| Slate Border | `#334155` | ⬛ | Borders |

---

## 📱 Platform Implementation

### 🌐 Web (Next.js + CSS Variables)

| Component | File | Role |
|-----------|------|------|
| CSS Variables | `globals.css` | Color tokens ทั้ง 2 ธีม |
| Theme Hook | `hooks/useTheme.ts` | State management + localStorage |
| Theme Context | `components/ThemeProvider.tsx` | React Context |
| Toggle Button | `components/ThemeToggle.tsx` | Sun/Moon icon button |

**Persistence:** `localStorage` key `theme-mode`

#### Screenshots

| Light Mode (Bright Sky ☀️) | Dark Mode (Deep Cosmos 🌙) |
|---|---|
| <img src="./screenshots/web_light.png" width="300" alt="Web Light"> | <img src="./screenshots/web_dark.png" width="300" alt="Web Dark"> |

---

### 🤖 Android (Jetpack Compose + Material 3)

| Component | File | Role |
|-----------|------|------|
| Color Palette | `ui/theme/Color.kt` | `AppColors.Light` + `AppColors.Dark` |
| Theme Composable | `ui/theme/Theme.kt` | `BrightSkyColorScheme` + `DeepCosmosColorScheme` |
| Theme State | `ui/theme/ThemeState.kt` | `ThemeViewModel` + SharedPreferences |
| Toggle Button | `ui/screens/home/HomeScreen.kt` | Lucide-style Sun/Moon icon in TopAppBar |
| Icon - Sun | `res/drawable/ic_sun.xml` | VectorDrawable — Lucide Sun (circle + 8 rays) |
| Icon - Moon | `res/drawable/ic_moon.xml` | VectorDrawable — Lucide Moon (crescent) |

**Persistence:** `SharedPreferences` key `isDarkMode`

#### Screenshots

| Light Mode (Bright Sky ☀️) | Dark Mode (Deep Cosmos 🌙) |
|---|---|
| <img src="./screenshots/android_light.png" width="300" alt="Android Light"> | <img src="./screenshots/android_dark.png" width="300" alt="Android Dark"> |

> 📸 *Screenshots จะเพิ่มจาก Emulator/อุปกรณ์จริงเร็วๆ นี้*

---

### 🍎 iOS (SwiftUI + @AppStorage)

| Component | File | Role |
|-----------|------|------|
| Color Palette | `Core/Theme/AppColors.swift` | `Light` + `Dark` enums + Dynamic tokens |
| Theme Config | `Core/Theme/ThemeConfig.swift` | Helper functions + storage key |
| Theme Stack | `Core/Theme/AppTheme.swift` | `ThemedNavigationStack` |
| Toggle Button | `Features/Home/HomeView.swift` | SF Symbol icon in toolbar |

**Persistence:** `@AppStorage("isDarkMode")` → UserDefaults

#### Screenshots

| Light Mode (Bright Sky ☀️) | Dark Mode (Deep Cosmos 🌙) |
|---|---|
| <img src="./screenshots/ios_light.png" width="300" alt="iOS Light"> | <img src="./screenshots/ios_dark.png" width="300" alt="iOS Dark"> |

> 📸 *Screenshots จะเพิ่มจาก Simulator เร็วๆ นี้*

---

## 🔧 Technical Details

### Default Theme
เริ่มต้นทุก platform ด้วย **Light Mode (Bright Sky)** — เปลี่ยนได้ผ่าน config:

| Platform | Config Location | Default |
|----------|----------------|---------|
| Web | `hooks/useTheme.ts` → `DEFAULT_THEME` | `"light"` |
| Android | `ThemeState.kt` → `DEFAULT_IS_DARK` | `false` |
| iOS | `@AppStorage` default | `false` |

### 🎯 Icon Consistency

ทุก platform ใช้ไอคอน **Lucide-style** ที่ตรงกัน:

| สถานะ | Icon | Web (Lucide) | iOS (SF Symbols) | Android (VectorDrawable) |
|--------|------|-------------|-----------------|-------------------------|
| Dark Mode (กดเพื่อ→Light) | ☀️ Sun | `<Sun>` | `sun.max.fill` | `ic_sun.xml` — circle + 8 rays |
| Light Mode (กดเพื่อ→Dark) | 🌙 Moon | `<Moon>` | `moon.fill` | `ic_moon.xml` — crescent |

### Cross-Platform Consistency

สีทุก token ตรงกันทุก platform:

```
Web (CSS)        → #EFF6FF / #2563EB / #DBEAFE
Android (Compose) → 0xFFEFF6FF / 0xFF2563EB / 0xFFDBEAFE
iOS (SwiftUI)     → "#EFF6FF" / "#2563EB" / "#DBEAFE"
```

---

## Related Issues

| Issue | Title | Relation |
|-------|-------|----------|
| [#14](https://github.com/oatrice/TheMiddleWay-Metadata/issues/14) | Design System Implementation | Provides color foundation |
| [#15](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15) | Persistence Layer | Theme uses localStorage/UserDefaults/SharedPrefs |
| [#18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18) | iOS TestFlight Setup | ให้ผู้ทดสอบติดตั้ง iOS ได้ |
| [iOS#2](https://github.com/oatrice/TheMiddleWay-IOS/issues/2) | TestFlight Setup & Distribution | Platform-specific issue |

---

## ✅ Changelog

| วันที่ | รายการ |
|--------|--------|
| 2026-02-10 | สร้าง feature doc, screenshots Web |
| 2026-02-10 | เปลี่ยน default theme → Light (Bright Sky) ทุก platform |
| 2026-02-10 | แก้ Android icon เป็น Lucide-style (sun/moon) |
| 2026-02-10 | สร้าง TestFlight issue [iOS#2] |

---

## Next Steps

- [ ] Capture real screenshots จาก Android Emulator + iOS Simulator
- [ ] ตั้งค่า TestFlight สำหรับ iOS ([Issue #18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18))
- [ ] Upload APK ไป GitHub Release สำหรับ Android
- [ ] เพิ่ม theme animations (matching Issue #17)
- [ ] เพิ่ม system theme auto-detect (follow OS setting)
