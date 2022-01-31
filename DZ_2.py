from abc import ABC, abstractmethod

class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence (self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence()


    def __str__(self):
        return f'пальто размер {self.size}, расход ткани {self.expence()}, общий расход {Coat.expence_count:.02f}'


    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float (f'{exp:.02f}')
