# Verification Guide: API-Centric Architecture & Data Sync

This application now operates on a **100% API-Centric Architecture**. Direct connections to Firebase Firestore from client applications (Web, Android, iOS) have been completely removed. All data operations are routed through the Go backend API.

## 1. Network Environment Switcher Verification

All three client platforms now feature a Network Environment Switcher in their Developer Settings or Profile page.

### A. Web Platform
1.  **Login:** Open the app (`http://localhost:3000`) and sign in with Google.
2.  **Locate Switcher:** Scroll to the bottom of the Profile page (visible in Development mode).
3.  **Test Modes:**
    - Switch to **Render (PROD)**. Verify data loads from the production Go backend.
    - Switch to **Localhost (DEV)**. Verify data loads from your local `http://localhost:8080/api/v1` server. (Ensure the Go server is running).
    - Switch to **Custom URL**. Enter a custom endpoint and verify requests are routed correctly.
4.  **Sync Check:** Toggle a practice item in the Wisdom Garden. Ensure the change persists after refreshing the page.

### B. Android Platform
1.  **Build & Run:** Deploy the app to an emulator or physical device.
2.  **Login:** Sign in with Google.
3.  **Locate Switcher:** Go to the Profile screen and find the "Developer Settings" section.
4.  **Test Modes:** Use the Radio buttons to switch between Render, Localhost (10.0.2.2), and Custom URL.
5.  **Sync Check:** Toggle items in the Wisdom Garden. Kill the app and reopen it to ensure the state persists and is fetched from the selected API.

### C. iOS Platform
1.  **Build & Run:** Deploy the app via Xcode.
2.  **Locate Switcher:** Open Developer Settings.
3.  **Test Modes:** Use the Picker to switch environments. The Custom URL option will reveal a TextField for custom input.
4.  **Sync Check:** Toggle items and verify network requests via Xcode console logs.

---

## 2. General "Cold Start" (Guest / New User)
1.  **Web:** Open in Incognito. Should see empty state or prompt to login.
2.  **Mobile:** Clear App Data. Launch. Should prompt for Google Sign-In.

---

## 3. Backend Scaling & Security (Neon + Multi-tenancy)

### Database Connectivity
- Both the **Localhost (DEV)** server and the **Render (PROD)** server are currently configured to connect to the **SAME Neon Postgres Database**. 
- The `DATABASE_URL` used locally in `.env` matches the connection string configured in the Render dashboard.

### Authentication
- Integrated **Firebase Authentication Middleware** in Go.
- Validates ID Tokens and extracts `UserID` for all `/api/v1/wisdom-garden/*` endpoints.

### User Segregation
- Implemented **Lazy Copy** logic: When a user requests data for a week, if they don't have it, the backend copies "Master Data" to their customized data tier.

### How to Run
- **Production (Neon):** `DATABASE_URL=postgres://... ./server`
- **Local (Neon):** The local server defaults to the Neon DB if `DATABASE_URL` is provided in `.env`.
