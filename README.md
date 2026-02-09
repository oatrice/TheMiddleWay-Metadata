# The Middle Way - Metadata

Central repository for shared metadata, documentation, and multi-platform coordination for The Middle Way project.

## 🌐 Platforms

| Platform | Status | Stack | Repository |
|----------|--------|-------|------------|
| 🌐 **Web** | ✅ v0.1.0 | Next.js 16, Tailwind v4 | [TheMiddleWay-Web](https://github.com/oatrice/TheMiddleWay-Web) |
| 📱 **Android** | ✅ v0.1.0 | Jetpack Compose, Material 3 | [TheMiddleWay-Android](https://github.com/oatrice/TheMiddleWay-Android) |
| 🍎 **iOS** | ✅ v0.1.0 | SwiftUI, iOS 17+ | [TheMiddleWay-IOS](https://github.com/oatrice/TheMiddleWay-IOS) |
| ⚙️ **Backend** | 🚧 Planned | TBD | [TheMiddleWay-Backend](https://github.com/oatrice/TheMiddleWay-Backend) |

## 🎨 Design System

**Warm Modern Sanctuary** - A calming, nature-inspired palette shared across all platforms:

| Token | Color | Hex | Usage |
|-------|-------|-----|-------|
| Ivory | ![#FCF9F6](https://placehold.co/15x15/FCF9F6/FCF9F6) | `#FCF9F6` | Background |
| Sage | ![#8B9D83](https://placehold.co/15x15/8B9D83/8B9D83) | `#8B9D83` | Primary Accent |
| Slate | ![#2D3748](https://placehold.co/15x15/2D3748/2D3748) | `#2D3748` | Primary Text |
| Sand | ![#F3F0ED](https://placehold.co/15x15/F3F0ED/F3F0ED) | `#F3F0ED` | Surface/Cards |

**Typography:**
| Platform | Headings | Body |
|----------|----------|------|
| Web | Playfair Display | Inter |
| Android | System Default | System Default |
| iOS | System Serif | System Sans |

## 📁 Repository Structure

```
├── Platforms/
│   ├── Web/             # Next.js 16 + Tailwind v4
│   ├── Android/         # Jetpack Compose + Material 3
│   ├── iOS/             # SwiftUI + iOS 17
│   └── Backend/         # (Planned)
├── docs/                # Shared documentation
│   └── features/        # Feature specifications
├── README.md            # This file
├── ROADMAP.md           # Project roadmap
└── CHANGELOG.md         # Changelog
```

## 🚀 Quick Start

### Web
```bash
cd Platforms/Web
npm install && npm run dev
```

### Android
```bash
cd Platforms/Android
./gradlew installDebug
```

### iOS
```bash
cd Platforms/iOS
open TheMiddleWay.xcodeproj
# Press Cmd+R in Xcode
```

## 📋 Documentation

- **[ROADMAP.md](./ROADMAP.md)** - Project milestones and timeline
- **[CHANGELOG.md](./CHANGELOG.md)** - Version history
- **[docs/features/](./docs/features/)** - Feature specifications

## 🔗 Related

- **Project Board:** [TheMiddleWay Kanban](https://github.com/users/oatrice/projects/8)
- **Main Web Repo:** [mdwmediaworld072/TheMiddleWay](https://github.com/mdwmediaworld072/TheMiddleWay)

## 📄 License

MIT
