# PR Draft Prompt

You are an AI assistant helping to create a Pull Request description.
    
TASK: [Infrastructure] Persistence Layer: LocalStorage System for Progress Tracking
ISSUE: {
  "title": "[Infrastructure] Persistence Layer: LocalStorage System for Progress Tracking",
  "number": 6
}

GIT CONTEXT:
COMMITS:
d10dd6f feat: [Infrastructure] Persistence Layer: LocalStorage S...
ef37981 docs: add code review report identifying UserProgress schema issues
790da75 docs: update persistence docs to reference issue #15
728244c docs: add persistence layer analysis document
e8d25f3 docs(roadmap): update to v0.2.0-dev, mark CI/CD complete, and set PR pending
35e2b4e docs: update testing guide for development builds

STATS:
.luma_state.json                                   |  16 +-
 CHANGELOG.md                                       |  14 +
 ROADMAP.md                                         |  28 +-
 TESTING_GUIDE.md                                   | 146 ++------
 .../3_issue-13_light-dark-theme/testing-guide.md   | 109 ++++++
 .../analysis.md                                    | 259 +++++++++++++
 .../code_review.md                                 |  79 ++++
 .../plan.md                                        | 192 ++++++++++
 .../screenshots/android.png                        | Bin 0 -> 135132 bytes
 .../screenshots/ios.png                            | Bin 0 -> 195805 bytes
 .../screenshots/web.png                            | Bin 0 -> 70770 bytes
 .../spec.md                                        | 131 +++++++
 .../specs/sbe_issue-6.md                           |  55 +++
 prompt_android.txt                                 | 399 ++++----------------
 prompt_backend.txt                                 | 354 ------------------
 prompt_frontend.txt                                | 398 ++++----------------
 prompt_ios.txt                                     | 409 +++++----------------
 17 files changed, 1133 insertions(+), 1456 deletions(-)

KEY FILE DIFFS:
diff --git a/.luma_state.json b/.luma_state.json
index a7884ab..0f87441 100644
--- a/.luma_state.json
+++ b/.luma_state.json
@@ -3,21 +3,21 @@
   "project_key": "6",
   "phase": "coding",
   "active_issue": {
-    "number": 4,
-    "title": "[Design] Design System Implementation: Colors (#0A192F, #F59E0B) and Typography",
-    "html_url": "https://github.com/mdwmediaworld072/TheMiddleWay/issues/4",
+    "number": 6,
+    "title": "[Infrastructure] Persistence Layer: LocalStorage System for Progress Tracking",
+    "html_url": "https://github.com/mdwmediaworld072/TheMiddleWay/issues/6",
     "body": "",
-    "project_item_id": "PVTI_lAHOATfKEM4BOWVDzgk3Kvc",
+    "project_item_id": "PVTI_lAHOATfKEM4BOWVDzgk3Kxs",
     "project_id": "PVT_kwHOATfKEM4BOWVD",
     "repository": "mdwmediaworld072/TheMiddleWay"
   },
-  "active_branch": "feat/4-design-design-system-implement",
-  "started_at": "2026-02-09T20:35:44.686392",
+  "active_branch": "feat/6-localstorage-persistence-layer",
+  "started_at": "2026-02-10T17:37:01.704061",
   "checklist": {},
   "context": {
-    "last_feature_dir": "/Users/oatrice/Software-projects/The Middle Way -Metadata/docs/features/2_issue-4_design-design-system-implementation-colors-0a192f-f59e0b-and-typography"
+    "last_feature_dir": "/Users/oatrice/Software-projects/The Middle Way -Metadata/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking"
   },
   "pr_url": null,
   "pr_number": null,
-  "last_updated": "2026-02-09T21:37:08.618038"
+  "last_updated": "2026-02-11T11:25:31.142858"
 }
\ No newline at end of file
diff --git a/CHANGELOG.md b/CHANGELOG.md
index ab5e442..8f1bca7 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -1,5 +1,19 @@
 # Changelog
 
