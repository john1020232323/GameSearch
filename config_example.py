import os
from dotenv import load_dotenv

load_dotenv()

RAWG_API = os.getenv("RAWG_API_KEY")
DEBUG_STR = os.getenv("DEBUG_MODE", "False")

DEBUG = DEBUG_STR.lower() in ('yes', '1', 'true')

cheapshark_url = "https://www.cheapshark.com/api/1.0/"
rawg_url = "https://api.rawg.io/api/"

headers = {
        "User-Agent": "MyPersonalGameTracker/1.0 (LearningProject; your_email_com)"
}

cheapshark_store_map = {
    "1": "Steam",
    "2": "GamersGate",
    "3": "Green Man Gaming",
    "4": "Amazon",
    "5": "GameStop",
    "6": "Direct2Drive",
    "7": "GOG",
    "8": "Origin",
    "9": "Get Games",
    "10": "Shiny Loot",
    "11": "Epic Games Store",
    "12": "IndieGameStand",
    "13": "AllYouPlay",
    "14": "Blink Bundle",
    "15": "Punkwave",
    "16": "SilaGames",
    "17": "MacGameStore",
    "18": "2Game",
    "19": "IndieGala",
    "20": "Etail Market",
    "21": "Imperial Games",
    "22": "Bundle Stars",
    "23": "GameBillet",
    "24": "Voidu",
    "25": "Epic Games Store (Alternative)",  # Often references custom Epic keys or developer-direct distribution
    "26": "Razed",
    "27": "Gamesplanet",
    "28": "Gamesload / Nexway",
    "29": "2Game (Alternative)",
    "30": "IndieGala (Alternative)",
    "31": "Blizzard Shop",
    "32": "AllYouPlay (Alternative)",
    "33": "DLGamer",
    "34": "Noctre",
    "35": "DreamGame"
}
