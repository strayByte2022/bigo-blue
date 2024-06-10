def next_string(s):
    
    s_list = list(s)
    
    for i in range(len(s) - 1, -1, -1):
        if s_list[i] != 'z':
            s_list[i] = chr(ord(s_list[i]) + 1)
            return "".join(s_list[:i+1]) + 'a' * (len(s) - i - 1)
        s_list[i] = 'a'
    
    return "".join(s_list)

def find_intermediate_string(s, t):
    candidate = next_string(s)
    if candidate < t:
        return candidate
    return "No such string"

# Input
s = input().strip()
t = input().strip()

# Output
result = find_intermediate_string(s, t)
print(result)