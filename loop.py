for i in ["primavera","otono","verano","invierno"]:
    print("hola " + i)
#################################################################################
email=False
for i in "alitunja27@gmail.com":
    if (i == "@"):
        email=True
if (email==True):
    print("Is an email")
else:
    print("Is not an email")
#################################################################################
for i in range(5):
    print("Hola")

#################################################################################
i=1
while i<=10:
    print("Ejecucion " + str(i))
    i+=1

################################################################################# CONTINUE in a for o while loop
for letra in "python":
    if letra=="h":
        continue
    print(f"The letter now is: {letra}")

################################################################################# ELSE in a for o while loop
email=input("Please introduce your email: ")

for i in email:
    if i=="@":
        arroba=True
        break
else:
    arroba=False
if arroba:
    print("The email has an \"@\"")
else:
    print("The email does not have an \"@\"")