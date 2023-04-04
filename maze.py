# Given a maze adn a nxn matrix. Some cells are blocked.
# Find if there is a path from cell start to cell end

class Maze:
    def __init__(self):
        self.max_rows = 5
        self.max_columns = 5
        row = [0]*self.max_columns
        self.maze = [row] * self.max_rows
        self.maze[0][3] = 9
        self.maze = [[0 for x in range(self.max_rows)] for y in range(self.max_columns)] 

        self.maze[0][3] = 9
        self.maze[1][2] = 9
        self.maze[2][2] = 9
        self.maze[4][2] = 9
        self.maze[3][4] = 9
        self.maze[4][3] = 9
        for i in range(self.max_rows):
            print(self.maze[i])

    def path(self, x1, y1, endx, endy):
        print('startx=%d starty=%d' % (x1, y1))
        # print('endx=%d endy=%d' % (endx, endy))

        if x1 == endx and y1 == endy:
            return True
        if not (0 <= x1 < self.max_rows):
            return False
        if not (0 <= y1 < self.max_columns):
            return False
        if self.maze[x1][y1] >= 1:
            return False

        self.maze[x1][y1] = 1

        return (self.path(x1+1, y1, endx, endy) or self.path(x1-1, y1, endx, endy) or self.path(x1, y1+1, endx, endy) or self.path(x1, y1-1, endx, endy))


def main():
    print('Maze: path exists ', Maze().path(1, 1, 4,4))


if __name__ == "__main__":
    main()
