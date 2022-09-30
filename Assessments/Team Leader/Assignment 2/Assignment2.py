import random
while True:
    T = random.randint(1,100)
    H = random.randint(1,100)
    if( T >  50 and H < 50):
        print("Temperature:",T,"and humidity:",H," is High and So Alarm is Detected")
    elif( T < 30  and H < 40):
        print("Temperature:",T," and humidity :",H," is low and So Alarm is Not Detected")    
    break
