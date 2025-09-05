# Estatística Probabilística - Análise Combinatória (arranjo, combinação, permutação)
import math
from itertools import permutations, combinations
from scipy.special import perm, comb
import numpy as np
import pandas as pd

# Arranjos
# Fórmula: A = n! / (n - p)!
# Arranjo = fatorial de n dividido pelo fatorial de (n - p)
# n = total de elementos
# p = elementos tomados por vez
def arranjo(n, p):
    return math.factorial(n) / math.factorial(n - p)
print(arranjo(5, 3))  # Exemplo: arranjo de 5 elementos tomados 3 a 3

# Permutações
# Fórmula: P = n!
# Permutação = fatorial de n
# n = total de elementos
def permutacao(n):
    return math.factorial(n)
print(permutacao(5))  # Exemplo: permutação de 5 elementos

# Combinações
# Fórmula: C = n! / (p! * (n - p)!)
# Combinação = fatorial de n dividido pelo fatorial de p vezes o fatorial de (n - p)
# n = total de elementos
# p = elementos tomados por vez
def combinacao(n, p):
    return math.factorial(n) / (math.factorial(p) * math.factorial(n - p))
print(combinacao(5, 3))  # Exemplo: combinação de 5 elementos tomados 3 a 3
print(comb(5, 3))        # Usando scipy.special.comb
print(comb(5, 3, exact=True))  # Combinação exata

# Permutações e Combinações com itertools
elements = ['A', 'B', 'C', 'D', 'E']
# Permutações
permuts = list(permutations(elements, 3))  # Permutações de 3 elementos
print(permuts)
# Combinações
combs = list(combinations(elements, 3))    # Combinações de 3 elementos
print(combs)