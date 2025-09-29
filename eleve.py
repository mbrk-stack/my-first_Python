class Eleve:
    def __init__(self, nom, classe, note):
        self.nom = nom
        self.classe = classe
        self.note = note
        
def compare(eleve1, eleve2):
        if eleve1.note > eleve2.note:
             return eleve1.nom
        else:
             return eleve2.nom

eleve1 = Eleve("Jeffrey Jefferson", "UpperSixth", 80)
eleve2 = Eleve("Zedicus Zoolander", "UpperSixth", 69)
eleve3 = Eleve("Dimitri Gredenko", "UpperSixth", 72)

eleves = {
    eleve1.nom: eleve1,
    eleve2.nom: eleve2,
    eleve3.nom: eleve3
}

# Demander à l'utilisateur quels élèves comparer
nom1 = input("Entrez le nom du premier élève : ")
nom2 = input("Entrez le nom du deuxième élève : ")


# Vérifier si les noms existent dans le dictionnaire
if nom1 in eleves and nom2 in eleves:
    resultat = compare(eleves[nom1], eleves[nom2])
    print("L'élève avec la meilleure note est :", resultat)

# Vérification si l'utilisateur entre deux fois le même nom
while nom1 == nom2:
    print("Vous avez saisi deux fois le même élève !")
    nom2 = input("Entrez un nom différent pour le deuxième élève : ")

else:
    print("Un des noms entrés n'existe pas dans la liste.")

# print(compare(eleve1, eleve2))
# print(compare(eleve2, eleve3)) 

