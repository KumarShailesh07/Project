import datefinder
import datetime
import winsound

def alarm(text):
    date_timeA = datefinder.find_dates(text)
    for i in date_timeA:
        print(i)
    stringA = str(i)  # convert it into str
    time = stringA[11:]   #slice time in string 
    hourA = int(time[:-6])   #convert str in int and slice it
    minutesA = int(time[3:-3])  #convert str in int and slice it
    #secondsA = int(time[6:])   #we use this to set seconds in alarm
    
    while True:
        if hourA == datetime.datetime.now().hour:
            if minutesA == datetime.datetime.now().minute:
                print("Alarm is running...")
                winsound.PlaySound("C:\\Users\\hp\Desktop\\My Code\\Projects\\Alarm-chosic.com_ (2)",winsound.SND_LOOP)
            elif minutesA < datetime.datetime.now().minute:
                break
    
text = input("Input time to set alarm[seperate by : and in 24 hour system] -> ")
alarm(text)