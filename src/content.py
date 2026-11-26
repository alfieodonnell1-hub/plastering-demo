"""Site content for The Plastering and Rendering Group demo.

Sources: the 23 Oct 2026 website brief and the 12 Nov 2026 meeting notes.
Anything in [SQUARE BRACKETS] is a placeholder still to be supplied by the client.
Service descriptions, benefits and FAQ answers are draft copy written for the demo:
check them with Rav before the site goes live.
"""

PHONE = "07894 915828"
PHONE_HREF = "tel:+447894915828"
WHATSAPP = "[WHATSAPP NUMBER]"
INSTAGRAM_URL = "https://www.instagram.com/theplasteringandrenderinggroup/"
INSTAGRAM_HANDLE = "@theplasteringandrenderinggroup"

# The service pages, Jobs we're proud of and Reviews pages are still built, but while
# their content is being gathered nothing in the menus or on the home page links to
# them. Set to True (and rebuild) to link them again.
SHOW_SUBPAGES = False
EMAIL = "info@theplasteringandrenderinggroup.co.uk"

GROUPS = [
    {
        "id": "render",
        "anchor": "external-rendering",
        "name": "External rendering",
        "short": "Rendering",
        "blurb": "Weatherproof, breathable finishes for new builds, extensions and tired elevations.",
        "image": "monocouche.jpg",
        "services": ["lime-render", "k-rend", "monocouche-render", "sand-and-cement-render", "stone-render"],
    },
    {
        "id": "plaster",
        "anchor": "internal-plastering-drylining",
        "name": "Internal plastering & drylining",
        "short": "Plastering",
        "blurb": "Flat walls, true ceilings and the boarding and insulation that sit behind them.",
        "image": "krend.jpg",
        "services": ["internal-plastering", "metal-stud-work", "ceilings", "insulation",
                     "fire-lining", "sound-boarding", "moisture-resistant-boarding"],
    },
    {
        "id": "decor",
        "anchor": "decorative-finishes",
        "name": "Decorative finishes",
        "short": "Decorative",
        "blurb": "Hand-applied feature finishes for walls, floors, wet rooms and pool surrounds.",
        "image": "marble.jpg",
        "services": ["microcement", "venetian-plaster", "marble-plaster"],
    },
]

COST_A = "Every job is different, so we price after a site visit. Quotes are free."
GUARANTEE = ("Is the work guaranteed?", "[GUARANTEE LENGTH AND TERMS]")

