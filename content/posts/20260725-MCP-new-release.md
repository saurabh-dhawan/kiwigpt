---
title: "MCP Goes Stateless: What the 2026-07-28 Spec Actually Changes for Architects"
date: 2026-07-25T00:00:00+00:00
draft: false
description: "The MCP 2026-07-28 release candidate drops sessions, promotes extensions, and deprecates three core features. Here is the architectural read, the impact on existing implementations, and what tech leaders should plan for."
summary: "The MCP 2026-07-28 release candidate drops sessions, promotes extensions, and deprecates three core features. Here is the architectural read, the impact on existing implementations, and what tech leaders should plan for."
keywords: ["MCP", "Model Context Protocol", "architecture", "agentic AI", "API gateway", "OAuth", "enterprise architecture", "NZ"]
tags: ["MCP", "Architecture", "AI", "Protocol", "Enterprise"]
categories: ["Architecture"]
author: "Saurabh"
showToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
  image: ""
  alt: ""
  caption: ""
  relative: false
---

Every so often a protocol grows up in public, and you get to watch. The [2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) is one of those moments. The maintainers are calling it the largest revision since launch, and for once that is not marketing enthusiasm. Sessions are gone. Extensions are first class. Three core features have been quietly walked to the departure lounge.

If you have an MCP server in production, or a roadmap that says "MCP server" in the Next horizon, this one is worth an hour of your attention. Not because the sky is falling. Because the shape of the thing you were about to build has changed underneath you.

Let me walk through what actually changed, and then the part most posts skip, which is what it means for the people who have to plan budgets and sprints and vendor conversations.

---

## The Headline: MCP Is Now Stateless

In the old world, calling a tool over Streamable HTTP meant first doing a handshake, receiving an `Mcp-Session-Id`, and then carrying that header on every subsequent request. Which pinned your client to one server instance. Which meant sticky sessions at the load balancer, a shared session store behind it, and gateway rules that had to peer into the request body to figure out what was even happening.

Anyone who has run that pattern at scale knows the feeling. You are not operating a protocol, you are babysitting one.

The new spec removes the `initialize`/`initialized` handshake entirely, and removes the session header with it. Protocol version, client info, and capabilities now travel in `_meta` on every request, and a new `server/discover` method lets clients fetch server capabilities when they want them. The result is that any MCP request can land on any server instance. Plain round-robin. No session store. Ordinary HTTP infrastructure doing ordinary HTTP things.

There is a lovely consequence hidden in there. Application state does not disappear, it just becomes honest. Instead of the transport secretly holding a session for you, a tool mints an explicit handle, a `basket_id` or a `browser_id`, and the model passes it back as a normal argument on the next call. The maintainers make an interesting claim here, which is that this is not merely a workable substitute but often a better one, because the model can compose handles across tools and reason about them, in ways hidden session state never allowed.

I think they are right. State that the model can see is state the model can use. State hidden in a header is state that only your ops team gets to worry about.

---

## Architectural Implications

Here is where I want to slow down, because the interesting effects are second order.

**The gateway becomes a first-class MCP participant.** Streamable HTTP now requires `Mcp-Method` and `Mcp-Name` headers, so load balancers, gateways, and rate limiters can route and throttle on the operation without inspecting the body. Servers must reject requests where the header and body disagree. For anyone running an APIM-fronted remote MCP server, this is the change that matters most. Your gateway policies can finally be written in the language of the protocol. Per-tool rate limits. Per-method routing. Per-name observability. All without body parsing, which was always a slightly grubby workaround anyway.

**Caching moves from folklore to contract.** List and resource read results now carry `ttlMs` and `cacheScope`, modelled on HTTP `Cache-Control`. A client knows exactly how long a `tools/list` response stays fresh and whether it is safe to share across users. That `cacheScope` field deserves a hard look in any regulated shop, because "safe to share across users" is a sentence that should trigger a design review, not a shrug. But the upside is real. You no longer need a long-lived SSE stream just to learn that a tool list changed.

