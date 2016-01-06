import json
from random import choice


class Weapon:
    def __init__(self):
        self._weapons = []
        self.picked_weapon = {}
        self.name = ''
        self.damage = ''

        def load_weapons(self):
            with open('./weapons.json', 'r') as weaponin:
                weapon_data = json.load(weaponin)
            self._weapons = weapon_data['Weapons']

        load_weapons(self)

        def pick_weapon(self, *args):
            self.picked_weapon = self._weapons[choice([x for x in range(0, len(self._weapons))])]

        pick_weapon(self)

        def gen_parameters(self):
            self.name = self.picked_weapon['name']
            self.damage = self.picked_weapon['damage']

        gen_parameters(self)

    def __str__(self):
        return 'weapon name={}, damage={}'.format(self.picked_weapon['name'], self.picked_weapon['damage'])

    def __repr__(self):
        return 'weapon name={}, damage={}'.format(self.picked_weapon['name'], self.picked_weapon['damage'])
