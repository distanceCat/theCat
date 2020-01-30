from tkinter import *
from tkinter import messagebox

import CatController


class CatGui:

    def __init__(self):
        # constants
        self.WINDOWSIZE = "640x480"
        self.LABELWIDTH = 20
        self.ENTRYWIDTH = 22
        # variables
        self.fenster = Tk()
        self.fenster.geometry(self.WINDOWSIZE)
        self.nameValue = StringVar()
        self.colorValue = StringVar()
        self.genderValue = StringVar()
        self.ageValue = IntVar()
        self.ageValue.set(-1)
        self.extraValue = StringVar()
        self.controller = CatController.CatController()
        # default window settings
        self.creatorFrame = Frame(self.fenster, width=self.fenster.winfo_width(), height=self.fenster.winfo_height())
        self.startGui(self.fenster, self.creatorFrame)

    def button_save(self):
        # name, color, age, gender, extrasound
        if not (self.nameValue.get() == ""):
            if self.checkCorrectEntries():
                self.controller.defineCat(
                    self.nameValue.get(),
                    self.colorValue.get(),
                    self.ageValue.get(),
                    self.genderValue.get(),
                    self.extraValue.get(),
                )
        if (self.controller.getNumberOfCats() > 0):
            print(self.controller.describeCatsAsText())
            self.creatorFrame.destroy()
            descriptionFrame = Frame(self.fenster, width=self.fenster.winfo_width(), height=self.fenster.winfo_height())
            descriptionLabel = Label(descriptionFrame, text=self.controller.describeCatsAsText(),
                                     width=self.fenster.winfo_width() - 5,
                                     height=self.fenster.winfo_height() - 5,
                                     bg="white", padx=10, pady=10)
            descriptionLabel.pack()
            descriptionFrame.pack()
        else:
            messagebox.showinfo("Error", "Please provide a cat first!")

    def button_next(self):
        if self.checkCorrectEntries():
            self.controller.defineCat(
                self.nameValue.get(),
                self.colorValue.get(),
                self.ageValue.get(),
                self.genderValue.get(),
                self.extraValue.get(),
            )
        self.resetValues()

    def checkCorrectEntries(self):
        if (self.nameValue.get() == "") and (self.ageValue.get() == -1):
            messagebox.showinfo("Error", "Please provide a name and an age!")
            return False
        elif self.nameValue.get() == "":
            messagebox.showinfo("Error", "Please provide a name")
            return False
        elif self.ageValue.get() == -1:
            messagebox.showinfo("Error", "Please provide an age")
            return False
        elif self.controller.isNameRedundant(self.nameValue.get()):
            messagebox.showinfo("Error", self.nameValue.get() + " already exists")
            self.resetValues()
            return False
        else:
            return True

    def resetValues(self):
        self.nameValue.set("")
        self.colorValue.set("")
        self.ageValue.set(-1)
        self.genderValue.set("blah")
        self.extraValue.set("")

    def createCatConfigurator(self, frame):
        self.genderValue.set("blah")
        # define components
        labelHeadline = Label(frame, anchor=W, text="\nDefine a cat:", width=self.LABELWIDTH - 2,
                              font=("Helvectia, 14"))
        labelHeadline.pack(side=LEFT)
        labelEmptyRow = Label(frame, text=" ", width=self.LABELWIDTH, padx=20)
        labelCatName = Label(frame, anchor=W, text="Name of cat: ", width=self.LABELWIDTH)
        entryCatName = Entry(frame, bd=2, width=self.ENTRYWIDTH, textvariable=self.nameValue)
        labelCatColor = Label(frame, anchor=W, text="Color of cat: ", width=self.LABELWIDTH)
        entryCatColor = Entry(frame, bd=2, width=self.ENTRYWIDTH, textvariable=self.colorValue)
        labelCatAge = Label(frame, anchor=W, text="Age of cat: ", width=self.LABELWIDTH)
        entryCatAge = Entry(frame, bd=2, width=self.ENTRYWIDTH, textvariable=self.ageValue)
        labelCatGender = Label(frame, anchor=W, text="Cat's gender: ", width=self.LABELWIDTH)
        radioCatGenderMale = Radiobutton(frame, text="Male", variable=self.genderValue, value="male", anchor=W,
                                         width=self.ENTRYWIDTH - 5)
        radioCatGenderFemale = Radiobutton(frame, text="Female", variable=self.genderValue, value="female", anchor=W,
                                           width=self.ENTRYWIDTH - 5)
        radioCatGenderUnknown = Radiobutton(frame, text="Unknown", variable=self.genderValue, value="unknown", anchor=W,
                                            width=self.ENTRYWIDTH - 5)
        # entryCatGender = Entry(frame, bd=2, width=self.__ENTRYWIDTH)
        labelCatExtrasound = Label(frame, anchor=W, text="Special sound of cat: ", width=self.LABELWIDTH)
        entryCatExtrasound = Entry(frame, bd=2, width=self.ENTRYWIDTH, textvariable=self.extraValue)
        buttonNextCat = Button(frame, text="Next cat", command=self.button_next)
        buttonSave = Button(frame, text="Save cat(s)", command=self.button_save)

        # add components to frame
        labelHeadline.grid(row=0, column=0)
        labelEmptyRow.grid(row=1, column=0)
        labelCatName.grid(row=2, column=0)
        entryCatName.grid(row=2, column=1)
        labelCatColor.grid(row=3, column=0)
        entryCatColor.grid(row=3, column=1)
        labelCatAge.grid(row=4, column=0)
        entryCatAge.grid(row=4, column=1)
        labelCatGender.grid(row=5, column=0)
        radioCatGenderMale.grid(row=5, column=1)
        radioCatGenderFemale.grid(row=6, column=1)
        radioCatGenderUnknown.grid(row=7, column=1)
        # entryCatGender.grid(row=5, column=1)
        labelCatExtrasound.grid(row=8, column=0)
        entryCatExtrasound.grid(row=8, column=1)
        labelEmptyRow.grid(row=9, column=0)
        buttonNextCat.grid(row=10, column=0)
        buttonSave.grid(row=10, column=1)
        frame.pack(anchor=W)

        return frame

    def startGui(self, fenster, frame):
        fenster.title("The Cat")
        p1 = PhotoImage(file="./ressources/pfotenabdruck.png")
        fenster.wm_iconphoto(False, p1)
        self.createCatConfigurator(frame).grid(row=0, column=0)
        fenster.mainloop()
