# I Stole a Mountain for My Game

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `78diFcn3Qas`
- **Publish Date**: 2026-09-24
- **Duration**: PT6M43S
- **Views**: 41,413 | **Likes**: 1,081
- **URL**: https://www.youtube.com/watch?v=78diFcn3Qas
- **Timestamped Lines**: 63

## Full Timestamped Transcript

[00:00:00] all right welcome back as you know we are making a game and the plan is to publish it to
[00:00:05] steam last time we got quite a lot done we built our first scene created vegetation grass and some smaller
[00:00:12] props and of course worked on optimizing the trees and other assets we also downloaded real terrain data from geoportal
[00:00:20] for a place here in the polish mountains the baskets but today we start with a character because well someone
[00:00:27] has to walk through all of this then we will get into the trails the asphalt road the river and
[00:00:33] the clearing and by the way we are almost at 10,000 subscribers so if you want to follow the game
[00:00:39] subscribe to the channel before we start a lot of you asked how i make assets like these trees so
[00:00:45] here's my workflow it's actually pretty simple first i talk with gpt about the style i want it generates a
[00:00:52] few reference images i pick the best one or we keep iterating once i have a game image i like
[00:00:57] with trees i like i ask gpt for just one of those trees on a plain background and that's my
[00:01:03] reference then that reference goes to the strongest model like opus 5.5 or gpt6 astra and i don't use blender
[00:01:10] mcp the model just writes a python script and runs it in blender in the background wider crown thinner trunk
[00:01:17] change a few numbers run it again and it's all code so it goes into git a version control system
[00:01:24] and it works in a gauntlet loop one critic agent compares the render with the reference and says pass or
[00:01:30] fail fail means another round with a list of fixes pass and it's my turn to judge and that's how
[00:01:37] we get trees like this okay now we can move to the character first the character so we made the
[00:01:43] model with tripo and got the animations from mixamo but now we need these animations to work together for this
[00:01:50] stage i've mainly been using gpt6 astra in the codex extension in visual studio code usually on extra high or
[00:01:58] ultra so i asked codex to put these animations together in god and i want to show you something without
[00:02:04] blending it just switches between them i start walking he walks i start running he runs action switch action switch
[00:02:12] it works but the change is pretty sudden so i asked astra to blend the animations and god has something
[00:02:19] called an animation tree that lets us do that basically instead of switching straight from walking to running we mix
[00:02:26] the two animations and he speeds up we get less walking and more running and when he slows down it
[00:02:33] goes the other way now look at the difference it's much smoother i also wanted the turns to feel more
[00:02:39] natural and that's the separate change to how the character moves instead of changing direction right away he follows a
[00:02:46] smooth curve and the animations keep blending while he turns okay so where is he actually going to walk well
[00:02:54] the mountains are real the shape comes from geoportal and open street map tells us where all the roads streams
[00:03:00] and forest are for now we build it in small test scenes one place at a time so today it's
[00:03:06] a mountain trail a forest road with the river and a clearing so first the trail i gave the agent
[00:03:12] our road scene as the reference so keep the trees the grass and the light but change the ground into
[00:03:18] a real mountain trail so a bank going up on one side and a drop on the other and the
[00:03:24] trail has its own rules like what grows on the bank what goes under the trees and where we leave
[00:03:29] space to walk but the rocks took a few tries and this one is just a floating above the bank
[00:03:35] so i just open the scene in the code editor and fix one rock myself wider flatter and just blend
[00:03:42] it in the bank and then i told the agent okay do the other rocks just like this one so
[00:03:48] show an example say what should change and what should stay and this approach works really well next the road
[00:03:55] and it follows the real route from our map in god this route becomes a spline which is basically just
[00:04:01] a smooth curve the agent wrote a blender script for one short straight piece of road and then god just
[00:04:08] repeats this piece along the curve and bends it to feed the ground and the ground is a real terrain
[00:04:14] so we never touch it directly the road sits on top so we can make it wider or move it
[00:04:19] to the side and the ground just follows we also added some decoration on the sides like leaves and right
[00:04:25] next to the road there is the river and honestly this river is my favorite part of the game so
[00:04:31] far and here is the fun part the game doesn't calculate any of this water while you play so how
[00:04:37] does it work well first we cut the empty river bed into tiny squares like a chessboard and each square
[00:04:44] only needs to know two things how deep the water is and which way it's going then we pour water
[00:04:50] in at the top and let the computer work out square by square where the water goes and look it's
[00:04:56] fast over the steps slow in the pools and it goes around this island just like a real river to
[00:05:02] check it we started a completely dry river and the water ended up in exactly the same place as in
[00:05:08] the game and it only takes about a minute then we save it into one small file and the game
[00:05:14] just reaches so it costs almost nothing while you play on top of that we just paint the water so
[00:05:20] the surface the little waves and the color even the foam follows the same current so it flows exactly where
[00:05:27] the water goes the waterfalls are a different trick the water just falls off the edge like a ball rolling
[00:05:33] of a table and it took us few tries look at the first one it was really bad but the
[00:05:38] last one is okay and when our character walks in the water goes around his legs and when he walks
[00:05:44] out he leaves wet footprints that slowly dry honestly i really like this part and finally a place where the
[00:05:53] forest opens up a bit it got some new props like the middle mushrooms made the same way as the
[00:05:58] trees at first there was a puff in the middle so i asked the agents to remove it and just
[00:06:03] let the grass take over and i wanted some mist to the ground so these are small patches of fog
[00:06:09] that slowly move around it's quiet but a little bit of mysterious like a place where you just stop and
[00:06:16] look around so that's where we are now three places in the mountains and next we need to connect them
[00:06:22] all together but the next episode is something i'm really excited about we took ai videos of animals and turned
[00:06:29] them into a real animations for the game and honestly for us it's a big breakthrough let me know in
[00:06:36] the comments which part do you want to see more thanks for watching and see you in the next one
