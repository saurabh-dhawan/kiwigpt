---
title: "Jev vs LLMs: Where TypeSafe's Model That Cannot Talk Actually Fits"
date: 2026-09-25
description: "What is Jev, how is it different from an LLM, and will it replace one? A practitioner's guide to TypeSafe's System One model and why it complements language models rather than competing with them."
tags:
  - AI
  - Architecture
  - LLM
  - Jev
---

You have used ChatGPT, Claude or Gemini. You know roughly how an LLM works. And this week your feed has been full of something called Jev, with people calling it 200 times faster than an LLM, "the end of chatbots", or just "a fancy classifier", depending on who you follow. So you searched. Welcome, sit down, I will try to be the explanation I was looking for last week.

The short answer first. **Jev is not a better LLM and it is not a replacement for one.** It is a different kind of model that does one job, making structured decisions inside software, and does it very fast and very cheap. It cannot write a sentence. The most useful way to think about it is as the fast half of a system in which the LLM remains the slow, thoughtful half.

Now the longer answer.

## Jev is a decision model, not a language model

[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) comes from TypeSafe AI, a San Francisco lab co-founded by Diogo Almeida, one of the authors of the InstructGPT paper that led to ChatGPT, along with Erik Gafni and Sasha Sheng. It launched in early access on 15 September 2026, together with a $40M seed round, after two years in stealth.

TypeSafe calls it the first "System One Model". Here is how it works in practice. You give it unstructured input, an email, a support ticket, a game state, a transaction. Along with it, you give a set of questions whose possible answers you define in advance. There are three kinds:

- **Choice:** pick one option from a list you define (up to 255 options).
- **Score:** a rating on a scale.
- **Noul:** yes or no. Yes, that is really what they named it. I have started saying it in meetings, purely to watch people's faces.

Jev answers all your questions in one parallel pass and returns each answer with a probability. It cannot return anything outside the options you gave it. There is no text, no JSON to parse, no "Sure! Here is your answer:" in front of the answer.

It is trained with a method TypeSafe calls RLCD, Reinforcement Learning for Calibrated Decisions. Where LLMs are tuned with human feedback (RLHF) to produce text people like, RLCD is tuned so that the probabilities are honest. When Jev says 80%, it should be right about 80% of the time.

## How Jev differs from an LLM

An LLM generates text one token after another, each token depending on the ones before. That is what makes it so flexible, it can write anything. It is also what makes it slow and expensive when all you actually want is one of four words.

Jev skips generation entirely. It fills a fixed set of answer slots all at once.

| | LLM | Jev |
|---|---|---|
| Output | Free text, token by token | Typed answers, all at once |
| Best at | Reasoning, writing, explaining, handling the unexpected | Classifying, routing, scoring, yes/no, at volume |
| Structured output | Asked for, then parsed and validated | Native, cannot break |
| Honest confidence | Weak, not what it was trained for | The main training goal |
| Latency (vendor claims) | Seconds | 70 to 500 milliseconds |
| Can explain its answer | Yes | No, not one word |
| Pricing (vendor claims) | Pay per input and output token | $0.042 per million input tokens, outputs not charged per token |

TypeSafe's headline numbers are up to 193x faster and 444x cheaper than the LLMs it compared against, on its own workflow evaluations. Keep that phrase "on its own" in mind, we will come back to it.

## I started out thinking it was just a classifier

A confession. The first draft of this post was titled "A Classifier With a Marketing Budget". We have had text classifiers for years. Every enterprise I have worked in has a small graveyard of intent models, trained once for one purpose, loved for a quarter and never retrained.

Then I read the details and deleted the title. The old classifier answered one fixed question, in one domain, after weeks of labelled training data. With Jev, you change the questions at the moment you call it. Today it sorts complaints, tomorrow it scores fraud risk, and no retraining in between. It behaves more like a general-purpose model that has been told it is only allowed to tick boxes. That is new, and it is not small.

## The name explains the whole idea

"System One" comes from Daniel Kahneman's *Thinking, Fast and Slow*. System 1 is fast, intuitive judgement, the snap call an experienced person makes in two seconds. System 2 is slow, deliberate reasoning. (The name Jev, for the curious, is after the economist William Stanley Jevons, whose paradox says that when something gets cheaper, people end up using far more of it. TypeSafe's bet is that the same thing will happen with intelligence.)

