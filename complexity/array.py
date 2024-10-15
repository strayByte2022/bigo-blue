n, k = map(int, input().split())
a = str(input()).split(" ")
a = [int(a) for a in a]
fre = [0] * (10 ** 5 + 5)
unique = 0
j = 0

for i in range(n):
    if fre[a[i]] == 0:
        unique += 1
    
    fre[a[i]] += 1

    while unique == k:
        # this steps is to eliminate duplicated values
        # 1 1 2 2 3 3 4 5
        # when reaching a[4] = 3, there are 3 unique digits, but 5 numbers in that range from the array_start
        # to eliminate the exceeding 1s
        fre[a[j]] -= 1

        if fre[a[j]] == 0:
            print(j + 1, i + 1)
            exit()
        
        j += 1

print('-1 -1')
