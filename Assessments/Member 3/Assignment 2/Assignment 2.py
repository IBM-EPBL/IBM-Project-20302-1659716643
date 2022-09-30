import random
while True:
    temperature = random.randint(1,100)
    humidity = random.randint(1,100)
    #Temperature is taken in terms of celcius, not in fahrenheit
    if(temperature > 50 and humidity < 30):
        print("temperature: ",temperature," and humidity of:",humidity, "is high, So Alarm is Detected!!!")
    elif(temperature < 30 and humidity < 50):
        print("Temperature :",temperature, " and humidity of:",humidity, " is low, So Alarm is not Detected.")    
    break

