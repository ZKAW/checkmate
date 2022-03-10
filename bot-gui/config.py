import configparser

class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        self.stockfish_path_name = f"libs/{config.get('stockfish', 'path')}"