SERVICES = {
    # ---------------- External rendering ----------------
    "lime-render": {
        "name": "Lime render", "h1": "Lime render in Cheshire", "image": "lime.jpg",
        "work": ["lime.jpg", "ashlar.jpg", "monocouche.jpg"],
        "intro": "A traditional, breathable render for older and solid-walled buildings, applied by hand in layers.",
        "what_title": "A render that lets old walls breathe",
        "what": [
            "Lime render is made from lime, sand and water. It sets slowly and stays slightly flexible, so it moves with the building instead of cracking away from it.",
            "It is the right choice for most period properties, cottages and listed buildings with solid stone or brick walls. Unlike cement render, it lets moisture in the wall dry out, which helps prevent damp and decay.",
        ],
        "benefits": [
            ("Breathable", "Moisture in solid walls can escape through the render rather than being trapped behind it."),
            ("Flexible", "Lime moves with older buildings, so it is less prone to cracking than hard cement render."),
            ("Right for heritage work", "Lime is the traditional material for period buildings, and is often preferred for listed buildings and conservation areas."),
            ("A soft, natural finish", "A gentle texture and colour that suits older properties, and can be finished with limewash."),
        ],
        "materials": ["Natural hydraulic lime (NHL)", "Lime putty", "Limewash finishes", "[BRANDS YOU USE]"],
        "faqs": [
            ("Is lime render right for my house?", "It usually is if the house has solid stone or brick walls, which most homes built before the 1920s do. Modern cavity walls built from blockwork often suit other renders. We check the walls at survey and recommend the right system."),
            ("Can lime render be painted?", "Yes, but it needs a breathable finish such as limewash or a mineral paint. Standard masonry paints can seal the surface and trap moisture."),
            ("Does lime render need special weather?", "Lime sets slowly, so it needs protecting from frost, heavy rain and strong sun while it cures. That makes spring to early autumn the best time for lime work."),
        ],
        "cost_name": "lime render",
    },
    "k-rend": {
        "name": "K Rend", "h1": "K Rend rendering in Cheshire", "image": "krend.jpg",
        "work": ["krend.jpg", "lime.jpg", "monocouche.jpg"],
        "intro": "A through-coloured render that keeps its finish without painting. We install all K Rend systems on new builds, extensions and existing homes.",
        "what_title": "Colour that runs right through the render",
        "what": [
            "K Rend is a range of factory-made renders. The colour is mixed into the material itself, so the finish you see goes the full depth of the top coat instead of sitting on the surface like paint.",
            "It is used on house fronts and extensions, on full re-renders of older properties, and on commercial elevations. The range covers silicone thin coat and scraped textures, which is why we fit every system and help you choose the one that suits the wall.",
        ],
        "benefits": [
            ("No painting", "The colour is in the render, so there is no paint film to peel or redo every few years."),
            ("Sheds water", "Silicone in the finish helps rain run off the face of the wall instead of soaking in."),
            ("Lets the wall breathe", "Moisture inside the wall can still escape through the finish."),
            ("A choice of looks", "Different textures and a wide colour range, matched to the building at survey."),
        ],
        "materials": ["K Rend silicone thin coat", "K Rend scraped finishes", "[OTHER K REND SYSTEMS USED]", "[APPROVED INSTALLER STATUS]"],
        "faqs": [
            ("Does K Rend need painting?", "No. The colour runs through the finish, so it does not need a paint coat. An occasional wash keeps it looking fresh."),
            ("Can it go over my existing render or brickwork?", "Often, but it depends on the condition of what is there. We check the wall at the survey and tell you whether it can be rendered over or needs taking back first."),
            ("How long does a job take?", "[TYPICAL TIMESCALE FOR A HOUSE]"),
        ],
        "cost_name": "K Rend",
    },
    "monocouche-render": {
        "name": "Monocouche render", "h1": "Monocouche render in Cheshire", "image": "monocouche.jpg",
        "work": ["monocouche.jpg", "krend.jpg", "blockwork.jpg"],
        "intro": "A through-coloured render applied as a single coat, for a clean, low-maintenance finish. We install all monocouche systems.",
        "what_title": "One coat, coloured all the way through",
        "what": [
            "Monocouche is French for “single layer”. It is a cement-based render with the colour mixed in, applied as one thick coat in two passes and then scraped back to give an even, lightly textured finish.",
            "Because the colour is in the render, it doesn’t need painting. It is mostly used on blockwork, which makes it a popular choice for new builds, extensions and modern re-renders.",
        ],
        "benefits": [
            ("No painting", "The colour runs through the render, so there is no paint to flake or redo."),
            ("Faster to apply", "One coat instead of two or three means less time on site than traditional render."),
            ("Weather-resistant", "It keeps rain out while still letting the wall breathe."),
            ("Consistent colour", "Factory-mixed colours give an even finish across the whole building."),
        ],
        "materials": ["Through-coloured monocouche render", "Reinforcing mesh and render beads", "[BRANDS YOU USE]"],
        "faqs": [
            ("What does monocouche mean?", "It’s French for “single layer”. The render goes on as one coat, in two passes, and is scraped back once it has firmed up to give the finished texture."),
            ("What can monocouche go on?", "It is designed mainly for blockwork and suitable masonry. Some existing walls need preparing or a base coat first, which we check at survey."),
        ],
        "cost_name": "monocouche render",
    },
    "sand-and-cement-render": {
        "name": "Sand and cement render", "h1": "Sand and cement render in Cheshire", "image": "sandcement.jpg",
        "work": ["sandcement.jpg", "brick.jpg", "monocouche.jpg"],
        "intro": "The traditional, hard-wearing render for brick and blockwork, finished smooth or textured and ready to paint.",
        "what_title": "The classic render, built up in coats",
        "what": [
            "Sand and cement render is applied in two or three coats: a scratch coat that bonds to the wall, then a float coat that is trued up and finished. The finish can be smooth or textured.",
            "It is a durable, cost-effective choice for modern brick and block walls, garden walls and outbuildings, and is usually finished with a masonry paint.",
        ],
        "benefits": [
            ("Hard-wearing", "A dense render that stands up well to knocks and weather."),
            ("Cost-effective", "Materials are widely available, which keeps costs down on larger walls."),
            ("Versatile finish", "Smooth or textured, and ready to paint in any colour."),
            ("Easy to repair", "Damaged areas can be patched and repainted to blend in."),
        ],
        "materials": ["Sharp sand and cement", "Waterproofing additives", "Masonry paint finishes", "[BRANDS YOU USE]"],
        "faqs": [
            ("Does sand and cement render need painting?", "Usually, yes. A masonry paint finishes the surface and adds weather protection. If you’d rather not paint, a through-coloured render such as K Rend or monocouche may suit better."),
            ("Is it suitable for older houses?", "It suits most modern brick and blockwork. Older solid-walled buildings are often better with a breathable lime render, and we’ll advise at survey."),
        ],
        "cost_name": "sand and cement render",
    },
    "stone-render": {
        "name": "Stone render", "h1": "Stone render in Cheshire", "image": "ashlar.jpg",
        "work": ["ashlar.jpg", "lime.jpg", "sandcement.jpg"],
        "intro": "Render finishes that give walls the look of natural stone, without the weight or cost of stone cladding.",
        "what_title": "The look of stone, in render",
        "what": [
            "Stone render gives a wall the appearance of natural stone. Depending on the finish, that can be a stone-textured surface or render scored with lines to look like cut stone blocks, often called ashlar effect.",
            "It is used to match period stonework, add character to new extensions, and lift plain or tired elevations. [CONFIRM WHICH STONE RENDER FINISHES YOU OFFER]",
        ],
        "benefits": [
            ("The look of stone", "Natural stone character for walls where real stone isn’t practical."),
            ("Lighter than cladding", "Render adds far less weight to a wall than stone slips or cladding."),
            ("Matches existing features", "Colour and texture can be chosen to sit alongside existing stonework."),
            ("Weather-resistant", "A durable finish that protects the wall as well as dressing it."),
        ],
        "materials": ["Stone-effect render finishes", "Ashlar-lined render", "[BRANDS YOU USE]"],
        "faqs": [
            ("What is ashlar effect?", "Ashlar is stone cut into neat rectangular blocks. Ashlar effect render recreates that look by scoring lines into the render before it sets."),
            ("Can stone render match my existing stone?", "Colour and texture can be chosen to sit well with existing stonework. Seeing samples against the wall is the best way to choose."),
        ],
        "cost_name": "stone render",
    },
    # ---------------- Internal plastering & drylining ----------------
    "internal-plastering": {
        "name": "Internal plastering", "h1": "Internal plastering in Cheshire", "image": "plaster.jpg",
        "work": ["plaster.jpg", "ceiling.jpg", "board.jpg"],
        "intro": "Smooth, flat walls and ceilings ready for decorating, from a single room skim to a full re-plaster.",
        "what_title": "Flat, smooth and ready to decorate",
        "what": [
            "Internal plastering covers skimming, where a thin finish coat goes over existing plaster or plasterboard, and full re-plastering, where old or damaged plaster is taken back and replaced.",
            "It is part of most renovations, extensions and rewires, and the quality of the plastering decides how good the walls look once they are painted.",
        ],
        "benefits": [
            ("A smooth finish", "Flat, even walls and ceilings that take paint well."),
            ("Hides the past", "Covers cracks, old patch repairs and uneven surfaces."),
            ("A fresh start", "New plaster after rewires, knock-throughs and extensions."),
            ("Right for the wall", "Skim, re-plaster or board and skim, depending on what’s there."),
        ],
        "materials": ["Gypsum finishing plaster", "Backing and bonding plasters", "Plasterboard and beads", "[BRANDS YOU USE]"],
        "faqs": [
            ("Do I need a skim or a full re-plaster?", "If the existing plaster is sound, a skim over the top is usually enough. If it is loose, blown or badly damaged, it needs taking back and re-plastering. We check at survey."),
            ("How long before I can paint new plaster?", "New plaster needs to dry fully first, which can take from a few days to a few weeks depending on thickness, heating and ventilation. It turns an even pale colour when dry. The first coat should be a mist coat of watered-down emulsion."),
        ],
        "cost_name": "internal plastering",
    },
    "metal-stud-work": {
        "name": "Metal stud work", "h1": "Metal stud work in Cheshire", "image": "studs.jpg",
        "work": ["studs.jpg", "board.jpg", "plaster.jpg"],
        "intro": "Lightweight steel-framed partitions and wall linings, boarded and finished to a flat, true surface.",
        "what_title": "Straight, strong internal walls",
        "what": [
            "Metal stud work uses galvanised steel studs and tracks to build internal walls, which are then boarded with plasterboard and finished. The same system is used for wall linings and boxing in.",
            "It is standard on commercial fit-outs and flats, and increasingly common in homes for loft conversions, room splits and extensions. Insulation and specialist boards can go into the build for sound and fire performance.",
        ],
        "benefits": [
            ("Straight and true", "Steel doesn’t twist, shrink or rot, so walls stay flat."),
            ("Quick to build", "Light, pre-made components go up quickly on site."),
            ("Built-in performance", "Add acoustic insulation or fire-rated boards to suit the building."),
            ("Room for services", "Cables and pipes run through the frame before it is boarded."),
        ],
        "materials": ["Galvanised steel studs and tracks", "Plasterboard", "Acoustic insulation", "[BRANDS YOU USE]"],
        "faqs": [
            ("Metal stud or timber stud?", "Metal studs are light, straight and don’t move with moisture, which makes for flatter walls. They are the norm on commercial jobs and work well in homes too."),
            ("Can you hang things on a metal stud wall?", "Yes, with the right fixings. For heavy items like TVs, radiators or kitchen units, extra supports are built into the wall before it is boarded."),
            ("Can a metal stud wall be soundproofed or fire-rated?", "Yes. Acoustic insulation and denser boards improve sound performance, and fire-rated boards are used where the building needs a fire-resisting wall."),
        ],
        "cost_name": "metal stud work",
    },
    "ceilings": {
        "name": "Ceilings", "h1": "Ceiling boarding and plastering in Cheshire", "image": "ceiling.jpg",
        "work": ["ceiling.jpg", "plaster.jpg", "studs.jpg"],
        "intro": "New ceilings, overboarding and skimming of cracked or textured ceilings, and dropped ceilings to hide services.",
        "what_title": "Flat ceilings, new or restored",
        "what": [
            "Ceiling work ranges from boarding and skimming new ceilings to overboarding old, cracked or textured ones, so the original often doesn’t have to come down.",
            "Metal frame ceilings hang below the structure on a steel grid and are boarded and skimmed. They hide pipes, ducting and cables, level out uneven ceilings, and can add fire and sound performance between floors.",
        ],
        "benefits": [
            ("Flat and crack-free", "A smooth ceiling that takes paint well."),
            ("Less disruption", "Overboarding often avoids pulling down the old ceiling."),
            ("Hides services", "Dropped ceilings tidy away pipes, cables and ducting."),
            ("Fire and sound upgrades", "Specialist boards improve performance between floors."),
        ],
        "materials": ["Plasterboard", "Metal frame ceiling systems", "Fire-rated and acoustic boards", "[BRANDS YOU USE]"],
        "faqs": [
            ("Can you plaster over an Artex ceiling?", "Often, yes: textured ceilings can be overboarded or skimmed. Textured coatings applied before 2000 can contain asbestos, so they should be tested before being sanded, scraped or drilled."),
            ("Should a cracked ceiling be replaced or overboarded?", "If the ceiling is sound and just cracked, overboarding and skimming is usually quicker and tidier. If it is sagging or loose, it needs taking down first. We check at survey."),
        ],
        "cost_name": "ceiling work",
    },
    "insulation": {
        "name": "Insulation: Kingspan and Rockwool", "menu": "Insulation (Kingspan and Rockwool)",
        "h1": "Kingspan and Rockwool insulation in Cheshire", "image": "stonewool.jpg",
        "work": ["stonewool.jpg", "board.jpg", "studs.jpg"],
        "intro": "Thermal and acoustic insulation for walls, ceilings and floors, using Kingspan rigid boards and Rockwool stone wool.",
        "what_title": "Warmer, quieter rooms",
        "what": [
            "Kingspan makes rigid insulation boards that give a high level of thermal insulation in a thin layer, including insulated plasterboard that boards and insulates a wall in one go.",
            "Rockwool is stone wool insulation. It fits between studs, joists and rafters, improves sound insulation and is non-combustible, which makes it a common choice for partitions and between floors. Many jobs use both.",
        ],
        "benefits": [
            ("Lower heating bills", "Better insulation keeps the heat in and rooms warmer."),
            ("Thin where space matters", "Kingspan boards insulate well without losing much room."),
            ("Quieter rooms", "Rockwool cuts sound between rooms and floors."),
            ("Fire performance", "Stone wool is non-combustible and suits fire-rated builds."),
        ],
        "materials": ["Kingspan rigid insulation boards", "Kingspan insulated plasterboard", "Rockwool stone wool slabs", "Rockwool acoustic insulation"],
        "faqs": [
            ("Kingspan or Rockwool: which do I need?", "They do different jobs. Kingspan boards give the most thermal insulation for their thickness, which saves room space. Rockwool is better for sound and is non-combustible. The right choice depends on where it’s going."),
            ("Can you insulate walls from the inside?", "Yes. Cold or solid external walls can be lined with insulated plasterboard, or with a stud wall filled with insulation, then plastered. It takes a little floor space, and the build-up needs to control condensation."),
        ],
        "cost_name": "insulation",
    },
    "fire-lining": {
        "name": "Fire lining", "h1": "Fire lining in Cheshire", "image": "board-fire.jpg",
        "work": ["board-fire.jpg", "studs.jpg", "stonewool.jpg"],
        "intro": "Fire-rated boarding for walls, ceilings, partitions and steelwork, built to the fire rating your building needs.",
        "what_title": "Boarding that holds back fire",
        "what": [
            "Fire lining uses fire-rated plasterboard, and where needed stone wool insulation, to give walls, ceilings and steel beams a set period of fire resistance, usually 30 or 60 minutes or more.",
            "It is needed in places like the wall between a house and an integral garage, stairways in loft conversions, flats, commercial units and around steelwork. A fire rating only holds if the whole system is installed as the manufacturer tested it.",
        ],
        "benefits": [
            ("Meets the regulations", "Built to the fire rating set by your drawings or Building Control."),
            ("Protects escape routes", "Gives people more time to get out safely."),
            ("Protects the structure", "Encasing steel beams and columns slows heat getting to them."),
            ("Works with other upgrades", "Fire boards combine with sound and thermal insulation."),
        ],
        "materials": ["Fire-rated plasterboard", "Stone wool insulation", "Fire-rated sealants", "[BRANDS YOU USE]"],
        "faqs": [
            ("Where is fire lining needed?", "Common places are between a house and an integral garage, around stairways in loft conversions, between flats and around steel beams. Your designer or Building Control will say what’s needed."),
            ("What fire rating do I need?", "Ratings are given in minutes, such as 30 or 60, and depend on the building and where the wall or ceiling is. The rating comes from your drawings or Building Control, and the system is built to meet it."),
        ],
        "cost_name": "fire lining",
    },
    "sound-boarding": {
        "name": "Sound boarding", "h1": "Sound boarding in Cheshire", "image": "board-sound.jpg",
        "work": ["board-sound.jpg", "stonewool.jpg", "studs.jpg"],
        "intro": "Acoustic boards and insulation that cut noise through walls and ceilings, for homes, flats and offices.",
        "what_title": "Keep noise where it belongs",
        "what": [
            "Sound boarding uses dense acoustic plasterboard, acoustic insulation and, where needed, resilient bars that separate the boards from the wall or ceiling behind, so less sound passes through.",
            "It is used between bedrooms, home offices and living spaces, on party walls, and in flats and conversions that need to meet sound insulation rules. It can be built into new stud walls or added to existing ones.",
        ],
        "benefits": [
            ("Quieter rooms", "Less noise from neighbours, the next room and the floor above."),
            ("More privacy", "Conversations and TV noise carry less between rooms."),
            ("Meets the rules", "Helps flats and conversions meet sound insulation requirements."),
            ("New or existing walls", "Built into new partitions or added to walls you already have."),
        ],
        "materials": ["Acoustic plasterboard", "Acoustic insulation", "Resilient bars", "Acoustic sealant", "[BRANDS YOU USE]"],
        "faqs": [
            ("How much quieter will it make a room?", "It depends on the existing wall and the type of noise. Sound also travels through gaps, sockets, floors and ceilings, so the best results come from treating those routes too."),
            ("Can you soundproof an existing wall?", "Yes. Common options are acoustic boards fixed on resilient bars, or a separate stud wall built in front and filled with acoustic insulation. Both take a little room space."),
        ],
        "cost_name": "sound boarding",
    },
    "moisture-resistant-boarding": {
        "name": "Moisture-resistant boarding", "h1": "Moisture-resistant boarding in Cheshire", "image": "board-moisture.jpg",
        "work": ["board-moisture.jpg", "plaster.jpg", "microcement.jpg"],
        "intro": "Moisture-resistant plasterboard for bathrooms, kitchens and utility rooms, ready to skim, paint or tile.",
        "what_title": "Boards made for humid rooms",
        "what": [
            "Moisture-resistant plasterboard has a water-repellent core and facing, so it copes with steam and humidity far better than standard board.",
            "It is used on walls and ceilings in bathrooms, en-suites, kitchens and utility rooms. Inside showers and wet rooms, where walls get soaked, a cement-based board or tanking system goes behind the tiles instead.",
        ],
        "benefits": [
            ("Copes with humidity", "Less risk of boards softening, sagging or growing mould."),
            ("Ready to finish", "Takes a skim and paint, or tiles directly."),
            ("Walls and ceilings", "Suits bathroom and kitchen ceilings as well as walls."),
            ("The right board for the room", "Moisture-resistant where it’s humid, cement-based where it’s wet."),
        ],
        "materials": ["Moisture-resistant plasterboard", "Cement-based boards for wet areas", "[BRANDS YOU USE]"],
        "faqs": [
            ("Can moisture-resistant board go in a shower?", "It’s made for humid rooms, not walls that get soaked. Inside showers and wet rooms, a cement-based board or a tanking system goes behind the tiles."),
            ("Can it be plastered or tiled?", "Yes. It can be skimmed and painted, or tiled directly, depending on the room."),
        ],
        "cost_name": "moisture-resistant boarding",
    },
    # ---------------- Decorative finishes ----------------
    "microcement": {
        "name": "Microcement", "h1": "Microcement in Cheshire", "image": "microcement.jpg",
        "work": ["microcement.jpg", "pool.jpg", "venetian.jpg"],
        "intro": "A seamless, hand-applied finish for floors, walls, showers and pool surrounds, with no grout lines.",
        "what_title": "One continuous surface",
        "what": [
            "Microcement is a thin cement-based coating, applied by hand in layers just a few millimetres thick and then sealed. It gives a smooth, seamless surface with no joints or grout.",
            "Because it is so thin, it can often go straight over existing tiles, screed or plaster. It is used on floors, walls, showers, wet rooms, stairs and worktops, and often around swimming pools.",
        ],
        "benefits": [
            ("No grout lines", "One continuous surface that’s easy to clean."),
            ("Goes over what’s there", "Often applied over sound tiles or screed without ripping them out."),
            ("Water-resistant when sealed", "Suits bathrooms, wet rooms and pool areas."),
            ("Colours and textures", "From smooth and soft to textured, slip-resistant finishes."),
        ],
        "pools": {
            "title": "Microcement around pools",
            "text": "Pool surrounds, terraces and changing areas suit microcement: the surface is seamless, so there is no grout to stain or clean, and it can be finished with a slip-resistant texture. Pool areas need a microcement system and sealer made for wet, chlorinated conditions. [CONFIRM THE POOL SYSTEM YOU USE]",
            "points": [
                ("Seamless", "No grout lines to stain, crack or clean."),
                ("Slip-resistant finishes", "Texture can be added where bare feet will be wet."),
                ("Made for wet areas", "Sealed with a system designed for pool conditions."),
            ],
        },
        "materials": ["Microcement base and finish coats", "Primers and reinforcing mesh", "Protective sealers", "[BRANDS YOU USE]"],
        "faqs": [
            ("Can microcement go over tiles?", "Often, yes, if the tiles are firmly fixed. The grout lines are filled and a primer and mesh go down first, so the old surface doesn’t need ripping out."),
            ("Is microcement waterproof?", "With the right sealer it is water-resistant, which is why it is used in showers, wet rooms and around pools. The sealer needs maintaining over time."),
        ],
        "cost_name": "microcement",
    },
    "venetian-plaster": {
        "name": "Venetian plaster", "h1": "Venetian plaster in Cheshire", "image": "venetian.jpg",
        "work": ["venetian.jpg", "marble.jpg", "microcement.jpg"],
        "intro": "A hand-polished lime plaster with the depth and sheen of marble, for feature walls and whole rooms.",
        "what_title": "Polished by hand, layer by layer",
        "what": [
            "Venetian plaster is a traditional Italian finish made from lime and marble dust. It is applied in thin layers with a steel trowel and burnished to a polished sheen, so light moves across the wall and gives it real depth.",
            "It is used on feature walls, hallways, living rooms and bathrooms at home, and in restaurants, hotels and shops. It can be tinted to almost any colour.",
        ],
        "benefits": [
            ("Depth paint can’t match", "Layers and polishing give movement and sheen."),
            ("Naturally breathable", "Lime-based, so it lets walls breathe and resists mould."),
            ("Long-lasting", "A hard, durable finish that ages well."),
            ("Any colour", "Tinted to suit the room, from soft neutrals to deep tones."),
        ],
        "materials": ["Lime and marble dust plasters", "Natural pigments", "Protective waxes", "[BRANDS YOU USE]"],
        "faqs": [
            ("How is Venetian plaster different from paint?", "It is built up by hand in thin layers and then polished, so it has a depth and sheen paint can’t give. Every wall is slightly different."),
            ("Can Venetian plaster go in a bathroom?", "Yes, with a protective wax or sealer. Inside the shower itself, microcement or another specialist finish is usually a better fit."),
        ],
        "cost_name": "Venetian plaster",
    },
    "marble-plaster": {
        "name": "Marble plaster", "h1": "Marble plaster in Cheshire", "image": "marble.jpg",
        "work": ["marble.jpg", "venetian.jpg", "ashlar.jpg"],
        "intro": "A lime and crushed marble finish that gives walls the look and feel of natural stone.",
        "what_title": "The look of stone, without the slabs",
        "what": [
            "Marble plaster is made from lime and crushed marble. Depending on how it is applied and finished, it ranges from a soft, stone-like matte texture to a smooth sheen, and it can be veined to look like marble.",
            "It brings the character of natural stone to feature walls, fireplaces, columns and curved surfaces, without the weight or joints of stone slabs. [CONFIRM THE MARBLE PLASTER FINISHES YOU OFFER]",
        ],
        "benefits": [
            ("The look of marble", "Natural stone character on walls and features."),
            ("Seamless", "No joints, and it follows curves and columns."),
            ("Breathable", "A lime base lets walls breathe."),
            ("Made to suit", "Colour, texture and sheen chosen for the room."),
        ],
        "materials": ["Lime and marble plasters", "Natural pigments", "Protective waxes and sealers", "[BRANDS YOU USE]"],
        "faqs": [
            ("What’s the difference between Venetian and marble plaster?", "Both are lime-based and applied by hand. Venetian plaster is polished to a high sheen, while marble plaster usually has more texture and a stone-like feel. Seeing samples side by side is the easiest way to choose."),
            ("Where can marble plaster be used?", "Most internal walls, fireplaces, columns and curved surfaces. Areas that get wet need a suitable sealer."),
        ],
        "cost_name": "marble plaster",
    },
}

