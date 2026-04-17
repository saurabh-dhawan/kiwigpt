---
title: "Data Readiness Checklist: 15 Questions to Ask Before Your Next AI Initiative"
date: 2026-04-17
slug: "data-readiness-checklist"
description: "A practical checklist for assessing whether your data is ready for AI. Five categories, fifteen questions, drawn from real AI trials inside a NZ government agency."
tags:
  - AI
  - Data
  - Architecture
  - New Zealand
  - Government
draft: false
---

> उलझे नहीं तो कैसे सुलझोगे, बिगड़े नहीं तो कैसे संभलोगे
>
> *If you never get tangled, how will you learn to untangle? If things never go wrong, how will you learn to set them right?*

I was part of three AI trials inside a New Zealand government agency. All three gave us invaluable lessons. Out of those three, one progressed quite a lot, through four stages of development, and has shown genuine promise.

The lesson across all three was the same: it wasn't the model that determined progress. It wasn't the cloud platform. It was the data underneath.

In one trial, the AI could automate quality checks on cadastral survey datasets. In another, it could verify memorandums on land title. The models performed well. But without data pipelines to connect them to source systems at scale, no data lake, no lakehouse, no integration path, there was only so far the trials could go.

The trial that progressed furthest worked with a different data shape entirely. Public consultation submissions arrive as standalone documents. You upload them. The AI ingests, classifies, and synthesises. No operational pipeline into a live system required.

That experience crystallised something I should have understood earlier: **you can't bolt AI onto a system that doesn't have accessible, well-structured data.** And you definitely shouldn't wait until the trial is underway to find out.

This checklist is what I wish I'd had before I started.

---

## How to use this

Sit down with your data team before your next AI initiative. Work through these fifteen questions across five categories. You don't need perfect answers. You need honest ones.

If you can answer more than half confidently, you're probably ready to proceed, with eyes open.

If you can't, that's not a failure. That's a signal to invest in data foundations first.

---

## 1. Data Accessibility

Your AI needs data. Can it get to it?

**Is your data in one place, or scattered across multiple systems?**
Fragmentation is the silent killer of AI trials. If the data you need lives in three different platforms with no integration layer, your AI project is really a data integration project wearing an AI costume.

**Can you access it programmatically (APIs, exports), or is it locked behind a UI?**
AI systems need machine-readable access. If the only way to get data out of your system is to log in and click export, you have a manual bottleneck that will throttle any automation.

**Do you have data pipelines, or are you relying on manual extracts?**
Pipelines move data from source systems to where AI can consume it. Reliably, repeatedly, at scale. Without them, every data refresh is a human task. That doesn't scale, and it introduces errors.

---

## 2. Data Quality

The AI will learn from your data. Is your data worth learning from?

**Have you profiled the data? Do you know what's missing, duplicated, or inconsistent?**
Data profiling isn't glamorous. It's also non-negotiable. If you don't know the shape of your data (nulls, duplicates, format inconsistencies) you can't assess whether AI outputs are trustworthy.

**Is there a 'good enough' quality bar defined for your AI use case?**
Perfection is expensive. But "good enough" needs to be explicit, not assumed. Define what quality means for your specific use case. A classification model tolerates different imperfections than a decision-support tool.

**Who owns data quality, and do they know about your AI plans?**
Data quality is someone's job. If that person doesn't know you're planning to feed their data into an AI model, you'll discover problems late and fix them slowly.

---

## 3. Data Governance

Who controls the data, and under what rules?

**Is there a data catalogue or metadata layer?**
A catalogue tells you what data exists, where it lives, what it means, and who owns it. Without one, your AI team will spend more time finding data than using it.

**Do you know who can access what, and under what conditions?**
AI doesn't exempt you from access controls. If anything, it intensifies the question. Who should the model see? What data is it allowed to use for training? For inference? For reporting?

**Are there privacy, sovereignty, or classification constraints?**
In New Zealand government, this is especially pointed. Data sovereignty, the Privacy Act, and information classification all constrain what you can feed into AI systems and where those systems can run. Know the boundaries before you build.

---

## 4. Organisational Readiness

AI trials don't fail in isolation. They fail inside organisations.

**Do the teams who own the data know about your AI initiative?**
Often, the teams who maintain the source systems are late entrants, possibly the last to hear about the AI trial. By the time they're involved, the AI project team is already failing on their first milestone. Getting data owners in the room early changes everything.

**Are there competing priorities that could block integration work?**
Your AI trial might need a small change to an API, a new data export, or access to a staging environment. If the team that owns that system is deep in a platform migration, your "small change" will sit in the backlog for months. Knowing this upfront lets you plan around it instead of being blindsided.

**Is there executive sponsorship for the data work, not just the AI work?**
Everyone wants to sponsor the shiny AI demo. Fewer people want to sponsor the data pipeline that makes it possible. If your executive sponsor thinks the job is done when the model works in a sandbox, you have a sponsorship gap that will stall the path to production.

---

## 5. Scale and Sustainability

A trial that works once is an experiment. A trial that works at scale is a service.

**Are you solving a problem that matters at scale, or a niche task?**
Some use cases are too narrow to justify the integration effort, even when the AI works. Make sure the problem you're solving is big enough to sustain the data work required to support it.

**Who will maintain the AI solution after the trial ends?**
Trials have end dates. Production systems don't. If nobody has been identified to maintain prompts, monitor quality, manage costs, and retrain models, your trial will quietly decay after the project team moves on.

**Could this be reusable, across teams, agencies, or domains?**
One of the trials I was involved in is now in active discussion as a potential all-of-government service. Every NZ government agency processes public submissions. Building it once, properly, is better than building it thirty times. Ask yourself: is your use case bigger than your team?

---

## The punchline

If you can't answer these fifteen questions confidently, your AI trial will struggle. Regardless of the model. Regardless of the platform.

Data foundations first. Then AI.

---

## What's next

I'll be writing a deeper piece on what "data foundations" actually means: medallion architecture, operational pipelines, streaming, feature stores, and the tools that make this real (Databricks, Microsoft Fabric, Azure Purview). If you found this checklist useful, that one will go further.

I'm also speaking at [Global Azure Bootcamp 2026 in Wellington](https://pearlinnovations.co.nz/global-azure-bootcamp-2026-wellington/) on 18 April, where I'll uncover why having solid data foundations is key to successful AI projects, including a live demo and architecture of the [Document Knowledge Mining Solution Accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator), the open-source accelerator from Microsoft.

If you've run an AI trial that hit a data wall, or one that sailed through, I'd love to hear your story. [Connect with me on LinkedIn](https://www.linkedin.com/in/saurabhdhawan/) or [get in touch](/contact/).

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz). Generated, Published and Tinkered with AI by a Kiwi.*
