import os, sys

input_text = "puzzle_tree_heights_1.txt"

class Treetops:
    def __init__(self, trees):
        self.trees = [list(map(int, ts)) for ts in trees.strip().splitlines()]
        self.seen_trees = [list(map(int, ts)) for ts in trees.strip().splitlines()]
        self.scenic_scores = [[0][:] * len(ts) for ts in trees.strip().splitlines()]

    def find_visible_trees(self):
        visible = 0

        for i in range(0, len(self.trees)):
            for j in range(0, len(self.trees[i])):
                if (i != 0 and i != len(self.trees)-1) and (j !=0 and j != len(self.trees[i])-1):
                    # We're in the center don't look here yet
                    continue
                if self.seen_trees[i][j] != "X":
                    visible += 1
                self.seen_trees[i][j] = "X"
                if (i == 0 and j == 0) or \
                    (i == 0 and j == len(self.trees[i])-1) or \
                    (i == len(self.trees)-1 and j == 0) or \
                    (i == len(self.trees)-1 and j == len(self.trees[i])-1):
                    # We're in a corner, so nothing to see
                    continue
                else:
                    max_tree = self.trees[i][j]
                    if i == 0:
                        for y in range(1, len(self.trees)):
                            new_y = i + y
                            tree = self.trees[new_y][j]
                            if tree > max_tree:
                                max_tree = max(max_tree, tree)
                                if self.seen_trees[new_y][j] != "X":
                                    visible += 1
                                self.seen_trees[new_y][j] = "X"
                    elif i == len(self.trees) - 1:
                        for y in range(1, len(self.trees)):
                            new_y = i-y
                            tree = self.trees[new_y][j]
                            if tree > max_tree:
                                max_tree = max(max_tree, tree)
                                if self.seen_trees[new_y][j] != "X":
                                    visible += 1
                                self.seen_trees[new_y][j] = "X"
                    elif j == 0:
                        for x in range(1, len(self.trees[i])):
                            new_x = j+x
                            tree = self.trees[i][new_x]
                            if tree > max_tree:
                                max_tree = max(max_tree, tree)
                                if self.seen_trees[i][new_x] != "X":
                                    visible += 1
                                self.seen_trees[i][new_x] = "X"
                    elif j == len(self.trees[i]) - 1:
                        for x in range(1, len(self.trees[i])):
                            new_x = j - x
                            tree = self.trees[i][new_x]
                            if tree > max_tree:
                                max_tree = max(max_tree, tree)
                                if self.seen_trees[i][new_x] != "X":
                                    visible += 1
                                self.seen_trees[i][new_x] = "X"

        for row in self.seen_trees:
            print(row)
        print()

        print(f"There were {visible} trees.")
    
    def find_scenic_score(self):
        views = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_scenic_score = 0
        for y in range(len(self.trees)):
            for x in range(len(self.trees[y])):
                scenic_score = 0
                for view in views:
                    view_scenic_score = 0
                    current_x = x
                    current_y = y
                    max_tree = -1
                    move_x, move_y = view

                    if move_x != 0:
                        for j in range(1, len(self.trees[y])):
                            current_x += move_x
                            if current_x < 0 or current_x >= len(self.trees[y]):
                                break
                            view_scenic_score += 1
                            if self.trees[y][current_x] >= max_tree:
                                max_tree = max(self.trees[y][current_x], max_tree)
                                if max_tree >= self.trees[y][x]:
                                    break
                    elif move_y != 0:
                        for j in range(1, len(self.trees)):
                            current_y += move_y
                            if current_y < 0 or current_y >= len(self.trees):
                                break
                            view_scenic_score += 1
                            if self.trees[current_y][x] >= max_tree:
                                max_tree = max(self.trees[current_y][x], max_tree)
                                if max_tree >= self.trees[y][x]:
                                    break
                    if view_scenic_score != 0:
                        if scenic_score == 0:
                            scenic_score = 1
                        scenic_score *= view_scenic_score

                self.scenic_scores[y][x] = scenic_score
                max_scenic_score = max(max_scenic_score, scenic_score)
        
        for row in self.scenic_scores:
            print(row)
        
        print(f"Max scenic score {max_scenic_score}")

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    treetops = Treetops(get_file(path, input_text))
    treetops.find_visible_trees()
    treetops.find_scenic_score()
