from src.generators.generator import Generator

class LFSR(Generator):
    def __init__(self, seed):
        seed = 1 if seed == 0 else seed
        super().__init__(seed)
        self.mask = (1 << 32) | (1 << 7) | (1 << 5) | (1 << 3) | (1 << 2) | (1 << 1) | (1 << 0) # маска (32, 7, 5, 3, 2, 1, 0)
        
    # def rand(self):
    #     if self.rng_state & 0x00000001:
    #         self.rng_state = (self.rng_state ^ self.mask >> 1) | 0x8000000
    #         return 1
    #     else:
    #         self.rng_state >>= 1
    #         return 0

    def rand(self):
        lsb = self.rng_state & 0x00000001  # Получаем младший бит состояния
        self.rng_state >>= 1  # Сдвигаем регистр на 1 вправо
        if lsb:  # Если младший бит был 1, то применяем обратную связь
            self.rng_state ^= self.mask  # Применяем маску
        return lsb  # Возвращаем младший бит
    
    @staticmethod
    def generator_str():
        return "Генератор LFSR"