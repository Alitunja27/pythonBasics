miLista=["Maria","Pepe","Marta","Antonio"]

print(miLista[:])        ## print all the list
print(miLista[2])        ## print an index    
print(miLista[-3])       ###### if you set a negative index, Py count it from the end of the List
print(miLista[0:3])      ### we are accessing a portion of the list form index 0-3(excluded)

miLista.append("Sandra") ### to add an element
print(miLista[:])

miLista.insert(2,"Ali")  ### to add an element in a position
print(miLista[:])

miLista.extend(["Ana","Lucia","Sandra"])   ### to concatenate 2 lists
print(miLista[:])

print(miLista.index("Ali"))  ### to know the element number

print("Ali" in miLista) ##### to know if the element is part of the list

miLista.remove("Ana")   #### to remove the element
miLista.pop()           #### to delete the last element in the list