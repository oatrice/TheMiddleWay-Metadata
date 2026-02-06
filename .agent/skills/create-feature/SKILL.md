---
name: create-feature
description: Create a new feature following Mobile First strategy (Issue + Branches)
---

# Create Feature Skill (Mobile First)

This skill automates feature creation across specific platform repositories based on the Mobile First strategy.

## Usage

When user says:
- "create feature [name]"
- "เริ่มงาน [name]"

## Workflow

### Step 1: Gather Information
Ask user for:
1.  **Feature Name**: Short description
2.  **Objective**: What needs to be done?

### Step 2: Create Issue in Metadata Repo (Main Project)
Create an issue to track progress.

```bash
# Create issue in Metadata repo (current directory)
gh issue create --title "[Feature] <Feature Name>" --body "## Objective\n<Objective>\n\n## Mobile First Checklist\n\n### 1. Mock UI (Web) 🎨\n- [ ] Create/Update Page/Component (Mobile View)\n- [ ] Verify Flow with Mock Data\n\n### 2. Android (Logic) 🤖\n- [ ] Implement UI (Compose)\n- [ ] Implement Business Logic (Repository/ViewModel)\n- [ ] Connect API/Database\n- [ ] Unit Tests\n\n### 3. Web (Integration) 🌐\n- [ ] Integrate Real API\n- [ ] Responsive Check (Mobile -> Desktop)\n\n### 4. iOS 🍎\n- [ ] (Pending)"
```

### Step 3: Create Branches (Web & Android Only)
We purposefully skip iOS for now as per strategy.

```bash
# Web (for Mock UI & Later Implementation)
cd Platforms/Web
git checkout main && git pull
git checkout -b feat/<Feature Name>
git push -u origin feat/<Feature Name>

# Android (for Full Implementation)
cd ../Android
git checkout main && git pull
git checkout -b feat/<Feature Name>
git push -u origin feat/<Feature Name>

# Return to root
cd ../..
```

### Step 4: Report Summary
Provide summary:
```
✅ Feature Started: <Feature Name>

Managed by: Mobile First Strategy 📱

Repositories Initialized:
1. Web (Platforms/Web): feat/<Feature Name>
   - NEXT STEP: Create Mock UI here.

2. Android (Platforms/Android): feat/<Feature Name>
   - Status: Ready for logic implementation after Mock UI.

3. Metadata Issue Created.
```
