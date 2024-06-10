sizes = str(input()).split(" ")

size_A = int(sizes[0])
size_B = int(sizes[1])
km = str(input()).split(" ")
k = int(km[0])
m = int(km[1])
A = str(input()).split(" ")
B = str(input()).split(" ")
for i in range(size_A):
    A[i] = int(A[i])
for i in range(size_B):
    B[i] = int(B[i])
A2 = []
B2 = []

if A[0] > B[size_B-1]:
    print("NO")
    exit()

for i in range(k):
    A2.append(int(A[i]))
for i in range(size_B-1,size_B-m-1,-1):
    B2.append(B[i])

print(A2)
print(B2)

if B2[m-1] <= A2[k-1]:
    print("NO")
else: 
    print("YES")


