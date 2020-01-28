import cat


if __name__ == '__main__':
    myCat = cat.cat()
    myCat.setName("Moritz")
    myCat.setColor("black")
    myCat.setAge(5)
    print(myCat.getCatDescription())
    myCat.addSound("Mauz")
    print(myCat.makeSound())
