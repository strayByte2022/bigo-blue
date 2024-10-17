n, x = input().split()
arr = list(map(int, input().split()))
n = int(n)
x = int(x)
sum = 0
arr.sort()

for i in arr:
    sum += i*x
    if x - 1 >= 1:
        x -= 1

print(sum)

