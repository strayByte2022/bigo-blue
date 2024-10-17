inputs = []

while True:
    a = int(input())
    if a == 0:
        break
    else:
        inputs.append(a)

def throw(num):
    discarded = []
    arr = list(range(1, num+1))

    while len(arr) >= 2:
        discarded.append(arr.pop(0))
        top = arr.pop(0)
        arr.append(top)

    if len(discarded) == 0:
        print("Discarded cards:")
    else:
        print("Discarded cards:", ', '.join(map(str, discarded)))
    print("Remaining card:", str(arr[0]))

for i in inputs:
    throw(i)
