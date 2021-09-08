import functools


#demo1

def is_even(n):
    return n % 2 == 0


def update(n):
    return n * 2


def add(a, b):
    return a + b


nums = [3, 2, 6, 8, 5, 6, 2, 9]

evens = list(filter(is_even, nums))
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(update, nums))
doubles = list(map(lambda n: n * 2, nums))
print(doubles)

summe = functools.reduce(add, doubles)
summe = functools.reduce(lambda a, b: a + b, doubles)
print(summe)

# demo 2


result = functools.reduce(lambda x, y: x + y, [1, 2, 2, 2])
# schritt 1: 1+2 = 3
# schritt 2: 2+2 = 4
# schritt 3: 3+4 = 7


#  [1, 2, 2, 2]
#  [  3,   4]
#       7

print(result)

werte = [100, 1000, 20, 10]
biggest = functools.reduce(lambda x, y: x if (x > y) else y, werte)
print(biggest)

# filter
noten = [1, 5, 3, 2, 5, 6, 1]
print(list(filter(lambda x: x > 3, noten)))

# filter auf strings

woerter = ("test", "anna", "peter", "regallager")
# for word in woerter:
#    print(word[::-1])
print(list(filter(lambda word: word == word[::-1], woerter)))
