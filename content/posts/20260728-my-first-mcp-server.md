---
title: "My First MCP Server"
date: 2026-07-28
description: "One silly publishing ritual involving Chrome on a phone, two failed attempts at connecting Claude to GitHub, a third I designed and never deployed, a fourth that could read everything and write nothing, and the little server I finally, finally shipped. If you are reading this, it worked."
tags:
  - AI
  - MCP
  - Claude
  - Cloudflare
  - Writing
  - Tinkering
---

![A hand drawn path of four attempts at building an MCP server: an empty search returning nothing, a locked official server, an abandoned blueprint, and finally a small working server publishing a post to a phone, with a kiwi walking the path](/images/my-first-mcp-server.png)

The oldest post on this site is a little Alexa demo from June 2020. I look at it occasionally the way you look at a photo of yourself with a bad haircut, with a mix of affection and disbelief.

But here is the thing about that post. The experiment it describes was not the hard part. I had been tinkering for years before that, pulling things apart, wiring things together, getting them working at eleven at night and feeling quietly pleased with myself. The tinkering was never the problem.

The writing was the problem.

I had plenty of ideas. My head has always been full of them, half formed, jostling, occasionally quite good. What I did not have was any reasonable path from a thought to a paragraph. Sitting down to write meant an hour of staring, then a first sentence I hated, then deleting the first sentence, then checking my email. And underneath all of it, the honest excuse that also happened to be true: I did not have the time. Between work and family and everything else, "write that idea up properly" sat at the bottom of a list it was never going to climb.

So the ideas stayed in my head. Years of them.

Then GPT-3 arrived, and it changed overnight.

I want to be precise about what changed, because people usually get this wrong. It did not write for me. What it did was demolish the blank page. Suddenly I could dump a messy half thought into a box and get back something structured enough to argue with, and arguing with a draft is a thing I can do all day. The bottleneck was never having ideas. The bottleneck was the terrifying distance between an idea and the first sentence, and that distance collapsed to about nine seconds.

I remember the feeling clearly. Joy is not too strong a word for it. All those years of thoughts that had nowhere to go, and now they had somewhere to go.

## The ritual

So I started writing. On my desktop, at first, which was fine.

Except my best ideas do not arrive at my desktop. They arrive on the train. They arrive when I am sitting on a beach with nothing to do and plenty of time, which is exactly the condition under which a half formed thought finally unfolds itself. Those are my most precious thinking hours, and they were completely unusable, because in those hours I have a phone and nothing else.

So I built a flow for the phone. And I would like to walk you through it, because I have never written it down before and I suspect describing it out loud is going to function as its own form of therapy.

Get the draft as markdown. Select the whole thing inside a code block, on a touchscreen, which is a fine motor skill that nobody warned me about. Copy. Switch to the GitHub mobile app. Navigate to `content/posts`. Create a new file. Type the filename by hand. Paste. Commit.

And it worked! Genuinely, it worked. I have published real posts this way, from real trains.

Then I wanted to add an image, and the whole thing fell over. The GitHub mobile app will not let you upload a binary file. So the solution, and I want you to sit with the shape of this for a moment, was to open Chrome on the same phone, load the full GitHub web interface, request desktop site, and then pinch and zoom my way around a UI designed for a twenty seven inch monitor until I found the upload button.

Phew. But it worked.

And then there is the filename. I am precise about the naming convention on this blog, date first and then the slug, no exceptions, because I want these posts to sort correctly forever. Sounds trivial, no? It is not. Typing a date by hand on a phone keyboard, on a moving train, having just worked out today's date from context clues, is a task that has stumbled me up more times than I would like to admit. Wrong month. Wrong year, twice, in January, which is its own special humiliation. I have gone back and fixed more filenames after the fact than I have fixed typos in the actual writing.

All these tooling advances, models that will happily hold a conversation with me about Vedanta, and there I am fat fingering a date into a mobile keyboard.

## A note on the drafting side

The writing tools moved along too, though not in a straight line.

For a long stretch I ran a custom GPT on ChatGPT. I had fed it my old posts, taught it my rules, told it about the em dashes I refuse to use. It knew the voice. These days I mostly work with Claude, with skills for the repetitive bits and now MCP for the plumbing, because the reasoning suits the kind of argumentative back and forth I like, where I push on a position and want it pushed back on rather than politely agreed with.

