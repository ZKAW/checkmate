import configparser

class Config:
    def __init__(self, disp_config=True):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        self.stockfish_path_name = f"libs/{config.get('stockfish', 'path')}"
        if 'true' in config.get('settings', 'legit').lower(): self.legit = True
        else: self.legit = False

        skill_level_conf = int(config.get('settings', 'skill_level'))

        if skill_level_conf > 20: self.skill_level = 20
        elif skill_level_conf < 0: self.skill_level = 0
        elif skill_level_conf == None: self.skill_level = 20
        else: self.skill_level = skill_level_conf

        if disp_config: self.disp_config()
    
    def disp_config(self):
        print(f"\nBot skill level: {self.skill_level}")
        print(f"Bot is {'legit' if self.legit else 'not legit'}\n")