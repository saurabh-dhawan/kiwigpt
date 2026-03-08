---
title: "From Boot Failure to Success — AI-Assisted Hardware Debugging"
date: 2026-02-19
description: "How AI and human persistence got my Reachy Mini from dead-on-arrival to fully working. Part 2 of the Reachy Mini Diaries."
tags: ["reachy-mini", "robotics", "debugging", "ai-assist", "maker-journey"]
keywords: ["reachy mini", "pollen robotics", "hugging face", "hardware debugging", "ai assistant"]
slug: "reachy-mini-debugging-ai-v2"
series: ["Reachy Mini Diaries"]
images: []
---

Back to [Part 1 — Reachy Mini Arrives in Aotearoa](/posts/reachy-mini-arrives-in-aotearoa/)

---

Sometimes a robot just refuses to cooperate.

After spending seven months waiting for my Reachy Mini to arrive, I assembled it with care — and then watched it refuse to boot. Power LED: green. ACT LED: one sad blink, then nothing. No WiFi hotspot. USB-C ignored. The motors twitched promisingly, but that was it.

My little desk robot was alive enough to taunt me, but too broken to respond.

This is the story of how AI and I debugged it together — and what I learned about collaborating with an assistant that never gets frustrated, never forgets documentation, and occasionally knows more than I do.

---

## When in Doubt, Document Everything

My first instinct was to throw the symptoms at Claude. I wrote up an `Issue.md` file with everything I'd observed: LED behaviour, USB response, motor activity, Bluetooth status. Then I asked:

> "Read issue.md and help me debug my Reachy Mini."

Within seconds, Claude had a theory: **corrupted OS on the CM4**. The ACT LED's brief blink suggested the CPU was trying to boot but couldn't load the system. The fix? Reflash the eMMC using `rpiboot`.

But Claude didn't stop there. I pushed harder:

> "What else might I have missed? Scan the docs, check GitHub issues, and make a full plan."

The result was a five-phase debug plan — and a critical discovery buried in the documentation: a **Bluetooth reset method** via nRF Connect that might fix the issue without reflashing. I wouldn't have found that on my own.

---

## The Bluetooth Reset That Wasn't

Using nRF Connect on my phone, I paired with the robot and sent reset commands:

1. `PIN_02687` — authentication using the serial number
2. `CMD_SOFTWARE_RESET` — trigger a reboot

Nothing happened.

Claude's diagnosis was calm and precise: the Bluetooth service runs at a low level, even when the OS isn't functional. The robot could receive commands, but it couldn't execute them — because there was no operating system to execute anything.

Lesson learned: **sometimes the low-level stuff is alive, but the full system is toast.**

Time to reflash.

---

## Reflashing the OS (The Hard Way)

This is where Claude earned its keep. Reflashing a CM4 isn't trivial — it requires:

- `rpiboot` to put the CM4 into USB mass storage mode
- `bmaptool` for fast, verified image flashing
- Physical access to a hidden switch inside the robot's head

Claude walked me through every step:

```bash
# Build rpiboot
cd ~/Development
git clone --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot && make

# Install bmaptool
pipx install git+https://github.com/yoctoproject/bmaptool.git

# Download ReachyMiniOS
curl -LO "https://github.com/pollen-robotics/reachy-mini-os/releases/download/v0.2.3/image_2026-01-14-reachyminios-lite-v0.2.3.zip"
curl -LO "https://github.com/pollen-robotics/reachy-mini-os/releases/download/v0.2.3/2026-01-14-reachyminios-lite-v0.2.3.bmap"
```

Then came the physical prep: power off, flip the switch to DOWNLOAD, connect USB internally. Claude reminded me to start `rpiboot` *before* powering on — a mistake that would have cost me another frustrating hour.

The flash took two and a half minutes. Then: switch back to DEBUG, power on, wait...

**WiFi connected.** 🎉

---

## One Bug Fixed, Another Appears

Of course it wasn't that simple.

The dashboard loaded, but the motors weren't responding. The testbench showed motors 11, 12, and 13 missing — the three Stewart platform motors that control the head's tilt.

Claude spotted the pattern immediately: **successive missing IDs usually mean a cable disconnect.** When I'd opened the head to flip the switch, I must have pulled the cable loose between motor 10 (body) and motor 11 (first Stewart motor).

I powered off, opened the neck, found the 3-wire cable dangling free, reconnected it, and powered back on.

**Everything worked.**

---

## What I Learned

| Phase | Problem | Solution |
|-------|---------|----------|
| 1 | No WiFi hotspot | Corrupted OS diagnosed |
| 2 | Bluetooth reset failed | OS wasn't running |
| 3 | Reflashed OS | rpiboot + bmaptool |
| 4 | Motors missing | Reconnected loose cable |

**Root cause:** A corrupted OS, plus a cable I accidentally disconnected while troubleshooting.

---

## Why AI Made the Difference

This wasn't a case of AI doing all the work. I still had to:

- Physically open the robot
- Flip switches
- Run commands
- Reconnect cables

But AI did things I couldn't:

1. **Found buried documentation** — The Bluetooth reset method was in a file I'd never have searched.
2. **Stayed systematic** — When I was ready to reflash immediately, Claude suggested trying the simpler fix first.
3. **Diagnosed the second failure instantly** — Successive missing motor IDs pointing to a cable break is hardware debugging experience I don't have.

The collaboration felt natural: AI provided knowledge and reasoning, I provided hands and real-time feedback. Neither of us could have done it alone.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| [rpiboot](https://github.com/raspberrypi/usbboot) | Put CM4 in USB mass storage mode |
| [bmaptool](https://github.com/intel/bmap-tools) | Fast image flashing |
| [nRF Connect](https://apps.apple.com/app/nrf-connect/id1054362403) | Bluetooth debugging |
| [ReachyMiniOS](https://github.com/pollen-robotics/reachy-mini-os/releases) | Official OS image |
| [Reachy Mini Testbench](https://huggingface.co/spaces/pollen-robotics/reachy-mini-testbench) | Motor diagnosis |

---

## Coming Up: Part 3 — First Impressions

With the OS flashed and motors cooperating, it's time for the real fun: testing behaviours, experimenting with what Reachy Mini can do, and discovering the quirks of a robot that's finally, stubbornly, alive.

---

*Written for [KiwiGPT.co.nz](https://kiwigpt.co.nz) — Generated, Published and Tinkered with AI by a Kiwi*