**Tracing is now nailed down.** W3C Trace Context propagation in `_meta` is documented, with `traceparent`, `tracestate`, and `baggage` key names fixed. A trace that starts in a host application can follow a tool call through the client SDK, the server, and whatever the server calls downstream, and land in an OpenTelemetry backend as one span tree. If you are building an agentic capability into a channel architecture, this is the difference between "the agent did something" and "here is exactly what the agent did, to which system, on whose behalf." Auditability stops being a slide and starts being a header.

**The protocol grows a spine about breaking things.** Extensions are now formal, with reverse-DNS identifiers, negotiation through an `extensions` capability map, their own repositories with delegated maintainers, and independent versioning. Alongside that sits a feature lifecycle policy giving every feature an Active, Deprecated, and Removed path with at least twelve months between deprecation and earliest removal. And a Standards Track proposal cannot reach Final until a matching scenario lands in the conformance suite.

That last one is the quiet governance win. A specification that will not bless a feature until it is testable is a specification you can actually procure against. Try writing that clause into a vendor contract today and see how the conversation goes.

**Server-initiated requests are constrained on purpose.** Servers may now only issue requests to the client while actively processing a client request. It was recommended before, it is required now. Nobody gets prompted out of nowhere, and every elicitation traces back to something the user or their agent started. Multi round-trip requests replace the held-open SSE stream with an `InputRequiredResult` carrying an echoed `requestState`, which the client returns with the answers. Any instance can pick up the retry, because everything needed is in the payload.

Read that again through a consent lens. This is not just a scaling change. It is a structural guarantee that an AI-mediated channel cannot pop a request at a customer that has no traceable origin. That is the sort of property you want to be able to state plainly to a risk committee.

---

## Impacts on Existing Implementations

Not all impact is equal, so here is the honest sorting.

| Change | Type of impact | Who feels it |
| --- | --- | --- |
| Handshake and session removed | Breaking, transport and lifecycle rewrite | Server and client implementers, platform ops |
| `Mcp-Method` / `Mcp-Name` required | Breaking, but mostly additive at the gateway | API management, network, SRE |
| Multi round-trip elicitation | Breaking, flow redesign | Anyone doing human-in-the-loop tools |
| Experimental Tasks API | Breaking, migration required | Early adopters of long-running work |
| Missing-resource error code moves from `-32002` to `-32602` | Breaking if you match on the literal | Client authors with error-handling logic |
| Full JSON Schema 2020-12 for tools | Additive, with new guardrails | Tool authors, schema reviewers |
| Authorization hardening | Mostly additive, some client obligations | Identity and security teams |
| Roots, Sampling, Logging deprecated | Annotation only, minimum twelve-month runway | Everyone eventually |

A few of those deserve a sentence more.

The Tasks one is a genuine migration, not a rename. Tasks shipped as an experimental core feature in `2025-11-25`, and production use surfaced enough redesign that it now lives as an extension with a reshaped lifecycle. A server can answer a `tools/call` with a task handle, and the client drives it with `tasks/get`, `tasks/update`, and `tasks/cancel`. Creation is server-directed, and `tasks/list` is gone because it cannot be scoped safely without sessions. If you built on the experimental API, you are migrating. Budget for it rather than discovering it.

The deprecations are gentler than they sound. Roots, Sampling, and Logging are annotation-only deprecations, still working in this release and in every version published within a year of it, with removal requiring a separate proposal. The replacements are sensible. Roots gives way to tool parameters, resource URIs, or server configuration. Sampling gives way to direct integration with LLM provider APIs, which is where most serious implementations quietly ended up anyway. Logging gives way to `stderr` for stdio and OpenTelemetry for anything structured.

Sampling going is the one that will start arguments. The idea that a server could borrow the client's model was elegant on a whiteboard and awkward everywhere else, because it smeared cost, consent, and model choice across a trust boundary. Cleaner to just call the provider yourself and own it. I will not be attending the wake.

And the schema change is more consequential than its one-line summary. Tool `inputSchema` and `outputSchema` lift to full JSON Schema 2020-12, so composition with `oneOf`, `anyOf`, `allOf`, plus conditionals and references, all become available. Output schemas are unrestricted, and `structuredContent` can be any JSON value. But note the two guardrails: implementations must not auto-dereference external `$ref` URIs, and should bound schema depth and validation time. Which is the spec politely saying that an expressive schema language is also an attack surface, so please do not fetch arbitrary URLs at validation time. Somebody was going to.

