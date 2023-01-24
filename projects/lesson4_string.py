string = "bla bla bla"

name = "mr vasYa pupkin"

print (name.title())
print (name.upper())
print(name.lower())

print("priver stroka nomer1\nPrivet stroka n2\n\nPrivet stroka n3")

print("Messages:\n\tmessage1\n\tmessage2\n\tmessage3\nEnd")
print("lower name: " + name.lower())
print("-----------\n")

a = " .dk "
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(" \n")

a = "...dk ..."
b = a.strip(".")   #udalenie tochek
b = b.strip()      #udalenie probelov
print(b)