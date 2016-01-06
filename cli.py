'''inheritance
gmap, hero, Enemy, tr
'''


class CLI:
    def __init__(self, *args):
        self.text = []
        self.fgmap = args[0]
        self.commands = {
            'up': [args[0].move_hero, 'up'],
            'down': [args[0].move_hero, 'down'],
            'left': [args[0].move_hero, 'left'],
            'right': [args[0].move_hero, 'right'],
            'map': [args[0].print_map, ''],
            'spawn': [args[0].spawn, args[0].map_entrance],
            'help': [self._help_message, ''],
            'collect': [args[1].collect, ''],
            'equip': [args[1].equip, ''],
            'check_items': [args[0].check_items, ''],
            'drop': [],
            'inventory': [args[1].open_inventory, ''],
            }

    def _hello_message(self):
        return 'Wellcome to Dungeon&Pythons.\nType <help> for list of supported game commands commands'

    def _help_message(self, *args):
        return 'List of supported commands:\n\
        map - Prints the map of the current level;\n\
        up - moves hero UP on the map;\n\
        down - moves hero DOWN on the map;\n\
        left - moves hero LEFT on the map;\n\
        right - moves hero RIGHT on the map;\n\
        spawn - puts the Hero st the starting "S" point on the map and respawns Hero on last save location\n\
        You need to spawn to begin the game;\n\
        help - prints this message;\n\
        pick_spell - picks a random spell for testing purposes;\n\
        quit - quits the game.'

    def start(self):
        print(self._hello_message())

        while True:
            console_input = input(">>> ")
            # try:
            self.text = console_input.split()
            print(self.text)
            command = self.text[0]

            if command == 'quit':
                break
            else:
                if len(self.text) == 1:
                    parameter = self.commands[command][1]
                elif command == 'collect':
                    parameter = self.fgmap.spawned_items[self.text[1]]
                    print(parameter)
                else:
                    parameter = self.text[1:]
            print(self.commands[command][0](parameter))
            # except:
            #    print('Unknown command. Type <help> for list of supported commands.')
