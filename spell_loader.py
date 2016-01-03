import json
from random import choice


class SpellLoader:
    def __init__(self):
        self._spells = []

    def load_spells(self):
        with open('./spells.json', 'r') as spellin:
            data = json.load(spellin)
        self._spells = data['Spells']

    def pick_spell(self, *args):
        return self._spells[choice([x for x in range(0, len(self._spells))])]
