from scipy.special import roots_legendre


class Integrator:
    def __init__(self, i):
        self.x, self.w = roots_legendre(i * 3)
        self.x = self.x + 1

    def integrate(self, f):
        result = 0
        for index in range(self.x.size):
            result += self.w[index] * f(self.x[index])
        return result
