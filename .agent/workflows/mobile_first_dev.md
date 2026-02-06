---
description: Workflow สำหรับการพัฒนา Feature ใหม่ด้วยกลยุทธ์ Mobile First
---

# Mobile First Development Workflow

> 🚀 Workflow นี้บังคับใช้ลำดับการพัฒนาแบบ Mock UI -> Android -> Web -> iOS

## Phase 1: Analysis & Design

### Step 1.1: Requirement Gather
- [ ] ระบุ User Story
- [ ] กำหนด Acceptance Criteria (เน้น Mobile Experience)

### Step 1.2: Mobile UI Design
- [ ] ออกแบบหน้าจอ Mobile (Wireframe หรือ Sketch)
- [ ] Review Flow การใช้งานบนมือถือ

## Phase 2: Mobile-Web Mock UI (First Code)

> 💡 สร้าง Mockup บนเว็บเพื่อให้เห็นภาพ UI เร็วที่สุด (ยังไม่ต้องต่อ API)

### Step 2.1: Setup Interface
- [ ] สร้าง Page/Component ใหม่ใน Web Project
- [ ] ใช้ Tailwind CSS ออกแบบ Mobile Viewport (`sm:` is default)
- [ ] ใช้ Mock Data (Hardcode) ในการแสดงผล

### Step 2.2: Verify UX
- [ ] ทดสอบกดปุ่มและ Flow หน้าจอ (ด้วย Mock Data)
- [ ] ปรับแก้ UI ตาม Feedback

## Phase 3: Android Implementation (Full Function)

> 🤖 เริ่มทำ Logic จริงบน Android ก่อน

### Step 3.1: Backend Integration (if needed) (Placeholder)
- [ ] ตรวจสอบว่า API พร้อมใช้งาน หรือ Mock API ไว้

### Step 3.2: Android UI & Logic
- [ ] สร้าง UI ใน Jetpack Compose (อิงจาก Web Mock)
- [ ] Implement Business Logic & State Management
- [ ] เชื่อมต่อ API / Database

### Step 3.3: Verify Android
- [ ] Run Test บน Android Emulator/Device
- [ ] ตรวจสอบความถูกต้องของข้อมูล

## Phase 4: Mobile Web Implementation (Full Logic)

> 🌐 กลับมาทำ Web ให้สมบูรณ์

### Step 4.1: Logic Integration
- [ ] แทนที่ Mock Data ด้วย Real API/Data
- [ ] Implement Client State Management

### Step 4.2: Responsiveness Check
- [ ] ตรวจสอบการแสดงผลบนขนาดหน้าจอต่างๆ (Mobile First -> Desktop)

## Phase 5: iOS Implementation (Deferred)

> 🍎 เก็บไว้ทำทีหลังเมื่อพร้อม

- [ ] (Pending) รออุปกรณ์ทดสอบ

## Checklist Summary

```markdown
## Mobile First Checklist

### 1. Mock UI (Web)
- [ ] Create Mobile Mockup on Web ✅
- [ ] Verify UX Flow (Mock Data) ✅

### 2. Android (Real Logic)
- [ ] Implement UI (Compose) ✅
- [ ] Connect API/Services ✅
- [ ] Test on Android ✅

### 3. Web (Real Logic)
- [ ] Integrate API to Web ✅
- [ ] Responsive Check ✅

### 4. iOS
- [ ] (Skipped) ✅
```
