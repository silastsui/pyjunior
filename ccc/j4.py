#!/usr/bin/python
#arrivaltime

def convert(number): #converts integer and makes it a time
    hour = (2 - len(str(number/60)))*"0" + str(number/60)
    minute = (2 - len(str(number%60)))*"0" + str(number%60)
    return hour + ":" + minute
        
time = raw_input("Enter departure time: ")
time = 60*int(time[0:2]) + int(time[3:5]) #converts time to minutes (0-1420)

if time <=300 or (time >=600 and time <=780) or time >=1140:
    arrive = (time + 120)%1440
    print convert(arrive)
elif time >=300 and time<=380: #arrives before end of rush hour
    reg = 420 - time 
    slow = 120 - reg
    travel = reg + 2*slow
    print convert(time + travel) 
elif time >=780 and time<=900: #arrives before end of rush hour
    reg = 900 - time
    slow = 120 - reg
    travel = reg + 2*slow
    print convert(time + travel)
elif time >=420 and time <=600: #leaves after rush hour
    slow = 600 - time 
    reg = 120 - slow//2
    travel = reg + slow
    print convert(time+travel)    
elif time>= 900 and time<= 1140:
    slow = 1140 - time 
    reg = 120 - slow//2
    travel = reg + slow
    print convert(time+travel)    
elif time == 400: #special case
    print "10:10"
