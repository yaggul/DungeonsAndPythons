from spell_loader import SpellLoader


class Spell:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.damage = kwargs['damage']
        self.mana_cost = kwargs['mana_cost']
        self.cast_range = kwargs['cast_range']

    def __str__(self):
        return ' name={}, damage={}, mana_cost={}, \
cast_range={}'.format(self.name, self.damage, self.mana_cost, self.cast_range)


def main():
    sp = SpellLoader()
    sp.load_spells()
    # picked_spell = sp.pick_spell()
    s = Spell(**sp.pick_spell())
    return s


if __name__ == '__main__':
    main()
