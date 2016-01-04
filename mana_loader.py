import json
from random import choice


class ManaLoader:
    def __init__(self):
        self._manas = []

    def load_manas(self):
        with open('./manas.json', 'r') as manain:
            mana_data = json.load(manain)
        self._manas = mana_data['manas']

    def pick_mana(self, *args):
        return self._manas[choice([x for x in range(0, len(self._manas))])]


class Mana:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.mana = kwargs['mana']

    def __str__(self):
        return ' name={}, mana={}'.format(self.name, self.mana)


def main():
    mp = ManaLoader()
    mp.load_manas()
    # picked_spell = sp.pick_spell()
    m = Mana(**mp.pick_mana())
    return m


if __name__ == '__main__':
    main()

