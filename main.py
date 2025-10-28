import models.narration as narration
import functions.arenes as arenefn
import termcolor
from tabulate import tabulate

narration.intgame()
input()
arenes = arenefn.get_arenes()
arenefn.affiche_arenes(arenes)

print(termcolor.colored("Taper entrer pour continuer ........ ", "red"))
input()



narration.choixArene()
choix = input()
arene_choisie = ""
if choix == "":
    new_arene = arenefn.create_bject_arene()
    arenefn.add_arene(new_arene)
    arene_choisie = new_arene.name
else :
    print("\n")
    print(" veuillez choisier une arene : ")
    print("\n")
   # arenefn.affiche_arenes(arenefn.get_arenes())
   # arene_choisie = input("entrer le nom de l'arene")
    while True:
      arene_choisie = input("entrer le nom de l'arene :  ")
      print("\n")
      if arene_choisie == "":
         continue
      if not(arenefn.arene_existe(arene_choisie)):
        print(termcolor.colored("❌ l'arène n'existe pas", "grey", "on_red", ["underline"]))
        print("\n")
        continue
      else:
         break

arene_choisie = arenefn.get_arene_by_name(arene_choisie)
print("Vous avez choisie l'arene : ")
table = []
table.append([
            termcolor.colored(arene_choisie.name, arene_choisie.color),
            termcolor.colored(arene_choisie.ville, arene_choisie.color),
            termcolor.colored(arene_choisie.dresseur, arene_choisie.color),
            termcolor.colored(arene_choisie.type, arene_choisie.color),
            termcolor.colored(arene_choisie.score, arene_choisie.color)
        ])
header = ["Nom", "Ville", "Dresseur","type","score"]
print(tabulate(table, headers=header, tablefmt="fancy_grid"))







    




