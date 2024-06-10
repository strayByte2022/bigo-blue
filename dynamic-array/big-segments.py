segments = int(input())
min_i = 1000000000000
max_j = -1
seg_list = []
result_index = -1
for i in range(segments):
    element = str(input()).split(" ")
    elements = []
    elements.append(int(element[0]))
    elements.append(int(element[1]))
    if int(elements[0]) <= min_i:
        min_i = elements[0]
    if int(elements[1]) >= max_j:
        max_j = elements[1]
    seg_list.append(elements)

for i in range(segments):
    if min_i == seg_list[i][0] and max_j == seg_list[i][1]:
        result_index = i+1 
print(result_index)
