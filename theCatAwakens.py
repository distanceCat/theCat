import cat


def defineCat(name, color, age, extrasound):
    aCat = cat.cat()
    aCat.setName(name)
    aCat.setColor(color)
    aCat.setAge(age)
    if extrasound != "":
        aCat.addSound(extrasound)
    return aCat


if __name__ == '__main__':
    # First cat
    myCat = defineCat("Moritz", "white-browm", 2, "Mauz")
    print(myCat.getCatDescription())
    print(myCat.getName() + " is currently " + myCat.getCurrentActivity())
    print(myCat.makeSound())
    # second cat
    mySecondCat = defineCat("James", "black", 5, "")
    print(mySecondCat.getCatDescription())
    print(mySecondCat.getName() + " is currently " + mySecondCat.getCurrentActivity())
    print(mySecondCat.makeSound())
