from fastapi import HTTPException
from trie import Trie
from log_config import get_root_logger, get_game_logger
from typing import List

root_logger = get_root_logger()


class Game:
    def __init__(self, min_length: int, max_len: int) -> None:
        """ 
        answer: dict[str, List[int]]
        maps the solution words to it's letter-index in the board as a list of integers
        """
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.min_ans_len= min_length
        self.max_ans_len= max_len
        self.answers = {}

    def populate_board(self, letters: str):
        """ """
        if len(letters) != 16:
            raise HTTPException(status_code=400)

        idx = 0
        letter_count = len(letters)

        while idx < letter_count:
            row = idx // 4
            col = idx % 4

            self.board[row][col] = letters[idx]
            idx += 1

    def find_solutions(self, trie: Trie, min_ans_len: int):
        if self.board is None or self.board[0][0] is None:
            return HTTPException(status_code=503, detail="board not populated correctly")

        root_logger.info("started solving")

        """
        - Do DFS at each <row><col> index pair in board
        - traverse along the with the trie
        - move to the next only if there is an next node in trie with that letter
        - check at each node if it is an word-ending
        - first log the <word : index> mapping and then add to answers UPON CHECKING MIN_LENGTH
        """

        for row in range(4):
            for col in range(4):
                
                self.dfs(row, col, trie.root) 

    def dfs(self, row: int, col: int, trie_node: dict, letters: List[str], indices: List[int]):
        
        
        
        