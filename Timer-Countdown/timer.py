import os, time
from playsound import playsound
import multiprocessing

def collectInfo():
    seconds = ""
    os.system('cls' if os.name == 'nt' else 'clear')
    while(not isinstance(seconds,int)):
        seconds = input("How Many Seconds would you like your timer to be :   ")
        try:
            seconds = int(seconds)
        except:
            print("The value you entered isn't a valid duration")
       


    os.system('cls' if os.name == 'nt' else 'clear')
    sound_choice = input(''' 
                        1. Classic alarm (Default)
                        2. Rooster
                        3. Beeping
                        (Press Enter for default)
                        ''')
    if sound_choice not in ["1","2","3"]:
        sound_choice = 1
    return seconds, sound_choice

def formatDuration(duration):
    durationFormatted =  time.strftime('%H:%M:%S', time.gmtime(duration))
    print(durationFormatted)

def triggerSound(sound_choice):

    p = multiprocessing.Process(target=playsound, args=(f"sounds/alarm-{sound_choice}.mp3",False))
    p.start()
    print(" BEEP BEEP BEEP !")
    input("press ENTER to exit")
    p.terminate()
    



def countdown(seconds,sound_choice):
    duration = seconds
    while duration>=0:
        os.system('cls' if os.name == 'nt' else 'clear')
        formatDuration(duration)
        duration -= 1
        time.sleep(1)
    triggerSound(sound_choice)



duration,sound_choice = collectInfo()
countdown(duration,sound_choice)