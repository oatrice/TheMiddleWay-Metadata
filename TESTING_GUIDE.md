# 📱 คู่มือทดสอบแอป The Middle Way
## สำหรับผู้ทดสอบทุกท่าน

> **วันที่อัปเดต:** 10 กุมภาพันธ์ 2569  
> **เวอร์ชัน:** v0.2.0-dev

---

## 📖 แอปนี้คืออะไร?

**The Middle Way** คือแอปสำหรับการฝึกสติและค้นหาสมดุลในชีวิต  
ขณะนี้อยู่ระหว่างพัฒนา — ขอเชิญท่านทดสอบเวอร์ชันล่าสุด 🙏

---

## 📊 สถานะแต่ละ Platform

### 🛠️ สำหรับนักพัฒนา (Development Builds)
หากต้องการทดสอบฟีเจอร์ล่าสุดที่ยังไม่ได้ปล่อย Release:

1. **Android:** ไปที่ [Actions Tab](https://github.com/oatrice/TheMiddleWay-Android/actions) > เลือก Workflow ล่าสุด > โหลด `app-debug` จาก Artifacts
2. **Web:** ไปที่ [Pull Requests](https://github.com/oatrice/TheMiddleWay-Web/pulls) > เลือก PR ที่ต้องการ > ดูลิงก์ **Visit Preview** จาก Vercel bot
3. **iOS:** ตรวจสอบสถานะการ Build ที่ [Actions Tab](https://github.com/oatrice/TheMiddleWay-IOS/actions) (ยังไม่มี Artifact ให้โหลด)

---

## 📊 สถานะแต่ละ Platform (Release)

| Platform | สถานะ | วิธีติดตั้ง |
|----------|--------|------------|
| 🤖 Android | ✅ พร้อมทดสอบ | ดาวน์โหลด APK จาก GitHub Releases หรือ Actions |
| 🍎 iOS | ⚠️ ต้องใช้ Mac | ติดตั้งผ่าน Xcode (สาย USB) หรือ TestFlight (ถ้ามีบัญชี Dev) |
| 🌐 Web | ✅ Deploy เรียบร้อย | เปิดจาก Vercel Preview URL (ใน PR) |

---

## 📦 วิธีเข้าถึง Build (Specific Versions)

เพื่อให้การทดสอบแม่นยำ กรุณาเลือก Build ให้ตรงกับ Version หรือ Commit ที่ต้องการทดสอบ:

### 🤖 Android
- **Latest Release (แนะนำ):**  
  [👉 Download Latest APK](https://github.com/oatrice/TheMiddleWay-Android/releases/latest/download/app-release.apk)
- **Specific Version:**  
  สามารถเปลี่ยน `TAG` ในลิงก์เป็นเวอร์ชันที่ต้องการ:  
  `https://github.com/oatrice/TheMiddleWay-Android/releases/download/<TAG>/app-release.apk`  
  (ตัวอย่าง: `.../v0.1.0/app-release.apk`)  
  หรือไปเลือกเองที่หน้า [Releases Page](https://github.com/oatrice/TheMiddleWay-Android/releases)

### 🌐 Web
- **Production (ล่าสุด):** [the-middle-way.vercel.app](https://the-middle-way.vercel.app)
- **Preview (Specific Commit/PR):**  
  ลิงก์จะอยู่ใน **Comment ของ PR** ใน GitHub หรือเช็คที่ Deployment Dashboard  
  Format: `https://the-middle-way-git-<branch-name>-oatrice.vercel.app`

### 🍎 iOS
- **TestFlight (Recommended):**  
  รอรับอีเมลเชิญ หรือลิงก์ Public Link (เมื่อเปิดใช้งาน)  
  *Build จะระบุ Version และ Build Number ชัดเจนในแอป TestFlight*

---

## 📥 วิธีดาวน์โหลดและติดตั้ง

### 🤖 Android (โทรศัพท์ Android)

1. เปิดลิงก์นี้จากโทรศัพท์ Android:  
   👉 [**ดาวน์โหลด APK จาก GitHub**](https://github.com/oatrice/TheMiddleWay-Android/releases/latest)

2. เลื่อนลงมาหา **Assets** แล้วกดที่ไฟล์ **`app-debug.apk`** เพื่อดาวน์โหลด

3. เมื่อดาวน์โหลดเสร็จ กดเปิดไฟล์เพื่อติดตั้ง
   - ถ้ามีข้อความเตือน "ไม่อนุญาตให้ติดตั้งจากแหล่งที่ไม่รู้จัก" → กดอนุญาต
   - นี่เป็นเรื่องปกติ เพราะแอปยังไม่อยู่ใน Play Store

4. กด **ติดตั้ง** → รอสักครู่ → กด **เปิด**

> ⚠️ หากยังไม่มีไฟล์ APK ใน Release กรุณาแจ้งทีมพัฒนาเพื่อ upload

---

### 🍎 iOS (iPhone)

การทดสอบบน iOS มีความเข้มงวดกว่า Android เล็กน้อย แบ่งเป็น 2 กรณี:

#### กรณีที่ 1: ติดตั้งผ่านสาย USB (ฟรี - แนะนำสำหรับ Dev)
หากคุณมีเครื่อง Mac และ Xcode ติดตั้งอยู่:
1. เปิดโปรเจกต์ `Platforms/iOS/TheMiddleWay.xcodeproj` ด้วย Xcode
2. เสียบ iPhone เข้ากับ Mac
3. เลือก Target เป็น iPhone ของคุณ
4. กดปุ่ม ▶️ **Run**
5. (ครั้งแรก) บน iPhone ไปที่ **Settings > General > VPN & Device Management** แล้วกด Trust Developer App

> 💡 **ข้อจำกัด:** แอปจะอยู่ได้ 7 วัน ต้องติดตั้งใหม่ถ้าหมดอายุ

#### กรณีที่ 2: ติดตั้งผ่าน TestFlight (ต้องมีบัญชี Apple Dev $99/ปี)
👉 *วิธีนี้สะดวกสุดสำหรับผู้ใช้ทั่วไป แต่ต้องรอทีมงานตั้งค่าระบบก่อน*

1. ติดตั้งแอป **TestFlight** จาก App Store (ฟรี)
2. รอรับ **Email เชิญทดสอบ** หรือกดลิงก์ที่ทีมส่งให้
3. กด **"View in TestFlight"** → **Install**
4. แอปจะอยู่ได้ 90 วัน ไม่ต้องต่อคอมพิวเตอร์

> ⏳ **สถานะปัจจุบัน:** รอการตั้งค่า Account (ติดตามที่ [Issue #2](https://github.com/oatrice/TheMiddleWay-IOS/issues/2))

---

### 🌐 Web (เปิดจาก Browser — ไม่ต้องติดตั้ง!)

1. เปิด Browser (Chrome, Safari, หรือ Firefox) ได้ทั้งจากมือถือและคอม
2. ไปที่ลิงก์:  
   👉 **Version ล่าสุด (Production):** [https://the-middle-way.vercel.app](https://the-middle-way.vercel.app)  
   👉 **Version ทดสอบ (Preview):** ดูลิงก์ใน Comment ของ PR แต่ละอัน

3. เปิดได้เลย ไม่ต้องติดตั้งอะไร! 🎉

> 💡 **Vercel** คือบริการ hosting เว็บไซต์ — เปิดจากลิงก์ได้เลย ปลอดภัย ไม่ต้องดาวน์โหลดไฟล์ใดๆ  
> ทดสอบได้ทั้งจากมือถือ (เปิด Safari/Chrome) และจากคอมพิวเตอร์

> 📋 **ติดตามสถานะ deploy:** [Issue #5](https://github.com/oatrice/TheMiddleWay-Metadata/issues/5)

---

## 🧪 สิ่งที่ต้องทดสอบ

คู่มือทดสอบแยกตาม Feature — กดลิงก์เพื่อดูขั้นตอนโดยละเอียด:

| Feature | Issue | คู่มือทดสอบ |
|---------|-------|------------|
| 🎨 Light/Dark Theme | [#13](https://github.com/oatrice/TheMiddleWay-Metadata/issues/13) | [📋 testing-guide.md](./docs/features/3_issue-13_light-dark-theme/testing-guide.md) |
| 💾 Persistence Layer | [#15](https://github.com/oatrice/TheMiddleWay-Metadata/issues/15) | [📋 testing-guide.md](./docs/features/4_issue-6_infrastructure-persistence-layer-localstorage-system-for-progress-tracking/testing-guide.md) |
| 🌿 Wisdom Garden (Dashboard) | [#1](https://github.com/oatrice/TheMiddleWay-Metadata/issues/1) | [📋 testing-guide.md](./docs/features/6_issue-1_feature-สรางหนา-สวนแหงปญญา-wisdom-garden-dashboard/testing_guide.md) |
| ✅ Weekly Practices (Room) | [#2](https://github.com/oatrice/TheMiddleWay-Metadata/issues/2) | [📋 testing-guide.md](./docs/features/7_issue-2_feature-weekly-practices-checklist/testing_guide.md) |
| 🔐 User Authentication & Sync | [#14](https://github.com/mdwmediaworld072/TheMiddleWay/issues/14) | [📋 testing-guide.md](./docs/features/9_issue-14_feature-user-authentication-sync/testing_guide.md) |

> 💡 เมื่อมี feature ใหม่ จะเพิ่ม testing guide เฉพาะ feature ไว้ใน `docs/features/<feature>/testing-guide.md`

---

## 🐛 เจอปัญหา? แจ้งตามนี้

กรุณาจดข้อมูลเหล่านี้แล้วส่งให้ทีมพัฒนา:

1. **ทดสอบข้อไหน?** (เช่น ทดสอบที่ 2)
2. **ใช้เครื่องอะไร?** (เช่น Samsung Galaxy S24, iPhone 16, Chrome บน Laptop)
3. **ทำอะไรอยู่ตอนเจอปัญหา?** (เช่น กดสลับธีม)
4. **เกิดอะไรขึ้น?** (เช่น หน้าจอกระพริบ, สียังคงเป็นสีเดิม)
5. **ถ่ายรูปหน้าจอ** (ถ้าสะดวก)

📧 ส่งรายงานได้ที่: *(ใส่ช่องทางติดต่อ)*

---

## 📌 ข้อมูลเพิ่มเติม

- 📋 **Feature Documents:** ดูที่ [docs/features/](./docs/features/)
- 🍎 **สถานะ TestFlight (iOS):** ติดตามที่ [Issue #2](https://github.com/oatrice/TheMiddleWay-IOS/issues/2)
- 🤖 **ดาวน์โหลด APK (Android):** [GitHub Releases](https://github.com/oatrice/TheMiddleWay-Android/releases/latest)

---

## 🙏 ขอบคุณที่ช่วยทดสอบ

ทุกความคิดเห็นมีค่ามากสำหรับทีมพัฒนา  
ขอบคุณที่เสียสละเวลาช่วยทดสอบครับ/ค่ะ 🙏✨
