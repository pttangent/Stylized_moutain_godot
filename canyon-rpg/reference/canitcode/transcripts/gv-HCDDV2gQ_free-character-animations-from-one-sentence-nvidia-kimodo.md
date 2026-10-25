# Free Character Animations From One Sentence | NVIDIA Kimodo

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `gv-HCDDV2gQ`
- **Publish Date**: 2026-10-20
- **Duration**: PT6M7S
- **Views**: 55,416 | **Likes**: 881
- **URL**: https://www.youtube.com/watch?v=gv-HCDDV2gQ
- **Timestamped Lines**: 57

## Full Timestamped Transcript

[00:00:00] hello guys look at these animations A high kick a zombie walk and even a push-up And the best part
[00:00:07] is this is not mix and nobody put on a motion capture suit Every one of these is just one
[00:00:13] sentence in a free tool from Nvidia It's called Kimodo So in this video I will show you what it
[00:00:19] is how to install it how to use it and how to put these animations on any character you want
[00:00:25] So who made it Well it comes from Nvidia and it came out in March this year Free and open
[00:00:32] source They train it on more than 700 hours of real motion capture So real people in a studio with
[00:00:39] text that says what they do And it's not only text You can also lock a pose put a hand
[00:00:45] in one place or draw a path on the ground and it fills in the rest And it works for
[00:00:50] people and even for humanoid robot One motion can be up to 10 seconds long And the main model is
[00:00:55] free to use in games you sell All right let's install it You need an Nvidia graphic card Python and
[00:01:01] Git First download the code from GitHub and make a clean Python environment so it doesn't mess with anything else
[00:01:08] Then install PyTorch with CUDA I have an RTX 5070 and the new RTX50 cards need CUDA 12.8 so I
[00:01:17] take that version and then Kimodo itself with the demo On Windows one part gets built on your computer So
[00:01:24] you also need CMake and the Visual Studio build tools Now the annoying part Kimodo uses Llama 3 from Meta
[00:01:30] to read your text and Llama is locked So you have to ask for access on hugging face So fill
[00:01:36] in the form with real info Our first request got rejected and we think it was because we put a
[00:01:42] dash in the company field Yes seriously When Meta says yes login with your having face token The text part
[00:01:48] wants about 17 GB on the graphics card My laptop has 12 so I just tell it to read the
[00:01:54] text on the processor It's a bit slower but it works Okay the first run downloads the model and that's
[00:02:01] a lot of gigabytes so coffee time And one more Windows thing The demo page didn't start for me so
[00:02:09] I had to build it once by hand All the comments are in the description Okay so what can it
[00:02:14] do Every one of these is just one sentence A person sneaks forward crouching low A person sits down on
[00:02:21] the ground and stands back up Two versions of each took about 20 seconds on my laptop so that's fast
[00:02:27] And styles like an old person or a drunk person So how do you use it The easiest way is
[00:02:38] Theor demo It opens in your browser in local host You write what the person does here on the timeline
[00:02:44] and press generate And you get a few versions at once So you pick the one you like And here
[00:02:49] is the real power You can draw a path on the ground and the person walks along it or you
[00:02:55] lock a few poses like here And Kimodo fills in the motion between them When you like it you export
[00:03:00] it For example a BVH file and Blenders open that directly And there is also command line tool For the
[00:03:07] game we made our own small program that runs Kimodo
[00:03:13] Now here is my mistake When I first used Kimodo for my game the axe and the lock looked really
[00:03:18] bad So I thought maybe Kimodo just can't do this But then I played the same motions on Kimodo's own
[00:03:24] body and they looked much better So the problem was us We forced our own poses into it We cut
[00:03:30] the clips and speed them up and our code just glued the ax and the log to the hands So
[00:03:35] this time I gave it only one sentence and a trick Wood chopping came out of too slow So I
[00:03:41] wrote it like a fight A warrior strikes down with a heavy axe with full force And look at that
[00:03:47] heat The look same thing One sentence and it squats down deep and lifted with its both hands So here
[00:03:54] is my tip Start with just a sentence and watch it on Kimodo's body first Add your own poses later
[00:04:00] one at a time Okay But Kimoto moves only its own skeleton Your character might have different one from Mixamo
[00:04:07] from Unreal from Tripo So how do you move the animation over First export the emotion from the demo We
[00:04:14] use the NPC file It has the turn of every bone in every frame Then a bone map You tell
[00:04:20] the script which of your bones is which Kimodo bones pairs And if you use Mixamo be careful here Kimodo's
[00:04:26] left leg is your upper leg and your left leg is Kimoto's shin Next the rest pose Kimoto stands in
[00:04:33] a T pose Your character maybe not So first we turn your character into the same to pose and we
[00:04:39] turn the hands so the palms face the same way And now the main part for every frame we copy
[00:04:45] how each bone turns not where it is Only the hips are moved around and we scale that to your
[00:04:50] character legs Then we check it in every frame Every arm and leg points the same way as on Kimoto's
[00:04:56] body The worst one was only 3° off And here is the result Kim Modo's own body our character and
[00:05:03] a character from Triple with a totally different skeleton The same chop the same key and the same lock
[00:05:17] And here is my axe again on my own character Before with our own poses after with just one sentence
[00:05:24] And we fixed our grip code too We also made a small Blender script for all of this with Opus
[00:05:29] So you can ask your AI to do the same thing These five steps are all it needs So is
[00:05:35] it worth it Yes it is a great tool with endless possibilities and I will prove it in the next
[00:05:40] video I will be building full motion matching system and it will be crazy Trust me And by the way
[00:05:47] all the steps and tips are in the description and Nvidia already made the build on Kimodo It makes the
[00:05:53] motion live while you steer your character with your keyboard It's not in game engines yet but maybe soon the
[00:05:59] game makes these animations while you play Thanks for watching and see you in the next one
