import random

temp = random.randint(1,100)
humd = random.randint(1,100)
#Temperature value is calculated for Celsius
if( temp > 75 and humd < 50):
    print("Temperature:",temp,"is High and humidity:",humd," is Low : High Temperature Hazard")
    print("ALARM DETECTED")
elif( temp < 10  and humd < 40):
    print("Temperature:",temp,"is Very low and humidity :",humd," is low : Low Temperature Hazard")    
    print("ALARM DETECTED")
elif( temp < 50 and humd > 60):
    print("High Humid Condition")
    print("ALARM NOT DETECTED")
elif(temp > 80):
    print("High Temperature Detected")
    print("ALARM DETECTED")
else:
    print("Normal Condition")
    print("ALARM NOT DETECTED")
