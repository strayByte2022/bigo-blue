n = int(input())
inputs = []
for i in range(n):
    inputs.append(input())


def check(str):
    count = 0
    stack = []
    count_closing = 0
    for i in str:
        if i == '<':
            stack.append(i)
        else:
            if len(stack) != 0:
                count_closing += 1
                stack.pop()
                count += 1
            else:
                break

    if len(stack) != 0 or count != count_closing:
        print(0)
    else:
        print(count*2)

for i in range(n):
    check(inputs[i])

# <<<><> - 0
# <<><<>><< - 0
