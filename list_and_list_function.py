lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Gorge", "Tom"]

print(lucky_numbers)
print(friends)
print(lucky_numbers + friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Jole")  # add the given argument as an item in list at the last postion
print(friends)

friends.insert(2, "Kaylee")  # inserts a item as given index position
print(friends)

friends.remove("Jim")  # Removes the item from list which is given as argument
print(friends)

friends.pop()  # removes last item in list
print(friends)

print(friends.index(42))
friends.append("Jim")
print(friends)

print(friends.count("Jim"))  # print how many times item occoured in list
