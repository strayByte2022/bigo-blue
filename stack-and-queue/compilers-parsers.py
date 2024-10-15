n = int(input())
instructions = []
def count_pair(instruction):
    final_length = 0
    current_length = final_length
    queue = []
    for i in range(len(instruction)):
        if instruction[i] == "<":
            queue.append(instruction[i])
        else:
            if len(queue) == 0:
                break
            else:
                queue.pop()
                current_length+=2
        

    return current_length
        

for i in range (n):
    instructions.append(str(input()))

for i in range (len(instructions)):
    print(count_pair(instructions[i]))