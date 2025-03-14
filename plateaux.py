class Plateau:
    def __init__(self,joueur:bool,sizex=10,sizey=10):
        self.__isplayer=joueur
        self.__grid=[]
        self.__discovered=[[False for _ in range(sizex)]for _ in range(sizey)]
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


class Ship:
    def __init__(self):
        self.placement=None
    def place(self,places:list[list[int,int]]):
        self.placement=places
    @property
    def placement(self):
        return self.placement
    @property
    def size(self):
        return len(self.placement)
    
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