n = int(input())
num = n
cnt = 0

while(True):
    num1 = num // 10
    num2 = num % 10
    num3 = (num1 + num2) % 10
    num = ( num2 * 10) + num3
    cnt = cnt + 1
    if num == n:
        break

print(cnt)