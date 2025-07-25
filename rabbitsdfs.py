start_state = "WWW_EEE"
goal_state = "EEE_WWW"

def get_next_states(state):
    state = list(state)
    empty = state.index('_')
    next_states = []

    for i in range(len(state)):
        if state[i] == 'W':
            if i + 1 == empty:
                new = state.copy()
                new[i], new[empty] = '_', 'W'
                next_states.append("".join(new))
            elif i + 2 == empty and state[i + 1] in ['W', 'E']:
                new = state.copy()
                new[i], new[empty] = '_', 'W'
                next_states.append("".join(new))

        elif state[i] == 'E':
            if i - 1 == empty:
                new = state.copy()
                new[i], new[empty] = '_', 'E'
                next_states.append("".join(new))
            elif i - 2 == empty and state[i - 1] in ['W', 'E']:
                new = state.copy()
                new[i], new[empty] = '_', 'E'
                next_states.append("".join(new))

    return next_states

def dfs(current, goal, path, visited):
    if current == goal:
        return path
    visited.add(current)
    for next_state in get_next_states(current):
        if next_state not in visited:
            result = dfs(next_state, goal, path + [next_state], visited)
            if result:
                return result
    return None

# Solve with DFS
solution = dfs(start_state, goal_state, [start_state], set())

# Output
if solution:
    print(f"Solution found in {len(solution)-1} steps:\n")
    for i, step in enumerate(solution):
        print(f"Step {i}: {step}")
else:
    print("No solution found.")
