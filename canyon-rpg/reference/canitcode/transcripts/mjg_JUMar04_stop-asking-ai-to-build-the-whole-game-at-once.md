# Stop Asking AI To Build The Whole Game At Once

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `mjg_JUMar04`
- **Publish Date**: 2026-08-10
- **Duration**: PT6M50S
- **Views**: 239,533 | **Likes**: 8,142
- **URL**: https://www.youtube.com/watch?v=mjg_JUMar04
- **Timestamped Lines**: 62

## Full Timestamped Transcript

[00:00:00] and this video will be different because in this one I'm going to show you how I built this it
[00:00:07] was made in Garat and yes it's not one prompt and I want to show you the whole process how
[00:00:14] I usually work with AI models and I'm using four fable 5 Opus 5 GPD56 Soul and Kim K3 and
[00:00:22] each of those models has different responsibility fable 5 takes the hard calls what we built and why opos 5
[00:00:30] rides the mechanics and build models too gpt56 is my Blender guy sometimes mechanics too and Kim K3 is Blender
[00:00:39] only it has really good feel of aesthetics I noticed so how do you start and that's the hard part
[00:00:46] i had a few of these and I finished none they all looked right but none of them had a
[00:00:52] gameplay loop this one started the same way i was looking at Pinterest and that one scene stopped me and
[00:00:59] I just wanted to make it a game so badly so I made it a reference not to copy it
[00:01:05] to catch the same feeling and we started with a color bible but the picture is daylight and I wanted
[00:01:11] the same place after dark so every color get translated first from now on nothing goes in the game without
[00:01:18] it okay let's make a game do not ask for the whole game in one prompt let the best model
[00:01:24] write the plan every job then gets its own clean session and every job ends the same way a test
[00:01:32] if it fails one job goes back not the game so one job one fresh chat the model is not
[00:01:38] carrying nine other jobs so it reads less and make fewer mistakes it also uses fewer tokens so first job
[00:01:46] on the list the ground i told Fable what I wanted snow deep in one place and thin in another
[00:01:53] fable made a plan and Opus wrote it it starts flat completely flat every corner gets asked one question how
[00:02:00] high are you 110,000 of them 60 times a second you may ask why I do not save the answers
[00:02:07] once because the height keeps changing a boot press the snow down the wind builds a drift up and I
[00:02:14] never asked about the whole map only 120 m of it and it slides along with the character next a
[00:02:20] house some trees and a car these are just placeholders the real Blender models come later then we put snow
[00:02:28] on the ground and remember the ground has a height so the snow can be deep here and thin there
[00:02:35] and now the snow slows you down deep snow you walk thin snow you can run and finally footprints you
[00:02:43] can see where you walked it is a small thing but it makes the world feel alive behind the scenes
[00:02:48] it works like this every step paints into one picture not a list of footprints one image fixed size the
[00:02:56] snow reads it the winds erase it the enemy writes into the same one a thousand tracks cost the same
[00:03:03] as one okay now let's replace those placeholders with real Blender models nobody modeled this house by hand an AI
[00:03:11] model wrote a script blender run it every line adds one piece so when the roof is wrong I do
[00:03:18] not touch the mesh i fix one line and run it again now let's add it to the scene and
[00:03:24] yes it is much better let's do the same with trees and a car okay it is starting to looks
[00:03:30] like a game if you like this video click subscribe button quick tip don't ask AI for realistic meshes it
[00:03:38] will not deliver simple shapes it does well this house is just the boxes and a roof the light does
[00:03:45] the rest and we will work on it in a second but first let's replace a character placeholder with the
[00:03:51] real character and first I wanted to create a concept with GPD so that's the prompt for GPD and those
[00:03:58] are the results and those images goes to mesh AI i like to use that tool for generating a character
[00:04:05] meshes we have 8,000 polygons which is perfectly fine for a main character okay let's texture it and that's fine
[00:04:12] we will map the colors to our color bible later and this time I also decided to use the animations
[00:04:18] from meshi directly and the rigged character looks much more simple and has like less details and a bit different
[00:04:25] colors but as I said we will fix it and it will look perfectly fine in our game and there
[00:04:31] it is our new character is in the game and it looks really really cool now let's just walk around
[00:04:36] oh I love those footprints and the fact that each footprints can have like a different depth and also the
[00:04:42] snow that you feel where it's deep okay so we have the character and we have all of the meshes
[00:04:47] on the map we will play with the light a bit about the lightning it is really helpful to ask
[00:04:53] your AI model to expose you this kind of lightning control panel with those sliders so you can play around
[00:04:58] of course if you can't do that directly in the game engine for example go do so here I have
[00:05:03] few presets each of them reflects a different daytime so let's play along this one is like a flat then
[00:05:10] nightfall and you can see how much this scene changes deep night which is a bit bit lighter and a
[00:05:16] white out blizzard a lot more density of the fog and the sunrise i love this one it is really
[00:05:22] warm here and then pale day um midday so you can see how much the same scene differs based on
[00:05:32] the lightning settings and I love this that you can affect the game a lot this way and now the
[00:05:38] enemies i want a very few of them but every meeting should be able to kill you right now there
[00:05:43] are two a starving man and bears i found the bear on Sketch Fab with CC attribution and a lot
[00:05:49] of animations so I downloaded it but the bear is realistic here and we need more low poly models so
[00:05:54] I asked AI to decimate it in Blender and here you can see a three stages of decimation and decimation
[00:06:01] simply reducing a polygon counts the man sees you the bear smells you on the wind this part is still
[00:06:08] a prototype you press F and the gun finds the target the bear you cannot outrun ever so it warns
[00:06:15] you first and then it charges it knocks you down and for now you just lie there last thing I
[00:06:22] want to show you the house interior it's not a different location it's the same one so player sees the
[00:06:27] danger outside the house how does it work simple the moment I step inside the roof and the front wall
[00:06:33] come off that's it but there is also another system when our character goes behind some object for example a
[00:06:39] tree then the whole shape fades out how the camera shoots array at me all the time and that's it
[00:06:46] guys if you want more deep dive videos let me know in the comments
