from random import randint
import json
from random import choice
from cli import CLI
from dungeon import Dungeon
from enemies import Enemy
from spell_loader import SpellLoader
from spells import Spell


def main():
    gmap = Dungeon('level2.txt')
    gmap.gen_map_matrix()
    gmap.gen_map_string()
    gmap.find_map_start()
    sp = SpellLoader()
    sp.load_spells()
    interface = CLI(gmap, sp, Enemy)
    interface.start()


if __name__ == '__main__':
    main()
