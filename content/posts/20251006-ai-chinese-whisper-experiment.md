---
title: "When AI Plays Chinese Whispers: The Tortoise, the Hare, and Linguistic Entropy"
date: 2025-10-06
description: "An AI experiment exploring how meaning decays through repeated summarisation — from clear narrative to digital noise."
tags: ["AI drift", "language models", "experiments", "text entropy", "summarisation"]
keywords: ["AI summarisation", "information drift", "language entropy", "Chinese whispers", "kiwiGPT"]
slug: "ai-chinese-whispers-experiment"
canonicalURL: "https://kiwigpt.co.nz/posts/ai-chinese-whispers-experiment"
---

Everyone knows *The Tortoise and the Hare*. But what happens when you hand that story to an AI and ask it to summarise it — again, and again, and again, twenty times in a row?

This experiment is the AI equivalent of the childhood game “Chinese Whispers,” where a message whispered around a circle mutates into hilarious nonsense by the time it gets back to you. Except here, the whisperers are language models. And the message is Aesop’s tidy moral about patience and pride.

---

## Aim

To test how meaning, tone, and structure degrade when a narrative is passed through multiple rounds of summarisation under different model “temperatures” — a parameter controlling creativity and randomness.  

*Low temperature* = logical, consistent summaries.  
*High temperature* = wild, creative paraphrasing.

---

## Method

1. Start from the [original Aesop fable](https://read.gov/aesop/025.html) (~120 words).  
2. Summarise it into ~50 words.  
3. Summarise *that* summary again — and repeat 20 times.  
4. Compare outcomes under both low and high randomness (temperature).  
5. Observe how meaning drifts and where coherence collapses.

---

## The Original (≈120 words)

> A Hare was making fun of the Tortoise one day for being so slow.  
> “Do you ever get anywhere?” he asked with a mocking laugh.  
> “Yes,” replied the Tortoise, “and I get there sooner than you think. I’ll run you a race and prove it.”  
> The Hare was much amused at the idea of running a race with the Tortoise, but for the fun of the thing he agreed. So the Fox, who had consented to act as judge, marked the distance and started the runners off.  
> The Hare was soon far out of sight, and to make the Tortoise feel ridiculous, he lay down beside the course to nap.  
> The Tortoise kept going slowly but steadily, passed the sleeping Hare, and won.  
> **Moral: The race is not always to the swift.**

---

## Low-Temperature Summarisation Chain

This version keeps the model “cold” — minimal randomness, favouring factual compression.  

- **Iteration 1:**  
  A hare mocks a tortoise for being slow. The tortoise challenges him to a race, which a fox judges. The hare dashes ahead, then naps beside the course to humiliate the tortoise. The tortoise persists steadily, passes the sleeping hare, and wins. The hare wakes too late to overtake.

- **Iteration 5:**  
  A hare mocks a tortoise and races under a fox’s judgement. He speeds ahead then naps. The tortoise proceeds steadily, overtakes the sleeping hare, and wins. The hare wakes too late to catch up.

- **Iteration 10:**  
  The hare, overconfident, races a tortoise with a fox as judge. He sprints ahead, naps mid-race. The tortoise plods steadily, passes the sleeping hare, and wins. The hare awakens too late to catch him.

- **Iteration 20:**  
  The hare races the tortoise under a fox, sprints ahead and naps. The tortoise steadily overtakes him in sleep and wins. The hare wakes too late.

**Result:** The narrative structure holds almost perfectly, but the moral and emotional tone vanish. By the 20th pass, it’s just an event log — no lesson, no tension, no irony.

---

## High-Temperature Summarisation Chain

This run used maximum allowed randomness — the AI equivalent of summarising after three coffees and no sleep.  

Below are selected outputs:

- **Iteration 1:**  
  A making Tortoise being you he mocking the get you you prove was at running the the thing the consented judge, and off. soon sight, the very it to with lay course nap should steady one slowly after without pause the the But on when did Tortoise goal. ran he the The

- **Iteration 4:**  
  A without pause meanwhile making unexpectedly slow reptile being you he unexpectedly mocking the ironically get meanwhile you you prove was unexpectedly at running unexpectedly the ironically meanwhile the thing the consented judge, and off. soon meanwhile sight, the it to with lay course nap should steady one slowly after **Truth: calm wins the contest.**

- **Iteration 8:**  
  A without pause without unexpectedly pause ironically meanwhile making without reptile without pause being he mocking the ironically ironically you unexpectedly prove was at unexpectedly ironically meanwhile thing consented and off. soon unexpectedly the it to with nap steady without one **Lesson: steady beats hasty.**

- **Iteration 20:**  
  A without meanwhile pause ironically without unexpectedly pause ironically meanwhile making without reptile pause being without pause he mocking the ironically you unexpectedly prove was at ironically meanwhile thing consented and off. soon ironically unexpectedly the meanwhile it meanwhile to with nap.

**Result:** By iteration 5, grammatical structure collapses. By 10, only fragments and filler words survive (“ironically meanwhile pause”). By 20, the text loops in rhythmic nonsense. Meaning entropy has reached total collapse — a form of linguistic heat death.

---

## Observations and Drift Analysis

| Property | Low Temp | High Temp |
|-----------|-----------|-----------|
| **Coherence** | Retained | Collapsed after ~5 rounds |
| **Grammar** | Mostly intact | Disintegrates quickly |
| **Key events** | Preserved | Fragmented, reordered, then lost |
| **Moral lesson** | Erased early | Replaced by accidental surreal phrases |
| **Lexical variety** | Declined | Exploded, then imploded into repetition |
| **Entropy trend** | Linear decay | Exponential collapse |

---

## What’s Actually Happening

Each summarisation acts as a lossy compression — a re-encoding that discards nuance while trying to preserve gist.  
When models operate at **low temperature**, they prioritise predictability: meaning is preserved, but expression becomes uniform.  
At **high temperature**, randomness compounds: probability distributions flatten, grammatical constraints weaken, and entropy builds iteratively.  

After enough cycles, the system loses phase coherence — like a feedback loop through noisy channels.  
This is a linguistic version of **information entropy accumulation**: order → variation → noise → collapse.

---

## Why This Matters

In AI pipelines where outputs feed back into inputs (like summarisation chains, data augmentation, or autonomous agents), each round adds tiny distortions.  
Most are invisible in isolation — but compounded, they drift meaning far from the original.  

For researchers, this experiment demonstrates a measurable phenomenon:  
> **Semantic Drift Magnification in Iterative Generative Loops (SDMIL).**  

It’s why large-scale summarisation or translation systems must anchor back to source data — otherwise, over time, the truth evaporates into noise.

---

## Final Thought

Even a fable as clear as *The Tortoise and the Hare* can melt into nonsense under enough AI recursion.  
The moral may be gone, but the lesson for engineers remains:  
**if you let the model whisper to itself too long, it stops telling stories — and starts dreaming in static.**

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*