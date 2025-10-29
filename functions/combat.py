import random
from models.Pokemon import Pokemon
import functions.pokemon as pokemonfn

def combat(pokemon_choisie, pokemon_adversaire):
    list = [pokemon_choisie , pokemon_adversaire]
    pokemon_random = random.choice(list)
    pokemon_battue = next(p for p in list if p != pokemon_random)
    pokemon_battue.pv -= pokemon_random.attaque
    pokemonfn.update_pv(pokemon_battue,pokemon_battue.pv)
    return pokemon_battue