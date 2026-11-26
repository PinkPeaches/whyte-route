# Page specs and regeneration prompts

**How these pages were made.** The image-generation account available during the build had no credits, so the 30 pages were drawn as original vector line art by code (not by an image model). The exact source for each page is the function named below; re-running `python3 src/build_interior.py` regenerates the identical page.

The *descriptive prompt* for each page is **not** what produced it — it describes the finished drawing so you can recreate the page with an image model later. Add the shared style line to every prompt:

> **Shared style line:** Children's coloring-book line art, black outlines only on a pure white background, thick bold uniform line weight, big simple shapes, cute chibi style, generous white space, no shading, no gray, no color fills, no text, no watermark, single centered scene, ages 4-8, original design, Christmas theme.

| # | PDF page | Page | Source (in `src/`) | Descriptive prompt |
|---|---|---|---|---|
| 1 | 3 | Kitten in a Christmas stocking | `animals_a.py` → `kitten_stocking()` | A cute baby kitten with a round head, pointed ears and forehead stripes, peeking out of a very large Christmas stocking with a fluffy cuff and a hanging loop; front paws resting on the cuff. A small gift box, a star bauble and falling snowflakes around it. |
| 2 | 5 | Puppy in a Santa hat | `animals_a.py` → `puppy_santa()` | A cute sitting puppy with floppy ears, an open smiling mouth, a collar with a jingle bell, and a tilted Santa hat with a pompom. A wrapped gift with a bow sits beside it; snowflakes fall. |
| 3 | 7 | Baby reindeer with jingle bell | `animals_a.py` → `reindeer()` | A cute sitting baby reindeer with branching antlers, big round ears, a big round nose and hooves, wearing a bell collar. Snowflakes, a holly sprig and a wavy snow line at the bottom. |
| 4 | 9 | Penguin chick with a scarf | `animals_a.py` → `penguin()` | A chubby penguin chick standing on snow, with a round white face disc, a small beak, flippers, orange webbed feet and a long striped scarf with fringe. Snowflakes fall around it. |
| 5 | 11 | Bunny with a candy cane | `animals_a.py` → `bunny()` | A sitting baby bunny with tall inner-ear outlines, round cheeks, buck teeth and a fluffy tail, holding a big candy cane in both paws. A holly sprig and snowflakes. |
| 6 | 13 | Bear cub peeking out of a gift box | `animals_a.py` → `bear_gift()` | A baby bear cub with round ears and a round muzzle peeking over the rim of a large open gift box, paws on the edge. The box has a vertical ribbon, a bow and star patterns; snowflakes around. |
| 7 | 15 | Fox kit by the little tree | `animals_a.py` → `fox()` | A sitting fox kit with pointed ears, cheek-fur tufts, a white muzzle, a long bushy tail and a striped scarf, standing beside a small decorated Christmas tree. A snowflake in the sky. |
| 8 | 17 | Owlet in a bobble hat | `animals_a.py` → `owl()` | A round owlet perched on a snowy branch, huge round eyes, small beak, ear tufts, feathered chest and wings, wearing a bobble beanie. A holly sprig and snowflakes. |
| 9 | 19 | Hedgehog with ornaments | `animals_a.py` → `hedgehog()` | A cute hedgehog with a spiky back, small round ears, a pointed snout and rosy cheeks. Three Christmas baubles float above its spines; holly and snowflakes. |
| 10 | 21 | Panda cub holding a star | `animals_a.py` → `panda()` | A sitting baby panda with eye patches, round ears and a tilted Santa hat, holding up a big five-point star in one paw. A snowflake and snow dots. |
| 11 | 23 | Baby elephant wrapped in lights | `animals_b.py` → `elephant()` | A sitting baby elephant with huge round ears, a curled trunk, small tusks and rosy cheeks. A string of Christmas lights hangs across the top; a gift and a star sit on the ground. |
| 12 | 25 | Lion cub with holly crown | `animals_b.py` → `lion()` | A sitting lion cub with a spiky mane, small round ears, a broad muzzle and a tail with a tuft, wearing two holly sprigs as a crown. A gift box and snowflakes. |
| 13 | 27 | Giraffe calf with a scarf | `animals_b.py` → `giraffe()` | A standing giraffe calf with a long spotted neck, two ossicones, side ears, a long striped scarf and a tail tuft, on a snowy ground line. A star and snowflake in the sky. |
| 14 | 29 | Koala in an elf hat with a gift | `animals_b.py` → `koala()` | A sitting koala with big fluffy round ears, a large oval nose and an elf hat, hugging a wrapped gift in its lap. Eucalyptus leaves and snowflakes. |
| 15 | 31 | Mouse in a mug with candy cane | `animals_b.py` → `mouse()` | A tiny mouse with huge round ears and whiskers peeking out of a giant Christmas mug decorated with holly and stars; a candy cane sticks out of the mug and the tail curls beside it. |
| 16 | 33 | Squirrel holding a bauble | `animals_b.py` → `squirrel()` | A sitting squirrel with tufted ears, a big bushy tail, puffy cheeks and a holly sprig by one ear, holding a Christmas bauble in both paws. |
| 17 | 35 | Duckling in a wreath | `animals_b.py` → `duckling()` | A fluffy duckling with a head tuft, flat beak, little wings and orange webbed feet, framed inside a large round Christmas wreath with leaves, berries and a bow. |
| 18 | 37 | Lamb with holly and a bell | `animals_b.py` → `lamb()` | A woolly lamb with a fluffy body, side ears, a curly forehead tuft, a holly crown and a bell collar, standing on a snowy ground line. |
| 19 | 39 | Piglet with a gingerbread cookie | `animals_b.py` → `piglet()` | A sitting piglet with a round snout with two nostrils, pointed ears and an elf hat, holding a gingerbread-man cookie. |
| 20 | 41 | Polar bear cub on a sled | `animals_b.py` → `polar_bear()` | A polar bear cub with small round ears, wearing winter earmuffs, sitting on a wooden sled with a gift on each side. Snowflakes. |
| 21 | 43 | Seal pup balancing a bauble | `animals_c.py` → `seal()` | A round seal pup with whiskers, flippers and tail flippers, balancing a large striped Christmas bauble on its head, standing on a wavy snow line. |
| 22 | 45 | Otter floating with a gift | `animals_c.py` → `otter()` | A sea otter floating on its back among wavy lines, wearing a Santa hat and holding a wrapped gift on its tummy; snowflakes above. |
| 23 | 47 | Raccoon hugging a big ornament | `animals_c.py` → `raccoon()` | A sitting raccoon with a mask, round ears, a ringed bushy tail and two holly sprigs on its head, hugging a big star-decorated bauble. |
| 24 | 49 | Fawn with wreath collar | `animals_c.py` → `fawn()` | A sitting baby deer with white spots, large ears and a wreath-and-holly collar, standing between two small Christmas trees. Snowflakes. |
| 25 | 51 | Chick hatching from an ornament | `animals_c.py` → `chick()` | A fluffy chick with a head tuft, small beak and little wings hatching out of a big cracked Christmas bauble with a zig-zag break line; shell scraps on the snow. |
| 26 | 53 | Frog on a gift | `animals_c.py` → `frog()` | A cheerful frog with big bulging eyes, a wide smile, webbed toes and a holly bow tie, sitting on top of a big gift box. A string of lights across the top. |
| 27 | 55 | Hippo calf with antlers | `animals_c.py` → `hippo()` | A baby hippo with a wide muzzle, nostrils, small ears and a reindeer-antler headband, wearing a bell collar, on a snowy ground line. |
| 28 | 57 | Monkey with baubles | `animals_c.py` → `monkey()` | A sitting baby monkey with a heart-shaped face, round ears and a long curling tail, holding up a Christmas bauble in each hand, under a garland of stars. |
| 29 | 59 | Tiger cub in a Christmas sweater | `animals_c.py` → `tiger()` | A sitting tiger cub with forehead and cheek stripes, round ears, a striped tail and a knitted sweater with a star on the front. Snowflakes. |
| 30 | 61 | Llama with festive blanket | `animals_c.py` → `llama()` | A standing baby llama with a long neck, banana-shaped ears, a fluffy head tuft, a bell collar and a star-patterned blanket on its back, on snow with a holly sprig. |
