import json
from random import choice


class WeaponLoader:
    def __init__(self):
        self._weapons = []

    def load_weapons(self):
        with open('./weapons.json', 'r') as weaponin:
            weapon_data = json.load(weaponin)
        self._weapons = weapon_data['Weapons']

    def pick_weapon(self, *args):
        return self._weapons[choice([x for x in range(0, len(self._weapons))])]


class Weapon:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.damage = kwargs['damage']

    def __str__(self):
        return 'name={}, damage={}'.format(self.name, self.damage)

    def __repr__(self):
        return 'weapon name={}, damage={}'.format(self.name, self.damage)

'''
def main():
    wp = WeaponLoader()
    wp.load_weapons()
    # picked_spell = sp.pick_spell()
    w = Weapon(**wp.pick_weapon())
    return w


if __name__ == '__main__':
    main()
'''
