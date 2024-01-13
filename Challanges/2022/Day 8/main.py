import os, sys

input_text = "puzzle_tree_heights_1.txt"

class Treetops:
    def __init__(self, trees):
        self.trees = [list(ts) for ts in trees.strip().splitlines()]
        self.seen_trees = [list(ts) for ts in trees.strip().splitlines()]

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
            print("".join(row))
        print()

        print(f"There were {visible} trees.")

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
