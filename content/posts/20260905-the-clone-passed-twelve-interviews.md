---
title: "The Clone Passed Twelve Interviews and Then Went Home"
date: 2026-09-05
description: "Companies are screening candidates with AI. A candidate built an AI clone of himself and passed twelve first-round screens at twelve companies. Then the story just stops, and I think the stopping is the whole point."
tags:
  - AI
  - Hiring
  - Architecture
  - Strategy
---

A recruiter, a candidate and a large language model join a Teams call. Nobody on the call is a person, and the call still starts eight minutes late.

That is the joke. Here is the news.

Companies have started putting AI in the first round of hiring. Not just the CV filter, which has been a machine for years, but the actual interview. An avatar with a name and a haircut asks you to tell it a story about a time you showed initiative, and something behind it scores your answer. [Semafor](https://www.semafor.com/article/08/07/2026/ai-avatars-enter-the-job-interview) and [The Next Web](https://thenextweb.com/news/ai-avatars-job-interviews-candidates-recruiters) have both covered the next turn of the screw, which is that candidates are now sending avatars of their own to sit those interviews, and recruiters are spending five minutes working out that the very polished person on screen is not, strictly speaking, a person.

Some people find this poor taste. Some people shrug and say the HR partner screen was equally baffling, only slower, and they have a point that I will come back to.

But the story that has stayed with me is one I read in passing and cannot now find the source for, so take it as a story. A candidate got tired of the process. He built an AI clone of himself, fed it his CV, his LinkedIn, a few notes on how he talks, and pointed it at the market. Twelve companies. Twelve first-round AI screens. Twelve passes.

Twelve out of twelve is a pass rate I have not achieved at anything, including parking.

And then the story stops. Nobody knows whether he attended the second round. Nobody knows whether anyone made him an offer. Nobody even knows whether he wanted a job.

I have been turning that over for a week now, and I have decided the abrupt ending is not a gap in the story. It is the story.

## The screen was never talking to him

Think about what actually happened in those twelve calls. On one side, a model that has been given a CV and asked to sound like the person on it. On the other side, a model that has been given a job description and asked to check whether the person sounds like the CV. They were always going to agree. It is the same document, having a conversation with itself, and rating the conversation highly.

Which tells you something uncomfortable about round one. It was never measuring the candidate. It was measuring how well the candidate had been described. A good CV, read aloud with confidence, passes. That was true when a bored human did the reading also, only the human got tired after the fourth call and let a few through on vibes. The machine does not get tired. The machine lets all of them through, consistently, at scale, with a dashboard.

The Next Web piece makes the point more sharply than I would have dared: when the machine screens the machine, the interview stops measuring anything. Their argument is that the fix is to change the process, not to police the candidates. The same is true here also, and I would go one step further.

## A control that the artefact can satisfy is not a control

I have sat in enough architecture forums to have seen the pattern before, just wearing a different jacket.

You set up a review gate. The gate is meant to check that the system is sound. What the gate actually checks is the slide deck about the system. Over time, teams get very good at slide decks. The gate passes everything. The systems still fall over on go-live, but the paperwork was immaculate, and somebody gets to say the process was followed.

That is what a first-round AI screen is. A gate that checks the artefact, not the thing the artefact describes. Once you see it that way, the clone story is not fraud, or not only fraud. It is a penetration test. Someone walked up to twelve gates with the artefact and nothing else, and all twelve opened. That is an audit result. The finding is: your first round has zero information content, and you are paying a vendor for it.

It is not that using AI to screen is in poor taste. Taste is the wrong frame, and it lets everybody off the hook. It is poor design. And poor design was there before the AI arrived, the AI just made it fast enough to notice.

## Square one, haha, except it is not square one

The instinct, and I had it too, is to laugh and say we are back where we started. Humans lied on CVs, humans skimmed CVs, everybody knew, the system muddled through.

But we are not back there. We are somewhere worse, because the response to the arms race is landing on the wrong people. The Next Web reports that a large majority of recruiting leaders now run at least one in-person stage specifically to counter AI-assisted fraud, and that big names have reintroduced mandatory face-to-face rounds. Which sounds sensible until you notice who it excludes. The candidate in Invercargill. The one in Pune. The parent who cannot fly to Auckland for a forty-minute chat. Remote hiring was supposed to widen the door, and the defence against the clone is to narrow it again, for everyone, including the ninety-something percent who would never build a clone in the first place.

So the clone did not just expose a weak gate. It handed the people who own the gate a reason to make the whole building harder to enter. That is the real cost, and it is being paid by people who were never in the story.

## Why the story stops there

Here is my honest theory about why nobody knows what happened next.

Because nothing happened next, and nothing needed to. Passing a screen is not a job. Twelve passes are twelve invitations to a second conversation, and the second conversation is the one where a person asks you something you have not seen before and watches your face while you think. The clone cannot do that round. Not yet, and I would argue not ever in a way that helps anyone, because the moment it can, the second round has become the first round and we are having this same argument one floor up.

The candidate, I suspect, knew that. I suspect he was not job hunting. I suspect he was making a point, and the point landed, and he closed the laptop. The clone did not ask about salary, which is how you know it was never a real applicant.

## What I would actually do

If I owned a hiring pipeline, and I do not, I would do one thing. I would stop asking the first round to do a job it cannot do.

Either make the first round cheap and honest, which means a short human conversation with someone who can say "tell me about the worst decision on that project", or make it a real test, which means putting something in front of the candidate that is not on the CV and cannot be. A messy problem from the team's actual backlog. A live thirty minutes. A person on the other end, or at the very least a person reading the transcript with their own eyes before anybody is rejected.

And if you cannot afford that for every applicant, then be honest that the first round is a lottery and shrink it, rather than dressing the lottery in an avatar and calling it evaluation. Publish the rubric, even. If the machine scores keywords, tell people the keywords. It is undignified, but it is less undignified than pretending.

## The most human thing in the story

I keep coming back to the ending, or the lack of one.

Twelve companies wanted a conversation with a person who had been very well described. The description held up. And somewhere out there the actual person is doing whatever he does, unhired and apparently unbothered, having proved that the hardest part of getting past round one was never the candidate.

Meanwhile, sitting in twelve inboxes, there are twelve second-round invitations waiting to ask the only question that ever mattered: is he any good.

That question is still open. It still needs a human to ask it, and a human to answer, and a room, real or virtual, where both of them are actually present. Everything the machines did on either side of the table was just clearing the way to that moment. Which is, when you think about it, exactly what the whole apparatus should be for.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) · Generated, Published and Tinkered with AI by a Kiwi*
