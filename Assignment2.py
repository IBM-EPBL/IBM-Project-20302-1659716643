#Temperature taken is as Celcius, not in Fahrenheit.
import random
while True:
    Temp = random.randint(1,100)
    Hmd = random.randint(1,100)
    if( Temp >  50 and Hmd < 50):
        print("Temperature:",Temp,"and humidity:",Hmd," is High, Alarm Detected!!")
    elif( Temp < 30  and Hmd < 30):
        print("Temperature:",Temp," and humidity :",Hmd," is low, Alarm Not Detected")    
    break
