# The Middle Way - Metadata

Shared metadata and documentation for The Middle Way project. Platform implementations live under `Platforms/`.

## Platforms

- Web - Next.js 16 (App Router) + TypeScript
- Backend - Placeholder (not initialized yet)
- iOS - Placeholder (not initialized yet)
- Android - Placeholder (not initialized yet)

## Design System (Current Web)

**Warm Modern Sanctuary** palette:

| Token | Color | Usage |
|-------|-------|-------|
| Ivory | `#FCF9F6` | Background |
| Sage | `#8B9D83` | Primary Accent |
| Slate | `#2D3748` | Text |
| Sand | `#F3F0ED` | Surface/Cards |

**Typography:**
- Headings: Playfair Display (Serif)
- Body: Inter (Sans-serif)

## Web Tech Stack

- **Framework:** Next.js 16 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **Animations:** Framer Motion
- **Icons:** Lucide React

## Repository Structure

```
├── Platforms/
│   ├── Web/             # Next.js app
│   ├── Backend/         # Placeholder
│   ├── iOS/             # Placeholder
│   └── Android/         # Placeholder
├── docs/                # Documentation
│   └── features/        # Feature docs
├── README.md
├── ROADMAP.md
└── CHANGELOG.md
```

## Getting Started (Web)

```bash
cd Platforms/Web

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

Open `http://localhost:3000` in your browser.

## Documentation

- Roadmap: `ROADMAP.md`
- Changelog: `CHANGELOG.md`
- Feature docs: `docs/features/`

## License

MIT
