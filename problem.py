from integrator import Integrator
from elements import Elements
from math import sin
import matplotlib.pyplot as plt
import numpy as np


class Problem:
    def __init__(self, n):
        self.n = n
        self.integrator = Integrator(n)
        self.elements = Elements(n)

    def integral(self, f):
        return self.integrator.integrate(f)

    def B(self, i, j):
        return -self.elements.e(i, 2) * self.elements.e(j, 2) + self.integral(
            lambda x: (self.elements.de(i, x) * self.elements.de(j, x)) - self.elements.e(i, x) * self.elements.e(j, x)
        )

    def L(self, j):
        return self.integral(lambda x: self.elements.e(j, x) * sin(x))

    def find_w(self):
        coefficient = [[self.B(i, j) if i - 1 <= j <= i + 1 else 0 for i in range(1, self.n + 1)] for j in
                       range(1, self.n + 1)]

        constant = [self.L(j) for j in range(1, self.n + 1)]
        w = np.linalg.solve(np.array(coefficient), np.array(constant))
        return w

    def u(self, x, w):
        y = []
        for i in range(len(x)):
            result = 0
            for j in range(len(w)):
                result += w[j] * self.elements.e(j + 1, x[i])
            y.append(result)

        return y

    def solve(self):
        x = np.linspace(0, 2, self.n+1)
        w = self.find_w()

        plt.plot(x, self.u(x, w), '-r', label='u(x)')
        plt.title('Acoustic vibrations of the material layer')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.grid()
        plt.show()
