import json
from random import choice


class Health:
    def __init__(self):
        self._healths = []
        self.picked_health = {}
        self.name = ''
        self.health = ''

        def load_healths(self):
            with open('./healths.json', 'r') as healthin:
                health_data = json.load(healthin)
            self._healths = health_data['Healths']

        load_healths(self)

        def pick_health(self):
            self.picked_health = self._healths[choice([x for x in range(0, len(self._healths))])]

        pick_health(self)

        def gen_parameters(self):
            self.name = self.picked_health['name']
            self.health = self.picked_health['health']

        gen_parameters(self)

    def __str__(self):
        return 'health name={}, health={}'.format(self.picked_health['name'], self.picked_health['health'])

    def __repr__(self):
        return 'health name={}, health={}'.format(self.picked_health['name'], self.picked_health['health'])
