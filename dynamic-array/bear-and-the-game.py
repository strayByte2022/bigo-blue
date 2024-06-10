no_minutes = int(input())

minutes = str(input())
minutes = "0 " + minutes
minutes = minutes.split(" ")
time_watched=0
before_90=True
for i in range(0,no_minutes):
    time_difference = int(minutes[i+1])-int(minutes[i])
    if(time_difference > 15):
        time_watched += 15
        before_90 = False
        break

    time_watched = int(minutes[i+1])

if minutes[no_minutes]!="90" and before_90:
    end_time = time_watched+15
    if end_time >90:
        print(90)
    else:
        print(end_time)
else:
    print(time_watched)

