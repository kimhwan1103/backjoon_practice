str = []
str = input().split

num1 = str[1]
num2 = str[2]

if num1 < num2:
    print("<")
elif num1 > num2:
    print(">")
elif num1 == num2:
    print("==")