import json
from random import choice


class WeaponLoader:
    def __init__(self):
        self._weapons = []

    def load_weapons(self):
        with open('./weapons.json', 'r') as weaponin:
            weapon_data = json.load(weaponin)
        self._weapons = weapon_data['Spells']

    def pick_weapon(self, *args):
        return self._weapons[choice([x for x in range(0, len(self._weapons))])]
