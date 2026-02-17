# Implementation Plan: User Authentication & Sync

> **Refers to**: [Spec Link](./spec.md)
> **Status**: Draft

## 1. Architecture & Design
This plan outlines the implementation of a user authentication and data synchronization system using **Supabase** as the Backend-as-a-Service (BaaS) platform. This choice significantly simplifies the backend work by providing built-in support for OAuth (Google, Apple), Magic Link authentication, and a PostgreSQL database, directly addressing the core requirements of the specification.

The client-side application will interact with Supabase via the `@supabase/supabase-js` library. A new set of services and UI components will be created to manage authentication state, handle data synchronization, and present the user interface for login and profile management.

### Component View

-   **Modified Components**:
    -   `ProgressTracker`: The existing component/service that manages user progress will be modified to interact with the new `ProgressSyncService`. Instead of writing only to `LocalStorage`, it will check the user's auth state. If authenticated, it will push updates to the backend via the service.

-   **New Components**:
    -   **Backend (Supabase Project)**:
        -   Authentication: Configuration for Google, Apple, and Email (Magic Link) providers.
        -   Database: PostgreSQL instance with `users` and `user_progress` tables, secured by Row Level Security (RLS) policies.
    -   **Frontend (Client Application)**:
        -   `services/auth.service.ts`: A service to encapsulate all Supabase authentication logic (login, logout, session management).
        -   `services/progress.service.ts`: A service to handle CRUD operations for user progress, abstracting whether the data source is `LocalStorage` or the Supabase backend.
        -   `store/user.store.ts`: A global state management store (e.g., using Zustand or Pinia) to hold the current user's session, profile, and authentication status (Guest vs. Authenticated).
        -   `pages/login.vue` (or `.tsx`): A new page for login/sign-up, containing the UI for the three authentication methods.
        -   `pages/profile.vue` (or `.tsx`): A new page to display user information and the logout button.
        -   `components/SignUpPrompt.vue` (or `.tsx`): A non-intrusive component to encourage guest users to sign up.

-   **Dependencies**:
    -   `@supabase/supabase-js`: The official JavaScript client library for Supabase.

### Data Model Changes
The following tables will be created in the Supabase PostgreSQL database.

```sql
-- users table to store authentication information
CREATE TABLE public.users (
    id uuid NOT NULL REFERENCES auth.users ON DELETE CASCADE,
    email text UNIQUE,
    name text,
    avatar_url text,
    provider text,
    created_at timestamptz DEFAULT now() NOT NULL,
    PRIMARY KEY (id)
);

-- user_progress table to store user-specific progress data
CREATE TABLE public.user_progress (
    user_id uuid NOT NULL REFERENCES public.users ON DELETE CASCADE,
    points integer DEFAULT 0 NOT NULL,
    progress_data jsonb,
    updated_at timestamptz DEFAULT now() NOT NULL,
    PRIMARY KEY (user_id)
);

-- Function to automatically copy new users from auth.users to public.users
create function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.users (id, email, name, avatar_url, provider)
  values (
    new.id,
    new.email,
    new.raw_user_meta_data->>'full_name',
    new.raw_user_meta_data->>'avatar_url',
    new.raw_app_meta_data->>'provider'
  );
  return new;
end;
$$;

-- Trigger to execute the function on new user creation
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```

The `LocalStorage` will continue to use the `userProgress` key for guest users and as a cache for authenticated users.
```json
// Structure for `localStorage.getItem('userProgress')`
{
  "points": 70,
  "progress_data": {
    "lastSession": "2023-10-26"
    /* ... other progress details */
  }
}
```

---

## 2. Step-by-Step Implementation

