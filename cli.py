class CLI:
    def __init__(self, *args):
        self.commands = {
            'up': [args[0].move_hero, 'up'],
            'down': [args[0].move_hero, 'down'],
            'left': [args[0].move_hero, 'left'],
            'right': [args[0].move_hero, 'right'],
            'print_map': [args[0].print_map, ''],
            'spawn': [args[0].spawn, args[0].map_entrance],
            'help': [self._help_message, ''],
            'pick_spell': [args[1].pick_spell, '']
            }

    def _hello_message(self):
        return 'Wellcome to Dungeon&Pythons.\nType <help> for list of game commands'

    def _help_message(self, *args):
        return 'Here goes the commands'

    def start(self):
        print(self._hello_message())

        while True:
            console_input = input(">>> ")
            try:
                text = console_input.split()
                command = text[0]
                if command == 'quit':
                    break
                print(self.commands[command][0](self.commands[command][1]))
            except:
                print('Unknown command. Type <help> for list of commands.')
