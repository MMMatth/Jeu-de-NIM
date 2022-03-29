class GraphOriente:
    def __init__(self) -> None:
        self.liste_sommets = []
        self.liste_arcs = []
    
    def __str__(self):
        return str(self.liste_arcs)
        
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
    G.ajouter_sommet("A")
    G.ajouter_sommet("B")
    G.ajouter_sommet("C")
    G.ajouter_sommet("D")
    G.ajouter_arc("A","B")
    G.ajouter_arc("A","C")
    G.ajouter_arc("B","D")
    G.ajouter_arc("C","D")
    print(G.liste_sommets)
    print(G.liste_arcs)
    G.supprimer_arc("A","B")
    print(G.liste_arcs)
    print(G.liste_sommets_issus("B"))
    