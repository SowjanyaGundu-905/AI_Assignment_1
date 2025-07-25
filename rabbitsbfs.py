from collections import deque

start_state = "WWW_EEE"
goal_state = "EEE_WWW"

def get_next_states(state):
    state = list(state)
    empty = state.index('_')
    next_states = []

    for i in range(len(state)):
        if state[i] == 'W':
            # W can move right into empty space
            if i + 1 == empty:
                new_state = state.copy()
                new_state[i], new_state[empty] = '_', 'W'
                next_states.append("".join(new_state))
            # W can jump over 1 rabbit to right
            elif i + 2 == empty and state[i + 1] in ['W', 'E']:
                new_state = state.copy()
                new_state[i], new_state[empty] = '_', 'W'
                next_states.append("".join(new_state))

        elif state[i] == 'E':
            # E can move left into empty space
            if i - 1 == empty:
                new_state = state.copy()
                new_state[i], new_state[empty] = '_', 'E'
                next_states.append("".join(new_state))
            # E can jump over 1 rabbit to left
            elif i - 2 == empty and state[i - 1] in ['W', 'E']:
                new_state = state.copy()
                new_state[i], new_state[empty] = '_', 'E'
                next_states.append("".join(new_state))

    return next_states

def bfs(start, goal):
    queue = deque()
    visited = set()
    queue.append((start, [start]))

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for next_state in get_next_states(current):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    return None

# Run BFS
solution = bfs(start_state, goal_state)

# Print result
if solution:
    print(f"✅ Solution found in {len(solution)-1} steps:\n")
    for i, step in enumerate(solution):
        print(f"Step {i}: {step}")
else:
    print("❌ No solution found.")



