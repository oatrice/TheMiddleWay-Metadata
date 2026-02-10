Closes https://github.com/[owner]/[repo]/issues/4

### Summary

This pull request introduces the foundational elements of our new design system, "Bright Sky". It implements the core color palette and typography, establishing a consistent and modern visual identity across all platforms (Web, iOS, and Android). This work includes full support for both light and dark themes, providing a more accessible and user-friendly experience.

### Key Changes

*   **🎨 Design System Implementation:**
    *   Established the primary color palette with `#0A192F` (Navy) for dark backgrounds and `#F59E0B` (Amber) as the main accent color.
    *   Implemented the base typography styles and hierarchy to ensure consistent and readable text.
    *   Introduced full support for **Light and Dark Modes**, which can be toggled by the user.

*   **📚 Extensive Documentation:**
    *   Added a comprehensive "Bright Sky" design system overview, including specifications and guidelines.
    *   Created a new `THEME_OVERVIEW.md` explaining the light/dark mode implementation.
    *   Updated the `TESTING_GUIDE.md` with detailed instructions for manually testing the new themes on all platforms.
    *   Added a `v0.3.0` entry to the `CHANGELOG.md` to reflect these significant changes.

*   **🛠️ Developer Tooling & Refinements:**
    *   Added a `run_guided_workflow.py` script to streamline development with the Luma dependency.
    *   Refactored the Luma dependency to use relative paths for improved project portability.
    *   Standardized prompt templates for development across different platforms.

### Screenshots

#### Web
| Light Mode | Dark Mode |
| :---: | :---: |
| <img src="docs/design_system/screenshots/web_light.png" alt="Web Light Mode" width="400"> | <img src="docs/design_system/screenshots/web_dark.png" alt="Web Dark Mode" width="400"> |

#### iOS
| Light Mode | Dark Mode |
| :---: | :---: |
| <img src="docs/design_system/screenshots/ios_light.png" alt="iOS Light Mode" width="250"> | <img src="docs/design_system/screenshots/ios_dark.png" alt="iOS Dark Mode" width="250"> |

#### Android
| Light Mode | Dark Mode |
| :---: | :---: |
| <img src="docs/design_system/screenshots/android_light.png" alt="Android Light Mode" width="250"> | <img src="docs/design_system/screenshots/android_dark.png" alt="Android Dark Mode" width="250"> |