# [Brother Channel Companion: AI Dev Challenge] Claude Opus 5.5 Looks Insane… But Can It Code My Game?

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `3nTQKJeYQfM`
- **Publish Date**: 2026-09-23
- **Duration**: PT6M42S
- **Views**: 35,280 | **Likes**: 396
- **URL**: https://www.youtube.com/watch?v=3nTQKJeYQfM
- **Timestamped Lines**: 45

## Full Timestamped Transcript

[00:00:09] 3 hours back range combat everybody is super excited about new oppus model so I had to check this out
[00:00:17] this is how it cooked the range combat in our game if you're new here my brother and I are
[00:00:23] building our own game and if you want to follow the whole build hit subscribe it really helps we're building
[00:00:32] it piece by piece with AI as a part of the team and today range combat let's go so before
[00:00:42] writing any code I just sat down with Hobos and talked through it like how it should even work i
[00:00:48] wrote my ideas some references from other games and a bunch of open questions and wow the questions it asked
[00:00:56] me spot on every single one stuff I hadn't even thought about here's where we ended up hold to pull
[00:01:03] back let go to shoot while you hold a shadow of your shot grows on the ground the longer it
[00:01:10] gets the further you shoot the wider it gets the more your arrow spread and the color shows how your
[00:01:17] string is holding up there's no aiming miniame so you can shoot in about a second even while you walk
[00:01:24] but a good shot is still up to you how long you hold and when you let go let go
[00:01:29] too early weak shot hit that sweet spot right after a full draw bonus damage hold it too long your
[00:01:36] hands start shaking and snap string is gone hope you packed the spur because that's 2 and 1/2 seconds to
[00:01:43] rering i just love this one if you're a bad archer your con is wider so yeah you can aim
[00:01:50] perfectly and still miss but you always sit no hidden dice no random crits a wolf takes around four hours
[00:01:58] if you knew two or three once you're good you slow down while you're drawing and sprint or dodge cancel
[00:02:05] it no penalty and arrows actually fly so something running you aim a bit ahead bow crossbow sling same system
[00:02:15] just different numbers guns and throwing weapons different story that's for another video a few things are still open and
[00:02:24] that's totally fine in the next step we brought a second model Astra 6 took that spec and turned it
[00:02:30] into a picture of how this should actually looks like in a game the spec literally became a prompt
[00:02:40] and that image that's what we were building toward okay new session time to build i gave the main orchestrator
[00:02:49] everything it needed and just as important told it what to ignore the spec the target image use this bow
[00:02:57] and no animation yet they will come from Mixamo later don't touch the character focus on mechanics and that's it
[00:03:05] for the first iteration
[00:03:09] now let's see what it actually cooked welcome to the range lab just a scene some sheep some archery targets
[00:03:16] and a bow let's see how it works hold Q to draw works quick shot weak and wide clean release
[00:03:27] bonus damage works hold too long snap rerring works
[00:03:36] moving target you have to lead it and you can pick your arrows back up now the ugly part no
[00:03:45] animations at all the bow is basically glued to his hand it works but man it looks rough but that's
[00:03:53] on me i told it to not care about this yet
[00:04:05] for run two the orchestrator stopped doing everything itself it handed over the work to three sub agents each one
[00:04:13] running on Oppus 5.5 on medium agent one bows three of them we already had a bow from Astra but
[00:04:21] I was really curious what Oppus would do with the same job
[00:04:30] agent two a quiver again real reference photos and yeah this time I broke my own rule and left Astra
[00:04:37] out of it
[00:04:44] agent 3 got the coolest job remember those missing animations i grabbed an urcher animation from Mixamo and asked our
[00:04:52] agent to retarget that onto our character's rig totally different skeleton and it just works incredible
[00:05:10] and now look at this real bow a quaver actual animation this is just cool better
[00:05:27] okay so what did it all cost here's the tokens for both rounds it's estimated with API pricing
[00:05:40] two rounds in now let's jump for the fun part
[00:05:47] final test a real meadow a real bear and it's coming straight at us
[00:05:59] wait aim shoot again and it's down and we survived
[00:06:13] so all in from the first spec to that bur here's what it would cost on the API and on
[00:06:20] my max plan just around 10% from weekly usage from a spec to a picture to this i love it
[00:06:34] if you want to see what we build next subscribe see you in the next one
