from plateaux import Plateau
from random import randint
def facile(grid:Plateau)->list[int,int]:
    """Frappe une case libre aléatoire"""
    choix=0
    while grid.test(choix)!=-1:
        choix=(randint(0,grid.sizex),randint(0,grid.sizey))
    return choix
def moyen(grid:Plateau)->list[int,int]:
    """Comportement très semblable à celui d'un humain"""
    if all(grid.apparent[i][j]!=1): #Si on n'a aucun bateau à découvert
        return facile(grid)
    result=analyze_grid_moyen(grid)
    indmax=[0,0]
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i][j]>result[indmax[0]][indmax[1]]:
                indmax=[i,j]
    else:
        return indmax
def difficile(grid:Plateau)->list[int,int]:
    raise NotImplementedError()
def analyze_grid_moyen(grid:Plateau):
    '''Renvoit une liste avec toutes les possibilités de bateau probable en fonction des bateaux déjà découverts (liste de 0 si aucuns bateaux trouvés )'''
    raise NotImplementedError()
    for i in range(len(grid.apparent)):
        pass
difficultes={"facile":facile,"moyen":moyen,"difficile":difficile}