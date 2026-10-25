# AI Can Now Animate Any Monster. Opus 5.5 Built the Tool

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `AS92HYsEBqo`
- **Publish Date**: 2026-10-17
- **Duration**: PT9M19S
- **Views**: 104,026 | **Likes**: 2,224
- **URL**: https://www.youtube.com/watch?v=AS92HYsEBqo
- **Timestamped Lines**: 95

## Full Timestamped Transcript

[00:00:00] hey guys have you ever tried to add a cool creature to a game you make with AI something that
[00:00:06] moves like in AAA games and every time the AI tried to animate it in Blender or anywhere else it
[00:00:12] was just bad well what if I told you I found a way to fix it and to animate any
[00:00:18] creature I want for people is easy you have motion capture Mixamo Kimodo because there are a huge databases of
[00:00:24] real people moving so AI has plenty to learn from but for a dragon a troll or anything with a
[00:00:31] strange body there is no database like that so there is no tool like that either not yet at least
[00:00:36] nothing public and I bet it's coming soon my way is honestly a bit crazy but look at this a
[00:00:44] brand new monsters the lizard and the raid and not a single frame was fixed by him and it works
[00:00:50] for any kind of creature four legs two legs wings a tail a sword and if you watched my previous
[00:00:57] videos you know I've been fighting with this for a long time and most of the methods we tried just
[00:01:02] broke on our monsters so here is the whole story every method we tried why it broke and how the
[00:01:07] tool works now and if you're not subscribing hit subscribe button so let me take you back to the very
[00:01:13] beginning all right so it all started with our game i wanted to add some animals into it so we
[00:01:19] picked deer and then Opus wrote the book itself key frames by code and well it looked like this just
[00:01:25] blocky then much better model from Tripo and the same old by code and still it was not real animal
[00:01:31] so we had this crazy idea don't animate the deer at all just film it well an AI video of
[00:01:37] our own deer and then copy that video onto the skeleton so for every frame a script written by Opus
[00:01:43] posts our model rendered it and checked does the outline match and for the deer it kind of worked but
[00:01:48] it had two big problems from the side the legs cross all the time and the script lost track of
[00:01:54] which leg is which so Opus had to go back and mark the feet itself point by point and the
[00:01:58] peasant has the same issue mixed up its near and far leg so again Oppus said to go through every
[00:02:03] frame and the second issue was the depth and man lifting a stone matched the video almost the pixel but
[00:02:08] you clearly see a lot of issues with it because the video is flat like a photo and script had
[00:02:13] to guess how far everything is and of course it guessed wrong but first one thing about cedance give it
[00:02:19] the same picture or the same words twice and you will get two different videos so if we film the
[00:02:24] front and the side as two separate videos they would just never match so for the troll we gave Cidance
[00:02:30] two cameras in one picture the front and the side with two cameras a point can only be in one
[00:02:34] spot the two lines cross right here and the depth problem was gone and then the script set 84% match
[00:02:41] like all checks passed and then I opened the lab and the majority of frames were just broken so again
[00:02:47] Opus went through every frame itself the video on top and our model right under it it found every broken
[00:02:52] frames and just fix it and that's when I said "Okay this can be how we make every monster because
[00:02:59] it takes a lot of time and a lot of tokens for Opus to fix everything by hand." So we
[00:03:03] needed one tool for any monster and any move with no hand fixes so we went shopping and here is
[00:03:10] every tool we tried and how it results first point tracking from Google Deep Mind the first frame of the
[00:03:16] video is our own render so we know exactly which pixel is which part of the body and the tracker
[00:03:21] just follows every one of them through the video sounds perfect right well look at the legs after a few
[00:03:27] steps the points slide up onto the body and the legs have nothing left then we tried outlines from Meta
[00:03:33] Sim 2 one outline for every leg on a walk it wasn't bad but in a run the legs blur
[00:03:40] and the far legs just disappear or jump onto the chest and sometimes the back leg gets the color of
[00:03:45] the front leg so we don't know which leg is which anymore then we tried an AI that guesses depth
[00:03:51] from one picture to tell the new leg from the far one bright means close and dark means far and
[00:03:57] here the new leg and the far one get the same score we checked every frame and it was right
[00:04:03] only four times out of 10 the two legs are just 10 cm apart and that is too small for
[00:04:08] this AI so we thought okay let's make it easy and we painted the legs every leg its own color
[00:04:14] like socks and it worked sidance kept the colors and in almost every frame we knew which leg is which
[00:04:21] but here's the catch now everything depends on the sidance keeping the paint right and remember sedance never makes the
[00:04:27] same video twice and this time it kept the paint next time it might not and this is just a
[00:04:33] wolf four legs four colors what about the dragon with wings or a centaur with six limbs so we need
[00:04:39] a different method and then we tried animal pose detectors trained on thousand of real animal photos from the side
[00:04:46] it draws the far legs right on the belly and from the front it's just a mess and then the
[00:04:51] newest research mockup anything train on a real animal motion capture and our wolf is just running inclined and the
[00:04:59] galoop is not perfect either and also it's just for animals so what about monsters so after all of those
[00:05:06] tries I was thinking okay let's stop for a moment and just rethink everything over and then we had some
[00:05:13] totally different idea if both cameras know exactly where a joint is in the picture the 3D part is just
[00:05:19] a simple map the two lines cross done so the whole problem is one thing find every joint in the
[00:05:24] picture in every frame and know which one is which but first every new monster needs a skeleton so that's
[00:05:31] now the first step of the tool we use Uni an AI that looks at a 3D model and draws
[00:05:37] the bone inside it and it's good but not perfect here are four tries of our raid bones sticking out
[00:05:43] of the body and once no legs at all so our tool checks each try against the model itself every
[00:05:49] leg on the ground needs a bone and left and right must match and it keeps the best one then
[00:05:55] it folds the fingers into the hand and cuts off whatever sticks out of the body so now the skeleton
[00:06:00] is inside the 3D model but finding those joints in the video is the hard part and no tool out
[00:06:05] there can do it for our troll because no AI has ever seen our troll but we have something better
[00:06:11] we have the troll so we take Dino an AI from meta that has already seen millions of photos and
[00:06:18] we teach it to one new job fighting every joint of our troll and for that we render the troll
[00:06:23] in 3,000 random poses from both cameras and because we made the pictures we know exactly where every joint is
[00:06:30] and we make it hard on purpose about half of the poses move fast so the arms and legs are
[00:06:35] blurred because that's exactly what Cedance gives us every picture is made like this we take our troll bend every
[00:06:42] joint at random but only as far as a real joint can go turn him blur what moves fast and
[00:06:47] then make it a bit worse like Cance does the light the colors and the blurry arm then Dino learns
[00:06:53] this one job on this one troll about 30 minutes on my graphics card and now it reads a sentence
[00:06:59] video like this every join lights up in both pictures frame by frame in just seconds but how do we
[00:07:05] know the tool is right without me checking every frame we give it an exam for every monster even a
[00:07:11] brand new one we make up a motion ourselves every joint moves at random but only inside these limits and
[00:07:17] we film it in our studio with the same two cameras and because we made that motion we know exactly
[00:07:22] where every joint is in every frame the tool reads that video like any sense clip and we compare its
[00:07:28] answer with our motion bone by bone so our new lizard took this exam before we paid for a single
[00:07:34] cedance video and every change to the tool has to pass this exam for every monster or it's out and
[00:07:40] before a cedance video even goes in the tool checks it do both pictures show the same move because sometimes
[00:07:46] CD shows two different moves in the two halves and then it's just faster to make a new video than
[00:07:51] to fix it okay but remember depth anything I thought maybe we can use a depth map here too and
[00:07:58] combine the two methods to make the results even better so we thought our own AI depth as well because
[00:08:04] in our render we know exactly how far every joint is and on the same move run it picked the
[00:08:09] near leer right every single time and depth anything got it four times out of 10 but combined it with
[00:08:14] our two cameras it changed almost nothing because two cameras already see the depth so can it replace the second
[00:08:20] camera not yet it knows which leg is nearer but not exactly how far so here is the whole thing
[00:08:26] from A to Z a model from triple the skeleton in a few minutes our monster from two cameras in
[00:08:32] one picture and cens make it move then the tool checks the video reads every join puts the move on
[00:08:39] the skeleton and it goes right into Blender and into the game four legs two legs wings a tail a
[00:08:45] sword it doesn't matter and before one troll used to take 4 days with Opus validating every frame and a
[00:08:52] lot of tokens now it's just few minutes because the learning process is just one time per monster then you
[00:08:58] can create any animations you want with it and it's not magic though if Cedance throws two different moves in
[00:09:05] the two pictures the tool can only follow one and the hand hidden behind the body is still a guess
[00:09:10] and let me know in comments what do you think about it and if you want to try it out
[00:09:14] as always thanks for watching and see you in the next one
