# Implementation Plan: Design System Foundation - Colors & Typography

> **Refers to**: [Spec] Design System Implementation: Colors (#0A192F, #F59E0B) and Typography
> **Status**: Draft

## 1. Architecture & Design
The implementation will establish a foundational design system using pure CSS, ensuring framework-agnostic compatibility and ease of use.

We will use **CSS Custom Properties** (variables) for the color system. This allows for a centralized, themeable, and easily maintainable color palette. Colors will be defined in two tiers: a primitive palette (the raw hex values) and a semantic palette (aliasing primitives for specific use cases like `background-primary`). This approach makes future theme updates trivial.

For the typography system, we will create a set of **utility classes** (e.g., `.h1`, `.h2`, `.body-text`) that apply the specified font properties. We will also apply these styles directly to the corresponding HTML tags (`h1`, `h2`, etc.) for sensible defaults and improved semantic HTML styling.

All new styles will be organized within a dedicated `src/styles/design-system` directory to keep them isolated and maintainable. A main `index.css` file within this directory will act as the entry point for importing all design system modules.

- **Modified Components**:
    - `src/styles.css` (or equivalent global stylesheet): To import the new design system styles.
- **New Components**:
    - `src/styles/design-system/_colors.css`: Defines all color tokens as CSS custom properties.
    - `src/styles/design-system/_typography.css`: Defines the typographic scale via utility classes.
    - `src/styles/design-system/index.css`: Imports and aggregates all design system styles.
- **Dependencies**:
    - The `Inter` font family is specified. This plan assumes the font is already loaded into the application. The implementation of the font loading mechanism is out of scope.

### Data Model Changes
```python
# No data model changes are required for this feature.
```

---

## 2. Step-by-Step Implementation

### Step 1: Set Up Design System File Structure
This step creates the foundational directory structure for our design tokens, ensuring a clean and scalable organization.

- **Code**:
    1.  Create a new directory: `src/styles/design-system/`.
    2.  Inside this new directory, create the following empty files:
        - `_colors.css`
        - `_typography.css`
        - `index.css`
- **Verification**:
    - Run `ls -R src/styles/design-system` and confirm the directory and all three CSS files exist.

### Step 2: Implement Color Tokens
This step defines the core color palette as specified, using a two-tiered system of primitive and semantic tokens for maximum flexibility.

- **Code**:
    - **File**: `src/styles/design-system/_colors.css`
    - **Content**: Add the following CSS to define the color variables on the `:root` element.

    ```css
    /* src/styles/design-system/_colors.css */

    :root {
      /* --- Primitive Color Palette --- */
      /* Do not use these directly in components. Use semantic tokens instead. */
      --primitive-color-navy-900: #0A192F;
      --primitive-color-amber-500: #F59E0B;
      --primitive-color-slate-200: #E2E8F0; /* A light color for text on dark backgrounds */
      --primitive-color-white: #FFFFFF;

      /* --- Semantic Color Tokens --- */
      /* These tokens describe the intended use of a color. */

      /* Background Colors */
      --color-background-page: var(--primitive-color-navy-900);

      /* Text Colors */
      --color-text-primary: var(--primitive-color-slate-200);
      --color-text-inverted: var(--primitive-color-white);
      --color-text-accent: var(--primitive-color-amber-500);

      /* Action/Accent Colors */
      --color-action-primary: var(--primitive-color-amber-500);
    }
    ```
- **Verification**:
    - After integrating in Step 4, open the browser's developer tools.
    - Select the `<html>` or `<body>` element.
    - In the "Computed" or "Styles" panel, verify that the CSS custom properties (e.g., `--color-background-page`) are defined and have the correct hex values.

### Step 3: Implement Typography Scale
This step defines the typographic styles for headings and body text, making them available as both direct element styles and reusable utility classes.

- **Code**:
    - **File**: `src/styles/design-system/_typography.css`
    - **Content**: Add the following CSS to define the typography scale.

    ```css
    /* src/styles/design-system/_typography.css */

    /* H1 / .h1 */
    .h1, h1 {
      font-family: 'Inter', sans-serif;
      font-size: 48px;
      font-weight: 700;
      line-height: 1.2;
    }

    /* H2 / .h2 */
    .h2, h2 {
      font-family: 'Inter', sans-serif;
      font-size: 36px;
      font-weight: 700;
      line-height: 1.25;
    }

    /* H3 / .h3 */
    .h3, h3 {
      font-family: 'Inter', sans-serif;
      font-size: 24px;
      font-weight: 700;
      line-height: 1.3;
    }

    /* H4 / .h4 */
    .h4, h4 {
      font-family: 'Inter', sans-serif;
      font-size: 20px;
      font-weight: 600;
      line-height: 1.4;
    }

    /* H5 / .h5 */
    .h5, h5 {
      font-family: 'Inter', sans-serif;
      font-size: 18px;
      font-weight: 600;
      line-height: 1.5;
    }

    /* H6 / .h6 */
    .h6, h6 {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      font-weight: 600;
      line-height: 1.5;
    }

    /* Body Text */
    .body-text, p {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      font-weight: 400;
      line-height: 1.6;
    }
    ```
- **Verification**:
    - Create a test HTML page. Add elements like `<h1>Title</h1>` and `<p class="h2">Subtitle</p>`.
    - Inspect these elements in the browser and confirm that all specified font properties (`font-family`, `font-size`, etc.) are correctly applied.

### Step 4: Integrate Design System into Application
This final step wires the new design system files into the main application stylesheet and applies the base page styles.

- **Code**:
    1.  **File**: `src/styles/design-system/index.css`
        - **Content**: Import the token files.
        ```css
        @import './_colors.css';
        @import './_typography.css';
        ```
    2.  **File**: `src/styles.css` (or your project's main stylesheet)
        - **Content**: Add the import statement at the top of the file.
        ```css
        /* Import Design System Foundation */
        @import './styles/design-system/index.css';

        /* Other global styles... */
        ```
    3.  **File**: `src/styles.css` (or a new `_base.css` file imported by it)
        - **Content**: Apply base styles to the `body`.
        ```css
        body {
          margin: 0;
          background-color: var(--color-background-page);
          color: var(--color-text-primary);
          font-family: 'Inter', sans-serif; /* Default font for elements not covered by typography scale */
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
        ```
- **Verification**:
    - Load the application in a browser.
    - The page background should now be the dark navy color (`#0A192F`).
    - Default text color on the page should be the light slate color (`#E2E8F0`).
    - All typography classes and color variables should be globally available for use in components.

---

## 3. Verification Plan
Success will be verified through manual inspection using a dedicated test page and browser developer tools.

### Automated Tests
- N/A for this CSS-focused implementation. Visual regression testing could be added in the future but is out of scope for this plan.

### Manual Verification
- [ ] **Create a Test Page**: Create a temporary `design-system-test.html` page in the project to showcase all new tokens.
- [ ] **Verify Color Tokens**:
    - The test page will display colored swatches for each semantic color token (e.g., `--color-background-page`, `--color-action-primary`).
    - Use browser dev tools to inspect each swatch and confirm the `background-color` is correctly resolving the CSS variable to the expected hex value.
- [ ] **Verify Typography Tokens**:
    - The test page will display sample text for each typography class/element from H1 to H6 and body text.
    - Use browser dev tools to inspect each text element and confirm that the correct `font-family`, `font-size`, `font-weight`, and `line-height` are applied.
- [ ] **Verify Global Application**:
    - Navigate through the main application.
    - Confirm the global `body` background and text colors have been applied correctly.
- [ ] **Confirm Acceptance Criteria**:
    - A central file for colors exists (`_colors.css`).
    - `#0A192F` is mapped to `--color-background-page`.
    - `#F59E0B` is mapped to `--color-action-primary`.
    - A central file for typography exists (`_typography.css`).
    - All typography styles include the required properties.
    - Tokens are accessible via `var()` and utility classes.
    - Comments explaining token usage are present in the CSS files.