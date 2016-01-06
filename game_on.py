# from random import randint
# import json
# from random import choice
# from spells import Spell
# from weapon import Weapon
# from treasures import Treasure
from load_game import LoadGame
from cli import CLI
from dungeon import Dungeon
from health_loader import Health
from mana_loader import Mana
from weapon_loader import Weapon
from spell_loader import Spell
from hero import Hero
from enemies import Enemy


def main():
    lg = LoadGame()
    gmap = Dungeon(lg.level_to_load, Health, Mana, Weapon, Spell)
    gmap.gen_map_matrix()
    gmap.gen_map_string()
    gmap.find_map_start()
    hero = Hero(**lg.hero_parameters)
    # tr = Treasure(Health, Mana, Weapon, Spell, hero)
    interface = CLI(gmap, hero, Enemy)
    interface.start()


if __name__ == '__main__':
    main()
