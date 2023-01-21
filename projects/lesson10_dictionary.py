# Python Study
#     (----ITEM----)
#     (key)   (value)
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo'
} #Sozdanie ob'ekta-slovariaL

print(enemy)
print("\n")
print("location x = " + str(enemy['loc_x'])) #pechat' s ob'ekta
print("location y = " +str(enemy['loc_y']))
print("His name is: " + str(enemy['name']))

enemy['rank'] = "General" #Dobavlenie novogo znacheniya v ob'ekt
print(enemy)

del enemy['rank'] #Udalenie znacheniya iz ob'ektaL
print("\nBefore attack = " + str(enemy))

enemy['loc_x'] = enemy['loc_x'] + 40 #Izmeneniya kotorie vnosiatsya v ob'ekt
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80 and enemy['health'] > 70:
    enemy['color'] = 'yellow'
elif enemy['health'] <= 70:
    enemy['color'] = "red"

print("After attack = " + str(enemy))