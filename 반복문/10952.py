while(True):
    num1, num2 = map(int, input().split())

    result = num1 + num2

    if num1 == 0 and num2 == 0:
        exit()
    else:
        print(result)