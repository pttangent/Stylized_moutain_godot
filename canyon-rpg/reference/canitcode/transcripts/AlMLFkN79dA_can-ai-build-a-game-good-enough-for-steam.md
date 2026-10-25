# Can AI Build a Game Good Enough for Steam?

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `AlMLFkN79dA`
- **Publish Date**: 2026-09-18
- **Duration**: PT8M21S
- **Views**: 180,332 | **Likes**: 3,609
- **URL**: https://www.youtube.com/watch?v=AlMLFkN79dA
- **Timestamped Lines**: 75

## Full Timestamped Transcript

[00:00:00] all right we are making a brand new series and I'm super excited about this one my brother and I
[00:00:06] are making a game and the plan is to take it all the way to Steam what you are seeing
[00:00:12] on the screen right now is what we have built so far and there is still a lot to do
[00:00:17] but we are going to turn this into a full polish indie game and bring you along for the whole
[00:00:22] process we will be trying different AI models and tools like building the world creating assets figuring out animations fixing
[00:00:29] bugs making optimization basically working through everything it takes to finish and release a game and we've already found plenty
[00:00:37] of interesting things i want to show you what AI can help with where it struggles and how much work
[00:00:43] still goes into making something good you will see the experiments the mistakes and all of the little changes that
[00:00:49] actually make a difference and as I said I'm building this with my brother so we will be splitting the
[00:00:55] work and figuring things out together he has his own channel too i will put it on the screen and
[00:01:00] leave a link below go check him out so let me tell you a little about the game i've always
[00:01:06] wanted to make a game inspired by a place I actually know and like and I live in Poland not
[00:01:13] far from a mountain range called the Besuit it's a beautiful place and that's where the inspiration for this world
[00:01:20] comes from the forests the little mountain roads the wooden houses i want to bring that atmosphere into the game
[00:01:27] even the trees and plants should you know feel like they belong there which brings me to the first thing
[00:01:33] I wanted to start the concept okay so what the game's actually about so we are making a survival game
[00:01:40] set in baskets here in Poland we want to recreate parts of the real landscape including recognizable places and bring
[00:01:47] some of the local legends into the game the atmosphere should feel mysterious with a sense that something dangerous might
[00:01:54] be out there and will be and we want to give a room for exploration instead of pushing through a
[00:02:00] complete linear story the story itself is still taking shape but we already have three things we want to build
[00:02:06] around exploration survival and mystery one thing I haven't mentioned yet we are building this in Gat why well it
[00:02:14] fits this kind of stylized top-down game we are making and it works really well with our AI work and
[00:02:22] I'm not using a Gad MCP server my agents work directly with the project files scripts scenes shaders and many
[00:02:29] more resources are stored as a plain text so the agents can read and edit them directly then we run
[00:02:36] the game check what actually works and iterate so to start turning that idea into an actual world I started
[00:02:44] with the vegetation i had AI agents research which trees and bushes are common in the area we picked a
[00:02:51] few and then I put the GPT6 Astra to work in Blender in a loop of modeling checking the results
[00:02:57] and making improvements so-called gauntlet loop a few hours later I had this whole gallery of trees and bushes and
[00:03:05] individually they looked pretty good but once I put them together in a scene I realized the style wasn't quite
[00:03:12] right they felt just too generic too realistic for the game I had in mind i wanted something more stylized
[00:03:19] so I went back to GPT we explored a few visual directions and generated these reference images and this was
[00:03:27] much closer to what I wanted we run another modeling loop this time with just three trees a small test
[00:03:34] to see whether the style would actually work in 3D and yes this fit the game so much better of
[00:03:41] course getting the look right wasn't the whole job these trees also had to run in an actual forest the
[00:03:48] first birch had over 34,000 triangles and that's fine for like one model but it adds up quickly when you
[00:03:54] start fitting the scene so we baked groups of leaves into color and normal textures and put those onto planes
[00:04:02] the trunk and main branches stayed in 3D and that brought the birch down to about 2800 triangles and the
[00:04:10] maple to about 1,500 we kept the overall shape and style with much lighter models and this became the starting
[00:04:17] point for the grass technique you will see in a moment with trees looking much closer to what I wanted
[00:04:23] it was time to build a proper test scene something that could actually look like the final game or at
[00:04:29] least close enough to see what we could achieve with this workflow so the next piece was the road the
[00:04:36] idea is to have a narrow trails you explore on foot and wider roads you can drive along in a
[00:04:41] off-road vehicle for this first scene I started with the second one a deer road winding through the forest and
[00:04:47] yes it went through a few iterations i wanted the deer to be procedural without relying on a real scans
[00:04:54] so we worked on the surface the wheel tracks and the shader details then we added small stones and gravel
[00:05:00] on top and yes there is still room to improve it but for this first test I think it's pretty
[00:05:06] cool then came the grass and this one was tricky to get right we started with simple grass meshes repeated
[00:05:13] across the scene using God's multi mesh performance was fine but I wasn't happy with the look so we just
[00:05:19] added more grass more coverage like bigger clamps and it still felt like a bunch of objects sitting on top
[00:05:26] of the ground it like didn't really blend in so I suggested trying the same idea we used for a
[00:05:31] trees a painted grass textures on a few simple planes and yes the textures give us all those thin curved
[00:05:38] blades with the actual geometry stays really simple and once we put that into the scene yes this looks so
[00:05:46] much better it finally feels like a part of the forest floor it was just softer and much closer to
[00:05:52] the style I wanted honestly I think it looks awesome next came the smaller props mushrooms tree stumps fallen logs
[00:06:00] rocks all of those little things that just lie on the forest floor for this patch I used Opus 5
[00:06:06] to create a bunch of small low poly assets then I spend some time on the lightning for now I'm
[00:06:12] just sticking to one time of the day and one lightning setup we will for sure expand that later and
[00:06:18] I played around with the lights and colors and this is the look I've settled on the first pass and
[00:06:25] here is a small settings that made a huge difference sorry by the way the panel is in polish this
[00:06:31] slider controls shadow softness when I push it all the way up watch the frame rate from over a 100
[00:06:38] to around 40 and that's more than half the FPS gone now let's bring it back up and we're back
[00:06:45] above 100 softer shadows takes extra GPU work so it's a trade-off between the look and performance here it is
[00:06:53] our first proper test scene honestly I like it it has this you know autumn feeling I was going for
[00:06:59] and everything is starting to fit together but obviously it's not polished and it doesn't feel like in the mountains
[00:07:06] yet because the terrain is flat so that's the next step since we are building a game inspired by a
[00:07:12] real place I wanted to start with the actual shape of the landscape so we downloaded elevation data from Poland's
[00:07:19] geoportal and used open street maps for things like roads and streams the elevation data is basically a grid of
[00:07:25] numbers think of an image except each pixel stores a high instead of a color we use those heights to
[00:07:32] leave the points of a flat grid then connect them into triangles and that's how the real hills and valleys
[00:07:39] become our terrain for this roughly 8x8 km area the height data alone takes up about 2 and 1/2 mgabytes
[00:07:47] we also keep our changes separate from the original data so we can reshape things like roads without losing the
[00:07:54] real landscape underneath i'm still not sure how big the map will be so that's like the first approach so
[00:08:01] now we have the real world terrain data the next step is to turn it into a playable landscape with
[00:08:07] the same style and atmosphere as our first testing but that and much more is coming in the next video
[00:08:15] thanks for watching see you in the next one
