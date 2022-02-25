from random import randint


def PickChara(used_charas: list, charas: dict):
    while True:
        seed = randint(1, len(charas))
        if seed in used_charas:
            continue
        else:
            break
    used_charas.append(seed)
    print(f"{charas[seed]}\n")


def CheckList(used_charas, charas):
    if len(used_charas) >= len(charas):
        print("All characters have been used!")
        used_charas = []


def main():
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
    used_chars = []

    while True:
        start = input(
            "Type 'g' to randomise, 'r' to reset the used list, or 'q' to quit: "
        ).lower()
        if start == "g":
            PickChara(used_chars, characters)
        elif start == "r":
            used_chars = []
        elif start == "q":
            quit()
        else:
            print("Invalid response.")

        CheckList(used_chars, characters)


if __name__ == "__main__":
    main()
