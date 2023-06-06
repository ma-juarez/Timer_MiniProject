from playsound import playsound
import time

#ANSI CODES TO MAKE TIMER PRETIER
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H" 

#Main timer function
def timer(seconds):
    seconds_elapsed = 0

    print(CLEAR) #Clear Terminal
    #Main timer loop
    while seconds_elapsed  < seconds: 
        time.sleep(1)
        seconds_elapsed += 1

        time_left = seconds - seconds_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d}:{seconds_left:02d}")
    #Alarm sound
    playsound("alarm.mp3")
    exit()



#Time input by user
user_minutes = int(input("How many minutes to wait: "))
user_seconds = int(input("How many seconds to wait: "))
total_seconds = user_minutes * 60  + user_seconds

timer(total_seconds)