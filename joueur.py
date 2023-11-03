from tkinter import messagebox


class Joueur:
    "Joueur"

    def __init__(self):
        self.fichier_score = "score.txt"  # Fichier où le score du joueur est stocké
        self.score = 0  # Score actuel du joueur
        self.score_max = self.get_score()
        print(self.score_max)

    def get_score(self):
        "Obtenir le score du joueur"
        with open(self.fichier_score, "r") as rf:  # Lire le score contenu dans le fichier
            score = int(rf.read())
            return score

    def update_score(self, montant):
        "Augmenter le score du joueur"
        self.score += montant
        self.update_best_score()
        self.save_score()

    def update_best_score(self):
        "Mettre à jour le meilleur score"
        if self.score_max < self.score:
            self.score_max = self.score

    def save_score(self):
        "Sauvegarder le score"
        with open(self.fichier_score, "w") as wf:  # Ecrire dans le fichier "score.txt"
            wf.write(str(self.score_max))
            wf.close()

    def game_over(self, condition, root):
        "Game Over"
        if condition:  # Si la condition donnée pour le Game Over est vérifiée
            messagebox.showerror("Vous avez perdu(e)",
                                 "Vous avez perdu(e) et terminez la partie.")
            self.save_score()
            root.destroy()
