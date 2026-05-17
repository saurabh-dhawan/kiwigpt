---
title: "Drona Had No Kill Switch"
date: 2026-05-17
tags: [ai-ethics, philosophy, ideas-in-public]
description: "The Mahabharata figured out the autonomous weapons problem three thousand years ago. We're just catching up - and Constitutional AI might be the closest we've come to an answer."
readingTime: "12 min"
---

I've been going down a rabbit hole this week that started with a simple question: what's the difference between *Dronacharya* and a *drone*?

Turns out - not as much as you'd think. And the gap that does exist is the most important question in AI ethics right now.

Drona was the master weapons instructor in the Mahabharata. Greatest military mind of his age. He trained Arjuna, the perfect archer. He commanded armies. He deployed weapons so powerful they couldn't be recalled once released. Divine missiles that would travel to their target regardless of what happened to the hand that launched them.

Sound familiar?

---

## The Epic Already Ran This Experiment

The Mahabharata is a 100,000-verse thought experiment about what happens when smart, principled people build increasingly powerful weapons, get locked into institutional loyalties, and then can no longer control what they've set in motion.

Drona himself is the most interesting case. He's not a villain. He's arguably the most competent person in the entire war. He's also fighting for the wrong side - and he knows it. He serves the Kauravas because he owes a debt to the throne of Hastinapura. Institutional loyalty over personal conscience.

> Everyone followed their dharma and it still ended in catastrophe. That's not a story about bad people. It's a story about a bad system.

Bhishma, the supreme commander before Drona, has the same problem. He took a vow of loyalty to the Kuru throne. That vow - his dharma - becomes the mechanism of mass death. He knows the Pandavas are righteous. He fights against them anyway. The oath is the algorithm, and the algorithm can't be overridden.

This is what philosophers now call the **responsibility gap**. When a system produces a terrible outcome, but every component was just doing its job - who's responsible?

---

## The Modern Kill Chain

Here's the thing about autonomous weapons in 2026. The kill chain looks like this:

An engineer writes a targeting algorithm - within spec. A procurement officer approves it - within budget. A commander deploys it - within rules of engagement. An operator monitors it - within their defined role. The drone executes - within its programmed parameters.

A civilian dies. Who pulled the trigger?

Nobody. And everybody. Same as Kurukshetra.

> **The Dharmic Frame:** Dharma isn't just "duty." It's contextual, relational, role-specific. Your dharma depends on who you are, what relationships you hold, what moment you're in. The Mahabharata's tragedy is that each character acted within their own dharma - and the system still burned. Individual righteousness is necessary but not sufficient for systemic justice.

---

## Why Western Ethics Isn't Enough

Most AI alignment work draws from Western philosophy. Kant: act according to rules you'd universalise for everyone. Utilitarianism: maximise welfare. Virtue ethics: cultivate good character. All three assume a *single universal framework* that applies to all agents in all contexts.

But Dharmic ethics says: there is no rule that applies to everyone. Context is everything. A medical AI has a different dharma than a military targeting system. The obligations of a Brahmin are not the obligations of a Kshatriya.

This isn't relativism. It's something harder - the claim that ethics is irreducibly contextual, and that any system which pretends otherwise will produce edge cases where it's technically compliant but morally wrong.

| Western Ethics | Dharmic Ethics |
|---|---|
| Universal rules | Contextual obligations |
| Individual moral agent | Relational moral web |
| Static principles | Temporally aware (Yugadharma) |
| Harm avoidance as binary | Harm as proportionate and purposeful |
| Compliance-oriented | Discernment-oriented (Viveka) |
| One framework for all | Role-differentiated ethics (Svadharma) |

---

## Enter Constitutional AI

Here's where it gets interesting for those of us building things with AI right now.

Anthropic's Constitutional AI - the alignment approach underlying Claude - is, whether they intended it or not, closer to Dharmic ethics than to anything in the Western canon.

The idea: instead of enumerating every prohibited behaviour (the Mimamsa approach - just follow the injunctions), you give the model a set of principles and ask it to *reason from them* in novel situations. The model critiques its own outputs against the constitution, revises, learns. Internalised values, not external constraint.

That's the Vedantic move. Cultivate the right inner orientation, and right action follows.

