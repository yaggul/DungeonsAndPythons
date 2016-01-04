from random import choice


class Treasure:
    def __init__(self):
        self.items = ['health_potion', 'mana_potion', 'weapon', 'spell']

    def pick_item(self, *args):
        return choice(self.items)


def main():
    tp = Treasure()
    t = tp.pick_item()
    print(t)

if __name__ == '__main__':
    main()
