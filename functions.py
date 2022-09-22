from typing import List


def sayhi(name):
    print("Hello " + name)


sayhi("Mike")

list_names = ["Ajay", "Vijay", "Sanjay", "Manjay", "Dananjay"]
age = [20, 25, 36, 15, 70]

def say_hi(names):
    res = {}
    for i in list_names:
        for j in age:
            list_names.sort()
            age.sort()
            # print(i, age)
            # index = list_names.index(i)
            # index = index + 1
            # print(str(index) + ") " + " hello " + i)
            res[i] = j
            age.remove(j)
            break

    print(str(res))



say_hi(" ")
