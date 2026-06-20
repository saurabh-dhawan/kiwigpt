---
title: "Eight things I noticed at Microsoft Build //localhost:Wellington"
date: 2026-06-19
tags: [microsoft, ai, agents, foundry, copilot, wellington]
slug: microsoft-build-localhost-wellington-2026
description: "Live notes and honest takes from Microsoft's Build //localhost event in Wellington: the good, the fuzzy, and the one thing I'm trying first."
readingTime: "8 min"
---

Yesterday I headed into the city for [Microsoft Build //localhost:Wellington](https://developer.microsoft.com/en-us/reactor/events/27230/), hosted at Level 13, 10 Brandon Street. It was part of Microsoft Reactor's global //localhost series, local echoes of the main Build 2026 event that ran in San Francisco on 2-3 June. The Wellington room had a good mix: developers, cloud engineers, a few architect types, and apparently at least one sales person who had clearly been told they needed to code now.

Speakers came from Microsoft New Zealand and the wider Asia-Pacific team. The format was live demos, guided lab walkthroughs, and time to actually try things. No slides-only keynote theatre. That suited me.

Here are eight observations from the day, in roughly the order they landed.

&nbsp;

### 1. Even the sales person codes now

The most quietly remarkable thing about the morning session was watching a Microsoft sales person walk through a GitHub Copilot coding workflow without blinking. Not performatively, not as a demo passenger. As someone who clearly uses it.

Microsoft's big framing at Build 2026 was that the platform shift is here -not just "AI helps developers" but "everyone in the organisation is being pulled toward building." The MAI-Code-1 model, tuned specifically for GitHub and VS Code, is part of that. So is the new GitHub Copilot app, which moves agentic workflows out of the editor and into a native desktop experience tracking sessions, issues, PRs, and background automation in one place.

When the tooling gets good enough that a sales person is doing it in a product demo without flinching, something has changed. Worth noting.

&nbsp;

### 2. Copilot Cowork is generally available today - but nobody could clearly explain what value does it provide and why it has its own licence (From my own experience of Claude cowork and Copilot cowork - Claude cowork is a much better offering btw)

Microsoft [announced Copilot Cowork GA](https://redmondmag.com/articles/2026/06/02/microsoft-uses-build-2026-to-put-ai-agents-at-the-center-of-windows.aspx) at Build, moving it from preview into broad enterprise use. The room was interested. Then yours truly asked the obvious question: why a separate licence rather than rolling it into the standard Microsoft 365 Copilot entitlement?

The answer was... not clear. There was talk of consumption models, Copilot Credits as the new pay-as-you-go meter for agent work, and some nuance about how per-user Copilot stays separate from agent execution costs. But the commercial logic — why this product, why this boundary, why now — was genuinely fuzzy. Nobody in the room left with a clean sentence they could take back to their CFO.

My read: Microsoft is trying to price agentic workloads differently from human-Copilot-assisted work, and they haven't finished working out how to explain it yet. The consumption meter concept (Copilot Credits) makes sense in principle. The product packaging around Cowork specifically does not yet have a clean narrative.

If you're evaluating this for your organisation, wait a cycle. The licensing will become clearer once a few more enterprises push back.

&nbsp;

### 3. Foundry Local sounds genuinely good and I'm going to try it

[Foundry Local](https://news.microsoft.com/build-2026/) lets you run AI models on your own machine — using the NPU, GPU, or CPU — without sending anything to the cloud. Microsoft has been building toward on-device inference for a while, and at Build this became a proper developer story, not just a preview whisper.

The pitch is simple: there are workloads you don't want leaving your network. Legal documents, client data, IP-sensitive drafts. Foundry Local gives you the Foundry developer experience (11,000+ models in the catalogue, the same SDK, the same eval tooling) running entirely on your hardware.

For me this is interesting both personally and at work. I want to try it for kind of documents that are too sensitive to run through a cloud API casually. The demo showed it's not a stripped-down fallback; it's the same platform, just with locality as a design constraint.

I'll write a follow-up post once I've actually run it. At the outset it is MS version of Ollama.

&nbsp;

### 4. Agent 365 is the right answer to agent sprawl

This one landed well in the room because it names a problem everyone is starting to feel. Organisations are now running agents they didn't formally approve — coding agents, automation agents, local agents running on developer machines. [Agent 365](https://devblogs.microsoft.com/foundry/agent-service-build2026/) is Microsoft's governance layer for all of them.

The [Agent 365 SDK is now generally available](https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/) and is framework-agnostic. Microsoft published packages for their own Agent Framework, OpenAI Agents SDK, LangChain, and Semantic Kernel. If you built an agent outside the Microsoft stack entirely, you can still bring it under the Agent 365 governance umbrella at no extra cost.

What that buys you: an Agent Registry that surfaces unmanaged local agents, Intune policies to block unsanctioned agents at the endpoint, Defender for runtime detection of prompt injection and risky actions, and Purview to prevent sensitive data leaking through local agent interactions. Every action becomes attributable, auditable, and governed.

From an enterprise architecture perspective this is the right move. Agent sprawl is a real risk. Having a control plane that works across frameworks rather than only for Microsoft-built agents is what makes it credible.

&nbsp;

### 5. Evals for agents are great — the rubric approach gives you something concrete

One of the things I find frustrating about most AI evaluation conversations is that they stay abstract. "How do you know if your agent is good?" ends up with vague answers about vibes and user satisfaction.

[Foundry's rubric evaluator](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) is more concrete. It reads your agent's definition and use case, then automatically generates evaluation criteria specific to your context. Not generic LLM benchmarks — actual criteria for your agent's job. It runs a two-step process: generate the rubric, then evaluate performance against it. Dimensions are weighted so you get an aggregate score with nuance, not a single pass/fail.

The [ASSERT framework](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) goes further: it converts your policies into measurable evaluations, systematically generates targeted test scenarios, and surfaces safety and quality defects before production. Open source, works across LangChain, CrewAI, OpenAI, and more.

The thing I liked about this framing: it treats evaluation as a continuous loop, not a pre-launch gate. Production traces feed back into the rubric, which feeds into Agent Optimizer. You don't just evaluate once — you get a closed observe, evaluate, optimize, deploy cycle running continuously. That's how you should think about agents in production.

&nbsp;

### 6. Agent Optimizer in Foundry is genuinely useful — but the same story for Copilot Studio agents is still missing

[Agent Optimizer](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/) replaces the guess-and-check improvement cycle for hosted Foundry agents. It reads your current prompts and skills, searches for configurations that lift quality against your scenarios and constraints, and surfaces ranked candidates with full diffs, lineage, audit trail, and rollback. You can see exactly what improved and what regressed before you promote the winner.

The demo was compelling. The continuous improvement loop — where every new production trace feeds back into evaluation and optimization — is the right architecture for agents that need to stay reliable over time.

This was my other question on the day: what about Copilot Studio agents?

A large number of Microsoft customers are going to build their first production agents in Copilot Studio, not in Foundry. The no-code, configuration-first path is where most business teams will start. Agent Optimizer is currently a Foundry story. The rubric evaluator is a Foundry story. The tracing and observability that makes all of this work — also Foundry.

If you're a Copilot Studio builder, you're watching this from outside the window. Microsoft needs to close that gap. The governance story for Copilot Studio agents should be at least as good as for developer-built Foundry agents, and right now it isn't.

&nbsp;

### 7. Guardrails, pen testing, safety — the full security stack is in Foundry

The afternoon had a solid block on agent security. The short version: Microsoft has built a real security stack into Foundry, not bolted it on.

[Runtime Data Loss Prevention](https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/) extends Microsoft Purview enforcement directly into the developer workflow — real-time detection and blocking of sensitive data in prompts and across agent interaction flows. You apply data protection controls as you build, not after deployment.

[Agent Control Specification (ACS)](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) is an open industry specification for runtime agent governance. It defines eight lifecycle interception points — input, pre/post model call, pre/post tool call, output, startup, shutdown — with a declarative YAML manifest. Write your policies once, enforce them across Python, Node, .NET, and Rust. You can place deterministic safety and security controls at exactly the points where the agent can fail.

There's also Defender AI model scanning, which detects and blocks potentially vulnerable or compromised models across registries, workspaces, and CI/CD pipelines before deployment.

The [Guided Guardrail Setup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/) in Foundry makes it easier to configure appropriate content safety for your specific agent — rather than applying generic defaults and hoping.

This is a mature security posture. Worth taking seriously if you're moving agents toward production.

&nbsp;

### 8. VS Code is becoming a serious application platform with the Foundry add-on

The last session touched on something I think is underreported. VS Code is no longer primarily a code editor with AI assistance added. With the Foundry extension now available, it becomes a development environment for building, testing, deploying, and managing AI agents end-to-end.

From VS Code you can now connect to the full Foundry agent development experience — model selection, evaluation runs, trace inspection, deployment to hosted agents — without leaving the editor. Combined with the [GitHub Copilot app](https://dev.to/pwd9000/microsoft-build-2026-top-announcements-from-a-devops-lens-419k) (native desktop experience for tracking agent sessions, PRs, and background automation) and the deeper Copilot integration in debugging and profiling, the VS Code surface has genuinely expanded.

Seven new MAI models were also announced, including MAI-Thinking-1 (reasoning) and MAI-Code-1 (tuned for GitHub and VS Code). The model router in Foundry can pick the right model for a task automatically, so you're not locked into a single choice. Claude Sonnet 4.5, Haiku 4.5, and Opus 4.6 are in public preview in Foundry. GPT-5.5 is generally available.

If you haven't looked at the VS Code + Foundry combination yet, it's worth a few hours.

&nbsp;

---

### What I'm doing next

One thing: try Foundry Local on a real internal document and write up what I find.

The event confirmed something I've been thinking about for a while: Microsoft's edge in the enterprise AI race isn't the flashiest model or the most impressive demo. It's the ability to wrap good capability in Entra, Intune, Defender, Purview, Teams, and GitHub — the systems organisations already bought and trust. Agent 365 and the Foundry security stack are that wrapper becoming real.

Thanks to the Microsoft Reactor team for putting on a good day in Wellington. Good room, good demos, honest conversations.

&nbsp;

---

*Written by a Kiwi, generating, publishing and tinkering with AI. On 18 June 2026 I attended Microsoft Build //localhost:Wellington, and this is what I brought back. Follow-up post on Foundry Local incoming - once I've actually run it. Views are genuinely my own, half-formed, and subject to revision. That's kind of the point :)*
