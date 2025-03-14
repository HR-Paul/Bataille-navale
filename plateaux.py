class Plateau:
    def __init__(self,joueur:bool,sizex=10,sizey=10):
        self.__isplayer=joueur
        self.__grid:list[Plateau]=[]
        self.__visible=[[-1 for _ in range(sizex)] for _ in range(sizey)]
        self.__sizex=sizex
        self.__sizey=sizey
        self.__flottemanquante={2:1,3:2,4:1,5:1} #size:amount
    def is_ready(self):
        return all(self.__flottemanquante.values()==0)
    def place_ship(self,emplacements:list[tuple[int,int]]):
        if not(2<=len(emplacements)<=5) or any(len(emplacements[i])!=2 for i in range(len(emplacements))):
            raise ValueError("Unproper format for emplacements")
        if self.__flottemanquante[len(emplacements)]==0:
            raise ValueError("No ships of this size are available")
        if any(self.__grid[i].placement[j]==emplacements[k] for i in range(len(self.__grid)) for j in range(self.__grid[i].placement) for k in range(len(emplacements))):
            raise ValueError("Place already occupied")
        for i in range(len(emplacements)):
            if not(not(0<=emplacements[i][0]<=self.__sizey and 0<=emplacements[i][1]<=self.__sizex)):
                raise ValueError(f"Tried to place a ship at {emplacements[i]} even though this place isn't on the board")
        new=Ship()
        new.place(emplacements)
        self.__grid.append(new)
    @property
    def sizex(self):
        return self.__sizex
    @property
    def sizey(self):
        return self.__sizey
    def test(self,emplacement):
        """Retourne l'état visible d'une case"""
        return self.__visible[emplacement[0]][emplacement[1]]
    def discover(self,emplacement):
        """Decouvre le vrai etat d'une case et le retourne"""
        for i in range(len(self.__grid)):
            attaque=self.__grid[i].attack(emplacement)
            if attaque==1:
                self.__visible[emplacement[0]][emplacement[1]]=1
                return 1
            elif attaque==2:
                for coule in self.__grid[i].placement:
                    self.__visible[coule[0]][coule[1]]=2
                return 2
        self.__visible[coule[0]][coule[1]]=0
        return 0
class Ship:
    def __init__(self):
        self.__placement=None
    def place(self,places:list[list[int,int]]):
        self.__placement=places
        self.__intacts=[[places[i],True] for i in range(len(places))]
    @property
    def placement(self):
        return self.__placement
    @property
    def size(self):
        return len(self.__placement)
    def attack(self,emplacement):
        for i in range(len(self.__placement)):
            if emplacement==self.__placement[i]:
                for j in range(len(self.__intacts)):
                    if self.__intacts[j][0]==self.__placement[i]:
                        self.__intacts[j][1]=True
                        if all(self.__intacts[k] for k in range(len(self.__intacts))):
                            return 2
                        return 1
        return 0
test=Ship()
test.placement=5
"""
1=j
2=d
3=e
4=h
5=f
6=
7=a
8=
9=g
10=
11=
12=m
13=
14=i
"""