import copy
from weapon import Weapons
from spell import Spell

class Hero:

	def __init__(self, name, title, health, mana, mana_regeneration_rate):
		self.name = name
		self.title = title
		self.health = health
		self.mana = mana
		self.mana_regeneration_rate = mana_regeneration_rate
		#self._weapon = Weapons("axe", 20)

	def __str__(self):
		return "{} the {}".format(self.name, self.title)

	def __repr__(self):
		return str(self)

	def know_as(self):
		return str(self)

	def get_health(self):
		return int(self.health)

	def get_mana(self):
		return int(self.mana)

	def is_alive(self):
		return self.get_health != 0

	def can_cast(self):
		return self.get_mana != 0

	def take_damage(self, damage_points):
		self.health -= damage_points


	def take_healing(self, healing_points):
		if self.health > 0:
			if self.health + healing_points > 100:
				self.health = 100
			else:
				self.health += healing_points


	def take_mana(self, mana_points):
		if self.health > 0:
			if self.health + mana_points > 100:
				self.health = 100
			else:
				self.health += mana_points

	def equip(self, weapon):
		self.weapon1 = weapon.get_damage()
		self.name1 = weapon.get_name()

	def learn(self, spell):
		self.spell1 = spell.get_name()
		self.damage1 = spell.get_damage()

	def attack(self, by, weapon, spell):
		if by == "weapon":
			return weapon.get_damage()
       	if by == "spell":
        	return spell.get_damage()

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
#print(h.know_as())
#print(h.get_health())
#print(h.get_mana())
#print(h.is_alive())
#print(h.can_cast())
h.take_damage(10)
print(h.get_health())
h.take_healing(5)
print(h.get_health())
#h.take_mana(1)
w = Weapons("axe", 20)
s = Spell("name", 5, 5, 5)
h.equip(w)
h.learn(s)
print(h.attack("weapon", w, s))
#h.take_healing(5)
#print(h.get_health())
