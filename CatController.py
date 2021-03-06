import Cat


class CatController:

    def __init__(self):
        self.theCats = []

    def defineCat(self, name, color, age, gender, extrasound):
        aCat = Cat.Cat()
        aCat.setName(name)
        aCat.setColor(color)
        aCat.setAge(age)
        aCat.setGender(gender)
        if extrasound != "":
            aCat.addSound(extrasound)
        self.theCats.append(aCat)

    def describeCatsAsText(self):
        returnString = "###########################################" + "\n"
        for aCat in self.theCats:
            returnString = returnString + (aCat.getCatDescription()) + "\n"
            returnString = returnString + (aCat.getName() + " is currently " + aCat.getCurrentActivity()) + "\n"
            returnString = returnString + aCat.makeSound() + "\n"
            returnString = returnString + "###########################################" + "\n"
        return returnString

    def isNameRedundant(self, name):
        for aCat in self.theCats:
            if aCat.getName() == name:
                return True
        return False

    def getNumberOfCats(self):
        return len(self.theCats)
