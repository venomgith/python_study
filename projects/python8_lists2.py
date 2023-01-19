# Python Study

#         0          1         2        3         4        5
cars = ['bmw', 'volkswagen', 'seat', 'skoda', 'toyota', 'lexus']

print(cars)

for x in cars:    #Vivod peremennih iz massiva s verhnim registrom
    print(x.upper())

print(" \n")

for x in range(1,6):
    print(x)

mynumber_list = list(range(0, 10 +1))  #Vvod peremennih chisel v massiv avtomaticheski
print(mynumber_list)

print(" \n")

for x in mynumber_list:
    x = x*2
    print(x)

mynumber_list.sort(reverse=True) #sortirovka massiva po ponizheniyu
print(mynumber_list)

print("Max numbers is: " + str(max(mynumber_list))) #max chislo iz massiva
print("Min number is: " + str(min(mynumber_list))) #min chislo iz massiva
print("Summa is: " + str(sum(mynumber_list)))  #summa chisel massiva

print("-----------------------------------------------------\n")

#         0          1         2        3         4        5
cars = ['bmw', 'volkswagen', 'seat', 'skoda', 'toyota', 'lexus']

mycars = cars[1:4] #napolnili massiv mycars s 1 po 3 massiva cars
print(mycars)
mycars = cars[:4] #napolnili massiv mycars s 0 po 3 massiva cars
print(mycars)
mycars = cars[-3:] #napolnili massiv mycars s 3 po 5 massiva cars (s konca sdelali otchet)
print(mycars)

print("-----------------------------------------------------\n")

#         0          1         2        3         4        5
cars = ['bmw', 'volkswagen', 'seat', 'skoda', 'toyota', 'lexus']
mycars = cars[:] #Sozdanie massiva mycars na osnove massiva cars, no pri izmenenii massiva cars, massiv mycars ne pomeniayitsya (2 otdelnih drug ot druga massiva)
cars.append('merc')
print(mycars)
print(cars)