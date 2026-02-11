# PR Draft Prompt

You are an AI assistant helping to create a Pull Request description.
    
TASK: [Data] CSV Data Ingestion & Logic: Mapping 11 Categories and 8-Week Content
ISSUE: {
  "title": "[Data] CSV Data Ingestion & Logic: Mapping 11 Categories and 8-Week Content",
  "number": 5
}

GIT CONTEXT:
COMMITS:
e69ae6a feat: [Data] CSV Data Ingestion & Logic: Mapping 11 Cate...
9ece723 chore(release): bump version to 0.5.0 with CSV ingestion docs
229d50b docs: add Luma code review report with CSV test suggestions
f070068 docs(issue-5): mark frontend integration tasks as completed
bef57c8 docs: mark manual verification complete in CSV ingestion plan
27b4336 docs: finalize Go backend architecture and add CSV test fixtures
a5ae9d6 chore: switch active issue to CSV ingestion and update roadmap
b231022 ci: add auto-tagging workflow and deployment documentation
15a7038 docs: add deployment URLs reference for QA and users
0652244 docs: remove missing web screenshot from testing guide
382b379 ci: add auto-tag workflow on version change

STATS:
.github/workflows/auto-tag.yml                     |  48 +++
 .luma_state.json                                   |  18 +-
 CHANGELOG.md                                       |  22 ++
 README.md                                          |  23 +-
 ROADMAP.md                                         |  34 +-
 VERSION                                            |   1 +
 docs/DEPLOYMENT_URLS.md                            | 104 ++++++
 .../testing-guide.md                               |   3 -
 .../analysis.md                                    | 254 +++++++++++++
 .../code_review.md                                 |  15 +
 .../fixtures/content_errors.csv                    |   5 +
 .../fixtures/content_upload.csv                    |   5 +
 .../plan.md                                        | 103 ++++++
 .../spec.md                                        | 139 ++++++++
 .../specs/sbe_issue-5.md                           |  55 +++
 prompt_android.txt                                 | 383 ++++++++++++++++----
 prompt_backend.txt                                 | 338 ++++++++++++++++++
 prompt_frontend.txt                                | 382 ++++++++++++++++----
 prompt_ios.txt                                     | 393 ++++++++++++++++-----
 19 files changed, 2061 insertions(+), 264 deletions(-)

KEY FILE DIFFS:
diff --git a/.github/workflows/auto-tag.yml b/.github/workflows/auto-tag.yml
new file mode 100644
index 0000000..500fd6c
--- /dev/null
+++ b/.github/workflows/auto-tag.yml
@@ -0,0 +1,48 @@
+name: Auto Tag on Version Change
+
+on:
+  push:
+    branches: [main]
+    paths:
+      - 'VERSION'
+
+permissions:
+  contents: write
+
+jobs:
+  auto-tag:
+    name: Create Git Tag from VERSION file
+    runs-on: ubuntu-latest
+
+    steps:
+      - uses: actions/checkout@v4
+        with:
+          fetch-depth: 0
+
+      - name: Extract version from VERSION file
+        id: version
+        run: |
+          VERSION=$(cat VERSION | tr -d '[:space:]')
+          echo "version=$VERSION" >> $GITHUB_OUTPUT
+          echo "tag=v$VERSION" >> $GITHUB_OUTPUT
+          echo "📦 Detected version: $VERSION"
+
+      - name: Check if tag already exists
+        id: check
+        run: |
+          if git rev-parse "v${{ steps.version.outputs.version }}" >/dev/null 2>&1; then
+            echo "exists=true" >> $GITHUB_OUTPUT
+            echo "⏩ Tag v${{ steps.version.outputs.version }} already exists, skipping."
+          else
+            echo "exists=false" >> $GITHUB_OUTPUT
+            echo "🆕 Tag v${{ steps.version.outputs.version }} does not exist yet."
+          fi
+
+      - name: Create and push tag
+        if: steps.check.outputs.exists == 'false'
+        run: |
+          git config user.name "github-actions[bot]"
+          git config user.email "github-actions[bot]@users.noreply.github.com"
+          git tag -a "v${{ steps.version.outputs.version }}" -m "Release v${{ steps.version.outputs.version }}"
+          git push origin "v${{ steps.version.outputs.version }}"
+          echo "✅ Tagged v${{ steps.version.outputs.version }}"
diff --git a/.luma_state.json b/.luma_state.json
index 0f87441..14c14c3 100644
--- a/.luma_state.json
+++ b/.luma_state.json
@@ -3,21 +3,19 @@
   "project_key": "6",
   "phase": "coding",
   "active_issue": {
-    "number": 6,
-    "title": "[Infrastructure] Persistence Layer: LocalStorage System for Progress Tracking",
-    "html_url": "https://github.com/mdwmediaworld072/TheMiddleWay/issues/6",
+    "number": 5,
+    "title": "[Data] CSV Data Ingestion & Logic: Mapping 11 Categories and 8-Week Content",
+    "html_url": "https://github.com/mdwmediaworld072/TheMiddleWay/issues/5",
     "body": "",
-    "project_item_id": "PVTI_lAHOATfKEM4BOWVDzgk3Kxs",
+    "project_item_id": "PVTI_lAHOATfKEM4BOWVDzgk3KxE",
     "project_id": "PVT_kwHOATfKEM4BOWVD",
     "repository": "mdwmediaworld072/TheMiddleWay"
   },
