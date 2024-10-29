import functools

words = ["id3", "touran", "golf", "passat"]
uppercase_words = list(map(lambda w: w.upper(), words))
print(uppercase_words)

numbers = list(range(1,11))

even_numbers = list(filter(lambda n: n%2 == 0, numbers))
print(even_numbers)



updated_numbers = list(map(lambda n:n**2, numbers))
print(updated_numbers)

summe = functools.reduce(lambda a,b:a+b,[1,2,3,4])
print(summe)


zahlen = [1,5,12,0,2,11]
print(list(filter(lambda n:n>5, zahlen)))
