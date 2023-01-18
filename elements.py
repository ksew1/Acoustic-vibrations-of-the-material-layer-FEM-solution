class Elements:
    def __init__(self, n):
        self.n = n

    def xi(self, i):
        return (2 / self.n) * i

    def e(self, i, x):
        if self.xi(i - 1) < x < self.xi(i):
            return (x - self.xi(i - 1)) / (self.xi(i) - self.xi(i - 1))
        elif self.xi(i) <= x < self.xi(i + 1):
            return (self.xi(i + 1) - x) / (self.xi(i + 1) - self.xi(i))
        else:
            return 0

    def de(self, i, x):
        if self.xi(i - 1) < x < self.xi(i):
            return 1 / (self.xi(i) - self.xi(i - 1))
        elif self.xi(i) <= x < self.xi(i + 1):
            return -1 / (self.xi(i + 1) - self.xi(i))
        else:
            return 0
