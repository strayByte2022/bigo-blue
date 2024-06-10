def check_automation(s,t):
    # remove chars 
    if len(s)>len(t):
        return t in s
    return s in t

def check_array(s,t):
    # swap chars 
    if len(s)!= len(t):
        return False
    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))
    return sorted_s == sorted_t

s = str(input())
t = str(input())

freq_1 = [0]*30
freq_2 = [0]*30

same_dict = True
for i in range(len(s)):
    freq_1[ord(s[i])-ord('a')]+=1

for i in range(len(t)):
    freq_2[ord(t[i])-ord('a')]+=1

for i in range(26):
    if freq_1[i]!=freq_2[i]:
        same_dict = False
        break

if len(s) > len(t):
    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))
    print(sorted_s)
    print(sorted_t)
    
    if check_automation(s,t) and check_array(s,t):
        print("both")
    elif check_automation(s,t):
        print("automation")
    else:
        print("need tree")
elif len(s) == len(t):
    if check_array(s,t):
        print("array")
    else:
        print("need tree")
