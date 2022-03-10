import chess.engine

class StockfishManager:

    def __init__(self, stockfish_path_name):
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path_name)

    def get_best_move(self, board):
        return str(self.engine.play(board, chess.engine.Limit(time=0.5)).move)
        
