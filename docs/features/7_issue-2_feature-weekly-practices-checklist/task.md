# Task Checklist: Wisdom Garden Web Refactor (Option B + C)

## Core Logic & State (TDD)
- [x] Implement pure logic for toggling practice items (`lib/logic/wisdom-garden.ts`)
    - [x] Create failing test
    - [x] Implement `togglePracticeItem` function
    - [x] Verify test passes
- [x] Create `useWisdomGarden` Hook
    - [x] extract state management and persistence from `app/page.tsx`
    - [x] Ensure it supports reading/writing to `localStorage`

## UI Implementation
- [x] Create `Weekly Practices` Page (`app/weekly-practices/page.tsx`) (NEW)
    - [x] Use `PracticeChecklist` with interactive mode
    - [x] Use `WeekSelector`
    - [x] Integrate `useWisdomGarden` hook
- [x] Refactor `Dashboard` Page (`app/page.tsx`)
    - [x] Make Checklist Read-only (or visual summary)
    - [x] Add "Go to Practice Room" button
    - [x] Sync data using `useWisdomGarden` (listener for storage changes?)

## Verification
- [x] Verify data persistence between pages
- [x] Verify score updates on Dashboard when items checked in Practice Room

## Documentation
- [x] Document missing features/enhancements as new GitHub issues
- [x] Migrate pending issues to `TheMiddleWay-Metadata` repo
