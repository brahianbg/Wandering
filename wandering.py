import random

class Wandering:
    
    def __init__(self, name):
        self.name = name
        
class ComunWandering(Wandering):
    
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        return random.choice([(0, 1),(0, -1), (1, 0), (-1, 0)])