+## [0.4.0] - 2026-02-11
+
+### Added
+
+- **Persistence Layer Documentation:** Introduced comprehensive documentation for the persistence layer, including analysis, planning, and technical specifications.
+- **Code Review Process:** Added a formal code review report to identify and track key issues, starting with the `UserProgress` data schema.
+- **Feature Testing Guide:** Created a dedicated testing guide for the Light/Dark theme feature.
+
+### Changed
+
+- **Project Roadmap:** Updated `ROADMAP.md` to reflect progress on CI/CD and to outline the development plan towards v0.2.0.
+- **Testing Guide:** Refined the main `TESTING_GUIDE.md` to better support development builds.
+- **Developer Prompts:** Overhauled and simplified developer prompts for Android, iOS, and Frontend to streamline the development process.
+
 ## [0.3.0] - 2026-02-10
 
 ### Added
diff --git a/ROADMAP.md b/ROADMAP.md
index e214a34..6dec2c7 100644
--- a/ROADMAP.md
+++ b/ROADMAP.md
@@ -17,9 +17,9 @@
 ### Current Versions
 | Platform | Version | Status |
 |----------|---------|--------|
-| Web | 0.1.0 | ✅ Scaffolding |
-| Android | 0.1.0 | ✅ Scaffolding |
-| iOS | 0.1.0 | ✅ Scaffolding |
+| Web | 0.2.0-dev | 🔄 Foundation (Vercel Deploy ✅) |
+| Android | 0.2.0-dev | 🔄 Foundation (CI ✅) |
+| iOS | 0.2.0-dev | 🔄 Foundation (CI ✅) |
 
 ---
 
@@ -37,18 +37,20 @@
 ---
 
 ### 📌 [v0.2.0 - Foundation](https://github.com/oatrice/TheMiddleWay-Metadata/milestone/1) 🔄 IN PROGRESS
-**Target:** 2026-02-16 | **Issues:** 7 open
+**Target:** 2026-02-16 | **Issues:** 9 open, 1 closed
 
 | Priority | ID | Title | Status |
 |----------|---|---|---|
