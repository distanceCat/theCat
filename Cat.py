import random


class Cat:

    def __init__(self):
        self.__name = "unknown"
        self.__age = 0
        self.__sounds = ["Miau", "Schnurr", "Brrr", "Mau", "Krrr"]
        self.__color = "unknown"
        self.__activities = ["sleeping", "playing around", "eating", "cleaning itself", "exploring the hood",
                             "sleeping"]
        self.__gender = "unknown gender"

    def makeSound(self):
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

    def setGender(self, gender):
        if (gender.lower() == "male") or (gender.lower() == "female"):
            self.__gender = gender.lower()

    def getGender(self):
        return self.__gender

    def getCatDescription(self):
        if (self.__gender == "male") or (self.__gender == "female"):
            return ("%s is a %s %s cat of %s years" % (self.__name, self.__gender, self.__color, self.__age))
        else:
            return ("%s is a %s cat of %s years and %s" % (self.__name, self.__color, self.__age, self.__gender))

    def getCurrentActivity(self):
        aRandomNumber = random.randint(0, len(self.__activities) - 1)
        return self.__activities[aRandomNumber]
