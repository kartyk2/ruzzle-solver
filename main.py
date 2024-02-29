from fastapi import FastAPI
from contextlib import asynccontextmanager
from trie import Trie
from game import Game
import sys


trie = Trie()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global trie
    # Load the trie object
    try:
        with open(
            "C:\\Users\\Comvision\\Desktop\\text8", "r", encoding="utf-8"
        ) as file:
            words = file.readline()
            corpus = words.split(sep=" ")

        corpora = []
        for each_word in corpus:
            each_word = each_word.strip()
            if len(each_word) > 1:
                corpora.append(each_word)

        trie.load(corpora)

    except Exception as error:
        # exit the application manually
        sys.exit(0)

    yield
    # Clean up and release the resources


app = FastAPI(lifespan=lifespan)


@app.post("/play_game")
async def play(letters: str, min_length: int = 0, max_len: int = 10):
    """ """
    letters = letters.lower().strip()
    
    game = Game(min_length, max_len)
    game.populate_board(letters)
    game.find_solutions(trie, min_length)
    
    return game.answers
    