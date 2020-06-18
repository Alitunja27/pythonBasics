########################### If ############################
grade=int(input("Please introduce the grade of this student: "))

def evaluation(nota):
    if nota <5:
        value = "Suspended"
    elif nota > 5:
        value = "Aproved"
    else:
        value = "lol"
    return value
print(evaluation(grade))

## if 0<edad<100 you can put more than one operator

