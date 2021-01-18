# world

# room_desc

enemies = {
    'urukhai': {
        'short': 'Urukhai',
        'description': 'Large, ugly, orc-like creature',
        'hp': 50,
    }
}

rooms = [
    {
        'uid': 'outside',
        'name': "Outside Cave Entrance",
        'description': """North of you, the cave mount beckons""",
        'exits': [
            ('n', 'foyer')
        ],
        'items': [
            ('torch', 'torch', 'a basic torch to light the way'),
            ('training sword', 'sword', 'a dull training sword made of wood'),
        ],
        'npc': [
        ]
    },
    {
        'uid': 'foyer',
        'name': "Foyer",
        'description': """Dim light filters in from the south. Dusty
passages run north and east.""",
        'exits': [
            ('n', 'overlook'),
            ('e', 'narrow'),
            ('s', 'outside')
        ],
        'items': [
        ],
        'npc': [
        ]
    },
    {
        'uid': 'overlook',
        'name': "Grand Overlook",
        'description': """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        'exits': [
            ('s', 'foyer')
        ],
        'items': [
        ],
        'npc': [
        ]
    },
    {
        'uid': 'narrow',
        'name': "Narrow Passage",
        'description': """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        'exits': [
            ('n', 'guardian'),
            ('w', 'foyer')
        ],
        'items': [
        ],
        'npc': [
        ]
    },
    {
        'uid': 'guardian',
        'name': "Guardian Room",
        'description': """You come upon a massive creature, clad
    in full plate armor, which seems to be blockin the exit to the north.""",
        'exits': [
            ('n', 'treasure'),
            ('s', 'narrow')
        ],
        'items': [
        ],
        'npc': [
            ('urukhai', True)
        ]
    },
    {
        'uid': 'treasure',
        'name': "Treasure Chamber",
        'description': """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        'exits': [
            ('s', 'guardian')
        ],
        'items': [
            ('dragon egg', 'egg', 'a precious dragon egg which may hatch a dragon pet'),
        ],
        'npc': [
        ]
    },

]
