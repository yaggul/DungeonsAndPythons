# class enemies


from random import randint


class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.health = 100
        self.mana = 100
        self.damage = 20

    def is_alive(self):
        if self.get_health():
            return True

    def can_cast(self, spell_mana):
        return self.mana > spell_mana > 0

    def get_health(self):
        print(self.health)

    def get_mana(self, mana_amount):
        print(self.mana)

    def take_healing(self, health_amount):
        if self.health > 0:
            if self.health + health_amount > 100:
                self.health = 100
            else:
                self.health += health_amount
        else:
            print("Dead monsters cannot resurrect")

    def take_mana(self, mana_amount):
        if self.mana > 0:
            if self.mana + mana_amount > 100:
                self.mana = 100
            else:
                self.mana += mana_amount
        else:
            print("Dead monsters do not need mana")

    def attack(self):
        self.take_healing(self.redeem())
        self.take_mana(self.redeem())
        return self.damage

    def take_damage(self, hero):
        if self.health - hero.attack() > 0:
            self.health -= hero.attack()
        else:
            print("Enemy is DEAD")

    def redeem(self):
        return randint(1, self.damage)
