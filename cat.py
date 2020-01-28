import random
class cat:

    def __init__(self):
        self.__name = "unknown"
        self.__age = 0
        self.__sounds = ["Miau", "Schnurr", "Brrr", "Mau", "Krrr"]
        self.__color = "unknown"

    def makeSound(self):
        """

        :rtype: object
        """
        aRandomNumber = random.randint(0, len(self.__sounds) - 1)
        return self.__sounds[aRandomNumber]

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def addSound(self, sound):
        self.__sounds.append(sound)

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return (self.__age)

    def getCatDescription(self):
        return ("%s is a %s cat of %s years" % (self.__name, self.__color, self.__age))