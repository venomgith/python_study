#Sozdanie ob'ekta-slovaria
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}
#Sozdanie ob'ekta-slovaria
print(enemy)
print("\n")

all_enemies = [] #massiv iz 10 slovarej

for x in range(0,10):
    all_enemies.append(enemy.copy())

for ene in all_enemies: #raspechatka otdelno kazhdogo
    print(ene)

all_enemies[5]['health'] = all_enemies[5]['health'] - 30
all_enemies[5]['name'] = 'Krendel'
all_enemies[3]['name'] = 'Sobaka'
print("\n==================\n")
# if all_enemies['health'] <= 80:
 #   all_enemies['image'] = 'image2.jpg'
for ene in all_enemies:
    print(ene)


