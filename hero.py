# from enemies import Enemy
from random import randint


class Hero:
    def __init__(self, name, title, health=100, mana=100):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.inventory = {}
        self.armed = ''
        self.damage = 0
        self.distance = 1
        self.mana_cost = 0

    def __str__(self):
        return '{} the {}'.format(self.name, self.title)

    def __repr__(self):
        return '{} the {}'.format(self.name, self.title)

    def known_as(self):
        return str(self)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self, spell_mana):
        return self.mana > spell_mana > 0

    def take_healing(self, health_amount):
        if self.health > 0:
            if self.health + health_amount > 100:
                self.health = 100
            else:
                self.health += health_amount
        else:
            print("Dead man cannot resurrect")

    def take_mana(self, mana_amount):
        if self.health > 0:
            if self.mana + mana_amount > 100:
                self.mana = 100
            else:
                self.mana += mana_amount
        else:
            print("Dead man do not need mana")

    def attack(self):
        self.take_healing(self.redeem())
        self.take_mana(self.redeem())
        return self.damage

    def take_damage(self, enemy):
        if self.health - enemy.attack() > 0:
            self.health -= enemy.attack()
        else:
            print("Hero has faced Death himself")

    def redeem(self):
        return randint(1, self.damage)

    def equip(self, item):
        if item in self.inventory.keys():
            if isinstance(self.inventory[item], Health):
                self.take_healing(self.inventory[item].health)
            elif isinstance(self.inventory[item], Mana):
                self.take_mana(self.inventory[item].mana)
            elif isinstance(self.inventory[item], Weapon):
                self.armed = self.inventory[item].name
                self.damage = self.inventory[item].damage
                self.mana_cost = 0
                self.distance = 1
            elif isinstance(self.inventory[item], Spell):
                self.armed = self.inventory[item].name
                self.damage = self.inventory[item].damage
                self.distance = self.inventory[item].cast_range
                self.mana_cost = self.inventory[item].mana_cost

    def collect(self, item):
        if isinstance(item, Health):
            self.inventory.update({'h': item})
        elif isinstance(item, Mana):
            self.inventory.update({'m': item})
        elif isinstance(item, Weapon):
            self.inventory.update({'w': item})
        elif isinstance(item, Spell):
            self.inventory.update({'s': item})
        return '{} is collected into inventory'.format(item.name)

    def drop(self,item):
        if item in self.inventory.keys():
            if self.armed == self.inventory[item].name:
                self.inventory.pop(item)
                self.armed = ''
                self.damage = 0
                self.distance = 1
                self.mana_cost = 0
            else:
                self.inventory.pop(item)
        else:
            pass