-  "active_branch": "feat/6-localstorage-persistence-layer",
-  "started_at": "2026-02-10T17:37:01.704061",
+  "active_branch": "feat/5-csv-data-ingestion",
+  "started_at": "2026-02-11T13:53:23.482217",
   "checklist": {},
-  "context": {
-    "last_feature_dir": "/Users/oatrice/Software-projects/The Middle Way -Metadata/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking"
-  },
+  "context": {},
   "pr_url": null,
   "pr_number": null,
-  "last_updated": "2026-02-11T11:25:31.142858"
+  "last_updated": "2026-02-11T13:53:25.372533"
 }
\ No newline at end of file
diff --git a/CHANGELOG.md b/CHANGELOG.md
index 8f1bca7..62cc389 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -1,5 +1,24 @@
 # Changelog
 
+## [0.5.0] - 2026-02-11
+
+### Added
+
+- **CSV Ingestion Documentation:** Introduced comprehensive planning for the CSV data ingestion feature, including analysis, technical specifications, and test data fixtures.
+- **Backend Architecture:** Finalized and documented the Go backend architecture.
+- **CI:** Implemented a GitHub Actions workflow to automatically create and push Git tags when the `VERSION` file is updated.
+- **Deployment Documentation:** Created `DEPLOYMENT_URLS.md` to provide a central reference for application links for QA and users.
+- **Code Review:** Added a formal `code_review.md` report with initial suggestions for CSV testing.
+
+### Changed
+
+- **Project Roadmap:** Updated `ROADMAP.md` to prioritize the CSV data ingestion feature.
+- **Developer Prompts:** Overhauled prompts for Android, iOS, Backend, and Frontend to align with new architectural decisions and improve development guidance.
+
+### Fixed
+
+- **Documentation:** Removed a reference to a missing screenshot in a feature testing guide.
+
 ## [0.4.0] - 2026-02-11
 
 ### Added
@@ -7,12 +26,15 @@
 - **Persistence Layer Documentation:** Introduced comprehensive documentation for the persistence layer, including analysis, planning, and technical specifications.
 - **Code Review Process:** Added a formal code review report to identify and track key issues, starting with the `UserProgress` data schema.
 - **Feature Testing Guide:** Created a dedicated testing guide for the Light/Dark theme feature.
+- **CI:** Implemented a new GitHub Actions workflow to automatically create and push Git tags when the `VERSION` file is updated.
+- **Documentation:** Created `DEPLOYMENT_URLS.md` to provide a central reference for application links for QA and users.
 
 ### Changed
 
 - **Project Roadmap:** Updated `ROADMAP.md` to reflect progress on CI/CD and to outline the development plan towards v0.2.0.
 - **Testing Guide:** Refined the main `TESTING_GUIDE.md` to better support development builds.
 - **Developer Prompts:** Overhauled and simplified developer prompts for Android, iOS, and Frontend to streamline the development process.
