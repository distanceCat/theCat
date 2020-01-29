import Cat
import CatGui
import CatController


def defineCat(name, color, age, gender, extrasound):
    aCat = Cat.Cat()
    aCat.setName(name)
    aCat.setColor(color)
    aCat.setAge(age)
    aCat.setGender(gender)
    if extrasound != "":
        aCat.addSound(extrasound)
    return aCat


def describeCats(theCats):
    for aCat in theCats:
        print("###########################################")
        print(aCat.getCatDescription())
        print(aCat.getName() + " is currently " + aCat.getCurrentActivity())
        print(aCat.makeSound())


if __name__ == '__main__':
    # myCats = []
    # First cat
    # myCats.append(defineCat("Moritz", "white-brown", 2, "Male", "Mauz"))
    # Second cat
    # myCats.append(defineCat("James", "black", 5, "male", ""))

    # describeCats(myCats)
    CatController.CatController()
    CatGui.CatGui()
