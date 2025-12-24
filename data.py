# data.py
import json
import os

SAVE_FILE = "save.json"

# 玩家資料
hero = {
    "name": "勇者",
    "hp": 50,
    "max_hp": 50,
    "attack_bonus": 5,
    "base_damage": 10,
    "brave_power": True,
    "strength": 10,
    "agility": 10,
    "intelligence": 10,
    "time": "Morning",
    "location": "Novice Village"
}

# 隊伍
party = []

# 地圖
game_map = {
    "Novice Village": ["Forest", "Town"],
    "Forest": ["Novice Village", "Town", "Cave"],
    "Cave": ["Forest", "Dungeon"],
    "Town": ["Novice Village", "Forest"],
    "Dungeon": ["Cave", "Dragon City"],
    "Dragon City": ["Dungeon"]
}

# 裝備
items = [
    {"name": "新手劍", "attack": 8, "rarity": 1},
    {"name": "木盾", "attack": 2, "rarity": 1},
    {"name": "騎士鋼劍", "attack": 18, "rarity": 3},
    {"name": "聖光鎧甲", "attack": 4, "rarity": 4},
    {"name": "勇者勝利之劍", "attack": 50, "rarity": 6}
]

# 怪物
monsters = [
    {"name": "Slime", "element": "None", "weakness": "Fire", "hp": 10, "ac": 8, "base_attack": 5},
    {"name": "Goblin", "element": "None", "weakness": "Ice", "hp": 15, "ac": 11, "base_attack": 6},
    {"name": "Skeleton", "element": "None", "weakness": "Light", "hp": 20, "ac": 13, "base_attack": 7},
    {"name": "Orc", "element": "None", "weakness": "Lightning", "hp": 25, "ac": 14, "base_attack": 8},
    {"name": "Fire Dragon", "element": "Fire", "weakness": "Ice", "hp": 50, "ac": 18, "base_attack": 12},
    {"name": "Ice Dragon", "element": "Ice", "weakness": "Fire", "hp": 50, "ac": 18, "base_attack": 12},
    {"name": "Wind Dragon", "element": "Wind", "weakness": None, "hp": 45, "ac": 17, "base_attack": 10},
    {"name": "Earth Dragon", "element": "Earth", "weakness": None, "hp": 45, "ac": 17, "base_attack": 10},
    {"name": "Water Dragon", "element": "Water", "weakness": None, "hp": 45, "ac": 17, "base_attack": 10},
    {"name": "Wood Dragon", "element": "Wood", "weakness": "Wood", "hp": 50, "ac": 18, "base_attack": 11},
    {"name": "Thunder Dragon", "element": "Thunder", "weakness": "Earth", "hp": 55, "ac": 19, "base_attack": 13},
    {"name": "Light Dragon", "element": "Light", "weakness": "Dark", "hp": 60, "ac": 20, "base_attack": 14},
    {"name": "Dark Dragon", "element": "Dark", "weakness": "Light", "hp": 60, "ac": 20, "base_attack": 14},
    {"name": "Ancient Dragon", "element": "Ancient", "weakness": "Brave Power",
     "hp": 100, "ac": 25, "base_attack": 20}
]

# 存檔/讀檔
def save_game(hero, party):
    data = {"hero": hero, "party": party, "items": items}
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("💾 遊戲已存檔")

def load_game(hero, party):
    if not os.path.exists(SAVE_FILE):
        print("📂 沒有存檔，開始新遊戲")
        return
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    hero.update(data["hero"])
    party.clear()
    party.extend(data["party"])
    print("📂 讀取存檔完成")
