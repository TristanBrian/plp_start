# implementing basic library functions
import math

print (math.sqrt(16))
print (math.pi)


# generate random numbers
import random

print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

# work with dates and time
import datetime

today = datetime.date.today()
print("Today's date is:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))