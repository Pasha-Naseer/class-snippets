import json
import matplotlib.pyplot as plt
import pygame
import random
import os
import datetime

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10
BLOCK_SIZE = WIDTH // COLS

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (80, 80, 80)

# Tetromino shapes
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]],
}

SHAPE_COLORS = {
    'I': CYAN,
    'O': YELLOW,
    'T': PURPLE,
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': ORANGE,
}


def create_grid(locked_positions=None):
    if locked_positions is None:
        locked_positions = {}

    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLS):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid


class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = SHAPE_COLORS[shape]
        self.rotation = 0
        self.x = COLS // 2 - len(SHAPES[shape][0]) // 2
        self.y = 0

    def image(self):
        return self.rotate(self.rotation)

    def rotate(self, rot):
        shape = SHAPES[self.shape]
        for _ in range(rot % 4):
            shape = [list(row) for row in zip(*shape[::-1])]
        return shape

    def get_cells(self):
        positions = []
        shape_matrix = self.image()
        for i, row in enumerate(shape_matrix):
            for j, val in enumerate(row):
                if val:
                    positions.append((self.x + j, self.y + i))
        return positions

    def valid_position(self, grid):
        for x, y in self.get_cells():
            if x < 0 or x >= COLS or y < 0 or y >= ROWS:
                return False
            if grid[y][x] != BLACK:
                return False
        return True

    def move(self, dx, dy, grid):
        self.x += dx
        self.y += dy
        if not self.valid_position(grid):
            self.x -= dx
            self.y -= dy
            return False
        return True


def clear_rows(grid, locked):
    full_rows = [y for y in range(ROWS) if BLACK not in grid[y]]

    for y in full_rows:
        for x in range(COLS):
            del locked[(x, y)]

    for key in sorted(list(locked.keys()), key=lambda k: k[1], reverse=True):
        x, y = key
        cleared_below = sum(1 for row in full_rows if row > y)
        if cleared_below > 0:
            locked[(x, y + cleared_below)] = locked.pop((x, y))

    return len(full_rows)


def calculate_score(lines_cleared):
    if lines_cleared == 1:
        return 100
    if lines_cleared == 2:
        return 300
    if lines_cleared == 3:
        return 500
    if lines_cleared == 4:
        return 800
    return 0


def draw_grid(screen, grid):
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(
                screen,
                grid[y][x],
                (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )

    for y in range(ROWS):
        pygame.draw.line(screen, WHITE, (0, y * BLOCK_SIZE), (WIDTH, y * BLOCK_SIZE))
    for x in range(COLS):
        pygame.draw.line(screen, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT))


