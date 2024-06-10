first_line = str(input()).split(" ")
no_passwords = int(first_line[0])
max_tries = int(first_line[1])
passwords = []
best_case = 1
worst_case = 0
for i in range(no_passwords+1):
    passwords.append(str(input()))


real_password = passwords[no_passwords]
real_password_length = len(real_password)
current_attempt = 0
smaller_list = []
bigger_list = []


for i in range(no_passwords):
    current_length = len(passwords[i])
    if current_length < real_password_length:
        smaller_list.append(passwords[i])
    elif current_length > real_password_length:
        bigger_list.append(passwords[i])

no_passwords = no_passwords-len(bigger_list)

if(len(smaller_list) == 0):
    best_case = 1
elif(len(smaller_list)+1 <=max_tries):
    best_case = len(smaller_list)+1
else:
    reminder = (len(smaller_list)+1)%max_tries
    if reminder == 0: 
        best_case = len(smaller_list)+1+5*((len(smaller_list)+1)/max_tries-1)
    
    else:
        best_case = len(smaller_list)+1+5*((len(smaller_list)+1)//max_tries)

if(no_passwords <= max_tries):
    worst_case = no_passwords
else:
    if no_passwords % max_tries == 0:
        worst_case = no_passwords+5*(no_passwords/max_tries-1)
    else:
        
        worst_case = no_passwords+5*(no_passwords//max_tries)

print(str(best_case)+" "+str(worst_case))