But I will admit something. I still open that custom GPT now and then. Not for the reasoning. For the tone. Sometimes it hands back a paragraph and the rhythm is just right, in a way I cannot fully explain and have not managed to reproduce anywhere else. Voice is a strange thing. It does not live where you expect it to live.

## So when MCP came along

You can see why I sat up.

Every one of those fiddly steps between "finished draft" and "published post" is clerical. Not one of them requires judgement. Copy, paste, name, commit, pinch, zoom. A protocol that lets a model reach into a system and simply do the thing was, for me, not an abstract architecture question at all. It was a very specific promise about trains.

## Attempt one, which found nothing

The obvious first move was to look for a GitHub connector. Back in May I asked Claude to connect to my GitHub account, fully assuming this was a solved problem, the sort of thing you tick a box for.

It searched the registry. GitHub, repository, code. Nothing came back.

Nothing! For GitHub. The single most connected piece of infrastructure in all of software, and it simply was not there.

I filed it under someday and went back to pinching and zooming.

## Attempt two, which would not let me in

Later I found that GitHub does run an official remote MCP server. It sits at `api.githubcopilot.com/mcp`, it is real, and it exposes a very large number of tools.

So I tried to connect it, and it would not authenticate. Which, in my experience, means I have done something wrong. That is almost always what it means. So I did the usual dance. Re-read my configuration. Checked the URL character by character. Revoked the token and minted a fresh one. Tried again. Same wall.

Then I went and read GitHub's own installation documentation properly, and found the line where they say it themselves. The authentication flow expects the thing to be registered as a GitHub App, and this does not currently work cleanly with Claude's connector interface.

I sat back from the screen and felt two things at once, which have not fully resolved even now.

The first was relief, and it was enormous. It was not me. I had not misread a doc or fumbled a scope or missed something obvious that a competent person would have caught. Forty minutes of quietly wondering whether I had lost a step, and no, the seam was real and documented and had nothing whatsoever to do with me.

The second feeling arrived about four seconds later and was considerably worse. Because a problem you caused is a problem you can solve. You can debug your own mistakes at eleven at night with enough coffee and stubbornness, and I have, many times, and there is a real pleasure in it. But you cannot debug somebody else's roadmap. There was no quantity of effort available to me that would move this thing even slightly. The wall was not high. It was just not mine.

That is the specific irritation, and I think anyone who builds things will recognise it instantly. Not "this is hard." Hard is fine. Hard is the fun part. This was "this is closed, and my effort is worth nothing here." All that energy, and nowhere to put it.

So I did what you do when you have energy and nowhere to put it. I decided to build my own.

## Attempt three, which I never deployed

This is my favourite part of the story, because it is the part where I did the most work and shipped the least.

The design was good. Small and sharp. Exactly two tools, one to publish a post and one to upload an image. Nothing else at all. If somebody ever compromised it, the maximum blast radius would be a weird blog entry, which frankly is a risk my readers already live with.

Cloudflare Workers was the obvious host. The free tier is properly free rather than a trial wearing a disguise, roughly a hundred thousand requests a day against my projected usage of about twenty a month. Responses in milliseconds. Deployable from a browser, which mattered enormously given that the entire point of the exercise was to stop being chained to a desk. And Anthropic's own connector documentation points at Cloudflare as the recommended route for remote MCP servers, so at least I would be lost on a well marked trail.

I looked at the other options too. GitHub's own native route, a few other edge hosts, and a Raspberry Pi under the stairs, which is not a solution, it is a hobby with a TLS certificate attached.

I had the tool schemas. I had the security model down to about five lines. I had the hosting decision made with actual reasoning behind it rather than vibes.

What I did not have was a deployed server. Because somewhere between "I understand this completely" and "I have typed it in", there is a gap, and that gap is where my side projects go to enjoy a long and comfortable retirement.

## Attempt four, which could read everything and write nothing

So this morning, slightly embarrassed, I went back and tried the official GitHub server one more time.

Not because anything had changed that I knew of. Only because of a small rule I have picked up, which is that walls in this industry move quietly and nobody sends you a notification when they do. The thing that refused you in May is perfectly free to say yes in July, and the only cost of finding out is about forty seconds. The alternative is carrying a stale assumption around for a year and calling it experience.

