n = int(input())
arr = list(map(int, input().split()))
arr.sort()
current = arr[0]
highest = 0
count = 0
types = 1
for i in arr:

    if i == current:
        count += 1
    else:
        count = 1
        types += 1
        current = i
    highest = max(count, highest)
print(highest, types)
