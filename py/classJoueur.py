class Joueur:
    def __init__(self):
        self.pseudo = ""
        self.joue = False
        self.gagne = False
        self.score = 0
        self.etat = ""
    
    def augmente_score(self):
        if self.gagne == True : self.score += 1
    
    def change_joueur(self):
        if self.joue == True: self.joue = False 
        else: self.joue = True
    
    def change_gagnant(self):
        self.gagne = True
    
    def set_etat(self,valeur):
        self.etat = valeur
        