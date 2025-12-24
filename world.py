import random
from collections import deque
import heapq
from data import hero, game_map, monsters

# 移動系統
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
            if dest == "Cave" and current == "Forest":
                roll = random.randint(1, 6)
                print(f"🎲 擲骰判定進入洞穴：{roll}")
                if roll not in [1,3,6]:
                    print("❌ 擲骰失敗，無法進入洞穴")
                    return
            hero['location'] = dest
            print(f"🚶 你移動到 {dest}")
            hero['time'] = "Evening" if hero['time'] == "Morning" else "Morning"
        else:
            print("❌ 無效編號")
    except ValueError:
        print("❌ 輸入錯誤")

# 怪物遭遇
def encounter_monster(location):
    if location in ["Novice Village", "Town"]:
        return None
    if location == "Cave":
        return random.choice([m for m in monsters if m["name"] in ["Slime", "Goblin"]])
    if location == "Dungeon":
        return random.choice([m for m in monsters if "Dragon" in m["name"] and m["name"] not in ["Ancient Dragon","Light Dragon","Dark Dragon"]])
    if location == "Dragon City":
        return random.choice([m for m in monsters if m["name"] in ["Fire Dragon","Ice Dragon","Ancient Dragon","Light Dragon","Dark Dragon","Water Dragon"]])
    return None

# BFS
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
            queue.append(path+[neighbor])
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

# Dijkstra
def dijkstra_shortest_path(start, goal, game_map_weights):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        cost, current, path = heapq.heappop(heap)
        if current == goal:
            return path, cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in game_map_weights.get(current, {}).items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost+weight, neighbor, path+[neighbor]))
    return None, None

def dijkstra_command():
    print("\n🛡️【裝備獲取難度 - Dijkstra】")
    print(f"你目前在：{hero['location']}")
    target = input("請輸入你想獲得裝備的地點：")
    game_map_weights = {
        "Novice Village":{"Forest":1,"Town":2},
        "Forest":{"Novice Village":1,"Town":2,"Cave":3},
        "Cave":{"Forest":3,"Dungeon":5},
        "Town":{"Novice Village":2,"Forest":2},
        "Dungeon":{"Cave":5,"Dragon City":7},
        "Dragon City":{"Dungeon":7}
    }
    path, cost = dijkstra_shortest_path(hero["location"], target, game_map_weights)
    if not path:
        print("❌ 找不到路徑")
        return
    print(f"📍 最短路徑（考慮難度）： {' → '.join(path)}")
    print(f"⚔️ 總難度權重：{cost}")
