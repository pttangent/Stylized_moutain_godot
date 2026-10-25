# AI Built This Space Game From Scratch — Here's Exactly How

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `Z9fyPTQVEdI`
- **Publish Date**: 2026-08-23
- **Duration**: PT17M30S
- **Views**: 50,801 | **Likes**: 1,669
- **URL**: https://www.youtube.com/watch?v=Z9fyPTQVEdI
- **Timestamped Lines**: 155

## Full Timestamped Transcript

[00:00:00] guys today we're going to have a lot of fun I hope Do you see this AI made it And
[00:00:06] it looks terrible But after a week it looks like this In this video I will show you exactly how
[00:00:15] to get from that to this Every step I will skip nothing But first numbers One week four models more
[00:00:22] than 100 agents and I just stop counting And I think that we just use enough power to light a
[00:00:28] small town Like really But I don't regret a single token Before we cook we start with the basics You
[00:00:36] asked for this in the last video so this time I will go deeper My setup is simple I'm using
[00:00:42] Visual Studio Code with three extensions Cloud code Kim Code and Codex And honestly Cloud Code did most of the
[00:00:49] work here We will use Go Engine for the game and Blender for the models and nothing else And during
[00:00:56] this video I'm going to show you how I actually get my agent stuck with Blender and also how I
[00:01:02] work with the God files with my models Okay so how to start And that's a valid question Well you
[00:01:10] need an idea and this one is mine I wanted to create a small science fiction game where you play
[00:01:16] as astronaut on the station and at the end something goes wrong Guys if you like my content just hit
[00:01:23] the subscribe button I would appreciate it So first I wanted a reference So I asked Chad GPT for the
[00:01:31] images and those are the results Based on them we created a color bible But what is a color bible
[00:01:38] Well it's a list of colors and every model must use this It's a contract Otherwise every model could use
[00:01:45] just a different shade of gray and we don't want that Next step the plan Now take your best model
[00:01:51] and just set it to max I will use Fable 5 and it will not build anything It just hands
[00:01:58] out the work and checks what comes back I called it the orchestrator So talk to it first about the
[00:02:04] game and about what you want So you are on the same page After that just ask it for a
[00:02:09] plan So that's my plan and these are the sections Every section has smaller tasks inside That's the rule One
[00:02:17] task should be one fresh session and it must be easy to test So how do you test a game
[00:02:22] with AI I'm going to show you how Ask your model to test it both ways First let it measure
[00:02:28] You just ask it to write a small script The script starts the game and presses the keys just simulating
[00:02:34] the real play test Walks through the hallway tries to open the door etc Then it prints the numbers and
[00:02:41] just check it If character walks if it can reach the door and open it pass or fail Second method
[00:02:47] let it look The same script takes screenshots along the way and then another agent opens them and tells you
[00:02:55] what's wrong For example this room is too dark So combining those two methods you have something like a play
[00:03:02] test And of course the last check is me Okay step one the gray boxes Before we start I wanted
[00:03:09] to make sure that I will get what I want So I talked to Fable 5 what I wanted and
[00:03:13] asked first for a blueprint and this is what I get and it looks correct After that we could delegate
[00:03:19] this task to Opus 5 And that's the prompt Okay guys let's go for a walk So here we sleep
[00:03:28] And that's a corridor and the bridge It looks terrible And I know that it's supposed to look like this
[00:03:34] Now my favorite section a greenhouse We will make it looks stunning I promise And there is an airlock and
[00:03:40] a store So yes Opus 5 delivered its task and it's fully valid Now it will get more interesting We
[00:03:47] want to replace those walls with modular kit from Blender And that's a second section But first how do I
[00:03:54] actually work with Blender And no I'm not using Blender MCP So in a nutshell the model just writes a
[00:04:01] Python script Then Blender runs it headless But how is that even possible Well Blender has a built-in Python interpreter
[00:04:09] So the model doesn't need a mouse at all It just writes a Python file Let me give you an
[00:04:14] example This line of code is a cube in Blender and this piece of code is a small house All
[00:04:20] right So now we can move to our modular walls Blender kit Let's go So here is the plan We
[00:04:27] want to split this wall into modules and then we can build whole station based on those modules Okay So
[00:04:33] here we are in Blender and this is what Opus 5 created for us and this is how it connects
[00:04:39] together But how do we actually get results this good Well we use a method called the gauntlet loop A
[00:04:47] lot of people talk about it lately And instead of building a whole game at once with this method we
[00:04:52] run it on a single task So that's the flow The model that gets the task spans a few agents
[00:04:58] one for each piece And when an agent is done it gives its output to an independent critic who can
[00:05:04] accept it or send it back And at the same time it gets measured against numbers For the wall kit
[00:05:10] that's the dimensions And those kind of sessions sometimes lasts even for a few hours And here before and after
[00:05:16] So it's getting better but still far from good Then we handed the next task to GPT56 Basically work on
[00:05:24] the props So all of the pipes fans and this kind of things on the walls just to make the
[00:05:29] station more detailed Same method as before the gauntlet loop So it will run until it's good And here is
[00:05:35] the result in Blender And this is the station side by side before and after And that's just the start
[00:05:42] guys But Kimik K3 is unemployed so we gave it a completely different task Work on the astronaut's hand so
[00:05:49] we can interact with the world around us So the task was model the hand and the welding torch Nothing
[00:05:55] fancy just point and weld We will keep it for now but honestly I am not sure if it will
[00:06:01] survive Okay the next step is pure pleasure Now we model the rooms for real this time GPD went to
[00:06:09] the engine room Oppus took the bridge the corridor and the greenhouse And for the quarters I sent Kimmy And
[00:06:15] at the same time I broke my own rule I sent Fable our orchestrator to build a room too I
[00:06:21] just wanted to see how they compare Okay so we start with the quarters And that's Kim in Blender Okay
[00:06:28] first thing I see is that everything is so square like the desk and the bed and I'm not super
[00:06:33] happy about it So let's see what Fable 5 did And yes I can see the differences There are much
[00:06:39] more smooth surfaces which is super important to me Let's see how it compares in the game And one thing
[00:06:45] I know for sure I will stick with Fable 5 quarter Second room is the engine room that GPT56 did
[00:06:53] And let's review it directly in the game Doesn't look bad but maybe I will iterate more over it later
[00:07:00] Now the bridge And guys look at this It was done in Blender by Opus 5 and it's really impressive
[00:07:06] Just look at the amount of details here and that's that's the stunning work Maybe you noticed there is already
[00:07:13] a planet out there and that's the completely different story and we will get to it No worries But first
[00:07:19] trees and here I was so surprised I expected simple low poly trees but Opus 5 came back with this
[00:07:26] and it made three versions The first one was almost perfect but look at the leaves and they are just
[00:07:32] triangles The second one has better leaves but the umbrella kind of lost its shape And the third version best
[00:07:38] proportions Look at this one All right let's see how it looks like in the station It already looks stunning
[00:07:45] And the best part is that we have not even touched the final lightning yet Okay a quick one about
[00:07:51] space First Oppus 5 modeled the ship We put it into the void but this planet was made in God
[00:07:58] and looked terrible So I decided to download the only ready-made model in this whole project License free and beautiful
[00:08:07] That's before and after And our ship fits this planet perfectly The next big milestone is the astronaut So first
[00:08:15] we let Opus 5 model it And it came back with four proposals And I took the second one because
[00:08:22] I just like it the most Now the hard part How do you make this guy move And technically we
[00:08:27] could skip it because a lot of firstperson games just don't show the body just show hands But I wanted
[00:08:32] to test what AI can really do So we took the hard way Well usually you do this in Blender
[00:08:38] You build a skeleton you tell the model which part follows which bone and then you record the movement pose
[00:08:44] by pose The game just plays it back But we did none of that What we did is we split
[00:08:50] the guy into 41 separate solid pieces connected by 17 joints There is no skeleton in that file and there
[00:08:57] is not a single animation frame in it Everything you will see this guy is doing is calculated by the
[00:09:03] code in God in every single frame Okay something is wrong here I think bro is just chilling on the
[00:09:10] floor Well he has all the parts but nobody told him what to do So let's take him to the
[00:09:16] lab and teach him how to walk And this is the lab One room one straight line and eight attempts
[00:09:22] Everything you see here is state the walk was really in including the ones that were wrong So that's actually
[00:09:28] super fun to see how it progressed
[00:09:37] And that's a final comparison And I think that it's good enough for now And there is also turning around
[00:09:44] All right let's test it in our spaceship On purpose I changed the camera to third person to see how
[00:09:50] it looked like And it's genuinely good enough I would leave it as it is So approve But we have
[00:09:58] another issue now Do you remember the glove and the welding torch Kim K3 did Yes Now it's a separate
[00:10:04] hand So what we need to do is basically make the astronaut model hand to do everything not a separate
[00:10:10] one And for this one we also had several attempts but finally we were able to get this And I'm
[00:10:17] happy with the result The next big thing was textures And I had a choice Keep assets as they are
[00:10:23] or actually texture the whole station And I went for it mostly out of Curio City So we run a
[00:10:28] few tests First we tried to make them in code straight in God No photos just noise in a shader
[00:10:35] Then I wanted to see how far that is from the real thing So we dropped in a textures from
[00:10:39] Polyheaven and put them side by side And the Polyhaven ones it's not one picture It's color plus a map
[00:10:46] that says where the surface is rough and where it's polished And the one that changed everything for us was
[00:10:51] roughness And the biggest lever isn't texture at all It's how big it is on the wall Same panel wrong
[00:10:57] scale and it reads as concrete Even that polyhaven textures looks really good I decided to keep the project pure
[00:11:03] So we stick with our code generated textures Let's talk about lightning because that's what keep the game it smooth
[00:11:11] Opus 5 prepared a set of presets And on the right there is a panel with every settings behind them
[00:11:17] So I can see what each one actually does We start with a gray box and that's not a dark
[00:11:22] mode That's no lamp on at all This is how the station looked before any lightning work Then we have
[00:11:29] a day It's warm above and cool down at the floor Nothing crazy Night The ceiling almost goes out and
[00:11:36] turns cold and you are walking on the floor strips Maintenance It's the brightest one It's something like I need
[00:11:42] to see what I'm doing light And finally emergency That's my favorite The ceiling goes off completely and red is
[00:11:51] the only color left It looks stunning Then we have a brown out Is the power failing Everything is flickering
[00:11:58] basically And finally blackout but it never goes fully black You are left with a line on the floor and
[00:12:04] the door So after adding all those lights we had a problem and not a small one less than 30
[00:12:12] fps So we started debugging what is causing that and it was obviously the light because switching it off double
[00:12:18] the frames just like that And after some time GPT56 came back with the reason It was shadows Every lamp
[00:12:25] that makes a shadow makes the game paint the whole room again from the lamp side So for my eyes
[00:12:31] it was 600 pieces For the shadows 14,000 So we stopped doing most of that Kept the light and the
[00:12:38] corridor went from 30 FPS to 50 But guys like I said before in this little story something has to
[00:12:45] go wrong And right now there is nothing that can hurt you So we need enemies And I went with
[00:12:50] spiders And not just because they are creepy but because a spider is really a movement problem eight legs and
[00:12:57] every single one of them has to find the floor on its own So it's something you can actually code
[00:13:02] But first Blender Fable gave this one to Kimik A3 who built the first pass of both of them and
[00:13:08] then simply run out of budget So Oppus 5 took it over and finished them Two different ideas at the
[00:13:14] same time left and right And I went with the right one Let's see him in our test scene Um
[00:13:20] okay He can walk already So that's a good start Let's just skip the test room and put three of
[00:13:27] them straight into the game And for the first few seconds it actually looks solid And then well they just
[00:13:33] started flying So I took them back to the lab and the first thing I asked Opus 5 was not
[00:13:39] a fix It was a button one that moves the animal one leg at a time So I can stop
[00:13:44] everything and see what it is really doing And the walking itself is fine The problem is on every surface
[00:13:51] change For example floor to wall wall to ceiling And there the body goes first and the legs just can't
[00:13:57] keep up So Opus 5 started iterating And this iteration is where we stopped And honestly this is good enough
[00:14:04] All right guys Time for the story I wanted to make actually something happen in this small game So the
[00:14:10] story goes like this The meteor hits the ship and our astronaut has to fix the ship from the outside
[00:14:17] At the same time our dangerous and illegal cargo in the lower deck has escaped That's the idea And let's
[00:14:24] just play this All right this is it We are on our spaceship Probably you're wondering where did we get
[00:14:31] those sound effects from Well Opus 5 downloaded everything from um Pixabay free license So that's that's it Okay let's
[00:14:40] go to our greenhouse because I want to I want to see that place one more time Okay if someone
[00:14:48] tell me one year ago that everything here will be built by an AI from scratch I wouldn't believe it
[00:14:54] Trust me Okay let's hit our bridge And there we are Beautiful room
[00:15:05] And that's the meteor hit And we just went emergency mode That's that's a great mode Okay So now we
[00:15:15] probably need to fix the the ship on the outside So we are going to the airlock
[00:15:24] Let's close the door before we turn the wheel
[00:15:32] And yes there we are On the outside we have magnetic shoes so we will just not fly away By
[00:15:39] the way this ladder system was one-shotted by Opus 5 Really
[00:15:48] Okay so that's our welding torch and that's that's the issue So we will just fix it now
[00:15:58] That's the progress bar we have And we need to just do it
[00:16:09] Okay perfect It's done Let's go back to the inside The next task on the list is to check our
[00:16:15] cargo
[00:16:26] And that's the cargo room And we can see that the capsules are broken And those are the spiders I
[00:16:35] mean it is it is amazing I love the animation of those spiders It is really solid
[00:16:46] They will try to catch me now So probably we will just stand here in the corridor and try to
[00:16:50] end this here And here they are One is down Yes he is just levitating here That's the back But
[00:17:01] whatever I literally didn't test this moment before So that's the first time actually And yes I think we cleared
[00:17:11] the corridor
[00:17:17] Let's just torch him Okay so that's our short game Hope you like it If you like the video and
[00:17:25] like the concept and what we are doing here just hit the subscribe button See you
