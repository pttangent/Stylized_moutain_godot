# Is This Really AI? Insane Opus 5.5 GameDev Workflow

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `XqtnBlPJ6KE`
- **Publish Date**: 2026-10-14
- **Duration**: PT11M1S
- **Views**: 43,395 | **Likes**: 805
- **URL**: https://www.youtube.com/watch?v=XqtnBlPJ6KE
- **Timestamped Lines**: 103

## Full Timestamped Transcript

[00:00:00] hey guys look at this a city at night with neons everywhere you've got a tourist that shoot for you
[00:00:07] a rocket launcher a shop where you can just smash everything doors you open with your own hands and a
[00:00:13] whole swarm of bugs that hunts you down and here is the crazy part all of it was built with
[00:00:19] Opus 5.5 in God engine so in this video I will show you some crazy workflows step by step what
[00:00:26] we tried first and what didn't work by the way guys let me know in comments if you want me
[00:00:31] to build the same game in Unreal Engine so we can compare the results so in my last video Oppus
[00:00:37] 5.5 built this a cyber punk shooter inside a giant cube where every wall is a street and honestly I
[00:00:44] really like it the movement the hands the gun it just felt really good so I said "Okay let's take
[00:00:51] the player out of the game and see how far Obus 5.5 can take it." Everything you see here will
[00:00:58] land on my Patreon right here and here is the idea a city even denser than Tokyo you know narrow
[00:01:05] streets and stairs everywhere a dead giant right in the middle of it and it's bugs crawling all over the
[00:01:11] place and here is how we work opus 5.5 built everything gpt6 Astra generates the pictures like the ideas and
[00:01:20] Triple made some smaller more detailed 3D models and me well I gave ideas and directions and of course did
[00:01:28] a testing and trust me that's a lot so we started with a plan a drawing of the whole street
[00:01:34] from above like a level planning then Opus made a street with simple grid blocks from a player's eyes just
[00:01:41] to feel how big everything is then GPT generates the look right on top of these blocks and it got
[00:01:48] back with three different looks i picked this one because that's exactly the mood and look I wanted dark wet
[00:01:54] and full of neons okay so the idea is to make a whole city of wall pieces that snap together
[00:02:00] kind of like a Lego but who should build these pieces well I tried three different ways of the same
[00:02:06] piece first Tripo that turns GPT's picture into a 3D model second is Blender where Opus writes a script that
[00:02:14] builds it part by part and the third one a blender again but this time with GPT is generating a
[00:02:20] textures on top of it and from far away they all look pretty much similar right but get close and
[00:02:26] you see piece looks great and it was the fastest by far but look this air conditioner is almost a
[00:02:33] meter of the wall and yes we could still build the whole kit this way but then Opus has to
[00:02:39] fix every piece afterwards the scale the sizes the grid and we have way less control over the final look
[00:02:45] because it's all painted into one texture the second approach Blender has perfect shapes but it's dirt is made by
[00:02:52] code so it looks way too clean and the third one has both the exact shapes from Blender and the
[00:02:57] real dirt from GPT's drawing so guys Blender with the GPT drawings wins so that's our rule from now on
[00:03:05] every wall piece from Blender with the GPT textures and triple only for the small details okay so let me
[00:03:12] show you the workflow how one of these pieces is made first GPT generates it we give it a prompt
[00:03:18] like one piece of a building a shop at the bottom a window and air conditioner on top and it
[00:03:24] generates exactly that then Opus 5.5 writes a script for Blender and here is the cool part the script measures
[00:03:32] GPT drawing every part goes exactly where GPT painted it and Blender builds the wall part by part and the
[00:03:38] textures well I don't want any textures from the internet so GPT just generates them we ask for something like
[00:03:45] a 1 m patch of old gray concrete with small holes and chips and that's exactly what we get but
[00:03:52] there is a problem a picture like that has edges so if you put two side by side you see
[00:03:57] a line so Opus made a small script that moves a copy by half so the edges meet in the
[00:04:02] middle and blends the two together and now it's seamless and from the same picture the script also makes the
[00:04:09] bumps and the shine so the concrete catches the light like a real one then we did tiles and shutter
[00:04:15] the same way and the dirt well the script puts GP's drawing over a clean wall and everything that's darker
[00:04:21] than clean well that's the deer then it all goes on the wall first the textures then the deer on
[00:04:27] top like from a projector
[00:04:32] and then finally Opus 5.5 built the whole street from pieces like this and that's crazy right but look the
[00:04:40] pipes didn't join there were gaps everywhere so I said I want to be sure they always join so Opus
[00:04:46] writes a quality test a test breaks things on purpose 11 times and it catches every single one so I'm
[00:04:53] sure it works and of course there is more stairs galleries a bridge and a bot that walks all of
[00:04:59] it up to the roof just to check you can really get everywhere okay now you go up these stairs
[00:05:05] and up on the roofs there was nothing so I wanted to camp up there where the survivors live and
[00:05:12] I wanted to make these assets with triple and that's 18 new things like a tarp a stove a generator
[00:05:18] and sandbox and more in the browser that's 18 times the same clicks upload the pictures set it up wait
[00:05:24] download so this time OPU 5.5 used triple CLI and that's triple in the terminal it writes just one file
[00:05:33] every prop with its pictures and its settings the same for all of them the pictures of course come from
[00:05:39] GPD every object from the front the side and the back and then it's just one comment and guys look
[00:05:45] at this six models at the same time and they just keep coming back one after another 18 models in
[00:05:51] about 10 minutes and I didn't click a single thing and because it's all text Opus does the rest by
[00:05:58] itself it checks every model make it their real size give its collision and puts it in the game and
[00:06:04] at one point my own script got stuck but the batch just picked up where it stopped and nothing got
[00:06:10] paid twice and yes it's not perfect though i asked for 3,000 faces and got more than 5,000 and four
[00:06:17] models came back facing backwards so Opus looks at everyone from four sides and turns it around and here is
[00:06:24] the camp warm lights a stove a lookout over the street a bridge to the shop's roof and if you
[00:06:30] shoot the gas bottle well the explosion okay Triple CLA is free to install and if you subscribe to Triple
[00:06:38] Pro you get 1,000 bonus API credits and 10% off all your future API top-ups and if you sign up
[00:06:44] with my link you get 500 credits for free the link is in the description next is the lightning and
[00:06:52] I wanted to iterate a bit more over it because it's super important so this is how it looked at
[00:06:57] first like everything was orange the whole city was one big street lamp so I gave a screenshot to GPT
[00:07:05] and look at this gpt generates the image and it looks much better so Opus checked why and well there
[00:07:12] were around 50 orange lamp and every wall had the same color so there was nothing for your eye to
[00:07:17] catch so it fixed that and yes it was better but still not quite what I wanted i wanted neon
[00:07:24] wet street and the ground like a mirror so we iterated around by round and the few rounds it finally
[00:07:32] looked really good
[00:07:35] and the idea was that in this city no door is closed you can go in anywhere and the first
[00:07:41] shop was so flat and tiny and the fridges were just boxes like primitives so Opus rebuild it way bigger
[00:07:48] with the real glass and thousands of things on the shelves and the doors i said I want hands because
[00:07:55] a door that just slides open by itself feels fake so now your hands really do it
[00:08:03] and everything breaks the glass the bottles and let me quickly show you how and this is Jolt a physics
[00:08:09] engine the same one they used in Horizon Forbidden West and now it's built right into God so when a
[00:08:15] bullet hits the glass the game cuts it into pieces around the heat and Jolt throws away piece along the
[00:08:21] shot same with shelves one bottle falls and it knocks down the one next to it and now the bugs
[00:08:27] at first I wanted a lot of them like hundreds a big swarm with one brain so first we had
[00:08:33] this ant and Opus gave the whole swarm one brain it's like one big map of arrows they all point
[00:08:39] the shortest way to you around the walls and up the stairs and every bug just follows the arrow under
[00:08:45] its feet but honestly I wasn't happy with it it wasn't polished and hundreds of small ants just looked bad
[00:08:52] together so I changed the approach i didn't like that ant either so we made new models in Tripo and
[00:08:58] Opus wrote the walk-in code the legs move into groups like a real insect three feet stay on the ground
[00:09:04] and the other three step forward a foot on the ground never slides and the next step starts when the
[00:09:09] body has gone half a step so a faster bug takes a bigger steps and instead of hundreds now there
[00:09:15] are just a few thousand at most each one has its own brain but they all want the same thing
[00:09:21] you so they come from different sides some sneak around to your back and they never just come at you
[00:09:26] in a line so what do you fight with them a tourets put one down and it shoots them for
[00:09:32] you and a rocket launcher and as I said it has to look cool like in the big games so
[00:09:37] first we look at the real explosions frame by frame and the fire last only a tenth of a second
[00:09:43] then it's all dark smoke and dust then GPT painted the pieces the fire the smoke the dust and the
[00:09:49] first dark burst like photos on the black background his script cut them into texture for the game and Opus
[00:09:55] made them move layer by layer the flesh the fire the smoke the dust and the debris and then we
[00:10:01] put ours next to the real one and fixed it until it matched but up close it still looked kind
[00:10:07] of fake because GPT's pictures don't move they just grow and fade so we tried something else cidance made a
[00:10:15] short video of a real looking explosion on a black background and the script cut it into 64 frames so
[00:10:22] now the fire and the smoke really move look at this before and after that's a huge difference and now
[00:10:29] it looks as an explosion
[00:10:34] and then I said "One street is not enough let's just build a whole small city because we already have
[00:10:41] models so it should be fast." So we did it and also GPT generated the new glowing signs over a
[00:10:47] hund of them so every street looks different and in my opinion this city looks great
[00:10:56] and that's it for today thanks for watching and see you in the next one
