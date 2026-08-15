---
title: "He Used AI to Build a Tool That Does Not Use AI"
date: 2026-08-15
description: "A maths teacher showed me an app he had built with ChatGPT. It generates exam questions, prints answer sheets, scans them back and marks them with OCR, and the whole thing is three megabytes and never phones home. Then he told me which part of the marking he refuses to automate, and that was the bit worth writing down."
tags:
  - AI
  - Education
  - Tooling
  - Strategy
---

Best conversation I had all month happened in the ten minutes after a school meeting, standing around, the way the good ones usually do.

My son's maths teacher was showing me what the class is working through at the moment, and the topic on the screen was vector coordinates. Points in space, described by numbers. Year 8 stuff.

I could not help myself. I said, do you know this is more or less how the whole of modern AI works? Every word, every image, every sentence you have ever typed into ChatGPT gets turned into exactly this, a list of coordinates. Just not two of them or three. Thousands. Meaning becomes a direction in a space with more dimensions than you can picture, and similar things end up pointing the same way. Your Year 8 class is doing the toy version of the thing that ate the technology industry.

He got quite excited about that. And then he said, actually, let me show you something.

## Three megabytes, and it never phones home

What he showed me was an app he had built himself with ChatGPT's help. School themed, tidy, working. It generates randomised question sets for objective exams. It lays out answer sheets you can print. You mark them on paper, feed the sheets back through the scanner, and the app reads them using OCR and marks them.

Whole thing, just over three megabytes.

I want to sit with that number, because I have written architecture documents that were bigger. A single hero image on a corporate homepage is bigger. There are npm packages that weigh more than this and all they do is check whether a number is odd.

The reason it is three megabytes is that it does everything on the machine in front of him. No API call. No round trip. Nothing leaving the building. I asked why he had gone to that trouble and he did not give me a privacy answer or a compliance answer, which is what I was braced for. He kept using one word, compute. He did not want to spend compute every time he marks a test. Electricity, yes, but also the plain running cost, because tokens are not free and a test sat by thirty students four times a term is a bill that arrives every term forever. The work does not require a data centre, so why involve one.

The power saved by one teacher not calling an API will not trouble anybody's climate model. But the cost side compounds in the nasty direction, because the more useful the tool becomes the more it gets used and the more it charges you. His version has a marginal cost of zero and stays there. That is the difference between a tool you own and a subscription you rent.

And the constraint is what produced the three megabytes. Once you decide the thing must run locally, you are forced to work out what the job actually is. Turns out generating a randomised maths question is arithmetic and templates. Reading a tick in a box is optical character recognition, which we solved before I finished school. Neither needs a language model. They only look like they do because we have all got into the habit of reaching for the biggest hammer in the shed.

Notice too where the AI actually went. Into the building, not into the running. He used a language model to write a tool that does not use a language model, which is quietly the most sensible pattern I have seen in a while, and nearly the opposite of what most organisations are doing right now. True story, at a friend's workplace: a small Google Apps Script that has been doing its job for years. Deterministic, free, boring in the best sense. The current suggestion is that the same logic should now be done by a model. Nobody has said what would improve. It just feels behind, not to have AI in it.

## The part where I was wrong

I did what architects do, which is immediately look for the gap.

I said, this works beautifully for objective exams. But your subjective papers, where a student gets marks for the working, for the method even when the final answer is wrong? That you cannot do with OCR. For that you would genuinely need a model in the loop.

And he said, no. Those ones I want to mark myself.

Not because a model could not attempt it. Because marking working is how he finds out what each kid is actually getting wrong. Not that they got it wrong, which the score already tells him, but where the reasoning bent. And then across thirty scripts a pattern shows up, half the class has quietly misunderstood the same thing, and now he knows what Monday's lesson is.

That stopped me, because I had been treating marking as a cost. It is the standard framing, no? Marking is the drudgery, the after-hours grind, the obvious candidate for automation, and every edtech pitch deck of the last two years has led with exactly that promise. Give us your marking, take back your weekend.

He is not protecting the task. He is protecting what the task tells him. Years in the education technology industry before he came back to teaching, which I suspect is exactly why he can smell a bad automation from across the room.

## Input signal and output signal

The question he handed me is portable, and it followed me home, which is the annoying thing about good questions.

Most of us have two kinds of signal. There is the input signal, which is how you come to understand anything: reading, articles, videos, seminars, the meeting, the argument, the long discussion that goes nowhere and then suddenly does. And there is the output signal, which is what you produce, and which becomes somebody else's input. A paper, a deck, a diagram, a decision written down so thirty other people can act on it.

I protect the input side absolutely. I still read the thing myself, sit in the meeting myself, have the conversation myself, and I would not hand any of that over for anything. What I hand over is the shaping of the output. The payoff is not just my Tuesday. It is that the organisation gets its input signal sooner and in better shape, while the question is still live, which is worth considerably more than the same paper arriving three weeks later with my fingerprints lovingly all over it.

His case is the interesting one, and it is the whole reason this is worth writing down. For him, the marking is both at once. The output is a mark on a script. But producing it is also his input channel, the only sustained look he gets into thirty separate minds, and there is no other way to obtain it. Automate that and you have not saved him work. You have cut the wire that tells him what to teach next.

So the rule is not about drudgery and it is not about difficulty. Some work produces an output and quietly hands you an input on the way past. That is the work to keep your hands on. Everything else, ship it to the machine and do not feel bad.

In fairness the boundary is fuzzy for me too. Three months after writing an options paper I could once recite all six options from memory, because I had built each one by hand and the effort had welded them in. That verbatim hold is shorter now. The direction stays, the reasoning stays, and I can still argue any of it standing up, which is just as well because decisions get relitigated beside the coffee machine far more often than they get relitigated in a governance forum. But six months on I reach for the paper sooner than I used to. Writing was never purely output. A little understanding was consolidating while I built each option by hand, and some of that has gone. I judge the leak small and the timeliness worth far more. It is a judgement though, not a free lunch, and anybody telling you otherwise is selling something.

Which leaves all of us with the same question, and it is worth ten quiet minutes. Which of your outputs is secretly also one of your inputs? Not the task you enjoy, and not the one you are best at. The one that, if a machine did it perfectly on Monday, would leave you strangely blind by Friday without you being able to say why.

## The bit that made me hopeful

Every week there is another piece about AI and education, and it is almost always about cheating. Kids generating essays, teachers running detectors, an arms race that neither side enjoys and nobody is winning.

Meanwhile a maths teacher, with no budget line and no vendor and no transformation programme, sat down and built the thing he needed. Three megabytes. Runs on his laptop, saves him hours a week, and he still marks the papers that teach him something.

The models will keep getting better and cheaper, and none of that decides anything. What decides the next ten years is whether the people holding them can tell which part of their own work is the actual work. He could tell, without anybody making him, before it was fashionable, on a school laptop, in three megabytes.

And my son is in that class, learning that a vector points somewhere, taught by a man who worked out exactly where the machine should stop. I did not choose that for him. I just got lucky. But I will take it.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) · Generated, Published and Tinkered with AI by a Kiwi*
