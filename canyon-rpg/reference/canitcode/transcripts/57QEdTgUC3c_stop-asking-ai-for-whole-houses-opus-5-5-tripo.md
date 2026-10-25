# Stop Asking AI for Whole Houses - Opus 5.5 + Tripo

- **Channel**: Can It Code? (`@CanItCode`)
- **Video ID**: `57QEdTgUC3c`
- **Publish Date**: 2026-10-07
- **Duration**: PT8M19S
- **Views**: 36,274 | **Likes**: 857
- **URL**: https://www.youtube.com/watch?v=57QEdTgUC3c
- **Timestamped Lines**: 78

## Full Timestamped Transcript

[00:00:01] okay guys Every single thing you see here came out of an AI The hats the walkways the lanterns the
[00:00:07] bone of this giant and even this guy And it's not one big model It's a kit 22 parts that
[00:00:14] snap together ego And you can actually walk through all of it And by the way all of this goes
[00:00:18] up onto my Patreon The whole kit this scene and the game The link is on screen and in the
[00:00:23] description So in this video we will be using GPT6 Astra for image generation for our references triple with their
[00:00:32] new P2.0 model for the 3D assets So our sync kit and Opus 5.5 to pull it all together I'm
[00:00:39] going to show you the failures the bad results and finally five rules that fix everything and let you create
[00:00:45] beautiful scenes like this one So what are these rules rule number one draw it Do not describe it So
[00:00:54] first the wrong way My very first idea was to make a whole house and just cut it into parts
[00:01:00] So I asked Trio to split a cabin into six to 15 parts and I got 256 So yeah Then
[00:01:08] I just wrote prompts four short descriptions like a wooden wall with a door And Triple gives you four versions
[00:01:13] of each So I got 16 walls and only four came back usable The size were random Some walls had
[00:01:20] no door at all and some look more like a fence And the four versions aren't four sizes of the
[00:01:26] same wall They are just four different walls So can you fix a bad one afterwards well I tried mesh
[00:01:32] edit to open up a doorway that came out blocked And both times it stay closed So then I gave
[00:01:38] it one flat picture of a wall And what did I get well a box A solid box Because from
[00:01:44] the front a wall and a box look exactly the same So how do you show an AI how thick
[00:01:50] a wall is without any words well you draw it and that's the right way So now Astra draws every
[00:01:58] part twice from the front and from the side on a dark background with nothing else in the picture And
[00:02:04] with the front the side and the mirrored side P2.0 finally knows how thick a wall is And look the
[00:02:10] parts come out just like the drawing And P 2.0 gives you clean quads and you can pick how many
[00:02:16] polygons you want which is exactly what the game needs So now we have four platforms four walkways and seven
[00:02:23] walls out of eight with a real hole for the door So the first parts goes into the swamp Platform
[00:02:29] walkways stairs and a ladder Rule number two every part needs its real size Because when Opus 5.5 put the
[00:02:39] first parts together the posts of the walkway were just hanging in the air way above the water So why
[00:02:46] well every drawing has its own scale So triple made every part at its own scale too And that's the
[00:02:52] thing about parts They have to agree with each other So now every drawing gets exact size of the same
[00:02:58] grid And the last few cm Opus 5.5 fixes with a small script that snaps every part into place It
[00:03:05] measures every part fix the sizes if it has to and puts its corner right on the grid So two
[00:03:10] walls always meet And now that every part has its real size the walls go in and every wall meets
[00:03:17] the next one Rule number three tell it what you don't want Take a good look at this roof Does
[00:03:24] it look okay to you well in the drawing it looks fine but look at the 3D model from the
[00:03:31] top Almost a third of every roof is just holes And in the game that means light coming through rain
[00:03:37] coming through and the camera that sees right into the house So Astra got one more sentence for every roof
[00:03:44] drawing No gaps also from below And the holes went from third to almost nothing So the roof goes on
[00:03:51] with banners barrels and bolts And then the last pieces And guys that's the whole kit 22 parts And together
[00:03:59] it looks just amazing That honestly surprised me
[00:04:05] But it was too early to celebrate because the village still has to work in a real game Rule number
[00:04:10] four test it with the body because a village can look perfect in a picture but still be impossible to
[00:04:17] walk through So first we need a body and yes he came out of 32 Astra generated a swamp warrior
[00:04:23] from the front and side and the back and P 2.0 gave me four versions and honestly all four were
[00:04:29] pretty good The outri puts a skeleton inside even the fingers and the animation library is free So walk run
[00:04:36] and idle are just few clicks Of course it wasn't perfect The walk moved him forward by itself So in
[00:04:42] the game his feet were sliding and his spear bent like a bow with every step So Opus 5.5 made
[00:04:49] the animations play in place The game measures how fast his feet really move and the spear is stuck to
[00:04:55] his back like a real spear So in God Opus 5.5 gives every part one simple rule Floors you can
[00:05:01] walk on walls you can't walk through and the whole village is built from those rules And to check it
[00:05:07] a little boat walks the whole village by itself from the boat to the giant and it never falls into
[00:05:12] the water Then we put him in the village and the doors were way too small for him And this
[00:05:18] is where a kit really pays off We changed one number the size of a hat and every hat in
[00:05:24] the village grew all at once Try doing that with one big model You would have to make the whole
[00:05:30] village again
[00:05:34] Rule number five and this one you can't see at least not at first Every model from Tribo comes with
[00:05:40] its own texture But how does a texture even sit on a 3D model well you cut the model open
[00:05:47] and lay it flat like a cardboard box And that flat picture is a UV map Doing that by hand
[00:05:53] takes ages In Triple it's just one click Smart UV And it unwraps the whole model for you And the
[00:05:59] pieces are packed so almost nothing is wasted And then Trippo paints the textures right onto that map from the
[00:06:06] same drawings And for one model that's perfect But in a kit it's a different story So what's the problem
[00:06:13] well a small post and a big roof get the same size of picture So the post get tons of
[00:06:18] details and the roof get almost none Look at this Orange means blurry Blue means wasted pixels And some parts
[00:06:26] are five times sharper than the part right next to them And of top of that it's 23 different materials
[00:06:32] which is just extra work for the engine So the good practice is a texture atlas One big picture for
[00:06:38] the whole kit where every part gets space based on how big it really is So we took the original
[00:06:43] textures from triple and packed all the buildings parts into one atlas and the swamp and the giant into a
[00:06:49] second one Same models same look but now it's two materials instead of 23 And everything is equally sharp Everything
[00:06:57] is green And here is a little bonus Because it's a kit the same village works for a different kind
[00:07:02] of game too one key and it's an isometric game The roof of the house you are in just disappears
[00:07:08] And when the giant bows hide you still see yourself And it's still the same 22 parts not a single
[00:07:14] new model
[00:07:18] So can I make parts for a game well yes but only if you stop asking for the whole houses
[00:07:25] Triple was really good at turning drawings into clean parts P 2.0 window with a front and a side views
[00:07:31] was the big change and smart UV the textures auto rig and the free animations just worked What didn't work
[00:07:37] well text prompts for exact parts Mesh Edit couldn't open the door and the textures needed one more step So
[00:07:44] my advice let Trippo make small parts and let a model like Opus 5.5 put them together The whole village
[00:07:50] and the warrior cost about 4,000 credits It could be much cheaper but we generated four versions for each model
[00:07:56] so that was also the cost And the link to Tripo is in the description So that's the method five
[00:08:03] rows and one kit Let me know in the comments what you would build with it Thanks for watching and
[00:08:07] see you in the next one
