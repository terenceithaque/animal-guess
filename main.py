# Programme principal
from tkinter import *
import random
import os


class Jeu(Tk):
    "Jeu"

    def __init__(self):
        super().__init__()  # Initialiser le constructeur
        # Indiquer au joueur ce qu'il doit faire
        self.label_guess = Label(
            self, text="Devinez quel animal est représenté sur l'image ci-dessous :")
        self.label_guess.pack()

        # Entrée dans laquelle le joueur devra entrer une suggestion d'animal
        self.guess = Entry(self)
        self.guess.pack(fill="x")

        self.guess_button = Button(self, text="Deviner !", command=None)
        self.guess_button.pack()

        image = self.choose_image()  # Choisir une image

        # Conteneur pour chaque image qui sera choisie par le jeu
        self.image_frame = Frame(self, width=1000, height=1000)

        self.image_frame.pack()

    def choose_image(self):
        "Choisir une image au hasard"
        # Dresser une liste de toutes les images existantes
        images = os.listdir("images")
        # Choisir une image au hasard parmi toutes les possibilités
        image_choisie = random.randrange(len(images))
        image_choisie = images[image_choisie]
        print(image_choisie)

        return image_choisie


jeu = Jeu()
jeu.mainloop()