# From the 12 Nov notes. The notes list names and company/role only: the
# testimonial wording itself still needs supplying.
TESTIMONIALS = [
    ("Ravi Sidhu", "Urban Building Projects"),
    ("Paula Noguerol", "Homeowner"),
    ("Dan Roberts", "Urban Homes"),
    ("Osborne & Co", None),
    ("Paddy Eyes", "Heritage Construction"),
    ("Club Invidual", None),
    ("Iceland Food Warehouse", None),
]

ENQUIRY_TYPES = ["Homeowner", "Developer", "Housebuilder", "Commercial", "Other"]

# "Jobs we're proud of": placeholder before/after pairs until real stills arrive.
JOBS = [
    {"id": "job-k-rend", "service": "k-rend", "before": "brick.jpg", "after": "krend.jpg"},
    {"id": "job-internal-plastering", "service": "internal-plastering", "before": "board.jpg", "after": "plaster.jpg"},
    {"id": "job-microcement", "service": "microcement", "before": "tiles.jpg", "after": "microcement.jpg"},
    {"id": "job-monocouche", "service": "monocouche-render", "before": "blockwork.jpg", "after": "monocouche.jpg"},
    {"id": "job-ceilings", "service": "ceilings", "before": "artex.jpg", "after": "ceiling.jpg"},
    {"id": "job-venetian", "service": "venetian-plaster", "before": "patchy.jpg", "after": "venetian.jpg"},
]
HOME_JOBS = ["job-k-rend", "job-internal-plastering", "job-microcement"]

INSTAGRAM_TILES = ["venetian.jpg", "krend.jpg", "microcement.jpg", "lime.jpg", "marble.jpg", "plaster.jpg"]
