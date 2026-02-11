```markdown
# Specification Document: spec.md

| | |
| --- | --- |
| **Title** | [Data] CSV Data Ingestion & Logic: Mapping 11 Categories and 8-Week Content |
| **URL** | https://github.com/mdwmediaworld072/TheMiddleWay/issues/5 |
| **State** | `DRAFT` |
| **Author** | @expert-pm |
| **Reviewers** | @dev-lead, @qa-lead |
| **Last Updated** | 2023-10-27 |

---

### 1. Goal (The "Why")

**User Story:** As a Content Manager, I want to upload a single CSV file containing 8 weeks of content across 11 distinct categories, so that the system can automatically populate the application's content structure, saving time and preventing manual data entry errors.

**Problem:** Manually creating, organizing, and linking content for 88 unique combinations (8 weeks x 11 categories) is a highly repetitive, time-consuming, and error-prone process. A small mistake can lead to inconsistent or incorrect content being displayed to end-users.

**Benefit:** This feature will automate the entire content population process. It will ensure data consistency, dramatically reduce the time required for content setup, and enable easy bulk updates by simply modifying and re-uploading the CSV file.

---

### 2. Actors (The "Who")

*   **Content Manager (Admin):** The primary user who prepares the CSV file according to a defined template and uploads it into the system.
*   **System:** The application responsible for receiving the file, validating its structure and content, processing the data, and storing it in the appropriate data model.

---

### 3. User Journey (The "How")

1.  The **Content Manager** prepares a CSV file containing the content for all 8 weeks and 11 categories. The file must adhere to a specific format and column structure.
2.  The **Content Manager** navigates to the "Content Import" section of the admin dashboard.
3.  They click an "Upload CSV" button and select the prepared file from their local machine.
4.  The **System** receives the file and immediately performs a validation check on its structure and data.
5.  **Happy Path:**
    *   If the validation is successful, the **System** processes each row.
    *   For each row, it identifies the `Week` and `Category` and either creates a new content entry or updates an existing one (upsert logic).
    *   Upon completion, the **System** displays a success message to the **Content Manager**, such as: "Success! 88 content items were imported/updated."
6.  **Unhappy Path:**
    *   If any part of the validation fails (e.g., missing columns, invalid week number, unrecognized category), the **System** halts the import process *before* making any changes to the database.
    *   The **System** displays specific, actionable error messages to the **Content Manager**, detailing which row and column caused the failure (e.g., "Error on Row 5: The value 'Mindfullness' in the 'Category' column is not a valid category.").
    *   The **Content Manager** corrects the errors in their CSV file and re-attempts the upload.

---

### 4. Requirements (The "What")

#### Functional Requirements (FR)

| ID | Requirement | Details |
| --- | --- | --- |
| **FR1** | **CSV Upload Interface** | The system must provide a user interface for an authenticated Content Manager to upload a file with a `.csv` extension. |
| **FR2** | **CSV Structure Validation** | The system must validate that the uploaded CSV contains the following required header columns: `Week`, `Category`, `Title`, `Content`. The column order should not matter. |
| **FR3** | **Data Type & Value Validation** | The system must validate the data in each row *before* processing the import: <br> - `Week`: Must be an integer between `1` and `8` (inclusive). <br> - `Category`: Must be one of the 11 predefined, case-sensitive category names. <br> - `Title`: Must not be empty. |
| **FR4** | **Atomic Import Process** | The entire import operation must be atomic. If even one row fails validation, the entire process must be aborted, and no data should be saved or modified in the database. |
| **FR5** | **Actionable Error Reporting** | If validation fails, the system must return clear, user-friendly error messages that specify the row number and the exact nature of the error. |
| **FR6** | **Data Mapping & Upsert Logic** | For each valid row, the system must map the data to the internal content model. It will use the combination of `Week` and `Category` as a unique key. <br> - If an entry for that `Week`/`Category` combination already exists, it will be **updated** with the new `Title` and `Content`. <br> - If no entry exists, a **new** one will be created. |
| **FR7** | **Success Confirmation** | Upon successful completion of the import, the system must display a confirmation message indicating the total number of records processed. |

#### Predefined Categories
The 11 valid, case-sensitive values for the `Category` column are:
1.  `Mindfulness`
2.  `Nutrition`
3.  `Fitness`
4.  `Sleep`
5.  `Stress Management`
6.  `Productivity`
7.  `Relationships`
8.  `Financial Wellness`
9.  `Creativity`
10. `Environment`
11. `Community`

---

### 5. Specification by Example (SBE)

#### Scenario 1: Successful Data Import

*   **Given** a Content Manager has the following valid CSV file named `content_upload.csv`.
*   **When** they upload this file through the "Content Import" interface.
*   **Then** the system validates the file successfully, processes all rows, and displays the message: "Success! 3 content items were imported/updated."
*   **And** the application's internal data reflects the new content.

**Example `content_upload.csv`:**
```csv
Week,Category,Title,Content
1,Fitness,"Introduction to Morning Stretches","Stretching is a great way to start your day. Here are three simple moves."
1,Nutrition,"The Importance of Hydration","Why drinking enough water is crucial for your health and energy levels."
8,Community,"Final Week Reflections","Share your journey and experiences with the community group this week."
```

**Expected System State (Data Model):**

| Week | Category | Title | Content |
| :--- | :--- | :--- | :--- |
| 1 | Fitness | "Introduction to Morning Stretches" | "Stretching is a great way to start your day. Here are three simple moves." |
| 1 | Nutrition | "The Importance of Hydration" | "Why drinking enough water is crucial for your health and energy levels." |
| 8 | Community | "Final Week Reflections" | "Share your journey and experiences with the community group this week." |

---

#### Scenario 2: Import Fails Due to Validation Errors

*   **Given** a Content Manager has a CSV file named `content_errors.csv` with several data issues.
*   **When** they upload this file.
*   **Then** the system rejects the file *before* making any database changes.
*   **And** the system displays a list of specific errors to the user.

**Example `content_errors.csv`:**
```csv
Week,Category,Title,Content
1,Fitness,"Valid Entry","This one is fine."
9,Nutrition,"Invalid Week","This week is out of range."
2,Mindfullness,"Typo in Category","The category name is misspelled."
3,Sleep,,"This entry is missing a title."
```

**Expected System Response (Error Messages Displayed to User):**

| Error Type | Details |
| :--- | :--- |
| Validation Failed | The import could not be completed due to the following errors: |
| Row 2 Error | The value `9` in the `Week` column is invalid. It must be between 1 and 8. |
| Row 3 Error | The value `Mindfullness` in the `Category` column is not a valid category. |
| Row 4 Error | The `Title` column cannot be empty. |

---

### 6. Out of Scope

*   **Support for other file formats:** This feature will only support `.csv` files. Excel (`.xls`, `.xlsx`), JSON, or other formats will not be supported.
*   **In-app Category Management:** A UI for adding, editing, or deleting the 11 predefined categories is not part of this feature.
*   **Real-time Progress Bar:** A simple loading indicator will be shown, but a detailed row-by-row progress bar is not required.
*   **Deleting Content via CSV:** The upload process will only create or update content. It will not handle the deletion of records.
```