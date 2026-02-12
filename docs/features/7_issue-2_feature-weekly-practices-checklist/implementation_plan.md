# Implementation Plan - Wisdom Garden Web UI Refactor

Isolate the "Doing" (Weekly Practices) from the "Viewing" (Dashboard) to improve UX and code maintainability.

## User Review Required

> [!IMPORTANT]
> This change splits the existing Dashboard into two pages. The Checklist on the Dashboard will become Read-Only (or a summary), and a new "Weekly Practices" page will be created for user interaction.

## Proposed Changes

### Logic & State
#### [NEW] [wisdom-garden.ts](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/lib/logic/wisdom-garden.ts)
- Implement pure function `togglePracticeItem(data, itemId)` to handle immutable state updates.
- Centralize logic currently in `page.tsx`.

#### [NEW] [useWisdomGarden.ts](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/hooks/useWisdomGarden.ts)
- Custom hook to manage `WeeklyData` state.
- Handles `localStorage` persistence (read/write).
- Provides `toggleItem` function.

### UI Components
#### [MODIFY] [page.tsx](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/app/page.tsx)
- Remove interactive `handleCheckItem` logic (move to hook).
- Use `useWisdomGarden` hook for data.
- Pass `readOnly={true}` to `PracticeChecklist` (need to update component props).
- Add "Go to Practice Room" button linking to `/weekly-practices`.

#### [NEW] [page.tsx](file:///Users/oatrice/Software-projects/The%20Middle%20Way%20-Metadata/Platforms/Web/app/weekly-practices/page.tsx)
- New page for "Weekly Practices & Checklist".
- Uses `PracticeChecklist` (Interactive).
- Uses `WeekSelector`.
- Uses `useWisdomGarden` hook.

## Verification Plan

### Automated Tests
- Run unit tests for logic:
  ```bash
  npm run test -- Platforms/Web/lib/logic/wisdom-garden.test.ts
  ```

### Manual Verification
1.  **Dashboard (Home):**
    - Verify checklist items are visible but **cannot** be clicked/toggled.
    - Click "Go to Practice Room".
2.  **Weekly Practices Page:**
    - Verify checklist items **can** be toggled.
    - Check an item (e.g., "Morning Chanting").
    - Verify progress bar updates.
    - Reload page -> Item should remain checked.
3.  **Sync Check:**
    - Go back to Dashboard.
    - Verify the item checked in step 2 is also shown as checked (Read-only).
    - Verify the tree/score visualization reflects the score.
