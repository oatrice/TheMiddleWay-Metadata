# User Sync API & Firestore Removal

## Backend
- [x] สร้าง Model `User` (`internal/model/user.go`)
- [x] สร้าง `user_repo.go` สำหรับ Sync User ลง Postgres (with Upsert logic)
- [x] สร้าง Handler `SyncUser` (`internal/handler/auth_handler.go`)
- [x] เพิ่มตาราง `users` ใน `cmd/server/main.go`
- [x] เพิ่ม Route `POST /api/v1/auth/sync`

## Web
- [x] ลบ Firebase Firestore API ออกจาก `auth.service.ts`
- [x] อัปเดต `createUserDocument()` ให้เรียก `fetch('/api/v1/auth/sync')`
- [x] ลบ `db` export จาก `lib/firebase.ts`
- [x] Uninstall แพ็คเกจที่เกี่ยวข้องกับ Firestore (ถ้ามี/ไม่ต้องใช้แล้ว)

## Android 
- [x] Refactor `AuthRepositoryImpl`
      - [x] Remove `FirebaseFirestore` from `AuthRepositoryImpl` class injection
      - [x] Replace `syncUserToFirestore` logic to call `AuthApi.syncUser`
      - [x] Update `signInWithGoogle` method to use `syncUserToBackend` instead of the Firestore one
- [x] Remove Firestore Providers in `DataModule.kt`
- [x] Create `AuthApi` in Android
- [x] Remove `firebase.firestore` dependency from `libs.versions.toml` and `app/build.gradle.kts`
- [x] Fix compilation issues due to `FirestoreWisdomGardenRepository` and Dagger cycle

## iOS
- [ ] อัปเดต SignIn Action ให้ยิงหน้า API `syncUser()`
- [ ] ลบ Dependency `FirebaseFirestore` ออกจาก SPM

## Documentation Updates
- [ ] อัปเดต `docs/features/...` (Metadata Repository) เพิ่มข้อมูล API ใหม่
- [ ] อัปเดต `README.md` หรือ Docs ที่เกี่ยวข้องใน Backend Repo
- [ ] อัปเดต `README.md` หรือ Docs ที่เกี่ยวข้องใน Web Repo
- [ ] อัปเดต `README.md` หรือ Docs ที่เกี่ยวข้องใน Android Repo
- [ ] อัปเดต `README.md` หรือ Docs ที่เกี่ยวข้องใน iOS Repo

## Verification
- [ ] ทดสอบ Login ใหม่ผ่าน Web ว่าข้อมูลเข้า Neon DB
- [ ] Project Android build ผ่านโดยไม่มี Firestore
- [ ] Project iOS build ผ่านโดยไม่มี Firestore
- [ ] Commit & Push ทุก Platform
