from collections import deque
from itertools import combinations

# Step 1: Define crossing times
times = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

# Step 2: Define initial state
initial_state = (frozenset(times.keys()), frozenset(), 'L', 0)  # (left, right, umbrella side, time)

# Step 3: BFS search
def is_goal(state):
    left, right, side, time = state
    return len(left) == 0 and time <= 60

def bfs():
    queue = deque()
    queue.append((initial_state, []))  # state, path
    visited = set()

    while queue:
        state, path = queue.popleft()
        left, right, side, time = state

        # Goal check
        if is_goal(state):
            return path + [state]

        # Avoid revisiting
        if state in visited:
            continue
        visited.add(state)

        # Generate next possible states
        if side == 'L':
            # Two people cross from left to right
            for a, b in combinations(left, 2):
                crossing_time = max(times[a], times[b])
                new_time = time + crossing_time
                if new_time > 60:
                    continue
                new_left = left - {a, b}
                new_right = right | {a, b}
                new_state = (frozenset(new_left), frozenset(new_right), 'R', new_time)
                queue.append((new_state, path + [state]))
        else:
            # One person returns from right to left
            for person in right:
                return_time = times[person]
                new_time = time + return_time
                if new_time > 60:
                    continue
                new_left = left | {person}
                new_right = right - {person}
                new_state = (frozenset(new_left), frozenset(new_right), 'L', new_time)
                queue.append((new_state, path + [state]))

    return None  # No solution

# Step 4: Run the algorithm
solution = bfs()

# Step 5: Display result
if solution:
    print(" Solution found!")
    for i, state in enumerate(solution):
        left, right, side, time = state
        print(f"Step {i}: Left: {left}, Right: {right}, Umbrella: {side}, Time: {time} mins")
    final_time = solution[-1][3]
    print(f"Total time taken: {final_time} minutes")
else:
    print(" No solution found within 60 minutes.")
