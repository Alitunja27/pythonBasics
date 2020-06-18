def evenNumberCreator(limit):
    num = 1
    while num < limit:
        yield num * 2
        num += 1


pairNumbers = evenNumberCreator(10)

##for i in pairNumbers:
##    print(i)

print(next(pairNumbers))
print("Could be more code here")
print(next(pairNumbers))
print("Could be more code here")
print(next(pairNumbers))
print("Could be more code here")


def returnCities(*city):
    for element in city:
        yield from element


returnedCities = returnCities("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(returnedCities))
print(next(returnedCities))