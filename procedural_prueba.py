from random import choices
class Perinola:
    def __init__(self):
       self.cara_visible = 'Pon 1'
    def __repr__(self):
        return f"Salio: {self.cara_visible}"
    def tirar(self):
        caras =("Pon 1","Pon 2","Toma 1","Toma 2","Todos Toman","Ponen Todos")
        self.cara_visible=choices(caras)
        return f"Salio {self.cara_visible}"