def draw_score(screen, score, player_name, font):
    score_text = font.render(f"{player_name} - Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def draw_pause(screen, font):
    pause_text = font.render("Paused", True, WHITE)
    pause_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(pause_text, pause_rect)


def get_player_name(screen, title_font, input_font):
    player_name = ""
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name.strip():
                        input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    if len(player_name) < 12 and event.unicode.isprintable():
                        player_name += event.unicode

        screen.fill(BLACK)
        title_text = title_font.render("Enter Player Name", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        screen.blit(title_text, title_rect)

        input_box = pygame.Rect(40, HEIGHT // 2 - 10, WIDTH - 80, 40)
        pygame.draw.rect(screen, WHITE, input_box, 2)

        name_surface = input_font.render(player_name, True, WHITE)
        screen.blit(name_surface, (input_box.x + 10, input_box.y + 8))

        hint_text = input_font.render("Press Enter to start", True, GRAY)
        hint_rect = hint_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        screen.blit(hint_text, hint_rect)
        pygame.display.update()

    return player_name.strip()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)
    title_font = pygame.font.SysFont("arial", 30)

    player_name = get_player_name(screen, title_font, font)
    if player_name is None:
        pygame.quit()
        return

    locked_positions = {}
    current_piece = Tetromino(random.choice(list(SHAPES.keys())))
    fall_time = 0
    fall_speed = 0.5
    score = 0
    paused = False

    running = True
    while running:
        clock.tick()
        grid = create_grid(locked_positions)

        if not paused:
            fall_time += clock.get_rawtime()

            if fall_time / 1000 >= fall_speed:
                fall_time = 0
                if not current_piece.move(0, 1, grid):
                    for x, y in current_piece.get_cells():
                        locked_positions[(x, y)] = current_piece.color
                    grid = create_grid(locked_positions)
                    lines_cleared = clear_rows(grid, locked_positions)
                    score += calculate_score(lines_cleared)
                    grid = create_grid(locked_positions)
                    current_piece = Tetromino(random.choice(list(SHAPES.keys())))
                    if not current_piece.valid_position(grid):
                        running = False
        else:
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif not paused:
                    if event.key == pygame.K_LEFT:
                        current_piece.move(-1, 0, grid)
                    elif event.key == pygame.K_RIGHT:
                        current_piece.move(1, 0, grid)
                    elif event.key == pygame.K_DOWN:
                        current_piece.move(0, 1, grid)
                    elif event.key == pygame.K_UP:
                        current_piece.rotation += 1
                        if not current_piece.valid_position(grid):
                            current_piece.rotation -= 1
                    elif event.key == pygame.K_SPACE:
                        # Hard Drop Logic: keep moving down until collision
                        while current_piece.move(0, 1, grid):
                            pass

        screen.fill(BLACK)
        draw_grid(screen, grid)

        for x, y in current_piece.get_cells():
            pygame.draw.rect(
                screen,
                current_piece.color,
                (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )

        draw_score(screen, score, player_name, font)
        if paused:
            draw_pause(screen, font)

        pygame.display.update()

    if os.path.exists("tetris-records.json"):
        with open("tetris-records.json", 'r') as f:
            data = json.load(f)
    else:
        data = {}

    new_data = {str(datetime.datetime.now()):{player_name:score}}
    data.update(new_data)
    with open("tetris-records.json", 'w') as f:
        json.dump(data, f)

    # print(f"Game Over - {player_name}: {score}")

    pygame.quit()

    with open("tetris-records.json", 'r') as f:
        data = json.load(f)
        scores = []
        names = []
        for i, j in data.items():
            names.append(list(j.keys())[0])
            scores.append(list(j.values())[0])

    print(names)
    print(scores)
    # try to rethink bubble sort if users are more than expected
    # for i in range(len(scores)):
    #     if i == 1:
    #         continue
    #     if scores[i]:
    for _ in range(len(scores)):
        for i in range(len(scores) - 1):
            if scores[i] > scores[i + 1]:
                scores[i], scores[i + 1] = scores[i + 1], scores[i]
                names[i], names[i+1] = names[i+1], names[i]

    names.reverse()
    names2 = names.copy()
    scores.reverse()
    scores2 = scores.copy()

    for i in range(len(names2)):
        names2[i] = names2[i].strip().lower()

    track_list_names = []
    track_list_scores = []
    for i in names2:
        if i in track_list_names:
            if scores2[names2.index(i)] > track_list_scores[track_list_names.index(i)]:
                track_list_scores[track_list_names.index(i)] = scores2[names2.index(i)]
            # elif scores2[names2.index(i)] < track_list_scores[track_list_names.index(i)]:
            #     pass
            # else:
            #     pass

        else:
            track_list_names.append(i)
            track_list_scores.append(scores[names2.index(i)])

        print(track_list_names)
        print(track_list_scores)

    fig, ax = plt.subplots()

    bars = ax.bar(track_list_names, track_list_scores)

    # Add the exact values on top of each bar
    ax.bar_label(bars, fmt='%d')  # Use '%d' if scores are integers

    ax.set_ylabel('Scores')
    ax.set_title('All time best players!')

    plt.show()
if __name__ == "__main__":
    main()
