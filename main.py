# Programme principal
from tkinter import *
import random
import os
from PIL import ImageTk, Image


class Jeu(Tk):
    "Jeu"

    def __init__(self):
        super().__init__()  # Initialiser le constructeur
        # Indiquer au joueur ce qu'il doit faire
        self.label_guess = Label(
            self, text="Devinez quel animal est représenté sur l'image ci-dessous :")
        self.label_guess.pack()

        # Entrée dans laquelle le joueur devra entrer une suggestion d'animal
        self.guess_entry = Entry(self)
        self.guess_entry.pack(fill="x")

        self.guess_button = Button(self, text="Deviner !", command=self.guess)
        self.guess_button.pack()

        self.labels = []

        self.display_image()

    def choose_image(self):
        "Choisir une image au hasard"
        # Dresser une liste de toutes les images existantes
        images = os.listdir("images")
        # Choisir une image au hasard parmi toutes les possibilités
        global image_choisie
        image_choisie = random.randrange(len(images))
        image_choisie = images[image_choisie]
        print(image_choisie)

        return image_choisie

    def display_image(self):
        "Afficher l'image choisie"
        image = self.choose_image()
        image = Image.open("images/{}".format(image))
        resized_image = image.resize((600, 800))

        tkimage = ImageTk.PhotoImage(resized_image)
        self.new_label(tkimage)

    def new_label(self, img):
        "Créer un nouveau conteneur pour l'image"
        for label in self.labels:
            label.destroy()
        label_image = Label(self, image=img)
        label_image.image = img
        label_image.pack()

        self.labels.append(label_image)

    def guess(self):
        self.display_image()


jeu = Jeu()
jeu.mainloop()
