t = int(input())
arr = []
operators = ['+','-','*','/','^']
for i in range(t):
    n = input()
    arr.append(n)


def transform(str):
    stack = []
    result = ""
    for i in str:
        if i.isalpha():
            result += i
        elif i in operators:
            stack.append(i)
        elif i == ')':
            op = stack.pop() # already popped from stack
            result += op

    print(result)


for i in range(t):
    transform(arr[i])
