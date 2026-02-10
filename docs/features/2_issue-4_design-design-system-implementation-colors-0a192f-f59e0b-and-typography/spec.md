```markdown
# Specification

**Title:** [Design] Design System Implementation: Colors (#0A192F, #F59E0B) and Typography
**URL:** https://github.com/mdwmediaworld072/TheMiddleWay/issues/4

---

## 1. Goal

To establish a foundational and consistent visual identity for the application by defining and implementing a core set of design tokens for colors and typography. This will ensure visual cohesion across all user interfaces, improve developer efficiency by providing reusable styles, and simplify future design updates.

## 2. Actors

*   **Developer:** The primary user of this system, who will consume the defined tokens to style UI components.
*   **Designer:** The stakeholder who defines the visual language and relies on its faithful implementation.
*   **End-User:** The beneficiary who experiences a polished, predictable, and visually appealing application.

## 3. User Journey

As a **Developer**, I want to style a new UI component. Instead of hardcoding hex values or pixel sizes, I need a simple and predictable way to apply the official brand styles.

1.  **Discovery:** I consult the design system documentation (or codebase) to find the appropriate token for my use case (e.g., I need the primary background color or the style for a level-two heading).
2.  **Application:** I reference the token by its semantic name (e.g., `color-background-primary` or `typography-h2`) in my styling code (CSS, SCSS, component styles, etc.).
3.  **Verification:** The component renders on the screen with the correct color and font styles, matching the design specifications perfectly.
4.  **Maintenance:** When a designer decides to update the brand's primary color, the change is made in one central token definition file. My component, along with all others using that token, updates automatically on the next build without any code changes on my part.

## 4. Requirements

### 4.1. Color System

*   A centralized color palette must be defined and made available as design tokens.
*   Tokens must have semantic names that describe their intended use (e.g., `background-primary`, `text-default`, `action-primary`) rather than their literal color (e.g., `dark-navy`, `bright-orange`).
*   The system must include the following colors, mapped to semantic roles:
    *   `#0A192F` (A dark navy blue)
    *   `#F59E0B` (A vibrant amber/orange)
*   The color tokens must be easily accessible throughout the application's styling layer (e.g., as CSS custom properties, theme variables, or utility classes).

### 4.2. Typography System

*   A typographic scale must be defined for all common text elements (e.g., headings H1-H6, body text, captions, labels).
*   Each typographic style in the scale must be available as a token or a reusable style class.
*   Each style definition must include the following properties:
    *   `font-family`
    *   `font-size`
    *   `font-weight`
    *   `line-height`
    *   `letter-spacing` (optional, where appropriate)

## 5. Specification by Example (SBE)

### Scenario 1: Styling a Primary Call-to-Action Button

**Context:** A developer is building a "Sign Up" button, which is the most important action on the page.
**Trigger:** The developer needs to apply the brand's primary action color to the button's background.
**Expectation:** The developer uses a semantic color token, and the button renders with the correct, centrally-managed color.

**Example:**

| Token Name              | Token Value | Example Application      | Rendered CSS Property      |
| ----------------------- | ----------- | ------------------------ | -------------------------- |
| `color-action-primary`  | `#F59E0B`   | `button.primary`         | `background-color: #F59E0B` |
| `color-text-inverted`   | `#FFFFFF`   | `button.primary`         | `color: #FFFFFF`           |
| `color-background-page` | `#0A192F`   | `body` or `main wrapper` | `background-color: #0A192F` |

---

### Scenario 2: Creating a Main Page Title

**Context:** A developer is adding the main heading to the "Welcome" page.
**Trigger:** The developer needs to style the text "Welcome to The Middle Way" as a level-one heading (H1).
**Expectation:** The developer applies the `h1` typography style, and the text is rendered with the predefined font properties for that level.

**Example:**

| Token/Style Name | Property        | Value           | Example Application | Rendered CSS                                                                                               |
| ---------------- | --------------- | --------------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| `typography-h1`  | `font-family`   | `'Inter', sans-serif` | `<h1>` or `.h1`     | `font-family: 'Inter', sans-serif;`                                                                        |
|                  | `font-size`     | `48px`          |                     | `font-size: 48px;`                                                                                         |
|                  | `font-weight`   | `700` (Bold)    |                     | `font-weight: 700;`                                                                                        |
|                  | `line-height`   | `1.2`           |                     | `line-height: 1.2;`                                                                                        |
| `color-text-primary` | `value`         | `#E2E8F0` (example) | `h1` or `.h1`     | `color: #E2E8F0;` (A light color for readability against the dark `#0A192F` background) |

## 6. Out of Scope

*   Implementation of specific UI components (Buttons, Inputs, Cards, etc.). This specification is only for the foundational tokens they will use.
*   Defining other design token categories like spacing, shadows, border-radius, or breakpoints.
*   Refactoring the entire existing application to use these new tokens.
*   The choice of specific font files or the setup for loading them.

## 7. Acceptance Criteria

*   [ ] A central file (e.g., `theme.js`, `_colors.scss`, `tailwind.config.js`) exists defining the application's color palette.
*   [ ] The color `#0A192F` is defined with a semantic name (e.g., `background-primary`).
*   [ ] The color `#F59E0B` is defined with a semantic name (e.g., `action-primary` or `accent`).
*   [ ] A central file exists defining the application's typographic scale (H1-H6, body, etc.).
*   [ ] Each typographic style includes `font-family`, `font-size`, `font-weight`, and `line-height`.
*   [ ] Developers can easily access and apply both color and typography tokens when styling components.
*   [ ] Basic documentation or comments exist alongside the token definitions explaining their intended use.
```