# GPT-6.1 Sol Is So Weird

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `U0AlQd5pdvw`
- **Publish Date**: 2026-09-30
- **Duration**: PT7M8S
- **Views**: 110,646 | **Likes**: 919
- **URL**: https://www.youtube.com/watch?v=U0AlQd5pdvw
- **Timestamped Lines**: 64

## Full Timestamped Transcript

[00:00:00] okay guys crazy times Two new models in two days from two competing companies We've got clothes onet 5.5 and
[00:00:08] GPT61 Soul in case I have no idea how but Sonet is actually head of Opus on Terminal Bench Like
[00:00:15] what the heck and on automation too OPUS still leads the overall index but Sonet is really close And Soul
[00:00:21] is just fine Now look at the prices $2 for input 10 for output per medium tokens That's both set
[00:00:28] and soul Opus cost twice that So yeah I'm really curious now So obviously we have to test this I'm
[00:00:35] putting all three on the same dungeon crawler project First they have to build the dungeon in Blender then make
[00:00:42] the character and animations and finally get all of it as a game in Ga Let's see if they can
[00:00:48] pull it off Oh and finally I launch a Patreon If you join you get the source files from my
[00:00:53] YouTube videos This episode's files are going up there too like this dungeon kit from Opus Grab the files mess
[00:01:00] around with them Link is in the comments just not the Steam game series Those source files aren't included but
[00:01:06] yeah if you join thank you All right enough talking Let's see what they can actually make Before we compare
[00:01:13] anything look at the reference This is the vibe I wanted A really stylized stone heavy shadows and cold water
[00:01:19] against the warfire Okay first up Sonet And honestly this is really good I like how rough the stone looks
[00:01:27] and those warm lines against the water It actually has that dungeon feeling kind of and compared with the reference
[00:01:34] I would still make everything a bit more stylized but that's a really good start And now soul And I
[00:01:40] don't know guys this one feels just a bit flat to me The layout is there Yes you can read
[00:01:46] everything but it doesn't have like the same atmosphere Look at those clean surfaces For this reference it's the least
[00:01:53] stylized of the three And here is Opus Yes And this one is the closest to the reference for me
[00:01:59] The shadows the stone the whole room has more character and the lightning is really good Sonet is really similar
[00:02:06] but Opus gets that heavy kind of stylized look a little better This feels much more like the dungeon I
[00:02:12] had in mind But guys there is a massive catch here at API prices Souls run comes to less than
[00:02:19] $4 and I have no idea how Sonet is about 165 Oppus is above 200 and Soul finished in 80
[00:02:27] minutes The others took almost 5 hours So yeah flatter results but way way cheaper and way faster So I
[00:02:34] went back and checked this because $4 sounds really suspicious And Soul made a 137 model calls Sonet 1670 and
[00:02:44] Sonet calls carried over four times as much context on average So guys just the cash reads cost Sonet about
[00:02:51] $114 and GPT $1 So yes fewer calls less history way less money That's what happened in this run and
[00:03:00] that's crazy Okay let's talk about solution itself Look at this wall for a second Let's pull it out There
[00:03:07] is no image textures on the wall These stones and all those little faces are actual geometry Then the AI
[00:03:13] code gives the faces different colors A bit lighter here darker there See the dark band near the bottom yes
[00:03:19] that's part of the color too Now bring back the lightning and put it back in the dungeon Pretty cool
[00:03:24] right and GPT soul does it differently Still no image textures And here is its wall Instead of storing the
[00:03:31] colors on the mesh it scripts makes 12 stone materials Then it assigns those materials to different faces Same idea
[00:03:38] visually and different way of building it The shape colors and lightning still makes the final look But guys how
[00:03:44] did we get such nice results let me quickly show you the workflow There is no Blender MCP here The
[00:03:51] models write Python scripts and run Blender headless Then it's a gaunt loop One agent builds one critic checks the
[00:03:58] result The agents gets the feedback fixes the problems and run it again And one more thing guys the model
[00:04:05] decides when it's done GBT could keep iterrating but it chose to hand over That was its goal Complete freedom
[00:04:12] All right round two characters And we are going for four here A knight a skeleton warrior an AC slime
[00:04:19] and a giant cave bat Everything was made from scratch in Blender The models the rigs the animations I allowed
[00:04:26] to mix or simu but none of the models use them So let's review a few animations First Summit guys
[00:04:33] Considering that it was all built from scratch in Blender it's actually really good I love how the bones fall
[00:04:40] apart when the skeleton dies And that's the slime walk and the flying bat And that's really nice bat So
[00:04:46] Sonet did a great job Now let's put all three side by side First the knights Okay so Sonet and
[00:04:52] Opus are pretty much tight but Soul is so wooden actually And the dead animation is so bad Same with
[00:04:58] the skeletons Sonet Opus looks good same level Soul still moves like an action figure The slimes are actually pretty
[00:05:06] even though And the bats those are close too All right so characters are done Now the most important part
[00:05:13] combine everything and give me a small playable game We start with Opus and Opus is simply pleasant to play
[00:05:20] The combat has good feedback the run animation is good the monsters looks nice and the whole scene is just
[00:05:26] very well done The only thing I would change is the water because in the game it never looks the
[00:05:31] way it did in Blender Okay now Sonet And this one is a big surprise The scene is also really
[00:05:37] good The fighting holds up It has the same water problem as Zopus but overall it did a great job
[00:05:43] And for me it is the big surprise of this episode And then there is Assol Honestly every round got
[00:05:49] worse The blender scene was still fine even if it was not good as the others The characters were much
[00:05:55] more blocky than its rivals And once they move in the game you can really see the difference And the
[00:06:00] special attack is pure hoodini The knight sinks into the floor and pops up somewhere else Amazing Now a quick
[00:06:07] side note on why some games feel much better than the others It is feedback Here is one sword hit
[00:06:13] from Opus game with every layer switched off and then added the back one at a time
[00:06:28] So to sum it up three models build the same thing A dungeon in Blender then a hero and three
[00:06:34] monsters then a real small game made only from their own stuff Sonet surprised me with its quality but it
[00:06:41] wasn't cheaper Its price per token is half of Opus but it used so many more tokens that the final
[00:06:46] bill was almost the same And Soul is the other way around Much worse at making games but really cheap
[00:06:53] Just a small part of what the other two costs Funny thing is that the previous Soul 5.6 was more
[00:06:59] or less on the level of Opus 5 And that's it for today If you like the video comment like
[00:07:04] and subscribe Bye
