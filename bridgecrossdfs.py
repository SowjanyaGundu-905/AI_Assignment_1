from itertools import combinations

# Crossing times
times = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

# Initial state: all on left, umbrella on left, time = 0
initial_state = (frozenset(times.keys()), frozenset(), 'L', 0)  # (left, right, umbrella side, time)

# Store best (minimum time) solution
best_solution = []
min_time = float('inf')

# Set to track visited states
visited_states = set()

def dfs(state, path):
    global best_solution, min_time

    left, right, umbrella_side, time = state

    # Goal check
    if len(left) == 0 and time <= 60:
        if time < min_time:
            min_time = time
            best_solution = path + [state]
        return

    # Prune if time exceeds limit
    if time > 60:
        return

    # Prune if already visited
    if (left, right, umbrella_side) in visited_states:
        return
    visited_states.add((left, right, umbrella_side))

    # DFS expansion
    if umbrella_side == 'L':
        # Send 2 people from left to right
        for a, b in combinations(left, 2):
            crossing_time = max(times[a], times[b])
            new_time = time + crossing_time
            new_left = left - {a, b}
            new_right = right | {a, b}
            new_state = (frozenset(new_left), frozenset(new_right), 'R', new_time)
            dfs(new_state, path + [state])
    else:
        # Return 1 person from right to left
        for a in right:
            return_time = times[a]
            new_time = time + return_time
            new_left = left | {a}
            new_right = right - {a}
            new_state = (frozenset(new_left), frozenset(new_right), 'L', new_time)
            dfs(new_state, path + [state])

# Start DFS
dfs(initial_state, [])

# Output result
if best_solution:
    print(" Solution found using DFS:")
    for i, state in enumerate(best_solution):
        left, right, umbrella, t = state
        print(f"Step {i}: Left: {left}, Right: {right}, Umbrella: {umbrella}, Time: {t}")
    print(f"Total time: {best_solution[-1][3]} minutes")
else:
    print("No solution found within 60 minutes.")


