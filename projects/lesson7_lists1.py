# Python Study

cities = ['New York', 'Kyiv', 'Kharkiv', 'Toronto', 'Donetsk'] #otschet idet s 0 - New York, 1 - Kyiv i t.d.

print(cities)
print(len(cities)) #kolichestvo peremennih v massive

print(cities[0]) #raspechatka peremennoj s nachala massiva
print(cities[-1]) #raspechatka peremennoj s konda massiva i tak dalee -2 -3 -4
print(cities[2].upper())

cities[-1] = 'Grozny' #Dobavlenie peremennoj v massiv v konce
print("\n")
print(cities)

cities.append('Lviv') #Dobavlenie peremennih v konec massiva
cities.append('Yalta')
print(cities)

cities.insert(0,'Zaporizhya') #Dobavlenie peremennoy v massiv
cities.insert(3,'Kryvij Rig')
print(cities)

del cities[-1] #Udalenie iz massiva peremennoy s konca
print(cities)

cities.remove('Kyiv') #Udalenie peremennoj iz massiva po nazvaniyu
print(cities)

deleted_city = cities.pop() #Virezaet poslednuyu peremennuyu v massive, mozhno ukazat lubuyu peremennuyu cherez chislo
print("deleted_cities is: " + str(deleted_city))
print(cities)

cities.sort() #Sortirovka po alfavity
print(cities)

cities.sort(reverse=True) #Sortirovka s konca alfavita
print(cities)




