# 🌐 Web Deployment URLs

> เอกสารนี้อธิบายวิธีเข้าถึง Web App ในแต่ละ Environment
> สำหรับ QA, Tester และ Users

---

## 📋 URL Reference

| ประเภท | URL | ใช้เมื่อไหร่ |
|--------|-----|-------------|
| 🟢 **Production** | https://the-middle-way.vercel.app | เวอร์ชัน Stable ล่าสุด (main branch) |
| 🏷️ **Version Tag** | `https://v{X-Y-Z}.the-middle-way.vercel.app` | ทดสอบเวอร์ชันเฉพาะ |
| 🔀 **PR Preview** | ดูจาก PR comment ของ Vercel bot | ทดสอบ PR ก่อน merge |
| 🖥️ **Local Dev** | http://localhost:3000 | dev บนเครื่องตัวเอง |

### ตัวอย่าง Version URLs

| Version | URL |
|---------|-----|
| v0.3.0 | https://v0-3-0.the-middle-way.vercel.app |
| v0.4.0 | https://v0-4-0.the-middle-way.vercel.app |

> ⚠️ Version URLs จะถูกสร้างอัตโนมัติเมื่อ merge PR เข้า `main` และ version เปลี่ยน

---

## 🔄 วิธีการทำงาน (Automated Pipeline)

```
PR Merge → main
  ↓
auto-tag.yml → สร้าง git tag (e.g. v0.4.0)
  ↓
vercel-version-alias.yml → สร้าง URL alias
  ↓
✅ v0-4-0.the-middle-way.vercel.app พร้อมใช้งาน
```

### Flow ทั้งหมด:

1. **Developer** bump version ใน `package.json`
2. **PR ถูก merge** เข้า `main`
3. **`auto-tag.yml`** อ่าน version → สร้าง git tag `v0.4.0`
4. **`vercel-version-alias.yml`** จับ tag → สร้าง Vercel alias URL
5. **QA/Users** เข้าถึงได้ผ่าน URL ข้างต้น

---

## 🔍 ตรวจสอบ Build Info (Runtime)

เปิด URL นี้เพื่อดูข้อมูล deployment ปัจจุบัน:

```
GET /api/app-info
```

**Response:**
```json
{
  "urls": {
    "current": "https://the-middle-way.vercel.app",
    "prod": "https://the-middle-way.vercel.app",
    "preview": "https://the-middle-way-git-feat-xxx.vercel.app",
    "dev": "http://localhost:3000",
    "commit": "https://the-middle-way-abc123.vercel.app"
  },
  "build": {
    "env": "production",
    "version": "0.4.0",
    "tag": "v0.4.0",
    "commitSha": "abc123def456...",
    "commitRef": "main"
  }
}
```

---

## 🔧 Setup Required (One-time)

ต้องเพิ่ม Secrets ใน GitHub repo settings:

| Secret | ที่มา |
|--------|------|
| `VERCEL_TOKEN` | [Vercel Settings → Tokens](https://vercel.com/account/tokens) |
| `VERCEL_ORG_ID` | จาก `.vercel/project.json` หลัง `vercel link` |
| `VERCEL_PROJECT_ID` | จาก `.vercel/project.json` หลัง `vercel link` |

### วิธี Setup:

```bash
# 1. Link project กับ Vercel (ทำครั้งเดียว)
cd Platforms/Web
vercel link

# 2. ดู org/project IDs
cat .vercel/project.json

# 3. เพิ่ม secrets ใน GitHub
gh secret set VERCEL_TOKEN --repo oatrice/TheMiddleWay-Web
gh secret set VERCEL_ORG_ID --repo oatrice/TheMiddleWay-Web
gh secret set VERCEL_PROJECT_ID --repo oatrice/TheMiddleWay-Web
```
