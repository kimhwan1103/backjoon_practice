num1, num2 = map(int, input().split())

nums = list(map(int, input().split()))
result = []

for i in nums:
    if num2 > i:
        result.append(i)

for j in result:
    print(j, end=' ')