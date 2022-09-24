# Sets: Unorded, mutable, no dupkicates
my_set = {1, 2, 3}
print(my_set)

my_set.add(5)
print(my_set)
for i in my_set:
    print(i)

my_set2 = set("Hello World")
print(my_set2)


my_set3 = set({})
my_set3.add(1)
my_set3.add(3)
print(my_set3)
print(my_set3.pop())
print(my_set3.discard(3))


#calculation Union

odds = {1, 3, 5, 7, 9, 11, 13}
evens = {2, 4, 6, 8, 10, 12, 14}
primes = {2, 3, 5, 7, 11, 13, 17}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
i_2 = odds.intersection(primes)
print(i)
print(i_2)

d = odds.difference(evens)
print(d)

new_set = odds.intersection_update(evens)
print(new_set)

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set) #not mutable sets
