def sum_count(a):
    total = 0
    for i in range(len(a)):
        total += (ord(a[i]) - ord("a"))
    return total

s = str(input())
t = str(input())

sum_t = sum_count(t)
s_sorted = "".join(sorted(s))
s_sorted_list = list(s_sorted)
s_sorted_list = s_sorted_list[:-1]
s_sorted_sum = sum_count(s_sorted_list)
replacement = chr((sum_t - s_sorted_sum - 1) + ord("a"))
s_sorted_list.append(replacement)
s_sorted = "".join(s_sorted_list)

if s_sorted != s:
    print(s_sorted)
else:
    print("No such string")