Seen this way, the debate mostly settles itself. An LLM, especially one reasoning step by step, is a System 2 machine. For three years we have been using that System 2 machine for System 1 work, because it was the only machine in the building. Asking a frontier LLM to decide which of four queues an email goes to is like hiring a poet to sort the post. The poet does it well. The poet is also slow, expensive, and now and then writes the address as a haiku.

People need both systems. So does software.

## The real product is the confidence score, not the speed

Everyone is talking about speed. As an architect, the part I care about is calibration.

A model that is right 95% of the time is not enough to automate a process. You need to know *which* 5% it is wrong about, otherwise you end up reviewing everything, and then why did you buy the model. If Jev's probabilities really are honest, you get something you can actually build around: a dependable signal for when to trust the machine and when to escalate.

And escalation is exactly where the LLM comes back into the picture.

## Why Jev complements an LLM instead of replacing it

Picture a customer service or claims inbox. Thousands of messages a day. Most are routine, a few are messy, a handful are serious.

Jev goes first. For every message it decides the queue, the urgency, and whether a human needs to be involved, in well under a second and for a tiny cost. When it is confident, the message is routed and nobody else is involved. When its confidence is middling, the message goes to an LLM, which can read carefully, reason about it, and draft a reply in proper sentences, which Jev cannot do. When the confidence is low or the stakes are high, it goes to a person.

Each layer is cheaper than the one above it, and each layer knows when to pass the parcel. The LLM is not replaced. It is simply stopped from doing clerk's work, so it spends its time on the cases that genuinely need thinking and writing.

The same pattern applies to AI agents. Much of an agent's loop is small decisions. Which tool next? Is this result good enough? Should I stop now? Today each of those is a full LLM call with a paragraph of reasoning nobody reads. A System One model could handle that steering, while the LLM keeps the planning and the writing. The loop gets faster without getting any less intelligent.

## What Jev cannot do, and what is still unproven

A post that only cheers is an advertisement, so here is the other side.

**It cannot explain itself.** I work in insurance. "The model said Complaints, 0.93" is not an explanation a regulator or a customer will accept for a declined claim. Any decision that carries consequences still needs an LLM or a person to produce the reasons.

**It always picks from your options.** If you forget an option, Jev will not tell you. It will choose the least bad one and attach a probability. Designing the questions well becomes a real skill, and a bad set of questions produces bad decisions at 350 requests per second.

**The evidence is thin.** There is no paper, no model weights, and no architecture description beyond "new architecture". The benchmarks are TypeSafe's own, run on evaluations it designed against GPT-6 Astra and Fable 5.1. Even the latency figures, TypeSafe admits, were measured from laptops on the US West Coast. From Wellington, add the Pacific Ocean. Undersea cable does not care how clever your training method is.

So: early access, a genuinely good idea, numbers not yet independently checked. If you want to know whether it works for you, do one thing. Take a single noisy decision step in your own system and run it through Jev and your current LLM side by side for a week. Check whether the 90% answers are right about 90% of the time. That one experiment will tell you more than every thread on X put together.

## Quick answers

**Is Jev an LLM?** No. It is built for language input but does not generate language. It only returns structured decisions.

**Will Jev replace ChatGPT or Claude?** No. It cannot chat, write, summarise or explain. It replaces the LLM only in the narrow job of fast, repeated decisions, which LLMs were never ideal for anyway.

**Can I use Jev now?** It is in early access through a waitlist at the time of writing.

**What is RLCD?** Reinforcement Learning for Calibrated Decisions, TypeSafe's unpublished training method, aimed at making the model's confidence scores honest rather than making its answers pleasing.

## The quietest launch is the loudest one

Most AI launches of the past three years have been about machines that talk more: longer answers, longer memories, better voices. Jev went viral for the opposite reason. It says nothing at all.

And that might turn out to be its gift to the LLM. Once the fast decisions are handled by something built for them, the language models are free to do what they were always best at: thinking slowly, explaining patiently, and writing to the actual human at the end of the chain. Fast mind, slow mind, each doing its own work.

If Jevons was right, cheaper judgement will not mean fewer thoughtful machines. It will mean far more work gets done, and the thoughtful ones finally get to spend their time on the questions that deserve them.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) · Generated, Published and Tinkered with AI by a Kiwi*