-| 1 | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | Implement Light/Dark Theme Support (Warm Modern vs Deep Cosmos) | 🔄 In Progress (iOS ✅) |
-| 2 | [#14](https://github.com/oatrice/TheMiddleWay-Metadata/issues/14) | [Design] Design System Implementation | 🔲 Todo |
+| 1 | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | Implement Light/Dark Theme Support (Bright Sky vs Deep Cosmos) | ✅ Complete |
+| 2 | [#14](https://github.com/oatrice/TheMiddleWay-Metadata/issues/14) | [Design] Design System Implementation | ✅ Complete |
 | 3 | [#15](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15) | [Infrastructure] Persistence Layer: LocalStorage/UserDefaults/DataStore | 🔲 Todo |
 | 4 | [#16](https://github.com/oatrice/TheMiddleWay-Metadata/issues/16) | [Data] CSV Data Ingestion & Logic | 🔲 Todo |
 | 5 | [#12](https://github.com/oatrice/TheMiddleWay-Metadata/issues/12) | [Architecture] iOS SPM Modularization | 🔲 Todo |
 | 6 | [#11](https://github.com/oatrice/TheMiddleWay-Metadata/issues/11) | [Architecture] Android Multi-Module Setup | 🔲 Todo |
-| 7 | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) | [DevOps] CI/CD Pipeline Setup | 🔲 Todo |
+| 7 | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) | [DevOps] CI/CD Pipeline Setup | 🔄 In Progress |
 | 8 | [#10](https://github.com/oatrice/TheMiddleWay-Metadata/issues/10) | [DevOps] Automated Testing Framework | 🔲 Todo |
+| 9 | [#18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18) | [DevOps] iOS TestFlight Setup & Distribution | 🔲 Todo |
+| 10 | [#20](https://github.com/oatrice/TheMiddleWay-Metadata/issues/20) | [DevOps] Android CI/CD & Automated APK Build | 🔲 Todo |
 
 ---
 
@@ -102,9 +104,9 @@
 ### CI/CD Pipeline
 | Platform | Tool | Status | Issue |
 |----------|------|--------|-------|
-| Web | GitHub Actions + Vercel | 🔲 Not configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) |
-| Android | GitHub Actions + Firebase | 🔲 Not configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) |
-| iOS | GitHub Actions + TestFlight | 🔲 Not configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) |
+| Web | GitHub Actions + Vercel | ✅ Configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9) |
+| Android | GitHub Actions (APK Artifact) | ✅ Configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9), [#20](https://github.com/oatrice/TheMiddleWay-Metadata/issues/20) |
+| iOS | GitHub Actions (Build only) | ✅ Configured | [#9](https://github.com/oatrice/TheMiddleWay-Metadata/issues/9), [#18](https://github.com/oatrice/TheMiddleWay-Metadata/issues/18) |
 
 ### Automated Testing
 | Type | Tool | Status | Issue |
@@ -133,9 +135,11 @@
 ## 📝 Notes
 
 - **Mobile-first approach** สำหรับทุก feature
-- **Design System ที่กำหนดไว้** ใช้อย่างสม่ำเสมอ (Warm Sanctuary / Deep Cosmos)
+- **Design System ที่กำหนดไว้** ใช้อย่างสม่ำเสมอ (Bright Sky / Deep Cosmos)
 - **TDD (Test-Driven Development)** สำหรับ core logic
 - **Cross-platform consistency** - Web, Android, iOS ต้องมี UI/UX เหมือนกัน
+- **Testing Guide** — ดูที่ [TESTING_GUIDE.md](./TESTING_GUIDE.md)
+- **Feature Docs** — ดูที่ [docs/features/](./docs/features/)
 
 ---
 
@@ -149,3 +153,5 @@
 | 🌐 **Web Repo** | [TheMiddleWay-Web](https://github.com/oatrice/TheMiddleWay-Web) |
 | 📱 **Android Repo** | [TheMiddleWay-Android](https://github.com/oatrice/TheMiddleWay-Android) |
 | 🍎 **iOS Repo** | [TheMiddleWay-IOS](https://github.com/oatrice/TheMiddleWay-IOS) |
+| 🌍 **Web (Vercel)** | [the-middle-way-web.vercel.app](https://the-middle-way-web.vercel.app) |
+| 📋 **Testing Guide** | [TESTING_GUIDE.md](./TESTING_GUIDE.md) |
diff --git a/TESTING_GUIDE.md b/TESTING_GUIDE.md
index 2b3123b..ccb5da2 100644
--- a/TESTING_GUIDE.md
+++ b/TESTING_GUIDE.md
@@ -15,11 +15,22 @@
 
 ## 📊 สถานะแต่ละ Platform
 
+### 🛠️ สำหรับนักพัฒนา (Development Builds)
+หากต้องการทดสอบฟีเจอร์ล่าสุดที่ยังไม่ได้ปล่อย Release:
+
+1. **Android:** ไปที่ [Actions Tab](https://github.com/oatrice/TheMiddleWay-Android/actions) > เลือก Workflow ล่าสุด > โหลด `app-debug` จาก Artifacts
+2. **Web:** ไปที่ [Pull Requests](https://github.com/oatrice/TheMiddleWay-Web/pulls) > เลือก PR ที่ต้องการ > ดูลิงก์ **Visit Preview** จาก Vercel bot
+3. **iOS:** ตรวจสอบสถานะการ Build ที่ [Actions Tab](https://github.com/oatrice/TheMiddleWay-IOS/actions) (ยังไม่มี Artifact ให้โหลด)
+
+---
+
+## 📊 สถานะแต่ละ Platform (Release)
+
 | Platform | สถานะ | วิธีติดตั้ง |
 |----------|--------|------------|
-| 🤖 Android | ✅ พร้อมทดสอบ | ดาวน์โหลด APK จาก GitHub |
-| 🍎 iOS | ⏳ กำลังตั้งค่า TestFlight | รอลิงก์จากทีมพัฒนา |
-| 🌐 Web | ⏳ กำลัง deploy ขึ้น Vercel | เปิดจาก Browser ได้เลย (เมื่อพร้อม) |
+| 🤖 Android | ✅ พร้อมทดสอบ | ดาวน์โหลด APK จาก GitHub Releases หรือ Actions |
+| 🍎 iOS | ⚠️ ต้องใช้ Mac | ติดตั้งผ่าน Xcode (สาย USB) หรือ TestFlight (ถ้ามีบัญชี Dev) |
+| 🌐 Web | ✅ Deploy เรียบร้อย | เปิดจาก Vercel Preview URL (ใน PR) |
 
 ---
 
@@ -44,22 +55,27 @@
 
 ### 🍎 iOS (iPhone)
 
-> ⏳ **กำลังตั้งค่า TestFlight** — ติดตามความคืบหน้าได้ที่ [Issue #2](https://github.com/oatrice/TheMiddleWay-IOS/issues/2)
+การทดสอบบน iOS มีความเข้มงวดกว่า Android เล็กน้อย แบ่งเป็น 2 กรณี:
 
-**เมื่อ TestFlight พร้อมแล้ว ขั้นตอนจะเป็นดังนี้:**
+#### กรณีที่ 1: ติดตั้งผ่านสาย USB (ฟรี - แนะนำสำหรับ Dev)
+หากคุณมีเครื่อง Mac และ Xcode ติดตั้งอยู่:
+1. เปิดโปรเจกต์ `Platforms/iOS/TheMiddleWay.xcodeproj` ด้วย Xcode
+2. เสียบ iPhone เข้ากับ Mac
+3. เลือก Target เป็น iPhone ของคุณ
+4. กดปุ่ม ▶️ **Run**
+5. (ครั้งแรก) บน iPhone ไปที่ **Settings > General > VPN & Device Management** แล้วกด Trust Developer App
 
-1. ติดตั้งแอป **TestFlight** จาก App Store (ฟรี):  
-   👉 [ดาวน์โหลด TestFlight](https://apps.apple.com/app/testflight/id899247664)
+> 💡 **ข้อจำกัด:** แอปจะอยู่ได้ 7 วัน ต้องติดตั้งใหม่ถ้าหมดอายุ
 
-2. รอรับ **Email เชิญทดสอบ** จากทีมพัฒนา  
-   หรือกดลิงก์ TestFlight ที่ทีมส่งให้
+#### กรณีที่ 2: ติดตั้งผ่าน TestFlight (ต้องมีบัญชี Apple Dev $99/ปี)
+👉 *วิธีนี้สะดวกสุดสำหรับผู้ใช้ทั่วไป แต่ต้องรอทีมงานตั้งค่าระบบก่อน*
 
-3. เปิด Email → กด **"View in TestFlight"** → กด **ติดตั้ง**
+1. ติดตั้งแอป **TestFlight** จาก App Store (ฟรี)
+2. รอรับ **Email เชิญทดสอบ** หรือกดลิงก์ที่ทีมส่งให้
+3. กด **"View in TestFlight"** → **Install**
+4. แอปจะอยู่ได้ 90 วัน ไม่ต้องต่อคอมพิวเตอร์
 
-4. แอปจะปรากฏบนหน้าจอ Home เหมือนแอปทั่วไป
-
-> 💡 **หมายเหตุ:** TestFlight เป็นระบบทดสอบอย่างเป็นทางการของ Apple — ปลอดภัย 100%  
-> Build ทดสอบจะหมดอายุภายใน 90 วัน
+> ⏳ **สถานะปัจจุบัน:** รอการตั้งค่า Account (ติดตามที่ [Issue #2](https://github.com/oatrice/TheMiddleWay-IOS/issues/2))
 
 ---
 
@@ -67,9 +83,8 @@
 
 1. เปิด Browser (Chrome, Safari, หรือ Firefox) ได้ทั้งจากมือถือและคอม
 2. ไปที่ลิงก์:  
-   👉 *(กำลัง deploy ขึ้น Vercel — จะอัปเดตลิงก์เร็วๆ นี้)*
-   <!-- TODO: ใส่ URL จริงเมื่อ deploy เสร็จ (Issue #5) -->
-   <!-- 👉 [**เปิดแอป The Middle Way**](https://the-middle-way.vercel.app) -->
+   👉 **Version ล่าสุด (Production):** [https://the-middle-way.vercel.app](https://the-middle-way.vercel.app)  
+   👉 **Version ทดสอบ (Preview):** ดูลิงก์ใน Comment ของ PR แต่ละอัน
 
 3. เปิดได้เลย ไม่ต้องติดตั้งอะไร! 🎉
 
@@ -82,78 +97,13 @@
 
 ## 🧪 สิ่งที่ต้องทดสอบ
 
-### ✅ ทดสอบที่ 1: เปิดแอปครั้งแรก
-
-| ขั้นตอน | สิ่งที่ควรเห็น |
-|---------|--------------|
-| เปิดแอปขึ้นมา | หน้าจอสีฟ้าอ่อนสดใส (Bright Sky) |
-| ด้านบน | มีข้อความ "The Middle Way" ตัวหนา สีน้ำเงินเข้ม |
-| มุมขวาบน | มีไอคอนรูป 🌙 **พระจันทร์เสี้ยว** (ปุ่มเปลี่ยนธีม) — ทุก platform ใช้ icon รูปแบบเดียวกัน |
-| ด้านล่าง | มีแถบ navigation: Home, Library, Courses, Profile |
-
-**ให้ทำเครื่องหมาย:** ☐ เห็นตามที่บอก / ☐ ไม่เห็น / ☐ เห็นแต่ไม่ตรง
-
----
-
-### ✅ ทดสอบที่ 2: สลับธีมสีเข้ม (Dark Mode)
-
-| ขั้นตอน | สิ่งที่ควรเห็น |
-|---------|--------------|
-| กดไอคอน 🌙 มุมขวาบน | หน้าจอเปลี่ยนเป็นสีเข้ม (สีน้ำเงินกรมท่า) |
-| สังเกตไอคอน | เปลี่ยนเป็นรูป ☀️ **ดวงอาทิตย์พร้อมเส้นรังสี** |
-| สังเกตตัวหนังสือ | เปลี่ยนเป็นสีขาว/อ่อน อ่านง่าย |
-| สังเกตปุ่ม/ลิงก์ | เปลี่ยนเป็นสีเหลือง/ทอง |
-
-**ให้ทำเครื่องหมาย:** ☐ เปลี่ยนได้ถูกต้อง / ☐ ไม่เปลี่ยน / ☐ เปลี่ยนแต่สีผิดปกติ
-
----
-
-### ✅ ทดสอบที่ 3: สลับกลับธีมสีอ่อน (Light Mode)
-
-| ขั้นตอน | สิ่งที่ควรเห็น |
-|---------|--------------|
-| กดไอคอน ☀️ มุมขวาบน | หน้าจอเปลี่ยนกลับเป็นสีฟ้าอ่อน |
-| สังเกตไอคอน | เปลี่ยนกลับเป็นรูป 🌙 พระจันทร์ |
-
-**ให้ทำเครื่องหมาย:** ☐ เปลี่ยนกลับได้ถูกต้อง / ☐ ไม่เปลี่ยนกลับ
+คู่มือทดสอบแยกตาม Feature — กดลิงก์เพื่อดูขั้นตอนโดยละเอียด:
 
----
-
-### ✅ ทดสอบที่ 4: ปิดแล้วเปิดใหม่ (จำค่าได้)
-
-| ขั้นตอน | สิ่งที่ควรเห็น |
-|---------|--------------|
-| สลับไปธีมสีเข้ม (Dark) | หน้าจอเป็นสีเข้ม |
-| ปิดแอปทิ้ง (ปัดทิ้ง / ปิด tab) | - |
-| เปิดแอปใหม่อีกครั้ง | ยังคงเป็นธีมสีเข้ม (Dark) ตามที่เลือกไว้ |
-
-**ให้ทำเครื่องหมาย:** ☐ จำค่าได้ / ☐ ไม่จำ (รีเซ็ตกลับไป)
-
----
-
-### ✅ ทดสอบที่ 5: กดดูทุกหน้า
-
-| ขั้นตอน | สิ่งที่ควรเห็น |
-|---------|--------------|
-| กด **Home** ในแถบด้านล่าง | หน้า Home แสดงธีมถูกต้อง |
-| กด **Library** | หน้า Library แสดงธีมถูกต้อง |
-| กด **Courses** | หน้า Courses แสดงธีมถูกต้อง |
-| กด **Profile** | หน้า Profile แสดงธีมถูกต้อง |
-| ทำซ้ำขั้นตอน 1-4 หลังสลับธีม | ทุกหน้าแสดงธีมตรงกัน ไม่มีหน้าค้างธีมเก่า |
-
-**ให้ทำเครื่องหมาย:** ☐ ทุกหน้าถูกต้อง / ☐ มีบางหน้าสีผิดปกติ (ระบุหน้า: __________)
+| Feature | Issue | คู่มือทดสอบ |
+|---------|-------|------------|
+| 🎨 Light/Dark Theme | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | [📋 testing-guide.md](./docs/features/3_issue-13_light-dark-theme/testing-guide.md) |
 
----
-
-### ✅ ทดสอบที่ 6: ตัวหนังสืออ่านง่ายไหม?
-
-| สิ่งที่ต้องสังเกต | Light Mode (สีฟ้าอ่อน) | Dark Mode (สีเข้ม) |
-|------------------|---------------------|-------------------|
-| หัวข้อหลัก | ☐ อ่านง่าย | ☐ อ่านง่าย |
-| ข้อความรอง | ☐ อ่านง่าย | ☐ อ่านง่าย |
-| ปุ่มและลิงก์ | ☐ เห็นชัด | ☐ เห็นชัด |
-| การ์ดเนื้อหา | ☐ แยกออกจากพื้นหลัง | ☐ แยกออกจากพื้นหลัง |
-| ไอคอน navigation | ☐ เห็นชัด | ☐ เห็นชัด |
+> 💡 เมื่อมี feature ใหม่ จะเพิ่ม testing guide เฉพาะ feature ไว้ใน `docs/features/<feature>/testing-guide.md`
 
 ---
 
@@ -171,29 +121,9 @@
 
 ---
 
-## 🎨 ตัวอย่างหน้าจอ
-
-### ☀️ Light Mode — "Bright Sky"
-- สีพื้น: ฟ้าอ่อนสดใส สบายตา
-- ปุ่มและสิ่งสำคัญ: สีฟ้าสด
-- การ์ด: สีฟ้าอ่อนโปร่ง
-- ตัวหนังสือ: สีน้ำเงินเข้ม
-- ไอคอนสลับธีม: 🌙 **พระจันทร์เสี้ยว** (กดเพื่อเปลี่ยนเป็นสีเข้ม)
-
-### 🌙 Dark Mode — "Deep Cosmos"
-- สีพื้น: น้ำเงินเข้มมาก
-- ปุ่มและสิ่งสำคัญ: สีทอง/เหลืองอำพัน
-- การ์ด: สีเทาเข้ม
-- ตัวหนังสือ: สีขาว/ครีม
-- ไอคอนสลับธีม: ☀️ **ดวงอาทิตย์พร้อมเส้นรังสี** (กดเพื่อเปลี่ยนเป็นสีอ่อน)
-
-> 💡 ไอคอน sun/moon มีรูปแบบเดียวกันทุก platform (Web, Android, iOS)
-
----
-
 ## 📌 ข้อมูลเพิ่มเติม
 
-- 📋 **รายละเอียดทางเทคนิค:** ดูที่ [Feature Documentation](./docs/features/3_issue-13_light-dark-theme/light-dark-theme.md)
+- 📋 **Feature Documents:** ดูที่ [docs/features/](./docs/features/)
 - 🍎 **สถานะ TestFlight (iOS):** ติดตามที่ [Issue #2](https://github.com/oatrice/TheMiddleWay-IOS/issues/2)
 - 🤖 **ดาวน์โหลด APK (Android):** [GitHub Releases](https://github.com/oatrice/TheMiddleWay-Android/releases/latest)
 
diff --git a/docs/features/3_issue-13_light-dark-theme/testing-guide.md b/docs/features/3_issue-13_light-dark-theme/testing-guide.md
new file mode 100644
index 0000000..65df1af
--- /dev/null
+++ b/docs/features/3_issue-13_light-dark-theme/testing-guide.md
@@ -0,0 +1,109 @@
+# 🧪 คู่มือทดสอบ: Light/Dark Theme
+
+> **Feature:** [Issue #13 - Light/Dark Theme Support](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13)  
+> **วันที่อัปเดต:** 10 กุมภาพันธ์ 2569  
+> **เวอร์ชัน:** v0.2.0-dev
+
+> 📖 **วิธีดาวน์โหลด/ติดตั้งแอป** และ **วิธีแจ้งบัค** ดูที่ [คู่มือทดสอบหลัก](../../../TESTING_GUIDE.md)
+
+---
+
+## ✅ ทดสอบที่ 1: เปิดแอปครั้งแรก
+
+| ขั้นตอน | สิ่งที่ควรเห็น |
+|---------|--------------|
+| เปิดแอปขึ้นมา | หน้าจอสีฟ้าอ่อนสดใส (Bright Sky) |
+| ด้านบน | มีข้อความ "The Middle Way" ตัวหนา สีน้ำเงินเข้ม |
+| มุมขวาบน | มีไอคอนรูป 🌙 **พระจันทร์เสี้ยว** (ปุ่มเปลี่ยนธีม) — ทุก platform ใช้ icon รูปแบบเดียวกัน |
+| ด้านล่าง | มีแถบ navigation: Home, Library, Courses, Profile |
+
+**ให้ทำเครื่องหมาย:** ☐ เห็นตามที่บอก / ☐ ไม่เห็น / ☐ เห็นแต่ไม่ตรง
+
+---
+
+## ✅ ทดสอบที่ 2: สลับธีมสีเข้ม (Dark Mode)
+
+| ขั้นตอน | สิ่งที่ควรเห็น |
+|---------|--------------|
+| กดไอคอน 🌙 มุมขวาบน | หน้าจอเปลี่ยนเป็นสีเข้ม (สีน้ำเงินกรมท่า) |
+| สังเกตไอคอน | เปลี่ยนเป็นรูป ☀️ **ดวงอาทิตย์พร้อมเส้นรังสี** |
+| สังเกตตัวหนังสือ | เปลี่ยนเป็นสีขาว/อ่อน อ่านง่าย |
+| สังเกตปุ่ม/ลิงก์ | เปลี่ยนเป็นสีเหลือง/ทอง |
+
+**ให้ทำเครื่องหมาย:** ☐ เปลี่ยนได้ถูกต้อง / ☐ ไม่เปลี่ยน / ☐ เปลี่ยนแต่สีผิดปกติ
+
+---
+
+## ✅ ทดสอบที่ 3: สลับกลับธีมสีอ่อน (Light Mode)
+
+| ขั้นตอน | สิ่งที่ควรเห็น |
+|---------|--------------|
+| กดไอคอน ☀️ มุมขวาบน | หน้าจอเปลี่ยนกลับเป็นสีฟ้าอ่อน |
+| สังเกตไอคอน | เปลี่ยนกลับเป็นรูป 🌙 พระจันทร์ |
+
+**ให้ทำเครื่องหมาย:** ☐ เปลี่ยนกลับได้ถูกต้อง / ☐ ไม่เปลี่ยนกลับ
+
+---
+
+## ✅ ทดสอบที่ 4: ปิดแล้วเปิดใหม่ (จำค่าได้)
+
+| ขั้นตอน | สิ่งที่ควรเห็น |
+|---------|--------------|
+| สลับไปธีมสีเข้ม (Dark) | หน้าจอเป็นสีเข้ม |
+| ปิดแอปทิ้ง (ปัดทิ้ง / ปิด tab) | - |
+| เปิดแอปใหม่อีกครั้ง | ยังคงเป็นธีมสีเข้ม (Dark) ตามที่เลือกไว้ |
+
+**ให้ทำเครื่องหมาย:** ☐ จำค่าได้ / ☐ ไม่จำ (รีเซ็ตกลับไป)
+
+---
+
+## ✅ ทดสอบที่ 5: กดดูทุกหน้า
+
+| ขั้นตอน | สิ่งที่ควรเห็น |
+|---------|--------------|
+| กด **Home** ในแถบด้านล่าง | หน้า Home แสดงธีมถูกต้อง |
+| กด **Library** | หน้า Library แสดงธีมถูกต้อง |
+| กด **Courses** | หน้า Courses แสดงธีมถูกต้อง |
+| กด **Profile** | หน้า Profile แสดงธีมถูกต้อง |
+| ทำซ้ำขั้นตอน 1-4 หลังสลับธีม | ทุกหน้าแสดงธีมตรงกัน ไม่มีหน้าค้างธีมเก่า |
+
+**ให้ทำเครื่องหมาย:** ☐ ทุกหน้าถูกต้อง / ☐ มีบางหน้าสีผิดปกติ (ระบุหน้า: __________)
+
+---
+
+## ✅ ทดสอบที่ 6: ตัวหนังสืออ่านง่ายไหม?
+
+| สิ่งที่ต้องสังเกต | Light Mode (สีฟ้าอ่อน) | Dark Mode (สีเข้ม) |
+|------------------|---------------------|-------------------|
+| หัวข้อหลัก | ☐ อ่านง่าย | ☐ อ่านง่าย |
+| ข้อความรอง | ☐ อ่านง่าย | ☐ อ่านง่าย |
+| ปุ่มและลิงก์ | ☐ เห็นชัด | ☐ เห็นชัด |
+| การ์ดเนื้อหา | ☐ แยกออกจากพื้นหลัง | ☐ แยกออกจากพื้นหลัง |
+| ไอคอน navigation | ☐ เห็นชัด | ☐ เห็นชัด |
+
+---
+
+## 🎨 ตัวอย่างหน้าจอ
+
+### ☀️ Light Mode — "Bright Sky"
+- สีพื้น: ฟ้าอ่อนสดใส สบายตา
+- ปุ่มและสิ่งสำคัญ: สีฟ้าสด
+- การ์ด: สีฟ้าอ่อนโปร่ง
+- ตัวหนังสือ: สีน้ำเงินเข้ม
+- ไอคอนสลับธีม: 🌙 **พระจันทร์เสี้ยว** (กดเพื่อเปลี่ยนเป็นสีเข้ม)
+
+### 🌙 Dark Mode — "Deep Cosmos"
+- สีพื้น: น้ำเงินเข้มมาก
+- ปุ่มและสิ่งสำคัญ: สีทอง/เหลืองอำพัน
+- การ์ด: สีเทาเข้ม
+- ตัวหนังสือ: สีขาว/ครีม
+- ไอคอนสลับธีม: ☀️ **ดวงอาทิตย์พร้อมเส้นรังสี** (กดเพื่อเปลี่ยนเป็นสีอ่อน)
+
+> 💡 ไอคอน sun/moon มีรูปแบบเดียวกันทุก platform (Web, Android, iOS)
+
+---
+
+## 📌 ข้อมูลเพิ่มเติม
+
+- 📋 **รายละเอียดทางเทคนิค:** ดูที่ [Feature Documentation](./light-dark-theme.md)
+- 📖 **คู่มือทดสอบหลัก:** ดูที่ [TESTING_GUIDE.md](../../../TESTING_GUIDE.md)
diff --git a/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/analysis.md b/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/analysis.md
new file mode 100644
index 0000000..30eb10f
--- /dev/null
+++ b/docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/analysis.md
@@ -0,0 +1,259 @@
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
+| **Feature Name** | Persistence Layer: LocalStorage System for Progress Tracking |
+| **Issue URL** | [#15](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15) |
+| **Date** | 2026-02-10 |
+| **Analyst** | Luma AI (Senior Technical Analyst) |
+| **Priority** | 🔴 High |
+| **Status** | ✅ Ready |
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
+The application currently lacks a mechanism to save user progress on their local device. When a user closes the application or browser tab, all progress (e.g., completed lessons, quiz attempts, current location in a course) is lost. This forces users to start over from the beginning in each new session, leading to a frustrating and disjointed user experience.
+```
+
+### 1.2 User Stories
+
+| # | As a | I want to | So that |
+|---|------|-----------|---------|
+| 1 | User | have my progress automatically saved on my device | I can close the app and resume where I left off later without losing my work. |
+| 2 | Developer | have a simple, standardized API to save and retrieve user progress data | I can easily implement progress tracking across different features consistently. |
+
... (Diff truncated for size) ...

PR TEMPLATE:


INSTRUCTIONS:
1. Generate a comprehensive PR description in Markdown format.
2. If a template is provided, fill it out intelligently.
3. If no template, use a standard structure: Summary, Changes, Impact.
4. Focus on 'Why' and 'What'.
5. Do not include 'Here is the PR description' preamble. Just the body.
6. IMPORTANT: Always use FULL URLs for links to issues and other PRs (e.g., https://github.com/owner/repo/issues/123), do NOT use short syntax (e.g., #123) to ensuring proper linking across platforms.
