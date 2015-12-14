class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.health = 100
        self.mana = 100
        self.damage = 20

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        self.mana > 0

    def get_health(self):
        return self.health

    def get_mana(self, mana_amount):
        return self.mana

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
        pass

    def take_damage(self):
        pass
