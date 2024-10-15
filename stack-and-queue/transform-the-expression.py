from collections import deque

n = int(input())
expressions = []


def convert_string(expression):
    alphabet = deque()
    character1 = deque()

    result_string = ""
    for i in range(len(expression)):
        if ord("a") <= ord(expression[i]) <= ord("z"):
            alphabet.append(expression[i])
        else:
            if expression[i] == "+":
                character1.append(expression[i])
            if expression[i] == "-":
                temp = character1.pop()
                character1.append(expression[i])
                character1.append(temp)

        if expression[i] == ")":

            temp = ""
            while len(alphabet) > 0:
                temp += alphabet.popleft()
            result_string += temp
            if i < len(expression) - 1:
                result_string += character.pop()
            else:
                result_string += character.pop()

    return result_string


for i in range(n):
    expressions.append(str(input()))

for i in range(n):
    print(convert_string(expressions[i]))
