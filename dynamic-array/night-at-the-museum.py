input_string = str(input())
input_string = "a"+input_string
minimal_step = 0
for i in range(len(input_string)-1):
    difference = abs(ord(input_string[i])-ord(input_string[i+1]))
    
    if(difference<= 13):
        minimal_step+=difference
        print(difference)
    else:
        reminder = difference-13
        difference = 13-reminder
        print(difference)
        minimal_step+=difference

print("Minimal steps: ", minimal_step)