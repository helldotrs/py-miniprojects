import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def get_blank_position(self):
        blank_index = self.state.index('E')
        return blank_index // 3, blank_index % 3

    def get_possible_moves(self):
        moves = []
        row, col = self.get_blank_position()

        if row > 0:
            moves.append(('UP', row - 1, col))
        if row < 2:
            moves.append(('DOWN', row + 1, col))
        if col > 0:
            moves.append(('LEFT', row, col - 1))
        if col < 2:
            moves.append(('RIGHT', row, col + 1))

        return moves

    def generate_child(self, move):
        row, col = self.get_blank_position()
        index = row * 3 + col
        new_state = list(self.state)
        new_state[index], new_state[move[1] * 3 + move[2]] = new_state[move[1] * 3 + move[2]], new_state[index]
        return "".join(new_state)

    def is_goal(self):
        return self.state == "12345678E"

    def heuristic(self):
        h_cost = 0
        for i in range(9):
            if self.state[i] != 'E':
                h_cost += abs(i // 3 - (int(self.state[i]) - 1) // 3) + abs(i % 3 - (int(self.state[i]) - 1) % 3)
        return h_cost


def solve_puzzle(initial_state):
    open_set = []
    heapq.heappush(open_set, PuzzleNode(initial_state))
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.is_goal():
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add(current_node)
        possible_moves = current_node.get_possible_moves()

        for move in possible_moves:
            child_state = current_node.generate_child(move)
            child_node = PuzzleNode(child_state, parent=current_node, move=move[0], depth=current_node.depth + 1)

            if child_node not in closed_set:
                heapq.heappush(open_set, child_node)

    return None

def print_puzzle(state):
    print(state[0], "|", state[1], "|", state[2])
    print(state[3], "|", state[4], "|", state[5])
    print(state[6], "|", state[7], "|", state[8])
    print("--------")

def main():
    initial_state = input("Enter the initial state of the puzzle (e.g., 12345678E): ")
    solution_path = solve_puzzle(initial_state)

    if solution_path:
        for step, node in enumerate(solution_path):
            print(f"Step {step}: Move {node.move}")
            print_puzzle(node.state)
    else:
        print("No solution found for the given puzzle.")

if __name__ == "__main__":
    main()
