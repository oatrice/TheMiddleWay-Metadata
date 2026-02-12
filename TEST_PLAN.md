# Test Plan - The Middle Way (Based on Code Review Suggestions)

## 1. 🌐 Metadata & Frontend (Localization & Persistence)

**Objective:** Verify robustness of language switching and user preferences.

- [ ] **[DEFERRED] Graceful Fallback for Missing Translations**
    - *Note: i18n feature is currently deferred in Web Platform implementation.*
    - **Scenario:** A translation key exists in Thai but is missing in English.
    - **Expected Result:** The app should NOT crash or show raw keys (e.g., `dashboard.welcome`). It should fallback to the default language or a safe placeholder.

- [ ] **[DEFERRED] Language Persistence with Disabled Storage**
    - *Note: i18n feature is currently deferred.*
    - **Scenario:**
        1. Select a language (e.g., Thai).
        2. Close and reopen the app.
        3. Feature Edge Case: Disable local storage/cookies (or fill them up).
    - **Expected Result:** The app should default to a sensible language (e.g., browser default) and must NOT crash.

- [ ] **[DEFERRED] Language Switching on Dynamic Content**
    - *Note: i18n feature is currently deferred.*
    - **Scenario:**
        1. Load the dashboard (wait for async data like user progress).
        2. Switch language.
    - **Expected Result:** All text, including dynamically loaded content (e.g., "Week 1 Assessment"), must update to the new language instantly.

---

## 2. 🔙 Backend & DevOps (CI/CD Workflows)

**Objective:** Verify the robustness of the `auto-tag.yml` workflow for backend versioning.

- [ ] **Existing Tag Handling**
    - **Scenario:** Push a commit updating `VERSION` to `1.5.0`, but tag `v1.5.0` already exists.
    - **Expected Result:** The workflow should detect the existing tag, log a warning, and skip tag creation gracefully (Status: Success/Skipped), NOT fail.

- [ ] **Invalid Version Format Validation**
    - **Scenario:** Update `VERSION` with invalid strings:
        - `v1.6.0` (Prefix 'v' included)
        - `1.6.0-alpha` (Pre-release suffix if not supported)
    - **Expected Result:** The workflow must FAIL at the validation step with a clear error message.

- [ ] **Empty/Whitespace Version File**
    - **Scenario:** Update `VERSION` file to contain only whitespace/newlines.
    - **Expected Result:** The workflow must FAIL and not create an empty tag (e.g., `v`).

---

## 3. 🍎 iOS (CI/CD Workflows)

**Objective:** Verify the robustness of the `auto-tag.yml` workflow for iOS project versioning.

- [ ] **Inconsistent `MARKETING_VERSION` Values**
    - **Scenario:** `project.pbxproj` has different versions for Debug (`1.2.3`) vs Release (`1.2.4`).
    - **Expected Result:** The workflow must FAIL validation to prevent ambiguous tagging.

- [ ] **Quoted Version String Handling**
    - **Scenario:** `project.pbxproj` stores version as `"2.1.0"` (with quotes).
    - **Expected Result:** The workflow should correctly strip quotes and create tag `v2.1.0`, NOT `v"2.1.0"`.

- [ ] **Multiple `project.pbxproj` Files**
    - **Scenario:** Repository contains multiple `.xcodeproj` or `.pbxproj` files.
    - **Expected Result:** The workflow should deterministically pick the correct main project file (or fail if ambiguous), ensuring it doesn't read from a backup or submodule.
