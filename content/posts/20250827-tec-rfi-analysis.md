---
title: "Project Brief: TEC Tahatū CV & Cover Letter Builder (Vendor Simulation)"
date: 2025-08-27
description: "A vendor-style project brief for TEC’s Tahatū CV & Cover Letter Builder, exploring learner needs, product roadmap, and architectural view."
tags: [TEC, Tahatū, CV Builder, AI, Careers]
keywords: [TEC, Tahatū, CV builder, cover letter, careers, AI, NZ]
slug: tahatu-cv-cover-letter-builder
---

*Context for new readers:*  
This document builds on [my earlier blog about vibe coding an RFI](https://www.kiwigpt.co.nz/posts/i-tried-to-vibe-code-a-govt-rfi/) where I explored whether a single “vibe coder” could respond to a government Request for Information (RFI) and even begin building the product.  
Here, I’ve reframed that exercise as a **formal project brief**, as if written by a **product vendor**. It also includes an **architectural view** to highlight what an internal team might consider.  

---

## 1. Executive Brief (Senior Executive)

**Context:** TEC seeks to add a CV and Cover Letter building capability to its [Tahatū Career Navigator](https://tahatu.govt.nz/) site.  
**Purpose:** Support learners to create tailored, professional documents integrated into the wider careers ecosystem.  

### Core Requirements (based on RFI themes)
- **Learner-focused:** Easy creation, editing, and storage of CVs and CLs.  
- **Tailoring:** Ability to customise for specific jobs, industries, or employers.  
- **Inclusion:** Meet [WCAG 2.2](https://www.w3.org/TR/WCAG22/); bilingual (English/te reo Māori); culturally aware.  
- **Integration:** Pulls from Tahatū learner profiles, career planning, and micro-credentials.  
- **AI Use:** Assist, not replace; focus on guidance, tone, and keyword match.  
- **Data Sovereignty:** Hosted in NZ; compliant with the [Privacy Act 2020](https://www.legislation.govt.nz/act/public/2020/0031/latest/LMS23223.html).  
- **Sustainability:** Affordable, scalable, with a roadmap for improvement.  

---

## 2. Product Requirements (Product Owner)

**Feature Highlights**  
1. Narrative/Upload input with LLM parsing.  
2. Master CV creation with live template previews.  
3. Tailored CV & CL generation from job ads.  
4. Editable cover letters with tone options.  
5. Template library (system + user uploaded).  
6. Application tracking with outcomes and feedback.  
7. Analytics dashboard (usage, success rates).  
8. Accessibility baked into every flow.  
9. Privacy: clear consent, no retention without approval.  

---

## 3. Roadmap (Architectural View)

### Phase 1 – MVP  
- Basic auth, profile parsing, 1–2 templates, cover letter generator, PDF export.  

### Phase 2 – Growth  
- Multiple templates, ATS optimisation, job ad tailoring, DOCX export, feedback loop.  

### Phase 3 – Advanced  
- Analytics, employer integration, multilingual support, PWA/offline.  

---

## 4. Architectural View

- **Frontend:** Next.js, React, TypeScript, Tailwind, shadcn/ui.  
- **Backend:** Vercel serverless API routes.  
- **Database:** Supabase Postgres.  
- **Storage:** Supabase Storage for files/templates.  
- **Auth:** NextAuth, SSO options.  
- **AI:** OpenAI/Azure orchestration for parsing and generation.  
- **Exports:** Playwright PDF; docx-templater.  
- **Validation:** Zod schema enforcement.  
- **Observability:** Logging and token use tracking.  

**Why this stack?** Fast to deploy, flexible, aligns with SaaS patterns, ensures sovereignty.  

---

## 5. TEC Architectural View

### MoSCoW Priorities

| Priority        | Features                                                                 |
|-----------------|--------------------------------------------------------------------------|
| **Must-Have**   | Accessibility, CV & CL creation, integration with Tahatū, NZ hosting     |
| **Should-Have** | ATS scoring, analytics, multi-template support                           |
| **Could-Have**  | Employer integrations, offline mode, advanced AI tone settings           |
| **Won’t-Have**  | Recruiter portals, job scraping (initially)                              |

### Integration Factors
- Single sign-on with Tahatū accounts.  
- APIs to share CVs securely with job boards.  
- Consider mobile-first performance and offline use.  

### AI Considerations
- Encourage uniqueness: multiple template styles, adjustable tone, and user review steps.  
- Avoid “sameness” by offering variant phrasing and style libraries.  
- Ensure ethical guardrails: clear consent, privacy-first.  

### Additional Context
- Incorporate cultural elements and co-design with Māori and Pacific stakeholders.  
- Monitor outcomes: track whether users get interviews/jobs.  
- Plan for maintainability: budget and roadmap must support continuous improvement.  

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*