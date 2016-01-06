'''order fo inheritance
Health, Mana, Weapon, Spell, Hero
'''
from random import choice


class Treasure:
    def __init__(self, *args):
        self.items = ['h', 'm', 'w', 's']
        self.spawned_items = {}
        self.c_items = args[:]
        self.tr_commands = {
            'collect': [args[4].collect, ''],
            'check_items': [self.check_items, ''],
            'leave': [],
            'help': [self.tr_help],
            'drop': [args[4].drop, ''],
            'inventory': [args[4].inventory, ''],
        }

    def pick_item(self):
        return choice(self.items)

    def enter(self):
        print(self.tr_wellcome())

        while True:
            tr_input = input('treasury > ')
            try:
                text = tr_input.split()
                tr_command = text[0]
                if len(text) == 1:
                    parameter = self.tr.commands[tr_command][1]
                else:
                    parameter = text[1:]
                print(self.tr_commands[tr_command][0](parameter))
            except:
                print('Unknown command. Type <help> for list of supported commands.')

    def spawn_item(self, item):
        if item == 'h':
            h = self.c_items[0]()
            self.spawned_items.update({'h': h})
        elif item == 'm':
            m = self.c_items[1]()
            self.spawned_items.update({'m': m})
        elif item == 'w':
            w = self.c_items[2]()
            self.spawned_items.update({'w': w})
        elif item == 's':
            s = self.c_items[3]()
            self.spawned_items.update({'s': s})
        print(item)
        print(self.spawned_items)

    def tr_help(self):
        pass

    def check_items(self, *args):
        return self.spawned_items

    def tr_wellcome(self):
        return '\n\
            After you enter the treasury you found\n\
            some items that can be of service.\n\
            Type <help> for list of supported commands.'
