from random import randint
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Window setup
root = tk.Tk()
root.title("Smash Character Randomiser")
root.geometry("600x600+400+50")
root.resizable(False, False)
root.config(background="DarkOrchid")

# Globals
characters = {
    1: "Mario",
    2: "Donkey Kong",
    3: "Link",
    4: "Samus/Dark Samus",
    5: "Yoshi",
    6: "Kirby",
    7: "Fox",
    8: "Pikachu",
    9: "Luigi",
    10: "Ness",
    11: "Captain Falcon",
    12: "Jigglypuff",
    13: "Peach/Daisy",
    14: "Bowser",
    15: "Ice Climbers",
    16: "Shiek",
    17: "Zelda",
    18: "Dr Mario",
    19: "Pichu",
    20: "Falco",
    21: "Marth/Lucina",
    22: "Young Link",
    23: "Ganondorf",
    24: "Mewtwo",
    25: "Roy/Chrom",
    26: "Mr Game & Watch",
    27: "Meta Knight",
    28: "Pit/Dark Pit",
    29: "Zero Suit Samus",
    30: "Wario",
    31: "Snake",
    32: "Ike",
    33: "Pokemon Trainer (Squirtle start)",
    34: "Pokemon Trainer (Ivysaur start)",
    35: "Pokemon Trainer (Charizard start)",
    36: "Diddy Kong",
    37: "Lucas",
    38: "Sonic",
    39: "King Dedede",
    40: "Olimar",
    41: "Lucario",
    42: "ROB",
    43: "Toon Link",
    44: "Wolf",
    45: "Villager",
    46: "Mega Man",
    47: "Wii Fit Trainer",
    48: "Rosalina & Luma",
    49: "Little Mac",
    50: "Greninja",
    51: "Mii Brawler",
    52: "Mii Swordfighter",
    53: "Mii Gunner",
    54: "Palutena",
    55: "Pac-Man",
    56: "Robin",
    57: "Shulk",
    58: "Bowser Jr",
    59: "Duck Hunt",
    60: "Ryu/Ken",
    61: "Cloud",
    62: "Corrin",
    63: "Bayonetta",
    64: "Inkling",
    65: "Ridley",
    66: "Simon/Richter",
    67: "King K Rool",
    68: "Isabelle",
    69: "Incineroar",
    70: "Piranha Plant",
    71: "Joker",
    72: "Hero",
    73: "Banjo & Kazooie",
    74: "Terry",
    75: "Byleth",
    76: "Min Min",
    77: "Steve",
    78: "Sephiroth",
    79: "Pyra",
    80: "Mythra",
    81: "Kazuya",
    82: "Sora",
}
used_charas = []

# Functions
def PickChara():
    CheckUsedCharas()
    while True:
        seed = randint(1, len(characters))
        if seed in used_charas:
            continue
        else:
            break
    used_charas.append(seed)
    messagebox.showinfo("Character", f"{characters[seed]}")


def CheckUsedCharas():
    if len(used_charas) >= len(characters):
        messagebox.showinfo(
            "Out of characters",
            "You've gotten every character!\nResetting the used_list.",
        )
        ResetUsedCharas()


def ResetUsedCharas():
    global used_charas
    used_charas = []


# Widgets
title = ttk.Label(
    root, text="Press 'Randomise' to pick a random character!", font=("Century", 15)
)
randomise = ttk.Button(root, text="Randomise", command=PickChara)
reset = ttk.Button(root, text="Reset used characters", command=ResetUsedCharas)
title.place(x=100, y=150)
randomise.place(x=150, y=300)
reset.place(x=300, y=300)

root.mainloop()
