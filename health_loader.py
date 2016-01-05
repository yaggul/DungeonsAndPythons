import json
from random import choice


class Health:
    def __init__(self):
        self._healths = []
        self.picked_spell = {}
        # self.name = kwargs['name']
        # self.health = kwargs['health']

        def load_healths(self):
            with open('./healths.json', 'r') as healthin:
                health_data = json.load(healthin)
            self._healths = health_data['Healths']

        load_healths(self)

    def pick_health(self):
        return self._healths[choice([x for x in range(0, len(self._healths))])]

    def __str__(self):
        return 'name={}, health={}'.format(self.picked_spell['name'], self.picked_spell['health'])

    def __repr__(self):
        return 'name={}, health={}'.format(self.picked_spell['name'], self.picked_spell['health'])

'''
def main():
    hp = HealthLoader()
    hp.load_healths()
    # picked_spell = sp.pick_spell()
    h = Health(**hp.pick_health())
    #return h
    print(h)

if __name__ == '__main__':
    main()
'''
