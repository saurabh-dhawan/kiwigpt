---
title: "I tried to “vibe code” a government RFI. Here’s what I learned."
date: 2025-08-17
description: "A solo experiment: vibe coding an NZ government RFI into a CV & cover letter builder with AI—what worked, what didn’t, and how long it really takes."
tags: ["vibe coding", "RFI", "AI engineering", "NZ government", "CV builder", "indie dev"]
keywords:
  - primary: "vibe coding government RFI"
  - secondary: ["AI prototypes", "CV builder", "New Zealand tech", "indie dev"]
slug: "i-tried-to-vibe-code-a-govt-rfi"
---

**Why I did this:** to test how far a single person can go from **RFI → product** using vibe coding + AI helpers.

## Edit — 27 Aug 2025
I’ve also expanded this experiment into a more formal vendor-style brief. You can read that follow-up here: [Project Brief: TEC Tahatū CV & Cover Letter Builder (Vendor Simulation)](https://www.kiwigpt.co.nz/posts/tahatu-cv-cover-letter-builder/)

---

## TL;DR
- RFIs can **look** simple. The work is **not**.
- Vibe coding gets you **~80%** (exploration, scaffolding, first drafts).  
- The final **20%** (debugging, infra, security, accessibility, export fidelity, compliance) still takes **months**, not weeks — but it’s **months**, not the year+ you might expect.
- Tooling friction is real: **Copilot vs ChatGPT context split** slowed me down.
- Would I build a production system solo? **Yes** — if the product has a **broad market**, not a single-customer (govt-only) dependency.

---

## A quick note on PM & architecture roles
While I wore the hats of product manager and architect here, I want to acknowledge these are **deep, strategic professions**. They can make or break products. My sketches came quickly because I’ve spent time around these functions, but it’s not trivial. **Respect to those crafts**.

---

## Why this exercise
I spotted an RFI from NZ’s Tertiary Education Commission (TEC) about a **CV & cover letter builder** for their Tahatū careers site and thought: *that looks straightforward*.  

Here are the tender details for context:

- **RFx ID:** [32236908](https://www.gets.govt.nz/TEC/ExternalTenderDetails.htm?id=32236908)  
- **Title:** CV and Covering Letter Builder  
- **Tender Type:** Request for Information (market research)  
- **Purchaser:** Tertiary Education Commission  
- **Closing Date:** 29/08/2025  

I wanted to stress-test vibe coding on this real brief:  
- **A few hours** thinking,  
- **A few hours** exploring features/roadmap,  
- **A few more** vibe-coding a small feature.  

The goal wasn’t to finish a full app — it was to see what a single person could realistically do **quickly**.  

> If you’re curious about tenders like this, NZ procurement is centralised at [GETS (Government Electronic Tenders Service)](https://www.gets.govt.nz) where you can browse or subscribe.

---

## My process (step-by-step)
1. **Skim the RFI → translate to product goals.**  
   Outcomes first, not features: what must a learner do in <5 minutes?
2. **List features → slice a roadmap.**  
   Minimal MVP, then stack value (parsing, tailoring, ATS, analytics).
3. **Architecture sketch.**  
   Next.js + Vercel, Supabase Postgres/Storage, NextAuth, Prisma, LLM via OpenAI/Azure, Playwright PDF, docx-templater.
4. **Vibe code a vertical slice.**  
   Paste profile text → LLM → structured JSON → preview → PDF.
5. **Reality check.**  
   Accessibility, exports, data governance, i18n, and integration always take longer than you think.

---

## My background & reliance on AI
I’m not a full-time developer. This was an experiment. I relied heavily on ChatGPT and Copilot.  
Some choices were **new territory** (Prisma ORM, Playwright for PDFs, docx-templater) and I trusted AI suggestions.  
But the big calls (Vercel vs AWS, Postgres, Supabase) I knew enough to choose.  

> **Lesson:** know your foundations. For production, research each component. Lean on AI for secondary tools, but validate core architecture.

**Lifestyle context:** I also split my work between **mobile and desktop**. ChatGPT is my brainstorming buddy on the train and in spare moments (mobile app), while VS Code + Copilot is my coding setup on the laptop. This causes some friction because context doesn’t carry smoothly between the two, but it’s how I fit the work into my life and make use of idle time.

---

## Feature set I landed on
- **Auth** (email or OAuth)  
- **Profile**: paste natural language or upload CV → parse → structured JSON  
- **Master CV**: pick template, live preview, edit, export **PDF/DOCX**  
- **Cover letter**: generate from job ad + profile, editable  
- **Applications**: save tailored CV/CL per job, track outcomes + feedback  
- **ATS check**: keyword coverage + suggestions  
- **Analytics**: funnel + template popularity  
- **Accessibility & inclusion**: WCAG 2.2 AA, plain language, te reo Māori + English, co-design input

---

## The roadmap that felt honest
- **Start:** thin MVP — auth, profile paste, one CV template, PDF export.  
- **Next:** upload parsing, multiple templates, cover letter basics.  
- **Then:** job ad tailoring, DOCX export, tracker.  
- **After:** ATS scoring, analytics, low-bandwidth support.  
- **Finally:** employer integrations, template uploads.

Even with vibe coding, shipping **polished** features that meet **gov-grade** accessibility, privacy, and export fidelity needs **months**, not weeks. Still better than a year.

---

## What surprised me
- **PM hat felt easy** with AI: you can draft features + architecture in an afternoon.  
- **Engineering is still the grind:** edge cases, auth, exports, accessibility.  
- **Debug/deploy tax:** CI/CD, secrets, PDF quirks turn days into weeks.

---

## Key tools & friction
- **VS Code + GitHub Copilot** for scaffolding. Smooth.  
- **ChatGPT premium** for brainstorming.  
  👉 Pain point: context doesn’t flow between Copilot and ChatGPT.

**Tip:** Keep a `requirements.md` in-repo. Feed Copilot, not tabs.

---

## What I’d do differently
- **Unify context in-repo.** Keep requirements, architecture, prompts next to code.  
- **Print-first design.** Build the print route early; test PDF often.  
- **Accessibility baked in.** Start with WCAG checks.  
- **Plan DOCX earlier.** Know placeholders and loops up front.  
- **Think bandwidth.** PWA or lightweight exports matter.

---

## Would I ship a production system solo?
Yes, but with caveats:  
- Choose a **broad market** product, not just one govt buyer.  
- Be full-stack curious (frontend, backend, auth, exports, privacy).  
- Budget **months**, not weeks.  

**Advice:**  
- Translate RFIs to outcomes first.  
- Ship vertical slices.  
- Validate schemas early.  
- Design for print + a11y first.  
- Treat AI as advisor.  
- Show you understand governance.  

---

**Covering tenders yourself?** Start with [GETS](https://www.gets.govt.nz) and subscribe. It’s free and gives you visibility.  

---

## Closing
Vibe coding is powerful. It gets you far, fast. But the last mile needs **craft, discipline, and respect for the work**. AI can help you sprint — but it won’t carry you over the finish line.  

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*