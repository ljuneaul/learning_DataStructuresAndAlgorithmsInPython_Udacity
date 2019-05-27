import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other


class D20(Die):
    def __init__(self):
        self = super().__init__(20)
        return self


class Hand(list):
    def __init__(self, amount=1):
        if not amount >= 1:
            raise ValueError("Must have at least 1 die")
        if not isinstance(amount, int):
            raise ValueError("Amount must be a whole number")
        for _ in range(amount):
            self.append(D20())

    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, amount):
        return cls(amount)


Hand().roll(2)
