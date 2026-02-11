Closes https://github.com/mdwmediaworld072/TheMiddleWay/issues/6, https://github.com/oatrice/TheMiddleWay-Metadata/issues/15

## Description

This pull request establishes the complete technical and strategic foundation for the application's persistence layer. While it does not contain the final implementation code for the client applications, it introduces the comprehensive documentation, analysis, and specifications required for a consistent cross-platform rollout.

The core of this PR is the creation of a detailed feature documentation suite that outlines the problem, solution, API contracts, and data schema for storing user progress locally.

Additionally, this work includes significant project-level updates to improve developer and QA workflows, including a major refactoring of the testing guide and updates to the project roadmap and changelog to reflect recent progress.

## Key Changes

### Persistence Layer Foundation
- **Technical Analysis:** A new `analysis.md` document has been added, defining the problem statement, user stories, and technical requirements for local data persistence.
- **Implementation Plan:** A `plan.md` outlines the phased approach for implementation across Web, Android, and iOS platforms.
- **Technical Specification:** A `spec.md` defines the `UserProgress` data schema and the `PersistenceService` API contract, ensuring all platforms adhere to the same interface for saving, loading, and clearing data.
- **Proactive Code Review:** A `code_review.md` has been included to identify and address potential issues with the proposed `UserProgress` schema upfront, such as the need for versioning and handling of complex data types.

### Project Documentation & Infrastructure
- **Roadmap Update:** The `ROADMAP.md` has been updated to `v0.2.0-dev`, marking the CI/CD pipeline setup as complete and reflecting the current status of foundational tasks.
- **Changelog:** A new entry for `v0.4.0` has been added to `CHANGELOG.md` to formally log the documentation and infrastructure changes introduced in this PR.
- **Testing Guide Refactor:**
    - The main `TESTING_GUIDE.md` has been streamlined to focus on how to access development builds (CI artifacts, Vercel previews).
    - The detailed test cases for the Light/Dark theme have been moved into their own dedicated guide (`docs/features/3_issue-13_light-dark-theme/testing-guide.md`) to create a more modular and scalable testing structure.
- **Developer Prompts:** The internal prompts for AI-assisted development (`prompt_*.txt`) have been significantly simplified and overhauled to improve efficiency.

## Rationale

- **Clear Path Forward:** By creating a detailed specification and plan *before* implementation, we ensure that all development teams (Web, Android, iOS) have a clear and consistent blueprint to follow. This minimizes ambiguity and reduces the risk of platform-specific inconsistencies.
- **Improved Quality:** The proactive code review on the data schema helps us build a more robust and future-proof system by addressing potential design flaws early in the process.
- **Enhanced Developer & QA Experience:** Refactoring the testing guide makes it easier for team members to find relevant test cases and access the latest builds for verification. This change speeds up the development and feedback cycle.