class Monster():
    def __init__ (self, name='monster1', health=200, shield=50, attack_damage = 40):
        self.name = name
        self.health = health
        self.shield = shield
    
    def attack(self):
        return (self.attack_damage*self.health) / 100
    
    def decrease_health (self, amount = 0):
        # self.shield -= amount
        # if self.shield < 0:
        #     self.health += self.shield
        #     self.shield = 0
        # if self.health <= 0:
        #     self.is_alive = False
        #     self.health = 0
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
