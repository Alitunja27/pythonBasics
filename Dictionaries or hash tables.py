myDictionary={"Alemania":"Berlin","Francia":"Paris","UK":"London","Espana":"Madrid"}
print(myDictionary["Francia"])

########## Add an element to the Dictionary ###################
myDictionary["Italia"] = "Lisboa"
print(myDictionary)

########## Update an element to the Dictionary ###################
myDictionary["Italia"] = "Rome"
print(myDictionary)

########## delete or update an element to the Dictionary ###################
del myDictionary["Francia"]
print(myDictionary)

########## Dictionary with diferent types of values in it ###################

myDictionary={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}

########## Dictionary keys, values and ###################
print(myDictionary.keys())
print(myDictionary.values())
print(len(myDictionary))
