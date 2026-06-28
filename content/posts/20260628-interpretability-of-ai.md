---
title: "Interpretability of AI: What It Means, How We See It, and What It Tells Us"
date: 2026-06-28
description: "A simple explanation of AI interpretability, how researchers peek inside the black box, and what happens when a model is asked to understand something as ordinary as 'small'."
tags:
  - AI
  - Interpretability
  - Machine Learning
  - Explainability
cover:
  image: "/interpretability-header.png"
  alt: "Interpretability of AI"
---

There is a question that comes up every time I explain AI to someone for the first time. They nod along when I talk about training data, about neural networks, about predictions. Then they ask the one question that stops the conversation: but how does it actually decide what to say? And honestly, for the longest time, nobody could give a proper answer. The model worked. Nobody quite knew why it worked the way it did, in any detail you could point to. That gap between "it works" and "we understand why it works" is exactly what interpretability is trying to close.

Interpretability, in plain language, is the effort to look inside an AI model and explain what is happening when it produces an answer. Not in the vague sense of "it learned patterns from data," which is true but tells you nothing useful. Interpretability wants the specific story. Which parts of the model lit up. Which concepts it was using. Why it chose one word over another. It treats the model less like a sealed box and more like a brain you are allowed to open, slice, and study, neuron by neuron if needed.

This matters more than it sounds. A model that gives the right answer for the wrong reason is a liability waiting to surface. A doctor's assistant that flags cancer correctly nine times out of ten because it happened to notice a date stamp on the scan, rather than the actual tumour, is not safe just because it scored well in testing. We need to know the reasoning, not just the result. That is the whole point of interpretability. It moves us from trusting the AI because it seems to work, to trusting it because we can see why it works.

So how do researchers actually see inside? There are a few approaches, and each gives a different kind of window.

The first is attention visualisation. Many modern models, especially the transformer-based ones that power things like ChatGPT and Claude, decide how much "attention" to pay to each word in a sentence while processing it. Researchers can literally plot this attention as a heat map. You can watch the model glance at certain words more intensely than others while forming its answer. It is a bit like watching someone's eyes move across a page and noticing where they linger.

The second is probing. Here researchers train small, simple classifiers on the internal activations of a large model, just to check if a particular concept, say grammatical gender, or sentiment, or even something like "is this sentence about size," is sitting somewhere inside those layers of numbers. If a tiny classifier can pull out that concept easily from the model's internal state, it tells us the big model has, in some form, learned and stored that idea.

The third, and probably the most exciting recent development, is mechanistic interpretability. This is the painstaking work of identifying actual circuits inside a model, specific groups of neurons that consistently perform one particular job, like detecting negation, or tracking whether a sentence is a question. Anthropic's own research has shown that models contain interpretable "features," recognisable concepts spread across combinations of neurons, almost like finding individual letters hidden inside what looked like random static.

Let's think of a concept - 'small' - how would a model interpret something so ordinary?

When a model encounters the word small, it does not look it up in a dictionary the way we might imagine. Instead, the word gets converted into a vector, a long list of numbers, based on everything the model learned about how "small" is used across enormous amounts of text. That vector sits close, in this abstract numerical space, to words like tiny, little, compact, modest. It sits far from words like enormous, vast, gigantic. The model has built, without anyone explicitly teaching it, a kind of internal map of size, where words cluster by meaning and relationship, not by spelling or sound.

But "small" is also relative, and this is where interpretability gets genuinely interesting. A small elephant and a small ant are wildly different sizes in the real world. A good model does not just retrieve a fixed notion of small. It adjusts its internal representation based on context, the surrounding words, the subject of the sentence, even the broader paragraph. Mechanistic interpretability researchers have started finding circuits that do exactly this kind of contextual adjustment, neurons that seem to track "smallness relative to category," rather than smallness as an absolute property. It tells us the model is not memorising definitions. It is building something closer to a flexible, situational sense of scale, learned purely from patterns in language.

What does all this tell us, stepping back? It tells us a few humbling things. It tells us large language models are not simply giant lookup tables, repeating memorised text. There are genuine internal structures, recognisable concepts and circuits, that resemble, in a rough and imperfect way, how human cognition organises ideas. It also tells us these models are still deeply mysterious in places. We have only begun mapping a small fraction of the circuits inside today's largest models. Most of the inside remains genuinely unexplored territory.

And it tells us why this work matters beyond academic curiosity. If we want AI systems we can trust with real decisions, in healthcare, in finance, in safety-critical infrastructure, we cannot keep treating them as black boxes that occasionally surprise us. Interpretability is how we move from "it seems to work" to "we know why it works, and we know when it might fail." That shift, slow and unglamorous as the research can be, may turn out to be one of the most important pieces of work happening in AI today.

I find something quietly reassuring in this pursuit. In a field often obsessed with making models bigger and faster, there is a steady, patient group of researchers asking a more humble question. Not "what can it do," but "what is actually going on in there." That curiosity, that refusal to simply accept the black box, feels like the right instinct to carry forward as these systems become more capable and more woven into our daily lives.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) · Generated, Published and Tinkered with AI by an Indian Kiwi*
