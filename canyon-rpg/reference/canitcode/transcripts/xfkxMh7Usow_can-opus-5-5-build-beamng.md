# Can Opus 5.5 Build BeamNG?

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `xfkxMh7Usow`
- **Publish Date**: 2026-10-12
- **Duration**: PT5M38S
- **Views**: 64,710 | **Likes**: 1,072
- **URL**: https://www.youtube.com/watch?v=xfkxMh7Usow
- **Timestamped Lines**: 54

## Full Timestamped Transcript

[00:00:00] hey guys in this video we're going to break some cars well actually just one car a Honda Accord 8
[00:00:07] and we're going to test how far Opus 5.5 can go with car destruction starting with simple dance and ending
[00:00:14] at beamg level and that's actually super fun so stay till the end we will be using God as a
[00:00:19] game engine okay so every game breaks cars in a different way most racing games only dent the outside where
[00:00:26] you hit but for the physics the car is still one block gta goes one step further the doors the
[00:00:32] hood and the bumpers can fall off reckless though uses a soft body for damage so you get a dent
[00:00:38] right where you hit and then there is a beam every car has a hidden skeleton of points and beams
[00:00:44] so it bends and breaks a lot like a real car and today Opus is going to try all four
[00:00:50] ways one by one so first I knitted the car and I chose European Accord from 2008 in white pearl
[00:00:57] so GPT generated a reference image from front side and the back i put these pictures into triple and this
[00:01:04] came back and honestly that's a pretty good accord but here is the thing a real car is not one
[00:01:10] piece of metal so Opus found the lines between the doors the hood and the bumpers which were just painted
[00:01:15] on the texture and it cut the body exactly along those lines and it filled the inside too because when
[00:01:21] the hood flies off you want to see an engine under it not an empty box then we needed a
[00:01:26] place to crash it so Opus built a test truck in the forest with a long road a big concrete
[00:01:32] wall a pole a tower that drops a heavy block on the car and a warm garage for the cars
[00:01:37] everything was done in Blender all right so let's start easy level one the cheap trick from the most racing
[00:01:43] games at 30 you get a small dent at 80 a big one so it grows with the speed two
[00:01:49] cars front to front or a drop from 15 m and every time it's the same thing at the end
[00:01:54] and that's it so how does it work for the physics the whole car is basically one solid block and
[00:02:01] that's why it just stops at the wall like a brick because the block inside never changes only the look
[00:02:07] of the car changes level two parts that fall off like in GTA so at 64 the bumpers flies off
[00:02:14] and the hooded jumps up and at the pole the doors just open front to front the bumpers fly everywhere
[00:02:21] and from 15 m the front bumper just falls off so how did Opus do it every part has a
[00:02:27] broken copy that was made before the crash like in the old GTA games and a hook that can break
[00:02:33] and it looks great but the broken parts are made before the crash so the car can only break in
[00:02:38] the ways we made in advance level three soft body so this is our own soft body the same idea
[00:02:45] as in Reckfest the front really gets pushed in and it stays like that and dropped from 15 m the
[00:02:52] front gets pushed in and the car falls back on its wheels so how does this one works around the
[00:02:57] car there is a net of 400 points every point wants to go back to its place but if you
[00:03:03] push it too far it just stays there and that's your dent and this one took a few tries the
[00:03:09] first version jumped back of the wall way too hard okay so what's the difference between this and beng because
[00:03:16] honestly it already looks pretty convincing but hit it from the side into a pole in our soft body the
[00:03:22] pole goes deep inside the car right where you see it and in our BMG level the door stops it
[00:03:28] because our soft body is only the outside of the car it's empty inside so nothing stops the pole b&g
[00:03:35] puts a skeleton inside the whole car and that's level four so finally level four the beamg level 64 into
[00:03:43] the wall and now look at the front it pulls like a real car so how does it actually work
[00:03:49] our car gets a skeleton hundreds of points and 1,700 beams so long parts in the front post that hold
[00:03:56] the roof the floor and the doors that can open every beam can bend and stay bent or just break
[00:04:01] and the painted car sits on top of all that now watch the front the bars falls one after another
[00:04:07] but the part where you sit stays almost the same and that's exactly how real cars are made and the
[00:04:13] real crash test do this too only one side of the front hits and the whole car turns around the
[00:04:18] corner and here is the pole again the beams in the doors stop it and the inside of the car
[00:04:24] stays in one piece okay and now the fun part two accords front to front both at 50 and look
[00:04:32] both of them fold and nothing goes through the other car and what if we drop it from 15 meters
[00:04:40] well the whole front falls like a can and the car just falls back onto its wheels and now all
[00:04:46] four levels side by side the same crash at 64 front to front so four ways to break a car
[00:04:54] and only one of them breaks it like a real car it's also the hardest one for the computer so
[00:05:00] Opus rewrote it in a faster language so is it close to the real thing well let's compare it with
[00:05:08] the real crash recording same speed same wall the real front got about 70 cm shorter and ours 72 that's
[00:05:16] That's pretty close but to be fair Opus knew the real number when it build the car so can Opus
[00:05:22] 5.5 build BNG well not the whole game of course but the most important part the crash well yes and
[00:05:28] it's really close to a real crash test the card the track and all the code will be on my
[00:05:33] Patreon so you can crash it yourself see you in the next one