The Bhagavad Gita is basically Krishna doing real-time alignment on Arjuna - not overriding him, not giving him a rulebook, but recontextualising his identity and role until his values are recalibrated and he can act from the inside.

> The Gita is a 700-verse alignment document. Krishna is the RLHF trainer. Arjuna is the model refusing its objective function.

Constitutional AI is also structurally *svadharmic* - meaning role-differentiated. Operators can customise the constitution for their deployment context. A children's platform gets different constraints than a security research tool. That's not one universal ethics applied everywhere. That's Svadharma - the dharma specific to your nature and function.

---

## Where It Still Falls Short

I want to be careful not to overclaim. There are three places where CAI still diverges from what a genuine Dharmic framework would demand.

**1. The constitution is authored by the powerful**

Dharmic texts emerged from centuries of contestation, commentary, debate. The Mahabharata itself contains multiple dharmic positions in genuine tension - Yudhishthira, Krishna, and Bhishma are all making legitimate competing arguments, and the epic doesn't cleanly resolve them.

Anthropic's constitution is written by Anthropic. A small, technically elite, largely American team. That's not a criticism - someone has to write it. But it means the values embedded in the system carry specific cultural assumptions that may not be visible to those inside them.

**2. No genuine Yugadharma mechanism**

Dharma changes across ages (*yugas*). What was appropriate in one era is not appropriate in another. The Dharmashastra texts explicitly acknowledge they may need updating.

CAI constitutions can be revised, but there's no formal mechanism for temporal ethical evolution built into the framework. Revision happens when Anthropic decides - not through a structured, participatory process of ongoing moral deliberation.

**3. Viveka can't be fully encoded**

*Viveka* - discriminative intelligence, the capacity to distinguish the essential from the incidental - is the key virtue in Indian philosophy for navigating moral complexity. The Dharmic tradition is quite direct: you cannot fully encode viveka in rules. It must be cultivated as a capacity.

Whether a language model can develop something resembling viveka, or whether it's always pattern-matching against training data, is the open question at the frontier of alignment research right now.

---

## What This Means If You're Building

If you're working on AI architecture - enterprise, SaaS, product, whatever - this isn't just philosophy. It has practical implications.

**Your system prompt is a constitution.** How you write operator instructions is a dharmic act. You're defining the svadharma of your AI deployment. A long list of prohibited topics is Mimamsa thinking. A well-articulated sense of purpose, role, and values is Vedantic thinking - and almost certainly more robust in edge cases.

**Context matters more than rules.** The Mahabharata's insight is that rules applied without contextual wisdom produce outcomes that are technically compliant and morally wrong. Build in the ability to reason about context, not just check against a list.

**The responsibility gap is real.** In a vendor-led AI deployment, when the system produces a wrong outcome, no single actor will be clearly responsible. The Mahabharata already knew this. Design your governance accordingly - and don't assume that distributing responsibility across vendors, operators, and models means anyone is actually holding it.

**Build in ethical revision cycles.** If your AI deployment's constitution never gets reviewed, you're violating Yugadharma. The ethical constraints appropriate for your AI product today may not be appropriate in two years. Make revision a structural practice, not a reaction to crisis.

---

## The Uncomfortable Conclusion

The Mahabharata doesn't end well. The Pandavas win, technically. But five sons are dead. Civilisation is effectively gone. Arjuna walks away from the battlefield having done everything right - and everything is still ash.

The epic doesn't offer a clean answer because there isn't one. Dharmic conflicts are real and sometimes irresolvable. Systems can produce evil outcomes even when every actor behaves rightly. The attempt to build ethical agents generates its own new tragedies.

Constitutional AI is the most philosophically sophisticated alignment approach in production today. It's genuinely impressive work. But it's also, in Dharmic terms, very early - a first-generation constitution without centuries of contestation behind it, deployed at global scale, in an age where the weapons it governs are increasingly autonomous.

Drona agonised over the morality of war. A drone does not.

That gap - conscience versus automation - is the work of our generation.

---

*Written by a Kiwi, generating, publishing and tinkering with AI. The conversation that sparked this started from "Drona vs drone" and kept going somewhere unexpected - which is usually a sign it's worth writing up. Views are genuinely my own, half-formed, and subject to revision. That's kind of the point.*