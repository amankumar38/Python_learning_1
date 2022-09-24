file = open("C:/Users/amank/Downloads/data/employees.txt", "r")
for data in file.readlines():
    print(data)
file.close()
