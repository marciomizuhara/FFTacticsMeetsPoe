from items.consumables import *

monster_type = {
    'Green Goblin': {'name': 'Green Goblin',
                     'life': 80,
                     'attack': 104,
                     'defense': 12,
                     'level': 1,
                     'xp': 10,
                     'crit_chance': 10,
                     'delve_drop': consumables['dense fossil']},

    'Chocobo': {'name': 'Chocobo',
                'life': 85,
                'attack': 106,
                'defense': 13,
                'level': 1,
                'xp': 13,
                'crit_chance': 20,
                'delve_drop': consumables['dense fossil']},

    'Skeleton': {'name': 'Skeleton',
                 'life': 90,
                 'attack': 110,
                 'defense': 15,
                 'level': 2,
                 'xp': 15,
                 'crit_chance': 10,
                 'delve_drop': consumables['dense fossil']},

    'Red Panther': {'name': 'Red Panther',
                    'life': 95,
                    'attack': 110,
                    'defense': 20,
                    'level': 2,
                    'xp': 18,
                    'crit_chance': 15,
                    'delve_drop': consumables['dense fossil']},

    'Black Chocobo': {'name': 'Black Chocobo',
                      'life': 98,
                      'attack': 115,
                      'defense': 20,
                      'level': 3,
                      'xp': 18,
                      'crit_chance': 25,
                      'delve_drop': consumables['dense fossil']},

    'Red Goblin': {'name': 'Red Goblin',
                   'life': 100,
                   'attack': 118,
                   'defense': 23,
                   'level': 3,
                   'xp': 25,
                   'crit_chance': 10,
                   'delve_drop': consumables['dense fossil']},

    'Coeurl': {'name': 'Coeurl',
               'life': 105,
               'attack': 120,
               'defense': 23,
               'level': 4,
               'xp': 25,
               'crit_chance': 20,
               'delve_drop': consumables['dense fossil']},

    'Bonesnatch': {'name': 'Bonesnatch',
                   'life': 110,
                   'attack': 125,
                   'defense': 30,
                   'level': 4,
                   'xp': 35,
                   'crit_chance': 10,
                   'delve_drop': consumables['dense fossil']},

    'Black Goblin': {'name': 'Black Goblin',
                     'life': 125,
                     'attack': 127,
                     'defense': 30,
                     'level': 5,
                     'xp': 45,
                     'crit_chance': 10,
                     'delve_drop': consumables['serrated fossil']},

    'Red Chocobo': {'name': 'Red Chocobo',
                    'life': 130,
                    'attack': 138,
                    'defense': 35,
                    'level': 5,
                    'xp': 50,
                    'crit_chance': 30,
                    'delve_drop': consumables['serrated fossil']},

    'Vampire Cat': {'name': 'Vampire Cat',
                    'life': 135,
                    'attack': 145,
                    'defense': 37,
                    'level': 6,
                    'xp': 70,
                    'crit_chance': 25,
                    'delve_drop': consumables['serrated fossil']},

    'Gobbledygook': {'name': 'Gobbledygook',
                     'life': 140,
                     'attack': 155,
                     'defense': 40,
                     'level': 6,
                     'xp': 90,
                     'crit_chance': 15,
                     'delve_drop': consumables['serrated fossil']},

    'Skeletal Fiend': {'name': 'Skeletal Fiend',
                       'life': 145,
                       'attack': 155,
                       'defense': 40,
                       'level': 7,
                       'xp': 100,
                       'crit_chance': 15,
                       'delve_drop': consumables['serrated fossil']},

    'Ghoul': {'name': 'Ghoul',
              'life': 100,
              'attack': 160,
              'defense': 10,
              'level': 7,
              'xp': 150,
              'crit_chance': 50,
              'delve_drop': consumables['serrated fossil']},

    'Floating Eye': {'name': 'Floating Eye',
                     'life': 220,
                     'attack': 170,
                     'defense': 46,
                     'level': 8,
                     'xp': 200,
                     'crit_chance': 20,
                     'delve_drop': consumables['serrated fossil']},

    'Ghast': {'name': 'Ghast',
              'life': 150,
              'attack': 180,
              'defense': 20,
              'level': 8,
              'xp': 220,
              'crit_chance': 50,
              'delve_drop': consumables['serrated fossil']},

    'Piscodaemon': {'name': 'Piscodaemon',
                    'life': 260,
                    'attack': 195,
                    'defense': 50,
                    'level': 9,
                    'xp': 250,
                    'crit_chance': 30,
                    'delve_drop': consumables['serrated fossil']},

    'Squidrakin': {'name': 'Squidrakin',
                   'life': 280,
                   'attack': 200,
                   'defense': 65,
                   'level': 10,
                   'xp': 300,
                   'crit_chance': 40,
                   'delve_drop': consumables['pristine fossil']},

    'Ahriman': {'name': 'Ahriman',
                'life': 280,
                'attack': 220,
                'defense': 65,
                'level': 10,
                'xp': 320,
                'crit_chance': 30,
                'delve_drop': consumables['pristine fossil']},

    'Mindflayer': {'name': 'Mindflayer',
                   'life': 300,
                   'attack': 250,
                   'defense': 70,
                   'level': 11,
                   'xp': 380,
                   'crit_chance': 50,
                   'delve_drop': consumables['pristine fossil']},

    'Plague Horror': {'name': 'Plague Horror',
                      'life': 350,
                      'attack': 270,
                      'defense': 80,
                      'level': 11,
                      'xp': 400,
                      'crit_chance': 40,
                      'delve_drop': consumables['pristine fossil']},

    'Dryad': {'name': 'Dryad',
              'life': 600,
              'attack': 260,
              'defense': 100,
              'level': 12,
              'xp': 450,
              'crit_chance': 0,
              'delve_drop': consumables['pristine fossil']},

    'Jura Aevis': {'name': 'Jura Aevis',
                   'life': 400,
                   'attack': 270,
                   'defense': 80,
                   'level': 12,
                   'xp': 450,
                   'crit_chance': 50,
                   'delve_drop': consumables['pristine fossil']},

    'Revenant': {'name': 'Revenant',
                 'life': 400,
                 'attack': 270,
                 'defense': 40,
                 'level': 13,
                 'xp': 450,
                 'crit_chance': 50,
                 'delve_drop': consumables['pristine fossil']},

    'Steelhawk': {'name': 'Steelhawk',
                  'life': 450,
                  'attack': 320,
                  'defense': 90,
                  'level': 13,
                  'xp': 500,
                  'crit_chance': 50,
                  'delve_drop': consumables['pristine fossil']},

    'Treant': {'name': 'Treant',
               'life': 900,
               'attack': 270,
               'defense': 120,
               'level': 14,
               'xp': 600,
               'crit_chance': 0,
               'delve_drop': consumables['pristine fossil']},

    'Cockatrice': {'name': 'Cockatrice',
                   'life': 600,
                   'attack': 390,
                   'defense': 100,
                   'level': 14,
                   'xp': 550,
                   'crit_chance': 50,
                   'delve_drop': consumables['pristine fossil']},

    'Wisenkin': {'name': 'Wisenkin',
                 'life': 650,
                 'attack': 420,
                 'defense': 120,
                 'level': 15,
                 'xp': 700,
                 'crit_chance': 15,
                 'delve_drop': consumables['deft fossil']},

    'Elder Treant': {'name': 'Elder Treant',
                     'life': 1600,
                     'attack': 400,
                     'defense': 140,
                     'level': 16,
                     'xp': 750,
                     'crit_chance': 0,
                     'delve_drop': consumables['deft fossil']},

    'Minotaur': {'name': 'Minotaur',
                 'life': 900,
                 'attack': 600,
                 'defense': 140,
                 'level': 17,
                 'xp': 900,
                 'crit_chance': 25,
                 'delve_drop': consumables['deft fossil']},

    'Malboro': {'name': 'Malboro',
                'life': 1400,
                'attack': 500,
                'defense': 180,
                'level': 18,
                'xp': 1000,
                'crit_chance': 15,
                'delve_drop': consumables['deft fossil']},

    'Behemoth': {'name': 'Behemoth',
                 'life': 1800,
                 'attack': 700,
                 'defense': 220,
                 'level': 19,
                 'xp': 1300,
                 'crit_chance': 25,
                 'delve_drop': consumables['deft fossil']},

    'Dark Behemoth': {'name': 'Dark Behemoth',
                      'life': 2100,
                      'attack': 800,
                      'defense': 240,
                      'level': 20,
                      'xp': 1500,
                      'crit_chance': 25,
                      'delve_drop': consumables['deft fossil']},

    'Tiamat': {'name': 'Tiamat',
               'life': 3000,
               'attack': 900,
               'defense': 300,
               'level': 21,
               'xp': 1800,
               'crit_chance': 25,
               'delve_drop': consumables['fractured fossil']},

    'Reaver': {'name': 'Reaver',
               'life': 5000,
               'attack': 800,
               'defense': 350,
               'level': 22,
               'xp': 2500,
               'crit_chance': 0,
               'delve_drop': consumables['fractured fossil']}
}