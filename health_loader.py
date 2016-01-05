import json
from random import choice


class HealthLoader:
    def __init__(self):
        self._healths = []

    def load_healths(self):
        with open('./healths.json', 'r') as healthin:
            health_data = json.load(healthin)
        self._healths = health_data['Healths']

    def pick_health(self, *args):
        return self._healths[choice([x for x in range(0, len(self._healths))])]


class Health:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.health = kwargs['health']

    def __str__(self):
        return 'name={}, health={}'.format(self.name, self.health)

    def __repr__(self):
        return 'health name={}, health={}'.format(self.name, self.health)

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
