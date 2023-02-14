#python_study


def create_record(name,telephone,adress):
    """"Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'adress': adress
    }
    return record

user1 = create_record('Vasya', '0734669595', 'boul.shevchenka')
user2 = create_record('Ibra', '0468499595', 'boul.ukrainki')

print(user1)
print(user2)

def give_award(medal, *persons):
    """"Give medals to persons"""
    for person in persons:
        print("Mister " + person.title() + " nagrazhdaetsya medaliyu " + medal)

give_award("za vzyatie moskvi", "vasya", "petya")
give_award("za vzyatie pitera", "krendel", "maks", "ellington")
