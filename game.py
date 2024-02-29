from fastapi import HTTPException
from trie import Trie
from log_config import get_root_logger, get_game_logger
from typing import List

root_logger = get_root_logger()


class Game:
    def __init__(self, min_length: int, max_len: int) -> None:
        """ 
        answer: dict[str, List[List[int]]]
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
                
                self.dfs(row, col, trie.root, [], [], {}) 

    def dfs(self, row: int, col: int, trie_node: dict, letters: List[str], indices: List[int], visited: dict):
        letter= self.board[row][col]
        
        # max len check
        if len(letters) >= self.max_ans_len:
            return
        
        # no word available in trie by choosing letter at <row><col> index in board
        if letter not in trie_node:
            return
        
        # add index and letter into their lists
        letters.append(letter)
        indices.append([row, col])
        
        # check if letter makes a word
        trie_node= trie_node[letter]
        if trie_node.get('#', False) and len(letters) > self.min_ans_len:
            answer_word= "".join(letters)
            if answer_word not in self.answers:
            
                root_logger.info(answer_word)        
                self.answers[answer_word]= indices
        
        
        possible_indices= self.find_possible_indices_form_index(row, col, visited)
        
        for position in possible_indices:
            self.dfs(position[0], position[1], trie_node, letters.copy(), indices.copy(), visited.copy())    

        
    def find_possible_indices_form_index(self, row: int, col: int, visited: set):

        possible_move= [-1, 0, 1]
        possible_indices= []
        
        for row_shift in possible_move:
            for col_shift in possible_move:
                
                new_row= row+row_shift
                new_col= col+col_shift 
                
                if (new_row, new_col) not in visited and new_col in range(4) and new_row in range(4):
                    possible_indices.append([new_row, new_col])
        
        return possible_indices