n = int(input())
times = str(input()).split(" ")
times = [int(time) for time in times]
left = 0
right = n - 1
alice_time = 0
bob_time = 0
alice_count = 0
bob_count = 0
while left <= right:
    if alice_time <= bob_time:
        alice_time += times[left]
        alice_count += 1
        left += 1
    else:
        bob_time += times[right]
        bob_count += 1
        right -= 1
print(alice_count, bob_count)
