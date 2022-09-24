# we can handel errors/exceptions in python using try and except statement

try:
    ans = 10/0
    numbers = int(input("Enter the number: "))
    print(numbers)
except ZeroDivisionError as err:
    print(err)
except ValueError as val:
    print(val, "\ninvalid Input!")

