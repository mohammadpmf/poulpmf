from creature import *

class Monster(Creature):
    def __init__ (self, name='monster1', health=200, shield=50, attack_damage = 40):
        self.name = name
        self.health = health
        self.shield = shield
        self.attack_damage = attack_damage
        self.is_alive = True
        
    def decrease_health (self, amount = 0):
        if self.shield > 0:
            self.shield -= amount
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
            if self.health <= 0:
                self.is_alive = False
                self.health = 0
        else:
            self.health -= amount
            if self.health <= 0:
                self.is_alive = False
                self.health = 0
    def show_all_info(self):
        result = ''
        result += 'Name: '
        result += self.name
        result += '\nHelath: '
        result += str(self.health)
        result += '\nShield: '
        result += str(self.shield)
        result += '\nAttack damage: '
        result += str(self.attack_damage)
        return result