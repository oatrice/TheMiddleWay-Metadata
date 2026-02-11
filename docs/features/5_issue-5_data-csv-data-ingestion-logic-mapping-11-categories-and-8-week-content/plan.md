# Implementation Plan: CSV Content Ingestion System

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Draft

## 1. Architecture & Design
The implementation will consist of a new backend API endpoint responsible for receiving, validating, and processing a CSV file. The logic will be encapsulated within dedicated services for validation and data import to ensure separation of concerns and testability. The entire import process will be wrapped in a single database transaction to guarantee atomicity as required by **FR4**.

The frontend will be a minimal, mock UI on the web-based admin panel, providing a simple file upload interface.

### Component View
> [!IMPORTANT]
> **Platform Scope Policy:**
> - **Web**: Mock UI only for this phase. The UI will provide the upload mechanism for the Content Manager.
> - **Android**: No direct changes. The Android app will consume the content populated by this feature at a later stage.
> - **iOS**: No direct changes. The iOS app will consume the content populated by this feature at a later stage.
>
> **Development Order:** Web Mock UI FIRST → Backend API & Services SECOND.

- **Modified Components**:
    - `admin/routes.py`: To add the new API endpoint route.
    - `admin/templates/content_management.html`: To add the file upload form.

- **New Components**:
    - **Backend**:
        - `models/content.py`: A new `Content` model to store the weekly categorized content.
        - `api/content_upload_controller.py`: A new controller to handle the `/api/admin/content/upload` endpoint.
        - `services/csv_processor.py`: A service containing two main classes:
            - `CsvValidator`: Responsible for all validation logic (**FR2, FR3, FR5**).
            - `ContentImporter`: Responsible for the transactional database upsert logic (**FR4, FR6**).
        - `constants/content_categories.py`: A file to store the list of 11 predefined categories.
    - **Database**:
        - A new `content` table in the database.

- **Dependencies**:
    - `pandas`: A Python library will be used on the backend for efficient CSV parsing and data validation.

### Data Model Changes
A new `Content` model will be created. The combination of `week` and `category` will be enforced as a unique key at the database level to facilitate the upsert logic.

```python
# File: models/content.py

from django.db import models

class Content(models.Model):
    """
    Stores the content for a specific week and category.
    """
    week = models.IntegerField(
        help_text="The week number, from 1 to 8."
    )
    category = models.CharField(
        max_length=100,
        help_text="One of the 11 predefined content categories."
    )
    title = models.CharField(
        max_length=255,
        help_text="The title of the content piece."
    )
    content = models.TextField(
        help_text="The main body of the content."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Enforces the unique key for the upsert logic (FR6)
        unique_together = ('week', 'category')
        verbose_name = "Weekly Content"
        verbose_name_plural = "Weekly Content"

    def __str__(self):
        return f"Week {self.week} - {self.category}: {self.title}"
```

---

## 2. Step-by-Step Implementation

### Step 1: Backend Foundation - Data Model and Constants
- **Description**: Define the `Content` data model and the list of valid categories. Create and apply the database migration.
- **Code**:
    - Create `models/content.py` with the `Content` class as defined above.
    - Create `constants/content_categories.py` to export the list of 11 category strings.
    - Run `python manage.py makemigrations` and `python manage.py migrate` to apply the schema changes.
- **Verification**:
    - The migration runs successfully.
    - Inspect the database schema to confirm the `content` table exists with the correct columns, types, and a unique constraint on `(week, category)`.

### Step 2: Backend Logic - CSV Validation Service
- **Description**: Implement the service responsible for validating the CSV file's structure and data content. This service will not interact with the database.
- **Code**:
    - Create `services/csv_processor.py`.
    - Implement the `CsvValidator` class within this file.
    - The validator will have a primary method, `validate(file_stream)`, which performs the following checks:
        1.  **Header Validation (FR2)**: Reads the CSV header and ensures `Week`, `Category`, `Title`, and `Content` are all present.
        2.  **Row-by-Row Data Validation (FR3)**: Iterates through each row and validates:
            - `Week` is an integer between 1 and 8.
            - `Category` is present in the list from `constants/content_categories.py`.
            - `Title` is not null or empty.
    - The `validate` method will return a list of structured error messages (e.g., `[{'row': 3, 'error': 'Invalid category: Mindfullness'}]`). An empty list signifies success.
