import cat


if __name__ == '__main__':
    myCat = cat.cat()
    myCat.setName("Moritz")
    myCat.setColor("white-brown")
    myCat.setAge(2)
    print(myCat.getCatDescription())
    myCat.addSound("Mauz")
    print(myCat.makeSound())

    mySecondCat = cat.cat()
    mySecondCat.setName("James")
    mySecondCat.setColor("black")
    mySecondCat.setAge(5)
    print(mySecondCat.getCatDescription())
    print(mySecondCat.makeSound())
