import sys 

num1 = int(input())

for i in range(num1):
    num2, num3 = map(int, input().split())
    print(f'Case #{i + 1}: {num2 + num3}')