- **Tests**:
    - Create `tests/services/test_csv_validator.py`.
    - Write unit tests for all validation scenarios:
        - Valid CSV.
        - CSV with missing headers.
        - CSV with extra headers.
        - Rows with invalid `Week` values (e.g., 0, 9, 'abc').
        - Rows with invalid `Category` values (typos, non-existent categories).
        - Rows with empty `Title`.
        - A file with a mix of valid and invalid rows.
- **Verification**: All unit tests for the `CsvValidator` pass.

### Step 3: Backend Logic - Data Import Service and API Endpoint
- **Description**: Implement the service that orchestrates the import process and the API endpoint that exposes this functionality.
- **Code**:
    - In `services/csv_processor.py`, implement the `ContentImporter` class.
    - It will have one method, `process_import(file_stream)`, which:
        1.  Calls `CsvValidator.validate()`. If errors are returned, it immediately returns them to the controller.
        2.  If validation passes, it opens a database transaction (`@transaction.atomic` in Django).
        3.  Inside the transaction, it iterates through the validated data rows.
        4.  For each row, it uses the ORM's `update_or_create` method with `week` and `category` as lookup keys to perform the upsert (**FR6**).
        5.  Returns a success status with the count of processed rows.
    - In `api/content_upload_controller.py`, create a new API view that:
        - Is protected and only accessible by authenticated admins.
        - Accepts a `POST` request with `multipart/form-data`.
        - Checks for a `.csv` file extension (**FR1**).
        - Calls `ContentImporter.process_import()`.
        - If errors are returned, responds with a `400 Bad Request` and the JSON-formatted list of errors (**FR5**).
        - If successful, responds with a `200 OK` and a success message (**FR7**).
    - Register the new endpoint in `admin/routes.py`.
- **Tests**:
    - Create `tests/api/test_content_upload.py`.
    - Write integration tests that simulate file uploads to the new endpoint:
        - Test with a valid CSV and assert the database state is correct and a 200 response is returned.
        - Test with an invalid CSV and assert the database remains unchanged and a 400 response with error details is returned.
- **Verification**: All integration tests pass. Manually test the endpoint using a tool like Postman with various CSV files.

### Step 4: Frontend - Mock UI for CSV Upload
- **Description**: Create a simple, unstyled web interface for the Content Manager to upload the CSV file.
- **Code**:
    - Modify `admin/templates/content_management.html` (or a similar template).
    - Add a new section with an HTML form:
      ```html
      <h2>Import Content</h2>
      <form action="/api/admin/content/upload" method="post" enctype="multipart/form-data">
          <input type="file" name="file" accept=".csv" required>
          <button type="submit">Upload</button>
      </form>
      <div id="upload-status"></div>
      ```
    - Add minimal JavaScript to handle the form submission via AJAX, display a loading state, and render the success or error messages returned by the API in the `upload-status` div.
- **Verification**:
    - The upload form is visible on the admin page.
    - Selecting a file and clicking "Upload" successfully sends the request to the backend.
    - Success and error messages from the API are correctly displayed to the user on the page.

---

## 3. Verification Plan
*How will we verify success?*

> [!IMPORTANT]
> **Android Build Policy**: MUST use scripts in `Android/scripts/` (e.g., `build_android.sh`) instead of direct `./gradlew` to ensure correct JDK version (Java 21).

### Automated Tests
- [X] **Unit Tests**: `tests/services/test_csv_validator.py` will cover all validation logic defined in **FR2**, **FR3**, and **FR5**.
- [X] **Integration Tests**: `tests/api/test_content_upload.py` will cover the end-to-end flow, including file handling, atomicity (**FR4**), upsert logic (**FR6**), and success/error responses (**FR7**).

### Manual Verification
- [ ] **Happy Path - Create**: Log in as Content Manager, navigate to the import page, and upload a valid CSV with 5 new content items. Verify a "Success! 5 content items were imported/updated" message is displayed and the new records exist in the database.
- [ ] **Happy Path - Update**: Upload the same CSV file again, but with modified `Title` and `Content` for 2 of the items. Verify the success message appears and the corresponding database records are updated (check `updated_at` timestamp).
- [ ] **Unhappy Path - Header Error**: Upload a CSV missing the `Category` column. Verify an error message related to the missing header is shown and no changes are made to the database.
- [ ] **Unhappy Path - Data Errors**: Upload the `content_errors.csv` from the specification. Verify that the exact error messages for rows 2, 3, and 4 are displayed to the user and the database remains completely unchanged.
- [ ] **Unhappy Path - Wrong File Type**: Attempt to upload a `.txt` or `.jpg` file. Verify the UI or backend rejects the file with an appropriate message.