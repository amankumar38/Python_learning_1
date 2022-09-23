is_male = True
is_tall = False

if is_male and is_tall:
    print("tall male")
elif is_male and not (is_tall):
    print("Not Tall male")
elif not (is_male) and is_tall:
    print("Tall but not male")
else:
    print("Neither male nor tall")


def max_num(num1, num2, num3):
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num("", "", ""))


