from collections import defaultdict, deque


def parse(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()
    
    rules_part, updates_part = content.split("\n\n")
    
    # Parse rules into list of tuples of integers
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y))) #tuple (X, Y) appended to the list

    # Parse updates into lists of integers
    updates = []
    update_lines = updates_part.splitlines()
    for line in update_lines:
        pages = line.split(",")
        updates.append([int(page) for page in pages])

    return rules, updates


def solve_part_two(rules, updates):
    def reorder_update(update, rules):
        # Build a directed graph for pages in the update
        graph = defaultdict(list)  # Tracks which pages must come after others
        in_degree = defaultdict(int)  # Tracks the number of dependencies (incoming edges), 
        # if not 0 cant be added to the sorted order because there is another number that must be added first.
        pages_in_update = set(update)  # Only consider rules relevant to this update

        # Add edges based on the rules
        for x, y in rules:
            if x in pages_in_update and y in pages_in_update:
                graph[x].append(y)
                in_degree[y] += 1
                in_degree[x] += 0  # Ensure all nodes appear in in_degree

        # Topological sort to reorder pages
        queue = deque()# Start with nodes having no dependencies (in-degree 0)
        for node in update:
            if in_degree[node] == 0:
                queue.append(node)
        sorted_order = []

        while queue:
            current = queue.popleft()  # Process a node with no dependencies
            sorted_order.append(current)
            for neighbor in graph[current]:  # Reduce dependencies for neighbors
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:  # If a neighbor has no more dependencies, add it to the queue
                    queue.append(neighbor)

        return sorted_order # assuming we always find way to sort it, else make statement to check length but it works.

    incorrect_updates_middle_sum = 0

    for update in updates:
        is_valid = True

        # Check if the update violates any rules
        for x, y in rules:
            if x in update and y in update and update.index(x) > update.index(y):
                is_valid = False
                break

        if not is_valid:
            # Reorder the update and add the middle page to the sum
            reordered_update = reorder_update(update, rules)
            middle_index = len(reordered_update) // 2
            incorrect_updates_middle_sum += reordered_update[middle_index]

    return incorrect_updates_middle_sum


file_path = "input.txt"
rules, updates = parse(file_path)
result = solve_part_two(rules, updates)
print(result)