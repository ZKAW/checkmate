from dis import dis
import chess.engine

from .config import Config
from libs.stockfishpy import *

class StockfishManager:
    config = Config(disp_config=False)

    def __init__(self, stockfish_path_name):
        self.engine = Engine(stockfish_path_name, param={
                        'Threads': 2,
                        'Ponder': None,
                        'Skill Level': self.config.skill_level, # min 0 max 20
                    })

    def get_best_move(self, board):
        self.engine.ucinewgame()
        self.engine.setposition(board.fen())

        move = self.engine.bestmove()

        bestmove = move['bestmove']

        return bestmove