I named it `github_try`. Because I was fully prepared to delete the thing within the hour and did not want to waste a good name on it.

And it connected.

For about ten minutes I thought the story was over and I had won. Because it was wonderful. It read my repository. It found the exact front matter on my last post and copied the field set. It read my deployment workflow and told me, unprompted, that any push to main goes straight to production with no review gate, which is true, and which I knew, and which I had somehow never said out loud to myself.

Then I asked it to publish the post. And it said:

```
403 Resource not accessible by integration
```

Ah. So I did the thing I had just finished recommending. I retried. I asked it to make a branch instead, thinking the write path to a new branch might be less locked down.

```
403 Resource not accessible by integration
```

I retried the file write one more time, in case the first was a hiccup.

```
403 Resource not accessible by integration
```

Read only. Comprehensively, immovably read only. And I went looking for the setting that would fix it, the way you do, and there was no setting. No repository selector. The permissions are fixed by the app itself, the token is minted somewhere above my account, and every single write endpoint returns the same four words.

Which is, when you sit with it, the most quietly frustrating failure mode there is. Not a connector that does nothing. A connector that can read my last forty posts, learn my naming convention, catch a deployment risk I had missed, and then watch, politely and with perfect comprehension, as I fail to publish a single word.

I had hit the same wall as attempt two. Not mine, not movable, not my fault.

So here is a correction to my own rule, delivered by the universe roughly ninety seconds after I had finished congratulating myself on it. Yes, retry. Walls do move without telling you, and attempt four proved it by connecting when it had flatly refused in May. But you have to be able to tell a wall that quietly moved from a wall that has not shifted an inch, because they look identical from the outside until you push. The connecting moved. The writing did not. Retrying is a coin you should always flip, but it is still a coin.

Which left exactly one option. The one I had designed in loving detail and never built.

## Attempt five, which is the one you are reading

I went back to the Worker.

Not to design it again, I had done that months ago. To finally close the gap between "I understand this completely" and "I have typed it in." Two tools, exactly as drawn. `publish_post`, which takes a slug and the full markdown and commits it. `upload_image`, which takes bytes and drops them into the images folder. A personal access token fenced to precisely two paths, the posts folder and the images folder, and nothing else on the whole account. Deployed to the Cloudflare edge from a browser tab, which is the detail that mattered most, because the entire point was never to be chained to a desk again.

Nobody's roadmap can revoke this one. There is no app in the middle minting a token with opinions of its own. It is mine, end to end, small and boring and completely under my control, which is exactly the set of words I keep reaching for at work when I actually trust an architecture.

And here is the part I could not write until it was true, so I am writing it at the very last moment before I find out.

This post was published by that server. The image at the top of this page was uploaded by that server. I did not copy anything into a code block. I did not switch to the GitHub app. I did not open Chrome, request desktop site, and pinch my way to an upload button. I did not type a filename on a train.

If you can see these words, it worked. That is the whole test, and it is a beautifully honest one. The proof of a publishing pipeline is not a green tick in a dashboard. It is a stranger, somewhere, reading the thing it published. You are the tick.

## What actually changed

I still press the button. That part has not changed and should not. The deploy fires on any push to main, there is no staging and no undo, and a commit is a publication. So I did not hand a machine the keys to the front door. I handed it the clerical labour and I kept the one step that needs a human, which is the decision to go.

Which is, now that I write it down, exactly the same conclusion I keep arriving at about agentic systems at work. Give the agent the tedious, reversible, judgement free steps. Keep the veto for yourself. Turns out my blog has been running a very small governance pilot this whole time and I did not notice.

The next post is about the architecture of this little server. How the two tools are shaped and why only two. How the write scope is fenced to two folders and what happens if you try to reach outside them. Why "the worst case is one weird blog post" was not a joke but the actual, entire threat model, and why that is a healthier way to design than pretending you can secure everything. The boring details, in other words, that make it safe to hand a machine a small key.

Once upon a time I could not get the ideas out of my head at all. Then a model came along and cleared the blank page, and after that the only thing standing between a thought and a published post was a filename I kept typing wrong on a train.

That bit is handled now. The next idea I have on a walk is getting published from the footpath, and this time I actually mean it, because the thing that publishes it is finally mine.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) · Generated, Published and Tinkered with AI by a Kiwi*
