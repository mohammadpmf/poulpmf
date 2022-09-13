class Soldier():
    def __init__ (self, name='soldier1', health=100, attack_damage = 20):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.is_alive = True

    def attack(self):
        return (self.attack_damage*self.health) / 100

    def decrease_health (self, amount = 0):
        self.health -= amount
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
    
    def __repr__(self):
        return str(self.name)