
⸻

title: “From Boot Failure to Success — AI-Assisted Hardware Debugging”
date: 2026-02-19
description: “How AI and human persistence got my Reachy Mini from dead-on-arrival to fully working. Part 2 of the Reachy Mini Diaries.”
tags: [“reachy-mini”, “robotics”, “debugging”, “ai-assist”, “maker-journey”]
keywords: [“reachy mini”, “pollen robotics”, “hugging face”, “hardware debugging”, “ai assistant”]
slug: “reachy-mini-debugging-ai”
series: [“Reachy Mini Diaries”]
images: []

Back to Part 1 — Reachy Mini Arrives in Aotearoa￼

⸻

Sometimes a robot just refuses to play ball. After assembling my Reachy Mini, that moment hit me square in the face: the little guy wouldn’t boot.

Power LED: green ✅
ACT LED: blinked once and died ❌
WiFi hotspot: gone ❌
USB-C: ignored me ❌
Motors 5 & 6: twitching like they were alive ✅
Bluetooth pairing from macOS: still worked ✅

So yes, it was alive… just not enough.

Welcome to Part 2 of the Reachy Mini Diaries, where AI and human grit teamed up to tackle a dead robot. Spoiler: we got there.

⸻

The Problem

I documented all the quirks in Issue.md and fired it off to my AI assistant, Claude:

“Read issue.md file and help me debug my Reachy Mini”

The diagnosis came back quickly: corrupted OS on the CM4 (Compute Module 4). The ACT LED blink told the story — the CPU was trying to boot but couldn’t load the system. The AI suggested reflashing the OS with rpiboot and gave step-by-step instructions for macOS.

⸻

Step 1: Cloning the SDK

First, the AI suggested grabbing the SDK repository, so it could access all the docs and troubleshooting guides:

git clone https://github.com/saurabh-dhawan/reachy_mini.git temp_clone
mv temp_clone/* temp_clone/.* .
rm -rf temp_clone

Now AI had all the context it needed to think like a Reachy Mini expert.

⸻

Step 2: Deep Dive into Documentation

Next, I asked AI to be thorough:

“Scan all directories and files, check forums and GitHub issues, and make a plan.”

It dug through:
	•	troubleshooting.md
	•	reflash_the_rpi_ISO.md
	•	reset.md
	•	motors_diagnosis.md

The nugget of gold? The nRF Connect Bluetooth reset method in reset.md. That could be tried before reflashing. The AI built a phased DEBUG_PLAN.md:
	1.	Basic verification
	2.	Bluetooth reset
	3.	Advanced hardware checks
	4.	Reflash OS
	5.	Post-flash verification

⸻

Step 3: Bluetooth Reset Attempt

Using nRF Connect, I connected to Reachy Mini. The AI guided me:
	•	Autoconnect: OFF
	•	PHY: default
	•	Bond: OFF

Commands sent:
	1.	PIN_02687 (last 5 of serial)
	2.	CMD_SOFTWARE_RESET

Nothing happened. The CM4 was polite but firm: “I can’t execute a software reset because my OS isn’t even loaded.”

Lesson learned: sometimes the low-level stuff is alive, but the full system is toast.

⸻

Step 4: Reflashing the OS

Time to bring out the big guns. AI walked me through rpiboot and bmaptool:
	•	Installed prerequisites (libusb, pkg-config, pipx)
	•	Built rpiboot
	•	Installed bmaptool
	•	Downloaded ReachyMiniOS v0.2.3 (1.7GB image + 14KB bmap)

Physical prep:
	1.	Power OFF
	2.	Set switch SW1 to DOWNLOAD
	3.	Connect USB-C internally

Then ran rpiboot and powered ON. Disk appeared, unmounted, flashed:

sudo bmaptool copy image_2026-01-14-reachyminios-lite-v0.2.3.zip \
  --bmap 2026-01-14-reachyminios-lite-v0.2.3.bmap /dev/rdisk5
diskutil eject /dev/disk5

Switch back to DEBUG, power ON… WiFi connected. Finally, a green light moment. 🎉

⸻

Step 5: Motors Missing

Next hiccup: motors not detected. AI quickly analysed the pattern: missing successive IDs usually mean a cable disconnect. Sure enough, the cable from motor 10 (body) to motor 11 (Stewart platform) had come loose when I toggled the switch.

Reconnect → power ON → all motors back online. Phew.

⸻

Summary Table

Phase	Problem	Solution
1	No WiFi hotspot	Corrupted OS
2	Bluetooth reset failed	OS not running
3	Reflashed OS	rpiboot + bmaptool
4	Motors not detected	Reconnected loose cable

Root cause: Corrupted OS + accidentally disconnected motor cable.

⸻

Tools Used

Tool	Purpose	Link
rpiboot	Put CM4 in USB mass storage mode	GitHub￼
bmaptool	Fast image flashing	GitHub￼
nRF Connect	Bluetooth debugging	iOS￼ / Android￼
ReachyMiniOS	Official OS image	Releases￼
Reachy Mini Testbench	Motor diagnosis app	Hugging Face￼


⸻

Key Takeaways
	1.	AI spotted buried documentation I missed
	2.	Step-by-step guidance is invaluable during flashing
	3.	Missing motor IDs usually point to a physical disconnect
	4.	Simple fixes + AI knowledge = success
	5.	AI + human collaboration accelerates debugging

⸻

Coming Up in Part 3: It Coming Alive

With the OS flashed and motors finally cooperating, it’s time for the real fun: first impressions, testing behaviors, and experimenting with what Reachy Mini can actually do. Expect tiny victories, surprising quirks, and a robot that slowly — but surely — starts to feel alive.

⸻

Written for KiwiGPT.co.nz￼ — Generated, Published and Tinkered with AI by a Kiwi