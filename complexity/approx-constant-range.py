n = int(input())
a = list(map(int, input().split()))

right = 0
cnt_diff = 0
best = 0
freq = [0] * (100000 + 5)

for left in range(n):
    while right < n and cnt_diff <= 2:
        if cnt_diff == 2 and freq[a[right]] == 0:
            break
        if freq[a[right]] == 0:
            cnt_diff += 1
        freq[a[right]] += 1
        right += 1

    best = max(best, right - left)
    
    if freq[a[left]] == 1:
        cnt_diff -= 1
    freq[a[left]] -= 1

print(best)
