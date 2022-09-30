import random
while True:
    Temperature = random.randint(1,100)
    Humidity = random.randint(1,100)
    if( Temperature >  50 and Humidity < 50):
        print("Temperature:",Temperature,"and humidity:",Humidity," which is High, Alarm Detected.")
    elif( Temperature < 30  and Humidity < 30):
        print("Temperature:",Temperature,"and humidity :",Humidity," which is low, So Alarm will not be Detected")    
    break
