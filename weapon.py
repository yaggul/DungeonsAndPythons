from weapon_loader import WeaponLoader


class Weapon:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.damage = kwargs['damage']

    def __str__(self):
        return ' name={}, damage={}'.format(self.name, self.damage)


def main():
    wp = WeaponLoader()
    wp.load_weapons()
    # picked_spell = sp.pick_spell()
    w = Weapon(**wp.pick_weapon())
    return w


if __name__ == '__main__':
    main()
