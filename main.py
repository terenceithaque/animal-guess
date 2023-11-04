# Programme principal
from tkinter import *
import random
import os
from PIL import ImageTk, Image
from joueur import *

joueur = Joueur()  # Créer un joueur


class Jeu(Tk):
    "Jeu"

    def __init__(self):
        super().__init__()  # Initialiser le constructeur
        # Indiquer au joueur ce qu'il doit faire

        self.barre_menu = Menu(self, tearoff=0)
        self.menu_jeu = Menu(self.barre_menu, tearoff=0)
        self.menu_jeu.add_command(
            label="Quitter le jeu", command=self.quit_game)

        self.barre_menu.add_cascade(label="Jeu", menu=self.menu_jeu)
        self.config(menu=self.barre_menu)
        self.label_guess = Label(
            self, text="Devinez quel animal est représenté sur l'image ci-dessous :")
        self.label_guess.pack()

        # Entrée dans laquelle le joueur devra entrer une suggestion d'animal
        self.guess_entry = Entry(self)
        self.guess_entry.pack(fill="x")

        self.guess_button = Button(self, text="Deviner !", command=self.guess)
        self.guess_button.pack()

        self.labels = []
        self.images_precedentes = []

        self.images = []
        self.n_images_choisies = 0
        self.image_name = ""
        self.display_image()

    def choose_image(self):
        "Choisir une image au hasard"
        # Dresser une liste de toutes les images existantes
        self.images = os.listdir("images")

        images_non_choisies = list(
            set(self.images) - set(self.images_precedentes))
        global image_choisie
        # Choisir une image au hasard parmi toutes les possibilités

        image_choisie = random.choice(images_non_choisies)

        if image_choisie not in self.images_precedentes:
            self.ajouter_image_precedente()

        return image_choisie

    def ajouter_image_precedente(self):
        self.images_precedentes.append(image_choisie)

    def display_image(self):
        "Afficher l'image choisie"

        image = self.choose_image()
        self.n_images_choisies += 1
        if self.n_images_choisies == len(self.images):
            messagebox.showinfo(
                "La partie est terminée", f"Toutes les images ont été tirées. La partie est terminée. Votre score total est de {joueur.score}, tandis que votre meilleur score est de {joueur.score_max}.")
            joueur.save_score()
            self.destroy()
            return
        self.image_name = image

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
        player_guess = self.guess_entry.get()
        if player_guess == "":
            messagebox.showinfo("Veuillez saisir un nom d'animal",
                                "Vous n'avez fait aucune suggestion. Tant que ce sera le cas, aucun point ne vous sera attribué. Remplissez la barre située au dessus du bouton Deviner !")
            return

        condition_game_over = joueur.score <= -90
        if player_guess in self.image_name:
            joueur.update_score(15)
            messagebox.showinfo(
                "Correct !", "Vous gagnez 15 points. Votre score actuel : {}".format(joueur.score))
            self.display_image()

        else:
            joueur.update_score(-15)
            messagebox.showerror(
                "Inccorrect !", "Vous perdez 15 points. Votre score actuel : {}".format(joueur.score))

        joueur.game_over(condition_game_over, self)

    def quit_game(self):
        "Quitter le jeu"
        ask_quit = messagebox.askquestion(
            "Quitter", "Voulez-vous vraiment quitter le jeu maintenant ? Votre meilleur score sera sauvegardé.")
        if ask_quit == "yes":
            joueur.save_score()
            self.destroy()


jeu = Jeu()
jeu.mainloop()
