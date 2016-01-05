import json
from random import choice


class Mana:
    def __init__(self):
        self._manas = []
        self.picked_mana = {}

        def load_manas(self):
            with open('./manas.json', 'r') as manain:
                mana_data = json.load(manain)
            self._manas = mana_data['Manas']

        load_manas(self)

        def pick_mana(self):
            self.picked_mana = self._manas[choice([x for x in range(0, len(self._manas))])]

        pick_mana(self)

    def __str__(self):
        return 'mana name={}, mana={}'.format(self.picked_mana['name'], self.picked_mana['mana'])

    def __repr__(self):
        return 'mana name={}, mana={}'.format(self.picked_mana['name'], self.picked_mana['mana'])
