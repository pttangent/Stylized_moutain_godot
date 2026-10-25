# Crazy AI Animation Workflow - Opus 5.5

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `evK-Y83Qlco`
- **Publish Date**: 2026-09-27
- **Duration**: PT8M37S
- **Views**: 160,176 | **Likes**: 3,166
- **URL**: https://www.youtube.com/watch?v=evK-Y83Qlco
- **Timestamped Lines**: 76

## Full Timestamped Transcript

[00:00:00] all right welcome back last time I promised you animals so here they are a road dear a hair a
[00:00:06] peasant and a sheep and yes even a bear and here is the crazy part nobody animated them by hand
[00:00:13] every hop every step and every bite comes from an AI video and for us that's a big breakthrough because
[00:00:20] yes AI can make a tree or an axe pretty well but an animal that really works like animal that
[00:00:26] was always the hard part so in this video I will show you exactly how we did it step by
[00:00:31] step what we tried first what didn't work and the new way that finally did but first let's go back
[00:00:38] to the start so our first idea was the obvious one just let the AI build the deer itself in
[00:00:45] Blender from code with no triple and no video i gave Opus 5.5 the same picture we later gave to
[00:00:52] Shrio and it wrote a Python script that builds the deer out of a simple shapes tubes for the body
[00:00:57] and the neck capsules for the legs and a few X shapes for the muscles and they all melt into
[00:01:02] one then it renders the deer compares it with the picture and fixes what looks wrong after round four rounds
[00:01:08] about 40 minutes next the skeleton 29 bones so the legs the neck the ears and the tail can actually
[00:01:15] bend and then the walk no video no motion capture just key frames written by code and honestly it isn't
[00:01:22] that bad i mean we used the best model right now opus 5.5 is an absolute monster and this is
[00:01:28] the limit the silhouette is kind of close but this face and in the animation I still feel a lot
[00:01:35] of like blockiness there is no small animal movement you can just see it's artificial and the weights these aren't
[00:01:41] very good so on some frames you can see the mesh deform just like here okay so maybe the problem
[00:01:49] was the model so this time we use trio the same picture and a minute later we had this and
[00:01:55] yes that's a huge difference the face the fur the proportions it actually look like a deer but Trio only
[00:02:01] gives you the model there is no skeleton so the AI build one and then the same work as before
[00:02:06] key frames written by code and of course it looks better because because the model is better but the animation
[00:02:12] is still not like organic enough you know what I mean and the mesh deforms again so the weights still
[00:02:18] aren't right okay to be fair this took like 10 minutes and just one try but still it's not the
[00:02:25] real thing so the model wasn't the problem anymore the motion was so then we had a crazy idea what
[00:02:33] if we don't animate the deer at all but just film it well not a real deer an AI video
[00:02:41] of our own deer so first we render our triple model exactly from the side on a plain gray background
[00:02:47] and that's important because now we know exactly where the camera is then this picture goes to C dance with
[00:02:53] a really strict prompt side view only the camera follows the deer no cuts no zoom and exactly four legs
[00:03:03] and a few minutes later we get this 4 seconds of our deer running and yes it even has sound
[00:03:11] and that was the very first try no retries but it's still just a video the game needs bones so
[00:03:19] now comes the hard part the AI copies this video on the skeleton frame by frame for every frame a
[00:03:26] script the AI wrote poses our model renders it and compares it with the video does the outline match do
[00:03:32] the X match if not it moves the bones a little and checks again 97 frames for every clip and
[00:03:38] about half an hour of computing for each one and look that's our model doing exactly what the video does
[00:03:46] okay so all three approaches same deer same camera first built-in blender then triple and blender walk and finally triple
[00:03:54] with cedance and honestly that's the moment we knew this is it but every animal came with its own problem
[00:04:02] with the hair the problem was hidden in the video file itself the video pretends to be 60 frames a
[00:04:08] second but the motion inside was only 24 so the legs kept speeding up and slowing down 12 times a
[00:04:14] second the road deer has really thin legs and in the gallop they cross all the time so the script
[00:04:20] lost track of which leg is which so the AI went back to the tricky frames and marked the legs
[00:04:26] itself point by point the peasant legs kept jumping because the script mix up the new leg and the file
[00:04:31] leg so the AI marked the legs itself again in every single frame and the wings well Trip only painted
[00:04:38] them on the bodies so the AI built real wings feather by feather and they fall back when it lands
[00:04:44] and the bear made with GPT6 Astra took 14 rounds the legs the shaking body and even the fur flickering
[00:04:51] in the route so for every animal the AI built a small lap so I just go frame by frame
[00:04:58] and let the AI for example frame 47 the legs jumps back please fix it and after a few rounds
[00:05:04] finally it was perfect and now the fun part any animal move like eating jumping flying and of course attacking
[00:05:13] this all cames with the sound from Cas
[00:05:23] and here they are walking around on our meadow but in a game an animal can't just play animations it
[00:05:32] has to react to you so the AI gave them a tiny brain for example a deer when you come
[00:05:37] close it leaves its head up and watches you come closer and it runs and then pheasants waits until the
[00:05:45] last moment and then it just takes off
[00:05:51] under the hood it's really simple every animal has two circles step into the first one and it stops and
[00:05:57] watches you keep coming closer and it runs away from you and straight to the trees and every step is
[00:06:03] still the seed animation so the feet don't slide it doesn't work for everything though we tried the exact same
[00:06:10] trick on the person lifting a stone and from the camera his outline matches the video almost to the pixel
[00:06:17] but put the real model in and even from that same camera his legs are in front of his chest
[00:06:22] walk around him and you see why his chest is just sunk into his legs and the stone is stuck
[00:06:28] inside his body and here's why a video is flat it only sees one plane left and right up and
[00:06:36] down what it can't see is depth how far away anything is from the camera so this stone could be
[00:06:42] here or here or here and the picture looks exactly the same so the AI has to guess and here
[00:06:48] it guessed wrong a header film from the side is the easy case its legs swing along the plane so
[00:06:55] the camera sees almost everything the only thing it can tell is which leg is the near one and which
[00:07:01] is the far one and that's exactly where the AI had to mark the legs but the person lifting something
[00:07:08] doesn't stay in one plane the arms reach forward toward the camera and rub around the stone the stone hides
[00:07:14] the hand and it has to sit in both palms exactly a few centimeters off and it goes right through
[00:07:20] him and filming a person from the side like the deer doesn't save it either here he is walking with
[00:07:28] a lock on his shoulder film straight from the side and from the camera it matches again but from the
[00:07:33] front the lock goes right through his arm whichever side you film from some depth is always missing so maybe
[00:07:42] the fix is just more cameras film the same move from a few sides at once and the depth is
[00:07:48] right there that's exactly how real motion capture works and that's the trick we used on our first boss a
[00:07:56] troll sid filmed every move from two sides at once and in the next episode I will show you how
[00:08:02] it went so that's our breakthrough five animals 21 AI videos and a few days of work well almost every
[00:08:12] animals runs from you but not the bear and honestly we're only just getting started next we are building a
[00:08:21] bestari because in our game the forest can't be safe and the story will tell you why let me know
[00:08:29] in the comments which animal you want to see next thanks for watching and see you in the next one
