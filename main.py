import models.narration as narration
import functions.arenes as arenefn
import functions.pokemon as pokemonfn
import termcolor
from tabulate import tabulate

#
narration.intgame()
input()
arenes = arenefn.get_arenes()
arenefn.affiche_arenes(arenes)

print(termcolor.colored("Taper entrer pour continuer ........ ", "red"))
input()



choix =input(termcolor.colored("Vous voulez choisir une Aréne ou crer votre propre Aréne ? (entrer/non) ", "magenta"))

arene_choisie = ""
if choix == "":
    new_arene = arenefn.create_bject_arene()
    arenefn.add_arene(new_arene)
    arene_choisie = new_arene.name
    arene_choisie = arenefn.get_arene_by_name(arene_choisie)
    input( termcolor.colored(" Commencer à crer vos Pokemon \n ", "magenta"))

    while True:
       choix = input("ajouter ? (oui/non) : ")
       if choix == "oui":
         new_pokemon =  pokemonfn.create_object_pokemon(arene_choisie.id)
         pokemonfn.add_pokemon(new_pokemon)
         continue
       elif choix == "non":
          break
       else:
          break

else :
    print("\n")
    print(" veuillez choisier une arene : ")
    print("\n")
 
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
         arene_choisie = arenefn.get_arene_by_name(arene_choisie)
         break
      
print(" ✨ ✨ ✨ ✨ ✨✨ ✨ ✨ ✨ ✨" ,termcolor.colored("Votre monde est prét","yellow") ,"✨ ✨ ✨ ✨ ✨✨ ✨ ✨ ✨ ✨ \n")
print(termcolor.colored("Vous avez choisie l'arene", "grey", "on_magenta", ["dark","bold"]))
print("\n")
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
pokemonfn.affiche_pokemons( pokemonfn.get_pokemons_by_arena_id(arene_choisie.id))

print(termcolor.colored("Taper entrer pour continuer ........ ", "red"))
input()

print(termcolor.colored("Maintenant il faut choisir l'arène adversaire ", "red"))
input()








    




