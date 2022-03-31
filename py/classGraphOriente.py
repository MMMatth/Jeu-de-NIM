from re import I


class GraphOriente:
    def __init__(self,level) -> None:
        self.liste_sommets = []
        
        if level == "hard":
            self.liste_arcs = self.retake("hard")
        elif level == "meduim":
            self.liste_arcs = self.retake("meduim")
        elif level == "simple":
            self.liste_arcs = self.retake("simple")
        else:
            self.liste_arcs = []
            
    def __str__(self):
        return str(self.liste_arcs)
    
    def save(self):
        """save function to save the graph in a file"""
        fichier = open("../other/save.txt", "wt")
        for i in range(len(self.liste_arcs)):
            fichier.write(str(self.liste_arcs[i][0]) + "\n" + str(self.liste_arcs[i][1]) + "\n")
        fichier.close()
    
    def retake(self,filename):
        """
        retake function to recup the save

        Returns:
            L (list) : the list of the graph like (self.liste_arcs)
        """
        L = []
        fichier = open("../other/"+str(filename)+".txt", "rt")
        liste = fichier.readlines()
        for i in range(0,len(liste)-1,2):
            L.append((int(liste[i].replace("\n", "")) , int(liste[i+1].replace("\n", ""))))
        fichier.close()
        return L

    def ajouter_sommet(self,A):
        self.liste_sommets.append(A)
    
    def ajouter_arc(self,A,B):
        self.liste_arcs.append((A,B))
        
    def supprimer_arc(self,A,B):
        for couple in self.liste_arcs:
            if couple == (A,B) :
                self.liste_arcs.remove(couple)
    def liste_sommets_issus(self,A):
        L = []
        for i in range(len(self.liste_arcs)):
            if self.liste_arcs[i][0] == A:
                L.append(self.liste_arcs[i][1])
        return L
# tests
if __name__ == '__main__':
    G = GraphOriente()
    G.save()