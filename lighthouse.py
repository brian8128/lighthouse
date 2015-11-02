__author__ = 'Brian'
import math
import random as r
from bayes import Bayes
import numpy as np

class Lighthouse(object):

    def __init__(self, m, d):
        self.m = m
        self.d = d
        self.create_dataset()

    def get_point(self):
        theta = math.pi * r.random()
        x = self.m - self.d / math.tan(theta)
        return x

    def create_dataset(self):
        self.dataset = [self.get_point() for i in range(0,500)]


class Finder(object):

    def __init__(self):
        self.lh = Lighthouse(.25,.75)
        x = np.linspace(0, 1, 99)
        y = np.linspace(0, 1, 99)
        pdf = {(xi,yi):1 for xi in x for yi in y}
        likelihood = lambda x, (d, m): d / (d**2 + (x-m)**2 )
        self.bayes = Bayes(pdf, likelihood)

    def solve_stuff(self):
        for datum in self.lh.dataset:
            self.bayes.update(datum)

    def print_distribution(self):
        self.bayes.print_distribution()

if __name__ == "__main__":
    f = Finder()
    f.solve_stuff()
    f.print_distribution()
    f.bayes.plot()