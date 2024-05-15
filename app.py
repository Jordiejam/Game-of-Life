import pygame
import sys
import random

# Initialize Pygame
pygame.init()

WIDTH = 1000

num_cols = 100
w = WIDTH // num_cols
print(num_cols, w)

screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 10)

class Cell:
    def __init__(self, x, y, index, state=None):
        self.pos = pygame.Vector2(x, y)
        self.w = w
        self.rect = pygame.Rect(x, y, self.w, self.w)
        self.index = index

        if state is not None:
            self.state = state
        else:
            self.state = 1 if random.random() < 0.15 else 0
        self.next_state = 0
    
    def draw(self):
        if self.state:
            colour = "limegreen"
        else:
            colour = "white"
        pygame.draw.rect(screen, colour, self.rect)
    
    def update(self):
        self.state = self.next_state
    
    def check_neighbors(self, grid):
        neighbours = 0
        i, j = self.index
        
        if i != 0:
            if j != 0:
                neighbours += grid[i-1][j-1].state
            if j != len(grid[i]) - 1:
                neighbours += grid[i-1][j+1].state
            neighbours += grid[i-1][j].state
        if i != len(grid) - 1:
            if j != 0:
                neighbours += grid[i+1][j-1].state
            if j != len(grid[i]) - 1:
                neighbours += grid[i+1][j+1].state
            neighbours += grid[i+1][j].state
        if j != 0:
            neighbours += grid[i][j-1].state
        if j != len(grid[i]) - 1:
            neighbours += grid[i][j+1].state
        
        if self.state:
            if neighbours < 2:
                self.next_state = 0
            elif neighbours > 3:
                self.next_state = 0
            else:
                self.next_state = 1
            # print(self.index, neighbours)
        else:
            if neighbours == 3:
                self.next_state = 1

gospers_gun = [
    (1, 25), (2, 23), (2, 25), (3, 13), (3, 14), (3, 21), (3, 22), (3, 35), (3, 36),
    (4, 12), (4, 16), (4, 21), (4, 22), (4, 35), (4, 36), (5, 1), (5, 2), (5, 11), 
    (5, 17), (5, 21), (5, 22), (6, 1), (6, 2), (6, 11), (6, 15), (6, 17), (6, 18), 
    (6, 23), (6, 25), (7, 11), (7, 17), (7, 25), (8, 12), (8, 16), (9, 13), (9, 14)
]

lwss_pattern = [
    (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 1), (2, 5),
    (3, 5),
    (4, 1), (4, 4)
]

pulsar_pattern = [
    (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
    (4, 2), (4, 7), (4, 9), (4, 14),
    (5, 2), (5, 7), (5, 9), (5, 14),
    (6, 2), (6, 7), (6, 9), (6, 14),
    (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
    (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
    (10, 2), (10, 7), (10, 9), (10, 14),
    (11, 2), (11, 7), (11, 9), (11, 14),
    (12, 2), (12, 7), (12, 9), (12, 14),
    (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12)
]

r_pentomino_pattern = [
    (1, 2), (1, 3),
    (2, 1), (2, 2),
    (3, 2)
]

grid = [[Cell(j*w, i*w, (i, j)) for j in range(num_cols)] for i in range(num_cols)]

# Glider
# grid[1][1].state = 1
# grid[2][2].state = 1
# grid[2][3].state = 1
# grid[3][1].state = 1
# grid[3][2].state = 1

# for s in r_pentomino_pattern: # change variable to above pattern init state in grid to 0
#     grid[s[0]][s[1]].state = 1

# Main game loop
running = True
loop = 0
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                input("Pause")

    screen.fill("white")
    if loop != 0:
        for row in grid:
            for cell in row:
                cell.check_neighbors(grid)

    for row in grid:
        for cell in row:
            if loop != 0:
                cell.update()
            cell.draw()
            #screen.blit(font.render(str(cell.index), True, (0, 0, 0)), cell.pos)

    pygame.display.flip()

    clock.tick(24)

    loop += 1

pygame.quit()
sys.exit()