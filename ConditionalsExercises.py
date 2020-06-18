num1 = int(input("Please type the first number to compare: "))
num2 = int(input("please type the second number to compare: "))


def devuelveMax(num1,num2):
    if num1>num2:
        print(str(num1) + " es mayor que " + str(num2))
    elif num2>num1:
        print(str(num2) + " es mayor que " + str(num1))
    else:
        print("Los numeros son iguales")

devuelveMax(num1,num2)

##########################################################################################################

name = input("Name: ")
address = input("Address: ")
telephone = input("Telephone: ")
data=[name,address,telephone]
print("Los datos personales son: " )
print("Name: " + data[0])
print("Address: " + data[1])
print("Telephone: " + data[2])


##########################################################################################################
num1=int(input("Number 1: "))
num2=int(input("Number 2: "))
num3=int(input("Number 3: "))

def average(num1,num2,num3):
    average=(num1+num2+num3)/3
    return average

print("The average of those numbers is: " + str(average(num1,num2,num3)))


########################################################################

distance=int(input("Distance to School: "))
siblins=int(input("Siblings: "))
salary=int(input("Salary: "))

if distance>40 and siblins>2 or salary<=20000:
    print("Beca granted")
else:
    print("Beca not granted")

#####################################################################

subjects=input("Please select one of this subjects: Computer, software or nothing")

if subjects.lower() in ("computer","software","nothing"):
    print(subjects+ " selected")
else: 
    print(subjects+ "is not in the list")

###################### the RANGE could be any value to any value range(5,10) will go from 5 to 9 and if you use
###################### a third parameter is to determined the addition range(5,10,3) from 3 to 3.

