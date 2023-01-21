# Python Study
#     (----ITEM----)
#     (key)   (value)
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo'
<<<<<<< HEAD
} #Sozdanie ob'ekta-slovariaL
=======
} #Sozdanie ob'ekta-slovaria
>>>>>>> 6af995dc7c7f16e0c30868c2c4754a4a9517a0ae

print(enemy)
print("\n")
print("location x = " + str(enemy['loc_x'])) #pechat' s ob'ekta
print("location y = " +str(enemy['loc_y']))
print("His name is: " + str(enemy['name']))

enemy['rank'] = "General" #Dobavlenie novogo znacheniya v ob'ekt
print(enemy)

<<<<<<< HEAD
del enemy['rank'] #Udalenie znacheniya iz ob'ektaL
=======
del enemy['rank'] #Udalenie znacheniya iz ob'ekta
>>>>>>> 6af995dc7c7f16e0c30868c2c4754a4a9517a0ae
print("\nBefore attack = " + str(enemy))

enemy['loc_x'] = enemy['loc_x'] + 40 #Izmeneniya kotorie vnosiatsya v ob'ekt
enemy['health'] = enemy['health'] - 30
<<<<<<< HEAD
if enemy['health'] < 80 and enemy['health'] > 70:
    enemy['color'] = 'yellow'
elif enemy['health'] <= 70:
    enemy['color'] = "red"
=======
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
>>>>>>> 6af995dc7c7f16e0c30868c2c4754a4a9517a0ae

print("After attack = " + str(enemy))