import sys
from functools import lru_cache

# Exercise 5
sys.setrecursionlimit(10000)


@lru_cache()
def F(n):
    if n == 1: return 1
    if n > 1: return (3 * n + 5) * F(n - 1)


print(F(2073) / F(2070))


# Ответ: 240757875872.0


# Exercise 6
@lru_cache()
def F1(n):
    if n == 1: return 1
    if n > 1: return n * F1(n - 1) + 1


print(F1(1202) / F1(1200))


# Ответ: 1443602.0


# Exercise 10

def isSimple(number):
    for i in range(2, (int)(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True;


def F2(n):
    if n == 0: return 1
    if n > 0:
        return 7 * (n - 1) + F2(n - 1)


counterSimpleNumbers = 0
for i in range(2, 201):
    if isSimple(F2(i)):
        counterSimpleNumbers += 1
print(counterSimpleNumbers)
#Ответ: 43