---

## Authorization, Briefly, Because It Matters More Than It Reads

Six proposals harden authorization toward how OAuth 2.0 and OpenID Connect actually get deployed.

Clients must validate the `iss` parameter on authorization responses per RFC 9207, a cheap mitigation for a class of mix-up attack that is more prevalent in MCP's one-client-many-servers pattern. In a future version clients will be expected to reject responses that omit `iss`, so authorization servers should start supplying it now. Clients also declare their OpenID Connect `application_type` during Dynamic Client Registration, which fixes the tediously common case where a desktop or CLI client gets defaulted to `"web"` and then has its localhost redirect rejected. Credentials bind to the issuing server's `issuer`, with re-registration when a resource moves between authorization servers. Refresh token behaviour, scope accumulation during step-up, and the `.well-known` discovery suffix are all documented more precisely.

None of this is glamorous. All of it is the difference between an integration that passes security review and one that generates a six-week email thread.

---

## What Tech Leaders Should Plan For

The release candidate locked on 21 May 2026, the final spec publishes on 28 July 2026, and the ten-week window in between exists so SDK maintainers and client implementers can validate against real workloads. Tier 1 SDKs are expected to ship support within it. Which means by the time you read this, the window is nearly shut and the useful question is not whether to move but in what order.

**One. Find out what you have.** Not "do we use MCP," but which servers, which clients, which SDK versions, which tools, and who owns each. Most organisations discover at this point that there are three more MCP servers than the architecture team knew about, usually built by the most useful person in the building. This is not a governance failure. It is a discovery exercise you should have done anyway.

**Two. Ask your vendors the dated question.** Not "do you support MCP." Ask which specification version, and what their `2026-07-28` conformance and migration plan looks like. The new conformance suite makes that answerable rather than aspirational, and a vendor who cannot name a version is telling you something.

**Three. Stop designing around sessions.** If a design in flight assumes sticky routing, a shared session store, or a long-lived SSE stream to notice list changes, revisit it now. The infrastructure you were going to procure for that may simply not be needed, which is the rare architecture change that removes a line item instead of adding one.

**Four. Move the policy to the gateway.** Routing, rate limiting, and quota enforcement on `Mcp-Method` and `Mcp-Name` is the single highest-leverage change available. For a shared remote MCP server serving multiple channels, per-tool policy at the edge is what makes shared infrastructure governable rather than merely shared.

**Five. Treat observability as a launch requirement.** With trace context key names fixed, there is no longer a good excuse for an agentic capability that cannot be traced end to end. Make it a gate, not a backlog item. Do it later never arrives.

**Six. Decide your extension posture deliberately.** Extensions being opt-in and independently versioned is a gift and a trap. The gift is that MCP Apps and Tasks can move at their own pace. The trap is a portfolio where every team has adopted a different set. Pick which extensions are sanctioned, write it down, and revisit it quarterly. Boring, and it works.

**Seven. Read the deprecation policy as a planning instrument.** Twelve months minimum between deprecation and earliest removal is a genuine commitment, and it means you can build a roadmap with real dates instead of vibes. Use it. Put the Roots, Sampling, and Logging migrations in a Later horizon with an actual named owner rather than a hopeful shrug.

---

## The Bit I Keep Coming Back To

There is a line in the announcement about the explicit-handle pattern making state visible to the model rather than hidden away. I have been turning that over all week.

We spent two decades learning to hide state from applications. Sessions, sticky routing, transparent caches, all of it built so the application would not have to think. Now we are building systems where the thing on the other end can think, and suddenly hidden state is not a convenience but a blindfold. The model cannot reason about what it cannot see.

That is a genuinely new design instinct. Make the state legible, because your consumer is no longer a dumb client faithfully replaying a header. It is something that can compose, reason, and hand off. Design for a colleague, not a cursor.

And the deeper thing, the one that will matter longer than any single header name, is that MCP just demonstrated it can make a clean break and then build the machinery to avoid needing another one. Deprecation windows, an extensions track, conformance gates before Final status. That is a protocol behaving like infrastructure rather than a project.

Which is exactly what you want, when you are about to bet a channel architecture on it. Enjoy the migration. Genuinely. It is not often you get to remove infrastructure and gain auditability in the same release.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*