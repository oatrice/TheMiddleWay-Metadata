# Mobile First Development Rules

> 📱 กฎเหล็กสำหรับการพัฒนาแบบ Mobile First Strategy

## 🔴 CORE PRINCIPLE (หลักการสำคัญที่สุด)

**"Mobile Mock UI First -> Android Full -> Mobile Web Full -> iOS Full"**

ลำดับการพัฒนาต้องเป็นดังนี้เสมอ:

1.  **Mobile-Web Mock UI (Step 1)**:
    -   **เป้าหมาย**: เห็นภาพ UI/UX บนหน้าจอมือถือก่อนเริ่ม Logic
    -   **Platform**: Web (Next.js)
    -   **Action**: สร้าง Mockup หน้าจอ โดยเน้น Mobile Viewport เท่านั้น
    -   **Condition**: ห้ามทำ PC View หรือ Full Responsiveness ในขั้นตอนนี้

2.  **Android Full Function (Step 2)**:
    -   **เป้าหมาย**: พัฒนา Logic และ Feature หลักให้เสร็จสมบูรณ์
    -   **Platform**: Android (Kotlin/Compose)
    -   **Action**: Implement API Integration, Local Database, Business Logic

3.  **Mobile Web Full Feature (Step 3)**:
    -   **เป้าหมาย**: นำ Logic มาใส่ใน Web Mockup ที่ทำไว้
    -   **Platform**: Web (Next.js)
    -   **Action**: เชื่อมต่อ API, State Management

4.  **iOS Full Feature (Step 4)**:
    -   **สถานะปัจจุบัน**: ⏸️ *Deferred / Pending*
    -   **หมายเหตุ**: รอมีเครื่อง Test หรือคำสั่งเพิ่มเติม

---

## 🟡 PRE-CODING RULES (ก่อนเริ่ม Code)

### 1. Requirement Confirmation
- **MUST** ยืนยัน Requirements และ Acceptance Criteria
- **MUST** ระบุว่า Feature นี้กระทบ Mobile Flow อย่างไร

### 2. Impact Assessment
- **MUST** วิเคราะห์ Impact ต่อระบบเดิม (ถ้ามี)
- **MUST** ตรวจสอบว่า API รองรับ Mobile use case หรือไม่

### 3. Task Documentation
- **MUST** สร้าง Issue/Ticket
- **MUST** ย่อยงานตาม Flow (Mock -> Android -> Web)

---

## 🟢 UI/UX GUIDELINES

### 1. Touch Trumps Click
- Elements ต้องมีขนาดใหญ่พอสำหรับนิ้วแตะ (Min 44x44px)
- Interaction ต้องออกแบบมาเพื่อ Touch Screen

### 2. Content Prioritization
- แสดงเนื้อหาที่สำคัญที่สุดก่อน
- ซ่อน Secondary Actions ใน Menu หรือ Bottom Sheet

---

## ❌ DON'T DO (ห้ามทำ)

- **DON'T** เริ่มทำ Desktop UI ก่อน Mobile UI
- **DON'T** เริ่มทำ Logic บน Web ก่อน Android (ยกเว้น Mock UI)
- **DON'T** ข้ามขั้นตอน Mock UI ไปทำ Logic เลย
