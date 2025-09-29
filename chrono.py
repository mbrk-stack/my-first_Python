class Chrono:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
        
    def affiche(self):
      t =  print(f'Il est {self.heures}h:{self.minutes}m:{self.secondes}s.')
      

    def avance(self, s):
        # convertir le temps total en secondes
        total = self.heures * 3600 + self.minutes * 60 + self.secondes
        total += s  # avancer de s secondes

        # recalculer heures, minutes, secondes
        self.heures = (total // 3600) % 24
        self.minutes = (total % 3600) // 60
        self.secondes = total % 60
    
    
chrono1 = Chrono(20,30,45)
chrono1.affiche()
chrono1.avance(10)
chrono1.affiche()
