Closes: https://github.com/mdwmediaworld072/TheMiddleWay/issues/5

### Summary

This pull request introduces the foundational planning, documentation, and logic for the **CSV Data Ingestion** feature. It lays the groundwork for the backend to process and map the 8-week content program, which is structured across 11 distinct categories.

In addition to the core feature planning, this PR significantly enhances the project's infrastructure by adding an automated CI workflow for version tagging and introduces comprehensive documentation for deployment URLs, improving the release and QA processes.

### Key Changes

*   **Feature: CSV Data Ingestion (Planning & Scaffolding)**
    *   Created extensive documentation outlining the feature's requirements, including `analysis.md`, `spec.md`, and a detailed implementation `plan.md`.
    *   Finalized the Go backend architecture and added test fixtures (`content_upload.csv`, `content_errors.csv`) to guide development and ensure data integrity.
    *   Added an initial code review report with suggestions for testing the CSV parsing logic.

*   **CI/CD Enhancements**
    *   Introduced a new GitHub Actions workflow (`auto-tag.yml`) to automatically create and push a Git tag when the `VERSION` file is updated on the `main` branch.
    *   Bumped the project version to `0.5.0` to reflect these significant additions.

*   **Documentation & Project Management**
    *   Added a new `DEPLOYMENT_URLS.md` file to provide a central, easy-to-reference list of application links for QA and users.
    *   Updated `CHANGELOG.md` with a detailed entry for version `0.5.0`.
    *   Updated the `ROADMAP.md` to mark the CSV data ingestion feature as "In Progress" and the CI/CD setup as "Complete".
    *   Overhauled the developer prompts for Android, iOS, Frontend, and Backend to align with the new architectural decisions and feature requirements.

### Impact

*   **Development Clarity:** Provides a clear and actionable blueprint for the backend team to implement the CSV ingestion logic in Go.
*   **Automated Releases:** The new auto-tagging workflow streamlines the release process, reduces manual effort, and ensures versioning consistency.
*   **Improved DX/QA:** Centralized deployment documentation and updated project status trackers make it easier for all team members to stay aligned and test effectively.