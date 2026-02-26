# Architecture Decision Record (ADR): Backend Infrastructure for MVP

**Date:** 2026-02-26
**Status:** Accepted

## Context
We need to determine the most cost-effective and maintainable infrastructure for the Go Backend during the MVP phase. The alternatives discussed were Firebase (direct client access), Vercel Serverless Functions, Google Cloud Run, and container PaaS providers like Render/Railway.

## Options Considered

### 1. Google Cloud Run 🌩️
- **Pros:** Highly scalable, zero maintenance, first-class Google ecosystem integration.
- **Cons:** Requires credit card linking which brings the risk of bill shocks if not capped correctly. Overkill for MVP scale.

### 2. Vercel Serverless Functions (API Routes) ⚡
- **Pros:** Zero-setup, free tier, co-located with the frontend Next.js app.
- **Cons:** Requires rewriting the backend logic from Go to TypeScript. Prone to cold starts. Not suitable for long-running processes or background jobs.

### 3. Firebase / Firestore Direct Access 🔥
- **Pros:** Real-time sync, zero deployment, offline support out-of-the-box.
- **Cons:** Business logic must be duplicated across Web, iOS, and Android clients. Security rules become complex as requirements grow.

### 4. Render.com (Go Environment) 🚀
- **Pros:** Native Go support, no initial credit card required for free tier, fixed predictable costs as traffic grows. Keeps the Go backend intact as a single source of truth without cold starts.
- **Cons:** Free instances may spin down on inactivity (if purely free tier), though less aggressively than serverless cold starts. Limited resources per container.

## Decision
We decided to proceed with **Option 4 (Render.com)** the central Go backend for all clients (API-Centric Strategy).
- **Reason:** It provides a unified backend (write once in Go for Web/iOS/Android), eliminates the need to expose Firestore directly to clients, avoids credit card requirements during MVP, and utilizes the existing Go codebase perfectly. This avoids the technical debt of rewriting logic in TS for Vercel or dealing with Cloud Run billing concerns prematurely.

## Consequences
- Web, iOS, and Android clients will no longer read/write to Firestore directly. They will fetch and update data exclusively via REST APIs pointing to the Go Backend.
- Firebase Auth remains the authentication provider, issuing tokens that the Go backend verifies.
