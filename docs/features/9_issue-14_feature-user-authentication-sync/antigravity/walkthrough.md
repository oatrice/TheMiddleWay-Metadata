# Verification Guide: Offline Support & Data Sync

## 1. Web Platform Verification

### A. Firestore Realtime & Persistence (Default)
1.  **Login:** Open the app (`http://localhost:3000`) and sign in with Google.
2.  **Modify Data:** Go to "Wisdom Garden" (Weekly Practices). Toggle a few checkboxes.
3.  **Persist Check:** Refresh the page. The checkboxes should remain checked.
4.  **Offline Check:**
    -   Open Browser DevTools -> Network -> Change throttling to **"Offline"**.
    -   Toggle more checkboxes.
    -   Refresh the page (while offline). The state should persist (loaded from IndexedDB).
5.  **Sync Check:**
    -   Turn Network back **"Online"**.
    -   Check Firestore Console (`users/{uid}/weekly_practices/{weekId}`). The changes made while offline should now appear.

### B. API Mode Switching (Go Backend)
1.  **Enable API Mode:**
    -   Open `.env.local` (or `hooks/useWisdomGarden.ts`).
    -   Set `NEXT_PUBLIC_USE_API=true`.
    -   Restart the dev server (`npm run dev`).
2.  **Verify Traffic:**
    -   Reload the page.
    -   Open Network Tab.
    -   You should see requests to `http://localhost:8080/api/v1/wisdom-garden/...` instead of Firestore WebSocket connections.
    -   **Note:** Offline support is *not* available in this mode (unless Service Workers are added).

---

## 2. Android Platform Verification

### A. Firestore Realtime & Persistence (Default)
1.  **Build & Run:** Deploy the app to a simulator/device.
2.  **Login:** Sign in with Google.
3.  **Modify Data:** Toggle practice items.
4.  **Offline Check:**
    -   Turn on **Airplane Mode** on the device.
    -   Toggle items.
    -   Kill the app and reopen it.
    -   The state should persist.
5.  **Sync Check:**
    -   Turn off Airplane Mode.
    -   Verify data syncing to Firebase Console.

### Verification Results
- [x] **iOS Data Sync**: Verified working with both API and Firestore (after seeding).
- [x] **Profile UI**: Updated to remove "Done" button and match Tab style.
- [ ] **Dynamic Switching**: Found bug where restart is required to switch modes.

### Known Issues
- **Issue #49**: [Bug: API/Firestore Switching requires App Restart on iOS](https://github.com/oatrice/TheMiddleWay-Metadata/issues/49). (Need to verify on Android/Web).

### B. Switching to Go Backend (Retrofit)
1.  **Modify Code:**
    -   Open `Platforms/Android/app/src/main/java/com/oatrice/themiddleway/di/AppModule.kt`.
    -   **Comment out** "Option A" (Firestore binding).
    -   **Uncomment** "Option B" (Network binding).
    -   *Note: Ensure `NetworkModule.kt` points to your computer's IP (e.g., `10.0.2.2` for Emulator), not `localhost`.*
2.  **Rebuild:** Re-run the app.
3.  **Verify:** Check Logcat (`Timber`) for network requests failing or succeeding depending on your local backend status.

---

## 3. General "Cold Start" (Guest / New User)
1.  **Web:** Open in Incognito. Should see empty state or prompt to login.
2.  **Android:** Clear App Data. Launch. Should prompt for Google Sign-In.
## Backend Scaling & Security (Neon + Multi-tenancy)

### 1. Database & Multi-tenancy
- **Postgres (Neon):** Primary database for production.
- **SQLite (Fallback):** Added support for local development via `DB_DRIVER=sqlite`.
- **User Segregation:** 
    - Added `UserID` to all Practice models (`WeeklyData`, `Category`, `PracticeItem`).
    - Implemented **Lazy Copy** logic: When a user requests data for a week, if they don't have it, the backend copies "Master Data" to their customized data.

### 2. Authentication
- Integrated **Firebase Authentication Middleware** in Go.
- Validates ID Tokens and extracts `UserID` for all `/api/v1/wisdom-garden/*` endpoints.

### 3. Security Measures
- **Secret Rotation:** Initiated protocol to rotate Database Passwords and Service Account Keys.
- **Environment Variables:** Enforced usage of `.env` for all sensitive strings.
- **CI/CD:** Prep for secret scanning.

### 4. How to Run
- **Production (Neon):** `DATABASE_URL=postgres://... ./server`
- **Local (SQLite):** `DB_DRIVER=sqlite ./server`