### Step 1: Backend Setup & Configuration
-   **Description**: Initialize the Supabase project, create the database schema, and configure authentication providers. This step is the foundation for all subsequent work.
-   **Tasks**:
    1.  Create a new project on [supabase.com](https://supabase.com).
    2.  Use the SQL Editor to run the scripts defined in the **Data Model Changes** section to create the `users` and `user_progress` tables, along with the trigger function.
    3.  Navigate to `Authentication -> Providers` and enable Google, Apple, and Email.
        -   For Google/Apple, follow the Supabase documentation to create OAuth credentials and add them to the dashboard.
        -   For Email, enable the "Magic Link" option. Customize the email template to match the app's branding.
    4.  Navigate to `Authentication -> Policies`. Create Row Level Security (RLS) policies for the `user_progress` table to ensure users can only access their own data.
        -   **SELECT Policy**: `auth.uid() = user_id`
        -   **INSERT/UPDATE/DELETE Policies**: `auth.uid() = user_id`
-   **Files**: N/A (Configuration in Supabase Dashboard).
-   **Verification**:
    -   The `users` and `user_progress` tables exist in the database schema.
    -   The RLS policies are active on the `user_progress` table.
    -   Google, Apple, and Email providers are marked as "Enabled" in the Supabase dashboard.

### Step 2: Frontend - Authentication Service & State Management
-   **Description**: Integrate the Supabase client library and create the core services for managing authentication state throughout the application.
-   **Tasks**:
    1.  Install the Supabase client library: `npm install @supabase/supabase-js`.
    2.  Create a Supabase client instance. Store Supabase URL and Anon Key in environment variables (`.env`).
        -   **File**: `lib/supabaseClient.ts`
    3.  Create the authentication service to wrap Supabase methods.
        -   **File**: `services/auth.service.ts`
        -   **Methods**: `signInWithGoogle()`, `signInWithApple()`, `signInWithMagicLink(email)`, `signOut()`, `getSession()`, `onAuthStateChange(callback)`.
    4.  Set up a global user store to manage the application's current user state.
        -   **File**: `store/user.store.ts`
        -   **State**: `user`, `session`, `status` ('guest', 'authenticated', 'loading').
        -   The store should subscribe to `auth.service.onAuthStateChange` to automatically update its state when the user logs in or out.
-   **Verification**:
    -   The application successfully initializes the Supabase client.
    -   The user store correctly reflects the 'guest' state on initial load.
    -   Calling `auth.service` methods triggers the corresponding Supabase functions (verified via network tab and Supabase logs).

### Step 3: UI - Login, Profile Pages & Routing
-   **Description**: Build the user-facing pages for authentication and profile management.
-   **Tasks**:
    1.  Create the Login/Sign-up page.
        -   **File**: `pages/login.vue`
        -   Implement three UI elements: "Login with Google" button, "Login with Apple" button, and an email input field with a "Send Magic Link" button.
        -   Style the page with Ivory and Sage Green colors as per the "The Warm Sanctuary" theme.
        -   Connect the UI elements to the corresponding methods in `auth.service.ts`.
    2.  Create the Profile page.
        -   **File**: `pages/profile.vue`
        -   Display the user's name or email from the `user.store`.
        -   Add a "Log out" button that calls `auth.service.signOut()`.
        -   On successful logout, the user should be redirected to the home page, and the `user.store` should revert to the 'guest' state.
    3.  Protect the Profile page route so it's only accessible to authenticated users. Unauthenticated users trying to access it should be redirected to the login page.
-   **Verification**:
    -   The `/login` page renders correctly with all three auth options.
    -   Clicking the login buttons initiates the OAuth/Magic Link flow.
    -   After successful login, the user is redirected away from the login page.
    -   The `/profile` page displays the correct user email/name.
    -   Clicking "Log out" clears the session, updates the state to 'guest', and redirects the user.
    -   A guest user cannot access `/profile`.

### Step 4: Data Synchronization Logic
-   **Description**: Implement the core logic for syncing user progress between `LocalStorage` and the Supabase database.
-   **Tasks**:
    1.  Create the progress synchronization service.
        -   **File**: `services/progress.service.ts`
        -   **Methods**: `getProgress()`, `updateProgress(newData)`.
    2.  Implement the `getProgress()` method. It should check the `user.store`:
        -   If authenticated, fetch data from the `user_progress` table in Supabase. On success, cache the result in `LocalStorage` and return the data.
        -   If guest, read data directly from `LocalStorage`.
    3.  Implement the `updateProgress()` method. It should check the `user.store`:
        -   If authenticated, send the update to the `user_progress` table *and* update the `LocalStorage` cache.
        -   If guest, write the update only to `LocalStorage`.
    4.  Implement the **Initial Data Migration** logic (R-SYNC-01).
        -   In the `user.store`'s `onAuthStateChange` handler, when a user transitions from 'guest' to 'authenticated' for the first time:
            a. Check for existing progress data in `LocalStorage`.
            b. If data exists, make a one-time call to `progress.service` to insert this data into the user's `user_progress` record in the database.
-   **Verification**:
    -   **Scenario 1**: A guest user with 70 points in `LocalStorage` logs in for the first time. Verify that a new record with 70 points is created in the `user_progress` table.
    -   **Scenario 2**: An authenticated user logs in on a new device (empty `LocalStorage`). Verify that their progress is fetched from Supabase and populated in the UI and `LocalStorage`.
    -   An authenticated user's progress updates are reflected in the Supabase database in real-time.
    -   A guest user's progress updates are only saved to `LocalStorage`.

### Step 5: UI - Sign-up Prompt
-   **Description**: Implement the non-intrusive prompt to encourage guest users to sign up.
-   **Tasks**:
    1.  Create the UI component for the prompt.
        -   **File**: `components/SignUpPrompt.vue`
        -   Design a small, dismissible banner or modal with a message like "Save your progress to the cloud! Sign up for free." and a link/button to the `/login` page.
    2.  Modify the `ProgressTracker` component or wherever progress points are updated.
        -   Add a condition: `if (user.status === 'guest' && newPoints >= 50 && oldPoints < 50)`.
        -   If the condition is met, trigger an event or update a state variable to show the `SignUpPrompt` component.
-   **Verification**:
    -   The prompt does not appear for guest users with less than 50 points.
    -   The prompt appears exactly once when a guest user's score crosses the 50-point threshold.
    -   The prompt does not appear for authenticated users, regardless of their score.
    -   Clicking the prompt's call-to-action navigates the user to the `/login` page.

---

## 3. Verification Plan
*How will we verify success?*

### Automated Tests
-   [ ] **Unit Tests**:
    -   `services/auth.service.test.ts`: Mock the Supabase client and test that the service methods call the correct client functions.
    -   `services/progress.service.test.ts`: Mock the Supabase client and user store. Test that `getProgress` and `updateProgress` correctly delegate to either Supabase or `LocalStorage` based on auth state.
    -   `store/user.store.test.ts`: Test state transitions (guest -> authenticated, authenticated -> guest).
-   [ ] **Component Tests**:
    -   `pages/login.test.vue`: Test that the page renders and that buttons trigger the correct `auth.service` methods when clicked.
    -   `components/SignUpPrompt.test.vue`: Test that the component renders correctly based on props and emits events on user interaction.

### Manual Verification
-   [ ] **Guest Flow**:
    -   [ ] As a new user, start the app. Verify progress is saved to `LocalStorage`.
    -   [ ] Close and reopen the tab. Verify progress is restored from `LocalStorage`.
-   [ ] **Sign-up & Migration (Scenario 1)**:
    -   [ ] As a guest, accumulate more than 50 points. Verify the sign-up prompt appears.
    -   [ ] Click the prompt and sign up using Google.
    -   [ ] Verify the user is now logged in.
    -   [ ] Verify the progress points are retained.
    -   [ ] Check the Supabase `user_progress` table to confirm the points were migrated correctly.
-   [ ] **Authenticated Flow (Scenario 2)**:
    -   [ ] Log out.
    -   [ ] Open the app in an incognito window or a different browser (simulating a new device).
    -   [ ] Log in using the same account (e.g., via Magic Link).
    -   [ ] Verify the correct progress is fetched from the cloud and displayed.
    -   [ ] Make some new progress. Verify it's saved.
    -   [ ] Refresh the page on the *original* browser. Verify the new progress is synced and displayed.
-   [ ] **Authentication Methods**:
    -   [ ] Successfully log in and out using Google.
    -   [ ] Successfully log in and out using Apple.
    -   [ ] Successfully log in and out using Magic Link.
-   [ ] **UI/UX**:
    -   [ ] All new UI components (`Login`, `Profile`, `Prompt`) conform to the "The Warm Sanctuary" design theme.
    -   [ ] The logout button correctly clears the user session and `LocalStorage` to prevent data conflicts for the next guest user.