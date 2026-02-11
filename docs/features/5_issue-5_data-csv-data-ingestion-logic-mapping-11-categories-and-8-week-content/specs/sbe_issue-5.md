# SBE: CSV Data Ingestion for Weekly Content Categories

> 📅 Created: 2026-02-11
> 🔗 Issue: https://github.com/mdwmediaworld072/TheMiddleWay/issues/5

---

## Feature: CSV Data Ingestion for Weekly Content Categories

To populate the application with structured content, the system must ingest a CSV file. This file contains weekly materials organized into 11 distinct categories over an 8-week period. The system should parse this data, validate it, and map it correctly into the application's data model.

### Scenario: Happy Path - Successful ingestion of a valid CSV file

**Given** a CSV file is available with the required headers: `Category`, `Week`, `Title`, `Content`
**When** the system ingests a row from the CSV file
**Then** the content is successfully parsed and mapped to the correct category and week

#### Examples

| Category | Week | Title | Content | Expected Status |
|---|---|---|---|---|
| Mindfulness | 1 | Introduction to Meditation | "Focus on your breath for 5 minutes each day." | Parsed Successfully |
| Fitness | 3 | Core Strength Workout | "Complete 3 sets of planks and crunches." | Parsed Successfully |
| Nutrition | 8 | Sustainable Eating Habits | "Plan your weekly meals to reduce food waste." | Parsed Successfully |
| Sleep | 5 | Creating a Bedtime Routine | "Avoid screens 30 minutes before bed." | Parsed Successfully |

### Scenario: Edge Cases - Ingesting a file with extra columns or special characters

**Given** a CSV file is provided that contains additional columns beyond the required set
**When** the system ingests a row from the CSV file
**Then** the system correctly parses the required data, ignores the extra columns, and preserves special characters in the content

#### Examples

| Category | Week | Title | Content | Author (Extra) | Expected Title | Expected Content |
|---|---|---|---|---|---|---|
| Relationships | 2 | "Active Listening" | "Practice repeating back what you've heard." | Dr. Eva Smith | "Active Listening" | "Practice repeating back what you've heard." |
| Finance | 4 | Budgeting with the 50/30/20 Rule | "Allocate 50% to needs, 30% to wants, & 20% to savings." | John Doe | Budgeting with the 50/30/20 Rule | "Allocate 50% to needs, 30% to wants, & 20% to savings." |
| Creativity | 6 | The "Morning Pages" Exercise | "Write three pages longhand, without judgment." | Julia Cameron | The "Morning Pages" Exercise | "Write three pages longhand, without judgment." |
| Productivity | 8 | Eisenhower Matrix | "Categorize tasks: Urgent/Important." | S. Covey | Eisenhower Matrix | "Categorize tasks: Urgent/Important." |

### Scenario: Error Handling - Ingesting a file with invalid or missing data

**Given** the system attempts to ingest a CSV file
**When** a row in the file contains missing values, incorrect data types, or out-of-range values
**Then** the system rejects the invalid row and logs a specific, descriptive error message

#### Examples

| Category | Week | Title | Content | Error Message |
|---|---|---|---|---|
| Mindfulness | nine | Invalid Week Format | "This row has a non-integer week." | Invalid data type for 'Week' at row 2. Expected integer. |
| Fitness | 10 | Week Out of Range | "This week is outside the 1-8 range." | Value for 'Week' at row 3 is out of range (1-8). |
| | 5 | Missing Category | "This row is missing the category." | Missing required value for 'Category' at row 4. |
| Unknown Category | 7 | Invalid Category Name | "This category is not one of the 11." | Invalid value for 'Category' at row 5: 'Unknown Category' is not a valid category. |