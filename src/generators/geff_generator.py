from src.generators.generator import Generator
from src.generators.lfsr_generator import LFSR

class GeffGenerator(Generator):
    def __init__(self, seed1, seed2, seed3):
        self.lfsr1 = LFSR(seed1)
        self.lfsr2 = LFSR(seed2)
        self.lfsr3 = LFSR(seed3)
        super().__init__(seed1)
    
    @classmethod
    def from_interface(cls):
        seed1 = int(input("Введите сид для LFSR1: "))
        seed2 = int(input("Введите сид для LFSR2: "))
        seed3 = int(input("Введите сид для LFSR3: "))
        print("")

        return cls(seed1, seed2, seed3)
        
    def rand(self):
        return self.lfsr2.rand() if self.lfsr1.rand() == 0 else self.lfsr3.rand()
    
    @staticmethod
    def generator_str():
        return "Генератор Геффа"