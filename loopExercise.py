##############################################      print all the even numbers in the same line from 10 to 100
# for i in range(100):
#     if(i%2!=0):
#         print(i,end=" ")

##################################################################################################################
##############################################      ask for a password and check if it's more than 8 characters 
##############################################      and does not have any spaces

# password=input("Please introduce a passwor (8 or more characteres and can't have any spaces): ")
# counter=0
# spaces=True
# for i in password:
#     if (i==" "):
#         spaces=False
# if(len(password)>8 and spaces==True):
#     print("Password OK")
# else:
#     print("Password is not OK")

##################################################################################################################
##############################################      Verify and email address to check if they have an "@"" and a "."
# email=input("Please introduce your email: ")
# arrova=False
# point=0
# for i in email:
#     if i=="@":
#         arrova=True
#     if i==".":
#         point+=1
# if arrova==True & point>=1:
#     print("This is a valid email")
# else:
#     print("This is not a valid email")

#################################################################################################################
##############################################      Input infinite numbers until the number introduced is smaller
##############################################      than the previous
# previousNumber=0
# newNumber=0
# statement=True
# while statement:
#     newNumber=int(input("Please introduce a number: "))
#     if newNumber>previousNumber:
#         previousNumber=newNumber
#     else:
#         print(f"You just introduce a number smaller than the previous ({newNumber}<{previousNumber})")
#         break

#################################################################################################################
##############################################      Input infinite positive numbers until the number introduced
##############################################      is a negative number
number=int(input("Please introduce a positive number: "))
suma=0
while number>0:
    suma+=number
    number=int(input("Please introduce a positive number: "))

print(f"The Sum of the positive numbers typed is = {suma}")