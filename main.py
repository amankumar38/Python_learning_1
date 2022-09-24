from classes_objects import student

name = "Mike Thompson Junior"
age = "65"

print("There once was a man name " + name + ", ")
print("he was " + age + " years old")

print("Hello\nWorld")  # print in next line

print(name.isupper())  # check if string is in uppercase or not
print(name.upper().isupper())  # frist convert to upper then check
print(name.islower())  # check if string is in lowercase or not
print(name.lower().islower())  # frist convert to lower then check
print(len(name))  # print lenght of string
print(name[0])  # print character at index 0
print("\n")
for i in name:
    print(i)

print(name.index("i"))
print(name.replace("Mike", "Spike"))

student1 = student("Jim", "B.tech", 5.8, False)

print("Name: ", student1.name)
print("Gpa: ", student1.gpa)
