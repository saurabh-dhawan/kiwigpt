---
title: "How I Got Prompt Engineering Wrong"
date: 2026-05-15
draft: false
description: "Why simple prompts sometimes outperform complex ones, and how chat apps, APIs, and local LLMs all respond differently."
tags:
  - AI
  - Prompt Engineering
  - LLMs
  - Azure AI Foundry
  - Claude
  - Local LLMs
keywords:
  - prompt engineering
  - AI prompting
  - Claude prompts
  - ChatGPT prompting
  - Azure AI Foundry
  - local LLMs
  - NZ AI blog
slug: how-i-got-prompt-engineering-wrong
images:
  - /images/how-i-got-prompt-engineering-wrong.png
---

# How I Got Prompt Engineering Wrong

At my work, one of my colleagues (whose age shall not be discussed publicly, though we regularly joke he may have been around during the Jurassic age) has unexpectedly become one of the most effective Claude users I know.

While I was building carefully engineered prompts full of instructions, formatting rules, context, edge cases, and constraints, he would casually type things like:

> “Give me everything about topic X.”

Annoyingly, his outputs were often better than mine.

Not just simpler. Better.

At first, I assumed he had simply stumbled onto good luck. But then I started noticing the same pattern elsewhere.

Around the same time, I was working with Azure AI Foundry APIs through Python scripts and document mining workflows. Those systems behaved very differently from Claude or ChatGPT conversations. Prompts that worked beautifully in chat interfaces suddenly became unreliable, vague, or inconsistent in API workflows.

Then local LLMs felt different again.

That sent me down a rabbit hole.

Maybe prompt engineering was not working the way I thought it was.

## I Thought More Instructions Meant Better Results

Like many people, I started with the assumption that prompts worked a bit like database queries or Google searches.

More detail in → better answer out.

So naturally, I kept adding more:
- context
- formatting requirements
- examples
- role definitions
- constraints
- instructions about tone
- instructions about structure
- instructions about what *not* to do

Sometimes this absolutely helped.

But other times, the outputs became strangely rigid.

The AI would focus heavily on following instructions while somehow missing the bigger point.

Meanwhile, my Jurassic-era colleague H would ask broad conversational questions and often get richer, more useful answers.

That was frustrating.

## The Coffee Conversation That Changed My Thinking

At one point, my supervisor E mentioned something interesting.

Despite all the “prompt engineering best practices” from training sessions, he found simple Q&A-style prompting worked best for him most of the time.

That led to one of those long coffee conversations where people start waving hands around trying to explain invisible concepts.

We started talking about whether prompts might work less like commands and more like steering.

The more I thought about it, the more it made sense.

Every prompt pushes the AI in certain directions while quietly pulling it away from others.

A very detailed prompt does not just add guidance.

It can also accidentally narrow the AI too early.

## Why Simple Prompts Sometimes Work Better

This was the part I initially got wrong.

I assumed a broad prompt was “lazy prompting”.

Now I think broad prompts can sometimes work better because they give the AI room to explore before narrowing down.

For example:

> “Tell me everything about enterprise AI adoption risks.”

allows the AI to explore:
- governance
- security
- culture
- cost
- architecture
- regulation
- integration problems
- change management

But a heavily constrained prompt might unintentionally force the AI into one narrow lane too early.

Sometimes that precision is exactly what you want.

Sometimes it makes the answer worse.

I started realizing that prompting is not just about adding more instructions.

Sometimes giving the AI too much direction too early actually made the output worse.

## Chat Apps Are Doing More Than We Think

Another thing I misunderstood was this:

ChatGPT and Claude are not just “raw AI models”.

They are heavily engineered products built around AI models.

When we type a simple prompt into Claude or ChatGPT, a lot is happening behind the scenes:
- conversation management
- hidden system prompts
- safety layers
- memory handling
- formatting guidance
- intent interpretation
- response shaping

In many ways, these systems quietly compensate for vague prompting.

That is probably why H’s simple prompts worked so well in Claude.

The platform itself was helping shape the interaction.

## Why APIs Feel Different

My Azure AI Foundry workflows helped expose this difference very quickly.

In API-based workflows, the AI felt less forgiving.

Loose prompts that worked beautifully in chat interfaces often produced:
- inconsistent outputs
- formatting drift
- incomplete extraction
- unpredictable structure

That makes sense in hindsight.

When using APIs, *you* are responsible for much more:
- orchestration
- context management
- retrieval
- conversation state
- formatting consistency
- workflow design

The chat application is no longer quietly fixing things for you.

You are much closer to the underlying model behaviour.

That is why API prompting often needs to be sharper and more deliberate.

## Local LLMs Felt Different Again

Then came local LLMs.

This was probably the most revealing experience.

Local models often felt:
- more literal
- less polished
- more fragile
- more prompt-sensitive

A vague prompt could drift badly.

A strong prompt could improve things dramatically.

You start noticing how much the chat apps normally stabilise the experience for you.

It also becomes obvious that there is no single “best” prompting style.

Different environments reward different approaches.

## So What Actually Works?

The biggest thing I learned is that prompting style depends heavily on what kind of interaction you are having.

### Broad prompts work well when:
- exploring ideas
- brainstorming
- learning new topics
- starting conversations
- discovering angles you had not considered
- using polished chat interfaces like Claude or ChatGPT

### Sharper prompts matter more when:
- using APIs
- building workflows
- extracting structured data
- automating tasks
- using local LLMs
- requiring consistency and repeatability

The mistake is assuming one style works everywhere.

## Why This Matters

A lot of AI advice online still treats prompting like there is a universal formula.

There is not.

The environment matters. The tooling matters. The model wrapper matters. Sometimes the difference between a brilliant answer and a terrible one is not the model itself, but the layer sitting around it.

That changed how I approach AI systems completely.

I no longer try to over-engineer every prompt from the start.

Now I usually begin broad, explore the space, and only tighten constraints once I understand what kind of output I actually want.

Oddly enough, the Jurassic-era prompting strategy turned out to be more sophisticated than I first realised.

## My Takeaway

I no longer think prompt engineering is about finding magical wording tricks.

And I definitely no longer think “more instructions” automatically means “better prompts”.

Instead, I think the real skill is understanding:
- how much direction to give the AI,
- when to start broad,
- when to narrow things down,
- and what kind of AI environment you are working with.

Sometimes the AI needs guidance.

Sometimes it needs room to think.

And sometimes the difference is not the model at all, it is the layer wrapped around the model.

That was the rabbit hole I did not expect to fall into.

But I am glad I did.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*