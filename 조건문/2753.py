num1 = input()
num1 = int(num1)

if num1 % 4 == 0 and num1 % 100 != 0 or num1 % 400 == 0:
    print("1")
else: 
    print("0")
