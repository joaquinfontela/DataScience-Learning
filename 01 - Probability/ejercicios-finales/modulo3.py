import matplotlib.pyplot as plt
from numpy.random import binomial
import numpy as np
from scipy.stats import norm

mu = 4
sigma = 0.1


def ej1():
    X = 0.2
    prob = norm(mu, sigma).pdf(X)
    print(prob)


def ej2():
    X = -10
    prob = norm(mu, sigma).pdf(X)
    print(prob)


def ej3():
    X = 10
    prob = norm(mu, sigma).pdf(X)
    print(prob)


def ej4():
    X = 4
    prob = norm(mu, sigma).cdf(X)
    print(prob)


def ej5():
    X = 4
    prob = 1 - norm(mu, sigma).cdf(X)
    print(prob)


ej1()
ej2()
ej3()
ej4()
ej5()
