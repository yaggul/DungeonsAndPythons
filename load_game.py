''' Hero, Dungeon'''


class LoadGame:
    def __init__(self):
        self.hero_parameters = {}
        self.levels = {'1': 'level1.txt', '2': 'level2.txt', '3': 'level3.txt', '4': 'level4.txt'}
        self.str_level = '\n 1: level1\n 2: level2\n 3: level3\n 4: level4'
        self.level_to_load = ''

        def create_hero(self):
            name = input('Please input Hero <Name>: ')
            title = input('Please input Hero <Tittle>: ')
            self.hero_parameters = {'name': name, 'title': title}

        def choose_level(self):
            print(self.str_level)
            while self.level_to_load not in self.levels.keys():
                self.level_to_load = input('Please choose level number from the list above: ')
            self.level_to_load = self.levels[self.level_to_load]

        def wellcome(self):
            print('Wellcome to Dungeon&Pythons')

        wellcome(self)
        create_hero(self)
        choose_level(self)
