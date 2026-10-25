# Can AI Make Building Fun?

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `xTxlZJwiIoQ`
- **Publish Date**: 2026-10-02
- **Duration**: PT6M2S
- **Views**: 16,683 | **Likes**: 337
- **URL**: https://www.youtube.com/watch?v=xTxlZJwiIoQ
- **Timestamped Lines**: 57

## Full Timestamped Transcript

[00:00:00] all right welcome back Today it's all about building because in a survival game you need a place to hide
[00:00:06] right and building should also be one of the most fun parts of a game People just love building because
[00:00:12] that's where you get to be creative So for us this was a really tough nut to crack And honestly
[00:00:19] it took us longer than anything else in the game as of now We built a whole building system then
[00:00:25] we deleted it because it didn't click and started again from zero and thought with just one single animation for
[00:00:31] a whole day And if you don't know we are building a whole survival game for Steam with AI and
[00:00:37] we already have a few episodes So in this video I will show you both the workshop we deleted and
[00:00:43] the one we kept where you built everything by hand And this time two AIs work on the same game
[00:00:49] GPT6 Astra in Codeex and Cloud Opus 5.5 I will also show you who built what So the first version
[00:00:57] my idea was a modular system So I asked the GP6 Astra to build the house from separate parts You
[00:01:03] know you could place every single part on its own So first it made pictures of every part like walls
[00:01:09] doors windows and roofs And we turned them into 3D models in Tripo Then came the book You open it
[00:01:17] pick a lock cabin and you can change its shape You drag a wall add other room change the roof
[00:01:23] and even the color And then you just press deliver materials and the house appears Foundation walls roofs like one
[00:01:32] cleage Later it even got lamps and paint for the whole house So GPT worked on this for more than
[00:01:38] a whole day And it rebuild it again and again one version on top of the other until the code
[00:01:44] was huge And it all worked But when I played something felt wrong The house had no job You click
[00:01:50] and it was there nothing to carry nothing to fill and nothing can go wrong It just felt like another
[00:01:56] city builder not a survival game So I said "This doesn't fit our game Let's just remove it All the
[00:02:02] code gone in one single comet." So we started again this time with Opus 5.5 and with a few simple
[00:02:10] rules First you carry everything yourself A lock goes on your shoulder just like for example in Sons of the
[00:02:17] Forest Small stuff like sticks stones and other items goes into your backpack and your backpack is just a mat
[00:02:23] you roll out on the ground Second nothing appears at once You build step by step and the book stays
[00:02:29] but it's more like a notebook with ideas not a shop And Opus had a working version super quickly So
[00:02:36] now it works like this You pick it in the book put down the plan bring the logs or other
[00:02:42] items and each lock flies right into place but carrying a log That was fun actually First we tried Mixamo
[00:02:50] but it only has animations for boxes not for a lock on your shoulder Then we found the CMU motion
[00:02:56] capture database Those are recordings of read people and one of them was pretty close So Opus 5.5 took it
[00:03:02] into Blender and kept fixing it until the logs sat right on the shoulder Then we added a sled so
[00:03:09] you can pull more logs at once And yes the first version was a little bit wild So I want
[00:03:14] to show you a few small tricks behind the scenes because those are actually interesting So why the first sled
[00:03:21] was so wild it slid sideways like it's on ice and it spin around like a clock But the real
[00:03:25] slat can only go where it's a runner's point So now it just goes forward and turns in soft curve
[00:03:37] and the character gets logs by cutting down the trees That part was done by my brother and he talked
[00:03:43] about it in this video And the biggest part of building by hand is your own house No plan from
[00:03:49] the book Just you and your logs Carry a log press E and split into two halves for the floor
[00:03:54] Put the next one beside and it snaps on And here is a trick almost every building games uses When
[00:04:00] you get close the plank snaps on but it only lets go when you move much farther away Otherwise it
[00:04:07] would just flicker back and forth right on the edge Then the walls One lock is one row And the
[00:04:13] next one goes right on top Need a window just grab the axe point at the wall and cut it
[00:04:19] out Low for a door and high for a window The floor the walls and the cutting That was all
[00:04:26] GPD on ultra in one long session And the door Well Codex hits its limit right in the middle of
[00:04:31] it So Opus finished it OPUS did the roof in three steps the beams the boards on top and the
[00:04:38] triangle at the front So here is one whole hat on the middle from the very first log to the
[00:04:44] roof
[00:04:48] And one more thing you see in games all the time and never notice The game hides anything that blocks
[00:04:54] your view If you go behind the tree it gets transparent Same happens with the roof Okay Around the camp
[00:05:00] a wooden fence You mark it out in the book and every lock you bring becomes one post Codex also
[00:05:08] rebuilt every camp thing in Blender The leanto the fire the tent and the traps And I'm not saying that
[00:05:14] this the final version but it looks okay now So that's what we kept Camp stuff comes from the book
[00:05:20] as a plan And your house you build yourself log by log And this is my camp right now Every
[00:05:26] single lock here I carried by hand Okay And here is a little sneak peek at the next episode This
[00:05:33] is the troll and he really doesn't like our camp
[00:05:38] And everything he breaks you can pick up again A whole log stays a log and the broken ones turns
[00:05:43] into a firewood And that's what the next episode is all about the best all the animals and monsters because
[00:05:49] in our game the forest cannot be safe Let me know in the comments what you would build first Thanks
[00:05:56] for watching and see you next time
