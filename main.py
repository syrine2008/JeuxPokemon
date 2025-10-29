import models.narration as narration
import functions.arenes as arenefn
import functions.pokemon as pokemonfn
import termcolor
from tabulate import tabulate
import functions.combat as combat
import random
import time
import models.dressuer as dresseur

#------------------------------------
#   introduction du jeux 
#------------------------------------
narration.intgame()
input()
arenes = arenefn.get_arenes()
arenefn.affiche_arenes(arenes)

print(termcolor.colored("Taper entrer pour continuer ........ ", "red"))
input()


#-------------------------------------------------
#   choisir si on creer une nouvelle arene ou  nn 
#-------------------------------------------------

choix =input(termcolor.colored("Vous voulez choisir une Aréne ou crer votre propre Aréne ? (entrer/non) : ", "magenta"))

arene_choisie = "" # a changer à la fin du test 
if choix == "":
    #---------------------------------------------------
    #   si on choisi la creation d'une nouvelle arene
    #---------------------------------------------------
    new_arene = arenefn.create_bject_arene()
    arenefn.add_arene(new_arene)
    arene_choisie = new_arene.name
    arene_choisie = arenefn.get_arene_by_name(arene_choisie)
    #---------------------------------------------------
    #   creation des pokemon 
    #---------------------------------------------------
    input( termcolor.colored(" Commencer à crer vos Pokemons 🐱 🐶 🐸 🦊 🐉 🦋 ⚡🔥 💧 🌿\n ", "magenta"))

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
       
#---------------------------------------------------
#   choisir une arene du catalogue 
#---------------------------------------------------
else :
    print("\n")
    print(termcolor.colored("veuillez choisier une arene 🏟️🏟️🏟️  ","magenta"))
    print("\n")
 
    while True:
      arene_choisie = input("entrer le nom de l'arene :  ")
      print("\n")
      
      if arene_choisie == "":
         continue
      if not(arenefn.arene_existe(arene_choisie)):
        print(termcolor.colored("❌ l'arène n'existe pas", "grey", ["underline"]))
        print("\n")
        continue
      else:
         arene_choisie = arenefn.get_arene_by_name(arene_choisie)
         break
#---------------------------------------------------
#   affichage du choix de l'arene 
#   arene_choisie (c'est l'arene choisie du cataloge ou crer )
#   pokemon_arene_choisie (c'est les pokemon qui appartiennent a l'arene choisie )
#---------------------------------------------------      
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
pokemon_arene_choisie = pokemonfn.get_pokemons_by_arena_id(arene_choisie.id)
pokemonfn.affiche_pokemons(pokemon_arene_choisie)

print(termcolor.colored("Taper entrer pour continuer ........ ", "red"))
input()

#---------------------------------------------------
#   choix de l'arene addversaire 
#   variables :
#   choix_addversaire (c'est l'arene adversaire )
#   
#---------------------------------------------------

print(termcolor.colored("Maintenant il faut choisir l'arène adversaire 👊👊👊 ", "yellow"))
arenefn.affiche_arenes(arenefn.get_reste_arenes(arene_choisie.id))

choix_addversaire = ""
while True :
   choix_addversaire = input(termcolor.colored("Veuiller choisir l'addversaire entrez le nom :  ","cyan"))
  
   print("\n")
   if choix_addversaire == "":     
      continue
   elif arenefn.arene_existe(choix_addversaire):
      choix_addversaire = arenefn.get_arene_by_name(choix_addversaire)
      break
   else :
      continue
print(termcolor.colored("adversaire choisie 👊👊👊 ", "yellow"))
table = []
table.append([
            termcolor.colored(choix_addversaire.name, choix_addversaire.color),
            termcolor.colored(choix_addversaire.ville, choix_addversaire.color),
            termcolor.colored(choix_addversaire.dresseur, choix_addversaire.color),
            termcolor.colored(choix_addversaire.type, choix_addversaire.color),
            termcolor.colored(choix_addversaire.score, choix_addversaire.color)
        ])
header = ["Nom", "Ville", "Dresseur","type","score"]
print(tabulate(table, headers=header, tablefmt="fancy_grid")) 

