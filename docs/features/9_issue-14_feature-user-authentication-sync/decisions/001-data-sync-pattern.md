# Architecture Decision Record (ADR): Wisdom Garden Data Sync Strategy

**Date:** 2026-02-19
**Status:** Accepted (Copy Pattern for MVP)

## Context
We need to design how "Weekly Practices" (Wisdom Garden) data is synced and stored for each user. There is "Master Data" (the template of tasks for Week 1-8) and "User Data" (progress/completion status).

## Options Considered

### 1. Copy Pattern (Current Implementation) 📦
When a user accesses a week for the first time, the entire structure (Titles, Points, IDs) is copied from Master Data to User's Firestore collection (`users/{uid}/weekly_practices/{weekId}`).
- **Pros:**
    - **Simplicity:** Reading implies getting the full state. No joining required.
    - **Historical Integrity:** If Master Data changes points/tasks in the future, existing users retain the version they started with (fairness).
    - **Offline-First Friendly:** easy to cache the whole object.
- **Cons:**
    - **Updates don't propagate:** Fixing a typo in Master Data won't be seen by users who already copied the data.
    - **Storage redundancy:** Repeating task titles for every user.

### 2. Merge Pattern (Read-Time Join) 🧩
User's Firestore collection only stores progress delta: e.g., `{ itemId: "task-1", isCompleted: true }`.
The Frontend fetches Master Data (for Titles/Points) and User Progress in parallel, then merges them in memory.
- **Pros:**
    - **Live Updates:** Admin fixes a typo -> everyone sees it instantly.
    - **Storage Efficiency:** Only storing boolean flags per user.
- **Cons:**
    - **Complexity:** Requires 2 reads + client-side merging logic.
    - **Historical Drift:** Changing points/tasks in Master might confuse users if not handled carefully (e.g., total score recalc).

### 3. Versioning Pattern (v1, v2) 🏷️
Creating distinct Master Data versions (e.g., `weeks/week-1-v2`). New users get v2, old users stay on v1.
- **Pros:**
    - Supports breaking changes in data structure.
- **Cons:**
    - High complexity to maintain multiple active versions.
    - Does not solve the "Typo Fix" use case effectively (old users still see typos).

## Decision
We decided to stick with **Option 1 (Copy Pattern)** for the MVP phase.
- **Reason:** It is already implemented and ensures stability.
- **Future Revisit:** If we find frequent need to update content text, we will refactor to **Option 2 (Merge Pattern)**, as it offers the best balance for content-heavy applications. Versioning (Option 3) is deemed unnecessary unless the data schema itself changes drastically.