+- **Documentation:** Updated the persistence layer testing guide by removing a reference to a missing screenshot.
 
 ## [0.3.0] - 2026-02-10
 
diff --git a/README.md b/README.md
index 4529bb8..414dd04 100644
--- a/README.md
+++ b/README.md
@@ -9,7 +9,7 @@ Central repository for shared metadata, documentation, and multi-platform coordi
 | 🌐 **Web** | ✅ v0.2.0-dev | Next.js 16, Tailwind v4 | [TheMiddleWay-Web](https://github.com/oatrice/TheMiddleWay-Web) |
 | 📱 **Android** | ✅ v0.2.0-dev | Jetpack Compose, Material 3 | [TheMiddleWay-Android](https://github.com/oatrice/TheMiddleWay-Android) |
 | 🍎 **iOS** | ✅ v0.2.0-dev | SwiftUI, iOS 17+ | [TheMiddleWay-IOS](https://github.com/oatrice/TheMiddleWay-IOS) |
-| ⚙️ **Backend** | 🚧 Planned | TBD | [TheMiddleWay-Backend](https://github.com/oatrice/TheMiddleWay-Backend) |
+| ⚙️ **Backend** | 🚧 In Progress | Go | [TheMiddleWay-Backend](https://github.com/oatrice/TheMiddleWay-Backend) |
 
 ## 🎨 Design System
 
@@ -17,10 +17,22 @@ Central repository for shared metadata, documentation, and multi-platform coordi
 
 | Token | Color | Hex | Usage |
 |-------|-------|-----|-------|
-| Sky White | ![#EFF6FF](https://placehold.co/15x15/EFF6FF/EFF6FF) | `#EFF6FF` | Background |
-| Bright Blue | ![#2563EB](https://placehold.co/15x15/2563EB/2563EB) | `#2563EB` | Primary / Accent |
-| Deep Blue | ![#1E3A5F](https://placehold.co/15x15/1E3A5F/1E3A5F) | `#1E3A5F` | Text Primary |
-| Sky Surface | ![#DBEAFE](https://placehold.co/15x15/DBEAFE/DBEAFE) | `#DBEAFE` | Surface/Cards |
+| Sky White | 
+![#EFF6FF](https://placehold.co/15x15/EFF6FF/EFF6FF)
+
+ | `#EFF6FF` | Background |
+| Bright Blue | 
+![#2563EB](https://placehold.co/15x15/2563EB/2563EB)
+
+ | `#2563EB` | Primary / Accent |
+| Deep Blue | 
+![#1E3A5F](https://placehold.co/15x15/1E3A5F/1E3A5F)
+
+ | `#1E3A5F` | Text Primary |
+| Sky Surface | 
+![#DBEAFE](https://placehold.co/15x15/DBEAFE/DBEAFE)
+
+ | `#DBEAFE` | Surface/Cards |
 
 > **Note:** Also supports **Deep Cosmos (Dark Mode)**. See details in [THEME_OVERVIEW.md](./THEME_OVERVIEW.md).
 
@@ -69,6 +81,7 @@ Available via **TestFlight** (Coming Soon).
 - **[CHANGELOG.md](./CHANGELOG.md)** - Version history
 - **[THEME_OVERVIEW.md](./THEME_OVERVIEW.md)** - Light/Dark mode implementation details
 - **[TESTING_GUIDE.md](./TESTING_GUIDE.md)** - Manual testing procedures and platform status
+- **[DEPLOYMENT_URLS.md](./docs/DEPLOYMENT_URLS.md)** - Live deployment URLs for QA and preview
 - **[code_review.md](./code_review.md)** - Luma AI code review and issue report
 - **[docs/features/](./docs/features/)** - Feature specifications
 
diff --git a/ROADMAP.md b/ROADMAP.md
index 5aeec18..3d15841 100644
--- a/ROADMAP.md
+++ b/ROADMAP.md
@@ -2,7 +2,7 @@
 
 แผนพัฒนาแอปพลิเคชัน "The Middle Way" สำหรับการเรียนรู้และ mindfulness
 
-**อัปเดตล่าสุด:** 2026-02-10
+**อัปเดตล่าสุด:** 2026-02-11
 
 ---
 
@@ -37,20 +37,24 @@
 ---
 
 ### 📌 [v0.2.0 - Foundation](https://github.com/oatrice/TheMiddleWay-Metadata/milestone/1) 🔄 IN PROGRESS
-**Target:** 2026-02-16 | **Issues:** 9 open, 1 closed
+**Target:** 2026-02-16 | **Issues:** 6 open, 4 closed
 
 | Priority | ID | Title | Status |
 |----------|---|---|---|
-| 1 | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | Implement Light/Dark Theme Support (Bright Sky vs Deep Cosmos) | ✅ Complete |
+| 1 | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | Implement Light/Dark Theme Support (Warm Modern vs Deep Cosmos) | ✅ Complete |
 | 2 | [#14](https://github.com/oatrice/TheMiddleWay-Metadata/issues/14) | [Design] Design System Implementation | ✅ Complete |
 | 3 | [#15](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15) | [Infrastructure] Persistence Layer: LocalStorage/UserDefaults/DataStore | ✅ Complete |
-| 4 | [#16](https://github.com/oatrice/TheMiddleWay-Metadata/issues/16) | [Data] CSV Data Ingestion & Logic | 🔲 Todo |
+| 4 | [#16](https://github.com/oatrice/TheMiddleWay-Metadata/issues/16) | [Data] CSV Data Ingestion & Logic | 🔄 In Progress |
 | 5 | [#12](https://github.com/oatrice/TheMiddleWay-Metadata/issues/12) | [Architecture] iOS SPM Modularization | 🔲 Todo |
 | 6 | [#11](https://github.com/oatrice/TheMiddleWay-Metadata/issues/11) | [Architecture] Android Multi-Module Setup | 🔲 Todo |
-| 7 | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) | [DevOps] CI/CD Pipeline Setup | 🔄 In Progress |
+| 7 | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) | [DevOps] CI/CD Pipeline Setup | ✅ Complete |
 | 8 | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) | [DevOps] Automated Testing Framework | 🔲 Todo |
 | 9 | [#18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18) | [DevOps] iOS TestFlight Setup & Distribution | 🔲 Todo |
 | 10 | [#20](https://github.com/oatrice/TheMiddleWay-Metadata/issues/20) | [DevOps] Android CI/CD & Automated APK Build | 🔲 Todo |
+| 11 | [#24](https://github.com/oatrice/TheMiddleWay-Metadata/issues/24) | [Quality] Epic: Observability & Reliability | 🔲 Todo |
+| 12 | [#21](https://github.com/oatrice/TheMiddleWay-Metadata/issues/21) | [Quality][Android] Logging + Crashlytics + LeakCanary | 🔲 Todo |
+| 13 | [#22](https://github.com/oatrice/TheMiddleWay-Metadata/issues/22) | [Quality][iOS] Logging + Crashlytics | 🔲 Todo |
+| 14 | [#23](https://github.com/oatrice/TheMiddleWay-Metadata/issues/23) | [Quality][Web] Logging + Monitoring | 🔲 Todo |
 
 ---
 
@@ -59,10 +63,10 @@
 
 | Priority | ID | Title | Status |
 |----------|---|---|---|
-| 1 | #1 | 🌿 สวนแห่งปัญญา (Wisdom Garden Dashboard) | 🔲 Todo |
-| 2 | #2 | 📝 ห้องปฏิบัติธรรม (Weekly Practices) | 🔲 Todo |
-| 3 | #12 | Navigation System: Bottom Tab Bar | 🔲 Todo |
-| 4 | #11 | Onboarding: Welcome Screen | 🔲 Todo |
+| 1 | [#1](https://github.com/mdwmediaworld072/TheMiddleWay/issues/1) | 🌿 สวนแห่งปัญญา (Wisdom Garden Dashboard) | 🔲 Todo |
+| 2 | [#2](https://github.com/mdwmediaworld072/TheMiddleWay/issues/2) | 📝 ห้องปฏิบัติธรรม (Weekly Practices & Checklist) | 🔲 Todo |
+| 3 | [#12](https://github.com/mdwmediaworld072/TheMiddleWay/issues/12) | Navigation System: Bottom Tab Bar & Week Navigation | 🔲 Todo |
+| 4 | [#11](https://github.com/mdwmediaworld072/TheMiddleWay/issues/11) | Onboarding: Welcome Screen & "Authentic Wisdom" Introduction | 🔲 Todo |
 
 ---
 
@@ -71,9 +75,9 @@
 
 | Priority | ID | Title | Status |
 |----------|---|---|---|
-| 1 | #7 | Bilingual Support (i18n): EN/TH | 🔲 Todo |
-| 2 | [#17](https://github.com/oatrice/TheMiddleWay-Metadata/issues/17) | [Animation] Micro-interactions & Motion Design | 🔲 Todo |
-| 3 | #8 | The Wisdom Wheel: Radial Progress | 🔲 Todo |
+| 1 | [#7](https://github.com/mdwmediaworld072/TheMiddleWay/issues/7) | Bilingual Support (i18n): EN/TH Toggle Framework | 🔲 Todo |
+| 2 | [#17](https://github.com/oatrice/TheMiddleWay-Metadata/issues/17), [#13](https://github.com/mdwmediaworld072/TheMiddleWay/issues/13) | [Animation] Micro-interactions & Motion Design | 🔲 Todo |
+| 3 | [#8](https://github.com/mdwmediaworld072/TheMiddleWay/issues/8) | The Wisdom Wheel: Radial Progress Chart Visualization | 🔲 Todo |
 
 ---
 
@@ -82,9 +86,9 @@
 
 | Priority | ID | Title | Status |
 |----------|---|---|---|
-| 1 | #9 | Audio Library: Meditation Players | 🔲 Todo |
-| 2 | #10 | AI Dhamma: Chat Interface | 🔲 Todo |
-| 3 | #14 | User Authentication & Sync | 🔲 Todo |
+| 1 | [#9](https://github.com/mdwmediaworld072/TheMiddleWay/issues/9) | Audio Library: Meditation Players for Urban Lifestyles | 🔲 Todo |
+| 2 | [#10](https://github.com/mdwmediaworld072/TheMiddleWay/issues/10) | AI Dhamma: Soft-bubble Chat Interface | 🔲 Todo |
+| 3 | [#14](https://github.com/mdwmediaworld072/TheMiddleWay/issues/14) | 🔐 User Authentication & Sync | 🔲 Todo |
 
 ---
 
diff --git a/VERSION b/VERSION
new file mode 100644
index 0000000..8f0916f
--- /dev/null
+++ b/VERSION
@@ -0,0 +1 @@
+0.5.0
diff --git a/docs/DEPLOYMENT_URLS.md b/docs/DEPLOYMENT_URLS.md
new file mode 100644
index 0000000..0498da7
--- /dev/null
+++ b/docs/DEPLOYMENT_URLS.md
@@ -0,0 +1,104 @@
+# 🌐 Web Deployment URLs
+
+> เอกสารนี้อธิบายวิธีเข้าถึง Web App ในแต่ละ Environment
+> สำหรับ QA, Tester และ Users
+
+---
+
+## 📋 URL Reference
+
+| ประเภท | URL | ใช้เมื่อไหร่ |
+|--------|-----|-------------|
+| 🟢 **Production** | https://the-middle-way.vercel.app | เวอร์ชัน Stable ล่าสุด (main branch) |
+| 🏷️ **Version Tag** | `https://v{X-Y-Z}.the-middle-way.vercel.app` | ทดสอบเวอร์ชันเฉพาะ |
+| 🔀 **PR Preview** | ดูจาก PR comment ของ Vercel bot | ทดสอบ PR ก่อน merge |
+| 🖥️ **Local Dev** | http://localhost:3000 | dev บนเครื่องตัวเอง |
+
+### ตัวอย่าง Version URLs
+
+| Version | URL |
+|---------|-----|
+| v0.3.0 | https://v0-3-0.the-middle-way.vercel.app |
+| v0.4.0 | https://v0-4-0.the-middle-way.vercel.app |
+
+> ⚠️ Version URLs จะถูกสร้างอัตโนมัติเมื่อ merge PR เข้า `main` และ version เปลี่ยน
+
+---
+
+## 🔄 วิธีการทำงาน (Automated Pipeline)
+
+```
+PR Merge → main
+  ↓
+auto-tag.yml → สร้าง git tag (e.g. v0.4.0)
+  ↓
+vercel-version-alias.yml → สร้าง URL alias
+  ↓
+✅ v0-4-0.the-middle-way.vercel.app พร้อมใช้งาน
+```
+
+### Flow ทั้งหมด:
+
+1. **Developer** bump version ใน `package.json`
+2. **PR ถูก merge** เข้า `main`
+3. **`auto-tag.yml`** อ่าน version → สร้าง git tag `v0.4.0`
+4. **`vercel-version-alias.yml`** จับ tag → สร้าง Vercel alias URL
+5. **QA/Users** เข้าถึงได้ผ่าน URL ข้างต้น
+
+---
+
+## 🔍 ตรวจสอบ Build Info (Runtime)
+
+เปิด URL นี้เพื่อดูข้อมูล deployment ปัจจุบัน:
+
+```
+GET /api/app-info
+```
+
+**Response:**
+```json
+{
+  "urls": {
+    "current": "https://the-middle-way.vercel.app",
+    "prod": "https://the-middle-way.vercel.app",
+    "preview": "https://the-middle-way-git-feat-xxx.vercel.app",
+    "dev": "http://localhost:3000",
+    "commit": "https://the-middle-way-abc123.vercel.app"
+  },
+  "build": {
+    "env": "production",
+    "version": "0.4.0",
+    "tag": "v0.4.0",
+    "commitSha": "abc123def456...",
+    "commitRef": "main"
+  }
+}
+```
+
+---
+
+## 🔧 Setup Required (One-time)
+
+ต้องเพิ่ม Secrets ใน GitHub repo settings:
+
+| Secret | ที่มา |
+|--------|------|
+| `VERCEL_TOKEN` | [Vercel Settings → Tokens](https://vercel.com/account/tokens) |
+| `VERCEL_ORG_ID` | จาก `.vercel/project.json` หลัง `vercel link` |
+| `VERCEL_PROJECT_ID` | จาก `.vercel/project.json` หลัง `vercel link` |
+
+### วิธี Setup:
+
+```bash
+# 1. Link project กับ Vercel (ทำครั้งเดียว)
+cd Platforms/Web
+vercel link
+
+# 2. ดู org/project IDs
+cat .vercel/project.json
+
+# 3. เพิ่ม secrets ใน GitHub
+gh secret set VERCEL_TOKEN --repo oatrice/TheMiddleWay-Web
+gh secret set VERCEL_ORG_ID --repo oatrice/TheMiddleWay-Web
+gh secret set VERCEL_PROJECT_ID --repo oatrice/TheMiddleWay-Web
+```
diff --git a/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/testing-guide.md b/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/testing-guide.md
index 4a236df..b678486 100644
--- a/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/testing-guide.md
+++ b/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/testing-guide.md
@@ -78,9 +78,6 @@
 4. Refresh หน้าเว็บ
 5. **คาดหวัง:** แอปกลับไปเป็นค่าเริ่มต้น (Light Mode, 0 Progress)
 
-#### Screenshot
-![Web Testing](./screenshots/web.png)
-
 ---
 
 ## ✅ Checklist สำหรับ QA
diff --git a/docs/features/5_issue-5_data-csv-data-ingestion-logic-mapping-11-categories-and-8-week-content/analysis.md b/docs/features/5_issue-5_data-csv-data-ingestion-logic-mapping-11-categories-and-8-week-content/analysis.md
new file mode 100644
index 0000000..7fb1527
--- /dev/null
+++ b/docs/features/5_issue-5_data-csv-data-ingestion-logic-mapping-11-categories-and-8-week-content/analysis.md
@@ -0,0 +1,254 @@
+# Analysis Template
+
+> 📋 Template สำหรับการวิเคราะห์ก่อนเริ่มพัฒนา Feature
+
+---
+
+## 📌 Feature Information
+
+| รายการ | รายละเอียด |
+|--------|-----------|
+| **Feature Name** | CSV Data Ingestion for 8-Week Content Program |
+| **Issue URL** | [#5](https://github.com/owner/repo/issues/5) |
+| **Date** | 2023-10-27 |
+| **Analyst** | Luma AI (Senior Technical Analyst) |
+| **Priority** | 🔴 High |
+| **Status** | 📝 Draft |
+
+---
+
+## 1. Requirement Analysis
+
+### 1.1 Problem Statement
+
+> อธิบายปัญหาที่ต้องการแก้ไข
+
+```
+ปัจจุบันไม่มีกระบวนการที่เป็นระบบสำหรับการนำเข้าข้อมูลเนื้อหา (Content) จำนวนมากเข้าสู่ระบบ โดยเฉพาะข้อมูลโปรแกรม 8 สัปดาห์ที่มีโครงสร้างซับซ้อน (แบ่งเป็น 11 หมวดหมู่) ทำให้ทีม Content ต้องเพิ่มข้อมูลด้วยตนเองซึ่งช้าและเสี่ยงต่อความผิดพลาด ระบบจึงต้องการกลไกในการนำเข้าข้อมูลจากไฟล์ CSV เพื่อเพิ่มความรวดเร็ว ลดข้อผิดพลาด และทำให้การจัดการข้อมูลมีประสิทธิภาพมากขึ้น
+```
+
+### 1.2 User Stories
+
+| # | As a | I want to | So that |
+|---|------|-----------|---------|
+| 1 | Content Manager | upload a CSV file containing the 8-week program content | I can quickly populate or update the application's content without manual data entry. |
+| 2 | System Administrator | have a backend process that parses, validates, and maps CSV data to the database | data integrity is maintained and the process is reliable and auditable. |
+
+### 1.3 Acceptance Criteria
+
+- [ ] **AC1:** ระบบต้องมี Script หรือ API Endpoint สำหรับรับไฟล์ CSV เพื่อประมวลผล
+- [ ] **AC2:** Script/Endpoint ต้องสามารถตรวจสอบความถูกต้องของโครงสร้างไฟล์ CSV (เช่น ชื่อคอลัมน์, ประเภทข้อมูล) และเนื้อหา (เช่น Category ทั้ง 11 ประเภทต้องถูกต้อง, ข้อมูลครบ 8 สัปดาห์)
+- [ ] **AC3:** ข้อมูลที่ผ่านการตรวจสอบแล้ว จะต้องถูกบันทึกลงในตารางฐานข้อมูลที่เกี่ยวข้องอย่างถูกต้องตามโครงสร้าง Category และ Week
+- [ ] **AC4:** ในกรณีที่ไฟล์หรือข้อมูลไม่ถูกต้อง ระบบจะต้องจัดการข้อผิดพลาดอย่างเหมาะสม เช่น ไม่บันทึกข้อมูลส่วนที่ผิดพลาดลงฐานข้อมูล และมีการบันทึก Log ของข้อผิดพลาดอย่างละเอียด
+
+---
+
+## 2. Feature Analysis
+
+### 2.1 User Flow
+
+> **Note:** This is a backend process, likely triggered by an admin or a scheduled job.
+
+```mermaid
+flowchart TD
+    A[Start: Admin triggers ingestion process via API/CLI] --> B[System reads the provided CSV file]
+    B --> C{Validate CSV structure and data}
+    C -->|✅ Valid| D[Parse and map data to database models]
+    D --> E[Perform upsert operation into the database]
+    E --> F[Log success and number of records processed]
+    F --> G[End]
+    C -->|❌ Invalid| H["Log detailed errors (e.g., row number, error message)"]
+    H --> G
+```
+
+### 2.2 Screen/Page Requirements
+
+| หน้าจอ | Actions | Components |
+|--------|---------|------------|
+| N/
... (Diff truncated for size) ...

PR TEMPLATE:


INSTRUCTIONS:
1. Generate a comprehensive PR description in Markdown format.
2. If a template is provided, fill it out intelligently.
3. If no template, use a standard structure: Summary, Changes, Impact.
4. Focus on 'Why' and 'What'.
5. Do not include 'Here is the PR description' preamble. Just the body.
6. IMPORTANT: Always use FULL URLs for links to issues and other PRs (e.g., https://github.com/owner/repo/issues/123), do NOT use short syntax (e.g., #123) to ensuring proper linking across platforms.
