# =========================
# world.py
# =========================
import random
from collections import deque
from data import hero, party, monsters, game_map, items, fusion_table

# =========================
# 🚶 移動系統
# =========================
def move_location(hero):
    current = hero['location']
    print(f"\n📍 你目前在 {current}，可以前往：")
    options = game_map.get(current, [])
    for i, loc in enumerate(options):
        print(f"{i+1}. {loc}")
    choice = input("輸入編號移動: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(options):
            dest = options[idx]
            # 洞穴進入判定
            if dest == "Cave" and current == "Forest":
                roll = random.randint(1, 6)
                print(f"🎲 擲骰判定進入洞穴：{roll}")
                if roll not in [1, 3, 6]:
                    print("❌ 擲骰失敗，無法進入洞穴")
                    return
            hero['location'] = dest
            print(f"🚶 你移動到 {dest}")
            # 切換時間
            hero['time'] = "Evening" if hero['time'] == "Morning" else "Morning"
        else:
            print("❌ 無效編號")
    except ValueError:
        print("❌ 輸入錯誤")

# =========================
# 👹 遭遇怪物系統
# =========================
def encounter_monster(location):
    if location in ["Novice Village", "Town"]:
        return None
    if location == "Cave":
        return random.choice([m for m in monsters if m["name"] in ["Slime", "Goblin"]])
    if location == "Dungeon":
        return random.choice([m for m in monsters if "Dragon" in m["name"] 
                              and m["name"] not in ["Ancient Dragon","Light Dragon","Dark Dragon"]])
    if location == "Dragon City":
        return random.choice([m for m in monsters if m["name"] in [
            "Fire Dragon","Ice Dragon","Ancient Dragon","Light Dragon","Dark Dragon","Water Dragon"]])
    return random.choice([m for m in monsters if m["name"] not in [
        "Fire Dragon","Ice Dragon","Ancient Dragon","Light Dragon","Dark Dragon","Water Dragon","Slime","Goblin"]])

# =========================
# 🧭 BFS 最短路徑搜尋（地圖用）
# =========================
def bfs_shortest_path(start, goal):
    if start not in game_map or goal not in game_map:
        return None
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in game_map[current]:
            new_path = path + [neighbor]
            queue.append(new_path)
    return None

def bfs_command():
    print("\n🧭【BFS 最短路徑搜尋】")
    print(f"你目前在：{hero['location']}")
    target = input("請輸入目標地點：")
    path = bfs_shortest_path(hero["location"], target)
    if not path:
        print("❌ 找不到路徑")
        return
    print("📍 BFS 最短路徑：")
    print(" → ".join(path))

# =========================
# 📍 Dijkstra 裝備獲取難度
# =========================
import heapq

def dijkstra_shortest_path(start, goal, weights):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        cost, current, path = heapq.heappop(heap)
        if current == goal:
            return path, cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in weights.get(current, {}).items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return None, None

def dijkstra_command():
    print("\n🛡️【裝備獲取難度 - Dijkstra】")
    print(f"你目前在：{hero['location']}")
    target_item_name = input("請輸入想要取得的裝備名稱：")

    # 找裝備位置
    target_item = next((i for i in items if i["name"] == target_item_name), None)
    if not target_item:
        print("❌ 找不到該裝備")
        return

    # 生成權重圖（裝備難度）
    weights = {}
    for loc, neighbors in game_map.items():
        weights[loc] = {}
        for n in neighbors:
            # 預設難度 1，如果目標是某裝備所在位置則用裝備的難度
            w = 1
            if n == target_item["location"]:
                w = target_item.get("difficulty", 1)
            weights[loc][n] = w

    path, cost = dijkstra_shortest_path(hero["location"], target_item["location"], weights)
    if not path:
        print("❌ 找不到路徑")
        return

    print(f"📍 最短路徑（考慮裝備難度）： {' → '.join(path)}")
    print(f"⚔️ 總難度權重：{cost}")
