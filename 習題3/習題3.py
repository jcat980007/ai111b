start_state = {"left": ["wolf", "goat", "cabbage"], "right": [], "boat": "left"} # 初始狀態，左岸有狼、山羊和白菜，右岸沒有東西，船在左岸

moves = [("wolf",), ("goat",), ("cabbage",), ("wolf", "goat"), ("goat", "cabbage")] # 可以進行的移動組合

def is_valid(state):
    # 檢查是否有山羊和白菜同時在同一岸
    if "goat" in state["left"] and "cabbage" in state["left"]:
        return False
    if "goat" in state["right"] and "cabbage" in state["right"]:
        return False
    # 檢查是否有狼和山羊同時在同一岸，且船在對岸
    if "wolf" in state["left"] and "goat" in state["left"] and state["boat"] == "right":
        return False
    if "wolf" in state["right"] and "goat" in state["right"] and state["boat"] == "left":
        return False
    return True

def search_solution(state, visited_states):
    if len(state["left"]) == 0: # 終止條件，左岸沒有物品
        return []
    for move in moves:
        new_state = state.copy()
        if state["boat"] == "left":
            new_state["left"] = [x for x in state["left"] if x not in move] # 更新左岸物品
            new_state["right"] = sorted(state["right"] + list(move)) # 更新右岸物品
            new_state["boat"] = "right" # 更新船的位置
        else:
            new_state["right"] = [x for x in state["right"] if x not in move] # 更新右岸物品
            new_state["left"] = sorted(state["left"] + list(move)) # 更新左岸物品
            new_state["boat"] = "left" # 更新船的位置
        if is_valid(new_state) and str(new_state) not in visited_states:
            visited_states.add(str(new_state))
            solution = search_solution(new_state, visited_states) # 遞迴調用，搜索下一個狀態
            if solution is not None:
                return [new_state] + solution # 找到解決方案，返回包含當前狀態和解決方案的列表
    return None # 沒有找到解決方案

visited_states = set()
visited_states.add(str(start_state))
solution = search_solution(start_state, visited_states)

if solution is None:
    print("No solution found!")
else:
    for i, state in enumerate(solution):
        print("Step", i + 1, ":")
        print("Left:", state["left"])
        print("Right:", state["right"])
        print("Boat:", state["boat"])
