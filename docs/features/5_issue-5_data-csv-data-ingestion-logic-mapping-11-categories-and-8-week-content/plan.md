# Implementation Plan: CSV Content Ingestion System (Go Backend)

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Approved

## 1. Architecture & Design
The implementation will be a **Go-based Backend API** that handles CSV ingestion. This shifts the logic from client-side (LocalStorage) to a centralized backend server, enabling data persistence across devices and ensuring a single source of truth.

### Component View
- **Backend (Go)**:
    - **Language**: Go (Golang)
    - **Framework**: [Gin Web Framework](https://github.com/gin-gonic/gin)
    - **Database**: SQLite (via [GORM](https://gorm.io/)) for MVP, compatible with PostgreSQL.
    - **Validation**: Standard logic + validation libraries.
    - **CSV Processing**: Native `encoding/csv` with robust validation logic.

- **Structure**:
    - `cmd/api/main.go`: Entry point, setup Router and DB.
    - `internal/model/content.go`: Data models.
    - `internal/repository/content_repo.go`: Database interactions (Upsert logic).
    - `internal/service/ingestion_service.go`: CSV Parsing, Validation, and Transaction Management.
    - `internal/handler/content_handler.go`: API Endpoints.

### Data Model (Go Struct)
```go
// internal/model/content.go

type Category string

const (
    Mindfulness       Category = "Mindfulness"
    Nutrition         Category = "Nutrition"
    Fitness           Category = "Fitness"
    // ... all 11 categories
)

type WeeklyContent struct {
    ID        uint      `gorm:"primaryKey" json:"id"`
    Week      int       `gorm:"index:idx_week_category,unique;not null" json:"week"`
    Category  Category  `gorm:"index:idx_week_category,unique;not null" json:"category"`
    Title     string    `gorm:"not null" json:"title"`
    Content   string    `gorm:"type:text" json:"content"`
    CreatedAt time.Time `json:"created_at"`
    UpdatedAt time.Time `json:"updated_at"`
}
```

## 2. Step-by-Step Implementation

### Step 1: Backend Initialization
- **Description**: Setup the Go project structure and dependencies.
- **Tasks**:
    - Initialize `go.mod` (Module name: `github.com/oatrice/TheMiddleWay-Backend`).
    - Install `gin`, `gorm`, `sqlite`, `zap` (logging).
    - Setup folder structure: `cmd/`, `internal/`, `pkg/`, `configs/`.

### Step 2: Domain Logic & Storage
- **Description**: Implement models and repository layer.
- **Tasks**:
    - Define `WeeklyContent` struct in `internal/model`.
    - Implement `ContentRepository` with `Upsert` capability.
        - Use GORM's `Clauses(clause.OnConflict{UpdateAll: true})`.

### Step 3: CSV Processing Service
- **Description**: Logic for parsing and validating CSV data.
- **Tasks**:
    - Implement `ParseAndValidate(reader io.Reader)` in `internal/service`.
    - **Validation Rules**:
        1. **Headers**: Must match `Week, Category, Title, Content`.
        2. **Week**: Integer 1-8.
        3. **Category**: Must be one of the 11 Valid Categories.
        4. **Atomicity**: If any row is invalid, fail the entire batch.

### Step 4: API Handler Implementation
- **Description**: Create the HTTP endpoint.
- **Tasks**:
    - Method: `POST /api/v1/content/upload`
    - Body: `multipart/form-data` (`file` key).
    - Handler Logic:
        1. Parse file from request.
        2. Call `service.ParseAndValidate`.
        3. Call `repo.BulkUpsert`.
        4. Return 200 OK with summary, or 400 Bad Request with Validation Errors.

### Step 5: Frontend Integration (Future/Optional)
- Update the Next.js Admin Page (`csvProcessor.ts`) to upload the file to this API instead of local processing.
- (For now, testing can be done via Postman/Curl).

## 3. Verification Plan

### Automated Tests
- [ ] **Unit Tests**: `internal/service/ingestion_test.go`
    - Test Parser with Valid/Invalid CSVs.
    - Test Validation Rules.
- [ ] **Integration Tests**: `internal/handler/content_handler_test.go`
    - Mock HTTP Request with file.
    - Verify DB state after request.

### Manual Verification
- [ ] **Setup**: Run Go server `go run cmd/api/main.go`.
- [ ] **Happy Path**: Use Postman to POST `content_upload.csv` -> Expect 200 OK.
- [ ] **Validation Error**: POST `content_errors.csv` -> Expect 400 Bad Request with JSON error list.
- [ ] **Persistence**: Restart server -> Data remains in SQLite file.