class Plateau:
    def __init__(self,joueur:bool,sizex=10,sizey=10):
        self.__isplayer=joueur #Is the player a person or a bot
        self.__grid:list[Ship]=[]
        self.__visible=[[-1 for _ in range(sizex)] for _ in range(sizey)]
        self.__sizex=sizex
        self.__sizey=sizey
        self.__flottemanquante={2:1,3:2,4:1,5:1} #size:amount
    def is_ready(self):
        return all(self.__flottemanquante.values()==0)
    def place_ship(self,emplacements:list[tuple[int,int]]):
        """Adds the ship after checking if it could cause problems"""
        if not(2<=len(emplacements)<=5) or any(len(emplacements[i])!=2 for i in range(len(emplacements))):
            raise ValueError("Unproper format for emplacements")
        
        if self.__flottemanquante[len(emplacements)]==0:
            raise ValueError("No ships of this size are available")
        
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i].placement)):
                for k in range(len(emplacements)):
                    if self.__grid[i].placement[j]==emplacements[k]:
                        raise ValueError("Place already occupied")
        
        for i in range(len(emplacements)):
            if not(not(0<=emplacements[i][0]<=self.__sizey and 0<=emplacements[i][1]<=self.__sizex)):
                raise ValueError(f"Tried to place a ship at {emplacements[i]} even though this place isn't on the board")
        
        valide=False
        for sens in [[0,1],[1,0]]: #Horizontal and vertical
            if all(emplacements[i][sens[0]]==emplacements[i-1][sens[0]] for i in range(1,len(emplacements))):
                maxi=max(emplacements,key=lambda val:val[sens[1]])[1]
                mini=min(emplacements,key=lambda val:val[sens[1]])[1]
                if maxi-mini==len(emplacements)-1 and all(emplacements[i]!=emplacements[j] for i in range(len(emplacements)) for j in range(i+1,len(emplacements))): #Checking whether all of the cases are next to each other there's no double
                    valide=True
        if not(valide):
            raise ValueError("That is not a ship you stoopid")
        
        self.__grid.append(Ship(emplacements))

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
    def test(self,emplacement):
        """Retourne l'état visible d'une case"""
        return self.__visible[emplacement[0]][emplacement[1]]
    def iscomplete(self):
        return all(self.__flottemanquante.values()==0)
    @property
    def sizex(self):
        return self.__sizex
    @property
    def sizey(self):
        return self.__sizey
    @property
    def apparent(self):
        return self.__visible

class Ship:
    def __init__(self,places):
        self.__placement=places
        self.__intacts=[[places[i],True] for i in range(len(places))]
    def attack(self,emplacement):
        for i in range(len(self.__placement)):
            if emplacement==self.__placement[i]:
                self.__intacts[i][1]=True
                if all(self.__intacts[k] for k in range(len(self.__intacts))):
                    return 2
                return 1
        return 0
    @property
    def placement(self):
        """Setting up the getter of placement"""
        return self.__placement
    @property
    def size(self):
        return len(self.__placement)
    