
number_of_button = int(input())
button_string = str(input()).split(" ")
zero_count = 0
for i in range(len(button_string)):
    if button_string[i] == "0":
        zero_count+=1
if (number_of_button == 1 and zero_count==1) or (zero_count>1) or(zero_count==0 and number_of_button>1):
    print("NO")
else:
    print("YES")

    

