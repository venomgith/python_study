#python_study


def napechatat_privet():
    """"Print Privetstvie"""
    print("Congrat, i wish you all the best")
    print("Hello, How are you?")


def aaa():
    print("Aaaaa")


def napechat_privet(name):
    """"print privet"""
    print("Congrat " + name + " wish you all the best")


def summa():
    x = input("Enter X: ")
    y = input("Enter Y: ")
    summa = int(x)+int(y)
    print("Summa ravna: " + str(summa))

def sum(x,y):
    s=x+y
    return s


def factorial(x):
    """"calculate factorial of number x"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet


def stepen(x,n):
    result = 1
    """"calculate number x with degree"""
    for i in range(n):
        result *=x #result = result * x
    return result
        # a*a*a*a*a*a


print("\n")

napechat_privet("Ibra")
napechat_privet("Krendel")
# summa()
x = sum(30,20)
print(x)

"""Programma po raschety chisla so stepeniyu"""
#h = input("Vvedite chislo: ")
#n = input("Vvedite stepen: ")
#result = 1
#for i in range(int(n)):
 #   result *=int(h)
#print(str(result))

p = input("Enter chislo: ")
k = input("Enter stepen: ")
print(p + " v " + k + " stepeni raven: " + str(stepen(int(p),int(k))))


h = input("Chislo faktoriala raven: ")
for u in range(1, int(h) + 1):
    print(str(u) + "! = " + str(factorial(u)))
