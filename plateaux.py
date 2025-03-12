class Plateau:
    def __init__(self,joueur:bool):
        self.__joueur=joueur
        self.__grille=[[None for _ in range(10)]for _ in range(10)]

class Ship:
    def __init__(self,size:int):
        self.__size=size