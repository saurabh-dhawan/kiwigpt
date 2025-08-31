---
title: "Why AI Forgets: The Context Window Explained"
date: 2024-11-14
draft: false
description: "Why AI models forget: the truth about context windows, token limits, and how to work with them."
tags: ["LLMs", "context window", "AI memory", "prompt engineering", "ChatGPT"]
keywords: ["LLM context window", "AI memory limits", "token limit in ChatGPT", "nz"]
slug: "why-ai-forgets-context-window-explained"
 
ShowReadingTime: true
canonicalURL: ""
aliases: []
---

You tell ChatGPT something in the morning and by afternoon it’s forgotten.  
Is it lying, lazy, or limited? Spoiler: it’s limited — by design.

## The Goldfish Problem

LLMs (large language models) aren’t “forgetful” in the human sense.  
They simply work with a limited sliding window of awareness.  
Once you’ve gone beyond it, earlier content disappears like the view in your rear-view mirror.

In Kiwi terms, it’s like watching a rugby match but only remembering the last few plays, not the whole season.

## What LLMs Actually ‘Remember’

Despite appearances, most LLMs have no permanent memory.  
They can only work with the text you’ve provided in the current conversation — plus their training data.

- **Training data** is what they learned before you met them.  
- **Conversation context** is their short-term “working memory”.

There’s no secret archive of your chats unless you’ve explicitly enabled long-term memory features.

## Context Windows Explained

A **context window** is the maximum amount of information the model can “see” at once.  
It’s measured in **tokens**, not words or characters.

Think of reading through a letterbox: you can’t see the whole page — just a slice.

Typical context windows:  
- Older models: 4,096 tokens (~3,000 words)  
- Newer models: 8k, 16k, 128k tokens and beyond

When you hit the limit, the oldest parts get chopped off.

For example:

> “Today is sunny.” + 100,000 other tokens → *bye-bye sunshine* once the window fills.

## Tokens: The Currency of AI Memory

Tokens are fragments of words.  
“KiwiGPT is awesome” becomes roughly `["Ki", "wi", "GPT", " is", " awesome"]`.

The context window counts **every token**:
- Your messages
- The model’s replies
- Any hidden system instructions

Long prompts + long replies = faster memory drain.

## When Context Runs Out

Once you hit the token cap, the earliest tokens are dropped.  
This is why a chatbot can “forget” what you told it earlier.

Picture it like a moving window sliding along a script — as the conversation advances, the start falls away.

**Risks of context loss:**
- Losing critical details mid-project
- Breaking multi-step reasoning chains
- Dropping agreed constraints

## How to Work with AI’s Memory Limits

You can work *with* the goldfish brain rather than against it:

- **Front-load** key details early in prompts
- Keep your language **concise**
- Periodically **re-summarise** what matters
- For long documents, use **retrieval-augmented generation** (RAG) so the model can fetch relevant pieces on demand

## Why This Matters for the Future

Yes, bigger context windows are coming — Anthropic’s Claude can handle million tokens, and OpenAI has models in the same range.  
But there are trade-offs:
- Higher compute cost
- Slower responses
- More potential for irrelevant details to sneak in

The future likely blends **big context** with **persistent memory** — so your AI can remember both the play-by-play and the season highlights.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*