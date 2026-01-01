# =========================
# data.py
# =========================

# 勇者資訊
hero = {
    "name": "勇者",
    "location": "Novice Village",
    "time": "Morning",
    "hp": 50,
    "max_hp": 50,
    "attack_bonus": 2,
    "base_damage": 10,
    "strength": 5,
    "agility": 4,
    "intelligence": 3,
    "brave_power": True
}

# 隊友
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

# 怪物列表
monsters = [
    {"name": "Slime", "hp": 20, "ac": 8, "base_attack": 2, "element": "Water"},
    {"name": "Goblin", "hp": 25, "ac": 10, "base_attack": 3, "element": "Earth"},
    {"name": "Ice Dragon", "hp": 100, "ac": 15, "base_attack": 12, "is_dragon": True, "element": "Ice"},
    {"name": "Fire Dragon", "hp": 120, "ac": 16, "base_attack": 14, "is_dragon": True, "element": "Fire"},
    {"name": "Ancient Dragon", "hp": 200, "ac": 18, "base_attack": 20, "is_dragon": True, "element": "Earth"},
    {"name": "Light Dragon", "hp": 150, "ac": 17, "base_attack": 16, "is_dragon": True, "element": "Light"},
    {"name": "Dark Dragon", "hp": 150, "ac": 17, "base_attack": 16, "is_dragon": True, "element": "Dark"},
    {"name": "Water Dragon", "hp": 110, "ac": 15, "base_attack": 13, "is_dragon": True, "element": "Water"},
    {"name": "Orc", "hp": 40, "ac": 12, "base_attack": 5, "element": "Earth"},
    {"name": "Troll", "hp": 60, "ac": 14, "base_attack": 6, "element": "Earth"},
    {"name": "Goblin King", "hp": 80, "ac": 16, "base_attack": 8, "element": "Earth"},
    {"name": "Slime King", "hp": 70, "ac": 15, "base_attack": 7, "element": "Water"},
    {"name": "Fire Elemental", "hp": 90, "ac": 14, "base_attack": 9, "element": "Fire"},
    {"name": "Ice Elemental", "hp": 90, "ac": 14, "base_attack": 9, "element": "Ice"}
]

# 裝備資料（加上難度和地點）
items = [
    {"name": "Iron Sword", "attack": 10, "rarity": "Common", "difficulty": 1, "location": "Novice Village"},
    {"name": "Steel Sword", "attack": 15, "rarity": "Uncommon", "difficulty": 3, "location": "Town"},
    {"name": "Flame Sword", "attack": 20, "rarity": "Rare", "difficulty": 5, "location": "Cave"},
    {"name": "Dragon Shield", "attack": 5, "rarity": "Rare", "difficulty": 6, "location": "Dragon City"},
    {"name": "Ice Staff", "attack": 18, "rarity": "Rare", "difficulty": 5, "location": "Dungeon"},
    {"name": "Light Bow", "attack": 22, "rarity": "Epic", "difficulty": 7, "location": "Dragon City"},
    {"name": "Dark Dagger", "attack": 20, "rarity": "Epic", "difficulty": 7, "location": "Dungeon"},
]

# 融合技能表（龍元素疊加）
fusion_table = {
    frozenset(["Fire", "Wind"]): {"name": "烈焰風暴", "bonus": 15},
    frozenset(["Water", "Ice"]): {"name": "極寒洪流", "bonus": 15},
    frozenset(["Light", "Dark"]): {"name": "混沌審判", "bonus": 25},
    frozenset(["Fire", "Ice"]): {"name": "融焰寒暴", "bonus": 20},
    frozenset(["Earth", "Wind"]): {"name": "大地旋風", "bonus": 18},
    frozenset(["Fire", "Water"]): {"name": "蒸汽爆擊", "bonus": 20},
    frozenset(["Light", "Water"]): {"name": "聖光洪流", "bonus": 22},
    frozenset(["Dark", "Earth"]): {"name": "暗影裂擊", "bonus": 22},
}

# =========================
# 💾 存檔 / 讀檔系統
# =========================
import json
import os

SAVE_FILE = "save.json"

def save_game(hero, party):
    data = {
        "hero": hero,
        "party": party
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("💾 遊戲已存檔")

def load_game(hero, party):
    if not os.path.exists(SAVE_FILE):
        return
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    hero.update(data.get("hero", {}))
    party.clear()
    party.extend(data.get("party", []))
    print("📂 已讀取存檔")
