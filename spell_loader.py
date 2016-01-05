import json
from random import choice


class SpellLoader:
    def __init__(self):
        self._spells = []

    def load_spells(self):
        with open('./spells.json', 'r') as spellin:
            spell_data = json.load(spellin)
        self._spells = spell_data['Spells']

    def pick_spell(self, *args):
        return self._spells[choice([x for x in range(0, len(self._spells))])]


class Spell:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.damage = kwargs['damage']
        self.mana_cost = kwargs['mana_cost']
        self.cast_range = kwargs['cast_range']

    def __str__(self):
        return ' name={}, damage={}, mana_cost={}, \
cast_range={}'.format(self.name, self.damage, self.mana_cost, self.cast_range)

    def __repr__(self):
        return 'spell - name={}, damage={}, mana_cost={}, \
cast_range={}'.format(self.name, self.damage, self.mana_cost, self.cast_range)

'''
def main():
    sp = SpellLoader()
    sp.load_spells()
    # picked_spell = sp.pick_spell()
    s = Spell(**sp.pick_spell())
    return s


if __name__ == '__main__':
    main()
'''
