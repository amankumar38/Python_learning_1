#Dictionary: Key-Value Pairs, Unordered, Mutable

my_dict = {"Name":"Ram", "Age":28, "City":"Bhopal", "Car":"Honda City", "Profession":"Engineer"}
print(my_dict)

try:
    value = my_dict["Name"]
    print(value)
    value = my_dict["car"]
    print(value)
except KeyError as v:
    print("No assosiate value of ", v, "Found")


my_dict["E-mail"] = "ramk@xyz.com"
print(my_dict)

my_dict["E-mail"] = "ramkm@xyz.com"
print(my_dict)

#to delete item

del my_dict["E-mail"]
print(my_dict)

my_dict.pop("Car")
print(my_dict)

my_dict.popitem()
print(my_dict)

#to check/get item

my_dict = {"Name":"Ram", "Age":28, "City":"Bhopal", "Car":"Honda City", "Profession":"Engineer"}

if "Name" in my_dict:
    print(my_dict["Name"])
else:
    print("not found.")

print("\n")

for keys in my_dict.keys():  # For keys only
    print("Keys:", keys)

print("\n")

for value in my_dict.values():  # For values only
    print("Values:", value)

print("\n")

for keys, value in my_dict.items():   # for both keys and values
    print(keys, " : ", value)



# to copy dicts
my_dict_copy = my_dict.copy()
my_dict_copy["Email"] = "Ramkm@xyz.com"
print(my_dict)
print(my_dict_copy)

my_dict = {"Name":"Ram", "Age":28, "City":"Bhopal", "Car":"Honda City", "Profession":"Engineer"}
my_dict2 = {"Name":"Sham", "Age":25, "City":"Ranchi" }

my_dict.update(my_dict2)
print(my_dict)

# We can use tuples in dictionary
mytuples = (2,3)
mydict2 = {mytuples:5}
print(mydict2)

# we cannot use list in dictionary
