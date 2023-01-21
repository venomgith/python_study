#Python study

x = 25 #if-else
if x == 25:
    print("Yes, you are right")
else:
    print("No, you are wrong")

print("======================================\n")

age = 10 #if-elif-else
if (age <= 20):
    print("you are smaller than 20")
elif (age > 20) and (age < 25):
    print("you are average guy")
else:
    print("You are older than 25")

print("\n-----------------THE END---------------------\n")

cars = ['toyota', 'lexus', 'bmw', 'mercedes', 'honda', 'seat', 'porsche'] #example with massive
japan_cars = ['toyota', 'lexus', 'honda']
print(cars)

if 'toyota' in cars:
    print("Toyota is in this list")
else:
    print("Toyota isn't in this list")

print("\n==========================================\n")

for x in cars:
    if x in japan_cars:
        print(str(x) + " is japan car")
    else:
        print(str(x) + " is not japan car")
