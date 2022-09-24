# Tuples: Ordered, Immutable, allows Duplicate elements

my_tuples = ("Ram", 25, "Bhopal")
print(my_tuples)

my_tuples2 = "Ram", 25, "Bhopal"  # Parenthesis are optional
print(my_tuples2)

if "Ram" in my_tuples:
    print("yes")
else:
    print("No")
try:
    tuple_len_check = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    print(len(tuple_len_check))
    print(tuple_len_check.count('e'))
    print(tuple_len_check.index('a'))
    print(my_tuples.index(9))
except ValueError as val:
    print(val)

name, age, city = my_tuples
print(name)
print(age)
print(city)


# size comparison
import  sys
import timeit
my_list = ["Ram", 25, "Bhopal"]
my_tuple = ("Ram", 25, "Bhopal")
print(sys.getsizeof(my_list), "bytes") # list takes more size even with same elements
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt="[42, 8, 23, 16, 15, 4]", number=1000000)) #list takes more time to create same list with elements as of tuples
print(timeit.timeit(stmt="(42, 8, 23, 16, 15, 4)", number=1000000))

