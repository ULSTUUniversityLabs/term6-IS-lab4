from src.generators.generator import Generator

class MillerParkGenerator(Generator):
    def __init__(self, seed):
        super().__init__(seed)
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1
        
    def rand(self):
        self.rng_state = (self.m * self.rng_state) % self.a
        return self.rng_state & 1
    
    @staticmethod
    def generator_str():
        return "Генератор Парка-Миллера"