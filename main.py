from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Pokemon(BaseModel):

    id = int
    name = str
    attack = int 
    life = bool
    type = str


pokemons = [
    Pokemon(id=1, name="bulbasaur", attack=49, life=45, type="grass"),
    Pokemon(id=2, name="ivysaur", attack=62, life=60, type="grass"),
    Pokemon(id=3, name="venusaur", attack=82, life=80, type="grass"),
    Pokemon(id=4, name="charmander", attack=52, life=39, type="fuego"),
    Pokemon(id=5, name="charmeleon", attack=64, life=58, type="fuego"),
    Pokemon(id=6, name="charizard", attack=84, life=78, type="fuego"),
    Pokemon(id=7, name="squirtle", attack=48, life=44, type="agua"),
    Pokemon(id=8, name="wartortle", attack=63, life=59, type="agua"),
    Pokemon(id=9, name="blastoise", attack=83, life=79, type="agua"),
    Pokemon(id=10, name="caterpie", attack=30, life=45, type="bug"),
]

