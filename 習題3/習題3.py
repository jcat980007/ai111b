start_state = {"left": ["wolf", "goat", "cabbage"], "right": [], "boat": "left"}


moves = [("wolf",), ("goat",), ("cabbage",), ("wolf", "goat"), ("goat", "cabbage")]


def is_valid(state):
    if "goat" in state["left"] and "cabbage" in state["left"]:
        return False
    if "goat" in state["right"] and "cabbage" in state["right"]:
        return False
    if "wolf" in state["left"] and "goat" in state["left"] and state["boat"] == "right":
        return False
    if "wolf" in state["right"] and "goat" in state["right"] and state["boat"] == "left":
        return False
    return True


def search_solution(state, visited_states):
    if len(state["left"]) == 0:
        return []
    for move in moves:
        new_state = state.copy()
        if state["boat"] == "left":
            new_state["left"] = [x for x in state["left"] if x not in move]
            new_state["right"] = sorted(state["right"] + list(move))
            new_state["boat"] = "right"
        else:
            new_state["right"] = [x for x in state["right"] if x not in move]
            new_state["left"] = sorted(state["left"] + list(move))
            new_state["boat"] = "left"
        if is_valid(new_state) and str(new_state) not in visited_states:
            visited_states.add(str(new_state))
            solution = search_solution(new_state, visited_states)
            if solution is not None:
                return [new_state] + solution
    return None


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