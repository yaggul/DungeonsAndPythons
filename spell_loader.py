import json
from random import choice


class Spell:
    def __init__(self):
        self._spells = []
        self.picked_spell = {}
        self.name = ''
        self.damage = ''
        self.mana_cost = ''
        self.cast_range = ''

        def load_spells(self):
            with open('./spells.json', 'r') as spellin:
                spell_data = json.load(spellin)
            self._spells = spell_data['Spells']

        load_spells(self)

        def pick_spell(self, *args):
            self.picked_spell = self._spells[choice([x for x in range(0, len(self._spells))])]

        pick_spell(self)

        def gen_parameters(self):
            self.name = self.picked_spell['name']
            self.damage = self.picked_spell['damage']
            self.mana_cost = self.picked_spell['mana_cost']
            self.cast_range = self.picked_spell['cast_range']

        gen_parameters(self)

    def __str__(self):
        return 'spell name={}, damage={}, mana_cost={}, \
cast_range={}'.format(self.picked_spell['name'], self.picked_spell['damage'], self.picked_spell['mana_cost'], self.picked_spell['cast_range'])

    def __repr__(self):
        return 'spell name={}, damage={}, mana_cost={}, \
cast_range={}'.format(self.picked_spell['name'], self.picked_spell['damage'], self.picked_spell['mana_cost'], self.picked_spell['cast_range'])
