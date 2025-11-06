import arrow, time

print('''Set your timer in hours or minuter
      -"timer for X hour"
      -"timer for Y minutes"
      -"timer for X hour Y minutes"''')
inp = input("Set your timer: ").lower()

# Get positions of keywords
pos1 = inp.find('timer for')
pos2 = inp.find('hour') # -1 if last inp is "timer for X hours"
pos3 = inp.find('minutes') # -1 if last inp is "timer for X hour Y minutes" "timer for Y minutes"

# user only set hours
if pos3 == -1:
    addmin = 0
    addhour = inp[pos1 + len('timer for'):pos2]
# if user only set minutes
elif pos2 == -1:
    addhour = 0
    addmin = inp[pos1 + len('timer for'):pos3]
    
# user set both hours and minutes
else:
    addhour = inp[pos1 + len("timer for"):pos2]
    addmin = inp[pos2 + len("hour"):pos3]
    
# Get the current time
current_hour = arrow.now().format('H')
current_min = arrow.now().format('m')
current_sec = arrow.now().format('s')

# Calculate the target time
new_hour = int(current_hour) + int(addhour)
new_min = int(current_min) + int(addmin)
new_sec = int(current_sec)

# Adjust for overflow of minutes and hours
if new_min >= 60:
    new_min -= 60
    new_hour += 1
new_hour = new_hour % 24

end_time = str(new_hour) + ':' + str(new_min) + ':' + str(new_sec)
print(f"Timer set for {addhour} hour(s) and {addmin} minute(s). It will go off at {end_time}.")

# Wait for the timer to finish
while True:
    current_time = arrow.now().format('H:m:s')
    if current_time == end_time:
        print("Time's up!")
        import os
        os.system('start alarm.wav')
        time.sleep(1)
        break