#---------------------------------------------------
#   affichage des pokemons addversaire
#---------------------------------------------------
print(termcolor.colored("Pokemons 🦊  qui partienne à l'arene \n ", "yellow"))
pokemon_adversaire = pokemonfn.get_pokemons_by_arena_id(choix_addversaire.id)
pokemonfn.affiche_pokemons( pokemon_adversaire)

print(termcolor.colored("Taper entrer pour continuer ........ ", "red"))
input()

print(termcolor.colored("⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️  Et que le combat commance  ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️", "red"))
print("\n")

print(termcolor.colored("Veuillez choisir votre pokemon pour le combat ", "red"))
print("\n")

pokemonfn.affiche_pokemons(pokemon_arene_choisie)
pokemon_combat_choisie = input(termcolor.colored("entrer le nom du pokemon :  ", "cyan"))
print("\n")


pokemon_combat_choisie = pokemonfn.get_pokemon_by_name(pokemon_combat_choisie,arene_choisie.id)
pokemon_adversaire_combat_random = random.choice(pokemon_adversaire)
resultat_combat = 0
score_pokemon_adversaire = 0
score_pokemon_choisie = 0


while True:
   if pokemon_adversaire_combat_random.pv <= 0 or pokemon_combat_choisie.pv <= 0:
      break
   else:
      resultat_combat = combat.combat(pokemon_combat_choisie,pokemon_adversaire_combat_random)
      if(resultat_combat == pokemon_adversaire_combat_random ):
         score_pokemon_adversaire += 1
      else :
         score_pokemon_choisie += 1
      print(" 💢 ",resultat_combat.name," a éte attaquer 💢 \n")
      time.sleep(0.4)

      continue   
vinqeur = "" 

if pokemon_adversaire_combat_random.pv > pokemon_combat_choisie.pv:
    vinqeur = pokemon_adversaire_combat_random
    score_vinquer = score_pokemon_adversaire
    print("💀💀💀 Votre Pokémon est KO 💀💀💀\n")

    nb_soin = 0
    while vinqeur != pokemon_combat_choisie and nb_soin < 3:
        nb_soin += 1
        choix_combat = input(" 💊 Voulez-vous soigner votre Pokémon et continuer le combat (oui/non): ")

        if choix_combat == "oui":
            dresseur.soigner_pokemon(pokemon_combat_choisie)     
            pokemon_adversaire_combat_random = pokemonfn.get_pokemon_by_name(pokemon_adversaire_combat_random.name,choix_addversaire.id)
            pokemon_combat_choisie = pokemonfn.get_pokemon_by_name(pokemon_combat_choisie.name,arene_choisie.id)
                  
            while True:
   
                if pokemon_adversaire_combat_random.pv <= 0 or pokemon_combat_choisie.pv <= 0:

                    break
                else:
                    resultat_combat = combat.combat(pokemon_combat_choisie, pokemon_adversaire_combat_random)

                    if resultat_combat == pokemon_adversaire_combat_random:
                        score_pokemon_adversaire += 1
                    else:
                        score_pokemon_choisie += 1

                    print(" 💢 ", resultat_combat.name, " a été attaqué 💢 \n")
                    time.sleep(0.4)
            if pokemon_adversaire_combat_random.pv > pokemon_combat_choisie.pv:
                 vinqeur = pokemon_adversaire_combat_random
                 score_vinquer = score_pokemon_adversaire
                 print("\n💀💀💀 Votre Pokémon est KO 💀💀💀\n")
            else:
                 vinqeur = pokemon_combat_choisie
                 score_vinquer = score_pokemon_choisie
                 print("\n🏆🏆🏆 Votre Pokémon a gagné 🏆🏆🏆\n")


        else:
            break

else:
    vinqeur = pokemon_combat_choisie
    score_vinquer = score_pokemon_choisie
    print("🏆🏆🏆 Votre Pokémon a gagné 🏆🏆🏆\n")

pokemonfn.update_score(vinqeur,score_vinquer)
print(termcolor.colored("le pokemon vainqueur est ", "magenta", ["dark","bold"]))
pokemonfn.affiche_pokemon(vinqeur)
pokemonfn.update_niveau(vinqeur)








    




