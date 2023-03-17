#1a
persons = ['tina', 'marcus', 'natalie', 'dirk']
uppered_persons = []

for person in persons:
    persons_ = person.capitalize()
    uppered_persons.append(persons_)
    
print(uppered_persons)

#1b
persons = ['tina', 'marcus', 'natalie', 'dirk']
uppered_persons = list(map(str.capitalize, persons))

print(uppered_persons)

#2a
floating_numbers = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, floating_numbers))

print(result)

#2b
floating_numbers = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, floating_numbers, range(1,7)))

print(result)

#3
my_chars = ['a', 'b', 'c', 'd', 'e']
my_nums = [1,2,3,4,5]
result = list(zip(my_chars, my_nums))

print(result)

#4
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
def is_over80(score):
    return score > 80
  
passing = list(filter(is_over80, scores))
print(passing)

# oder mit anonymer Funktion:
list(filter(lambda s: s > 80, scores))

#5
myStrings = ("Regallager", "Anna", "C++", "python", "Volkswagen", "PHP")
palindromes = list(filter(lambda word: word.upper() == word.upper()[::-1], myStrings)) # alternativ lower()
print(palindromes)

#6
from functools import reduce

myNumbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second
    
result = reduce(custom_sum, myNumbers)
print(result)

#7
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def group_function(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
result = group_by(input_list, group_function)
print(result)
