from fastapi import FastAPI
from pydantic import BaseModel
import random
app = FastAPI()

class Pokemon(BaseModel):
    id: int
    nombre: str
    vida: int
    ataque: int
    tipo: str
    vivo: bool


pokemons = [
    Pokemon(id=1, nombre="bulbasaur", ataque=49, vida=45, tipo="grass", vivo=True),
    Pokemon(id=2, nombre="ivysaur", ataque=62, vida=60, tipo="grass", vivo=True),
    Pokemon(id=3, nombre="venusaur", ataque=82, vida=80, tipo="grass", vivo=True),
    Pokemon(id=4, nombre="charmander", ataque=52, vida=39, tipo="fuego", vivo=True),
    Pokemon(id=5, nombre="charmeleon", ataque=64, vida=58, tipo="fuego", vivo=True),
    Pokemon(id=6, nombre="charizard", ataque=84, vida=78, tipo="fuego", vivo=True),
    Pokemon(id=7, nombre="squirtle", ataque=48, vida=44, tipo="agua", vivo=True),
    Pokemon(id=8, nombre="wartortle", ataque=63, vida=59, tipo="agua", vivo=True),
    Pokemon(id=9, nombre="blastoise", ataque=83, vida=79, tipo="agua", vivo=True),
    Pokemon(id=10, nombre="caterpie", ataque=30, vida=45, tipo="bug", vivo=True),
]

# Mostrar todos los pokemon

@app.get("/mostrarpokemons")
def mostrar_pokemons():
    return pokemons


# Mostrar un pokemon por nombre

@app.get("/mostrarunpokemon")
def mostrar_un_pokemon(nombre: str):

    for pokemon in pokemons:

        if pokemon.nombre == nombre:
            return pokemon

    return {"mensaje": "pokemon no encontrado"}

# muestra un pokemon por id

@app.get("/mostrarpokemonid")
def mostrar_pokemon_id(id:int):
    for pokemon in pokemons:
        if pokemon.id == id:
            return pokemon
    
    return {"mensaje":"Pokemon no fue encontrado por el id"}

@app.get("/batallapokemon")
def batalla_pokemon():
    pokemon1= random.choice(pokemons)
    pokemon2= random.choice(pokemons)

    if pokemon1.ataque > pokemon2.ataque:
        ganador = pokemon1.nombre 
    elif pokemon2.ataque > pokemon1.ataque:
        ganador = pokemon2.nombre
    else:
        ganador = "empate"

    return {
        "pokemon1": pokemon1,
        "pokemon2": pokemon2,
        "ganador" : ganador
    }

@app.get("/ordenarpokemon")
def odernar_pokemon(campo:str):
    if campo == "ataque":
        lista = sorted(pokemons, key=lambda pokemon: pokemon.ataque)
    elif campo == "vida":
        lista = sorted(pokemons, key= lambda pokemon: pokemon.vida)

    else:
        return {
            "mensaje":"campo no valido"

        }
    return lista


