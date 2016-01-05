# from random import randint
# import json
# from random import choice
from cli import CLI
from dungeon import Dungeon
from enemies import Enemy
from spell_loader import SpellLoader
# from spells import Spell
from weapon_loader import WeaponLoader
# from weapon import Weapon
from health_loader import *
from mana_loader import *


def main():
    gmap = Dungeon('level2.txt')
    gmap.gen_map_matrix()
    gmap.gen_map_string()
    gmap.find_map_start()
    sp = SpellLoader()
    sp.load_spells()
    wp = WeaponLoader()
    wp.load_weapons()
    hp = HealthLoader()
    hp.load_healths()
    mp = ManaLoader()
    mp.load_manas()
    interface = CLI(gmap, sp, wp, hp, mp, ,Hero, Enemy)
    interface.start()


if __name__ == '__main__':
    main()
