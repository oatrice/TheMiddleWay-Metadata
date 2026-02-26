import sys
import glob
import re

replacement = """## 1. Architecture & Design
This plan outlines the implementation of a user authentication and data synchronization system using **Firebase Authentication** for identity management and a Custom **Go Backend / PostgreSQL** as the Single Source of Truth for user profiles and progress. 

**IMPORTANT**: We NO LONGER USE FIREBASE FIRESTORE. All client applications MUST communicate with the Go Backend REST API for data synchronization. Do NOT import or use `firebase/firestore` or any Firestore client libraries.

### Component View
- **Backend (Go / PostgreSQL)**:
  - `POST /api/v1/auth/sync`: Endpoint to create/update the user profile using the Firebase ID Token.
- **Frontend (Client Application)**:
  - Firebase App initialization (Auth only).
  - Service to handle Firebase Authentication and call the Backend API to sync user data.

### Data Flow
1. User logs in via Firebase Auth (Google, Apple, etc.)
2. Client gets the `IdToken` and User Profile info.
3. Client posts the data + token to `POST /api/v1/auth/sync`.
4. Backend verifies the token using Firebase Admin SDK and upserts the user into the `users` PostgreSQL table.

---

## 2. Step-by-Step Implementation

### Step 1: Firebase Auth Setup
- **Tasks**:
  1. Initialize Firebase Auth.
  2. DO NOT INITIALIZE `firebase/firestore`.

### Step 2: Backend API Integration
- **Tasks**:
  1. Create `syncUserToBackend(user)` method.
  2. Fetch `POST /api/v1/auth/sync` with `Authorization: Bearer <token>`.
  
### Step 3: Removing Legacy Firestore Code
- **Tasks**:
  1. Ensure no `Firestore` calls exist.
  2. Ensure the build does not depend on `firebase-firestore`.
"""

for fname in glob.glob('prompt_*.txt'):
    with open(fname, 'r') as f:
        content = f.read()
    
    # 1. replace Database
    content = content.replace("Database: Firebase Firestore", "Database: PostgreSQL (via Go Backend REST API)")
    
    # 2. replace the implementation plan block
    # We match from "## 1. Architecture & Design" down to right before "## Default Guidance"
    pattern = re.compile(r"## 1\. Architecture & Design(.*?)## Default Guidance", re.DOTALL)
    content = pattern.sub(replacement + "\n## Default Guidance", content)
    
    with open(fname, 'w') as f:
        f.write(content)
    print(f"Updated {fname}")
