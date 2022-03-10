# Chess.com bot

Automatically win chess.com games using stockfish engine.

## Install libaries

Download Stockfish engine at: https://stockfishchess.org/download/, add it to the stockfish folder and put the filename in the config

```
pip3 install -r requirements.txt
```


## Config

* stockfish_path_name: filename of stockfish.exe


## Play

Terminal version:
```
python3 bot.py
```
GUI version:
```
python3 -m bot-gui
```

Search for a game.
When found, start the bot.