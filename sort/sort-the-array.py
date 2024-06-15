n = int(input())
A = list(map(int, input().split()))

start_index = 0
end_index = n - 1


while start_index < end_index and A[start_index] < A[start_index + 1]:
    start_index += 1


while end_index > start_index and A[end_index] > A[end_index - 1]:
    end_index -= 1


A[start_index:end_index + 1] = reversed(A[start_index:end_index + 1])

if A == sorted(A):
    print("yes")
    # Print the 1-based indices of the segment
    print(start_index + 1, end_index + 1)
else:
    print("no")