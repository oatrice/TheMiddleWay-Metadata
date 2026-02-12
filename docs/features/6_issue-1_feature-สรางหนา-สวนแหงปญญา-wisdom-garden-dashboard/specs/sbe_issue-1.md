# SBE: Wisdom Garden Dashboard

> 📅 Created: 2026-02-11
> 🔗 Issue: https://github.com/mdwmediaworld072/TheMiddleWay/issues/1

---

## Feature: Wisdom Garden Dashboard

To provide users with a calming and motivating home screen that visually represents their spiritual practice progress as a growing tree. The dashboard displays the total progress score for the selected week and a checklist of practices that users can interact with to update their progress in real-time.

### Scenario: Happy Path - Completing a practice updates progress

**Given** a user is viewing the "Wisdom Garden" dashboard for the current week
**When** the user taps the checkbox for an incomplete practice
**Then** the practice is marked as complete, the total score increases, and the tree graphic updates to reflect the new score

#### Examples

| Initial Score | Practice Ticked (Points) | Expected New Score | Expected Tree State |
|---------------|--------------------------|--------------------|---------------------|
| 0/70          | Giving (10)              | 10/70              | Seedling            |
| 25/70         | Ethics (5)               | 30/70              | Small Sapling       |
| 65/70         | Meditation (5)           | 70/70              | Fully Grown Tree    |
| 40/70         | Chanting (10)            | 50/70              | Medium Tree         |

### Scenario: Edge Case - Switching between weeks

**Given** a user is on the "Wisdom Garden" dashboard
**When** the user selects a different week from the week selector
**Then** the dashboard content updates to show the score, tree graphic, and checklist corresponding to the selected week

#### Examples

| Current Week View | Week Selected | Expected Score Displayed | Expected Checklist State |
|-------------------|---------------|--------------------------|--------------------------|
| Week 3 (20/70)    | Week 1        | 70/70 (Completed)        | All items checked        |
| Week 1 (70/70)    | Week 4        | 0/70 (Not started)       | All items unchecked      |
| Week 5 (0/70)     | Week 2        | 55/70 (Partially done)   | Some items checked       |
| Week 2 (55/70)    | Week 8        | 0/70 (Future week)       | All items unchecked      |

### Scenario: Error Handling - Changing the display language

**Given** the user is viewing the dashboard in a specific language
**When** the user clicks the language toggle button
**Then** all display text on the screen immediately changes to the alternate language

#### Examples

| Initial Language | UI Element Text (Initial) | Expected UI Element Text (After Toggle) |
|------------------|---------------------------|-----------------------------------------|
| Thai (TH)        | สวนแห่งปัญญา             | Wisdom Garden                           |
| English (EN)     | Week 3                    | สัปดาห์ที่ 3                            |
| Thai (TH)        | ทาน (Giving)              | Giving                                  |
| English (EN)     | Total Score               | คะแนนรวม                                |