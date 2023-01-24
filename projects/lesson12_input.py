#Python_study
name = input("Please enter your name: ")
print("Privet " + name)

num1 = input("Enter X: ")
num2 = input("Enter Y: ")

sum = int(num1) + int(num2)
print("Summa ravna " + str(sum))

message = ""
while True:
    message = input("Enter password ")
    if message == 'Admin@123$':
        break
    print("Password " + " ( " + message + " )" + " is not correct")

print("Password was: " + message)

mylist = []
msg = ""
while msg != 'sekret':
    msg = input("Enter new item, and stop to finish ")
    mylist.append(msg)

print(mylist)