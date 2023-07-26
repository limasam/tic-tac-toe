import pygame
import sys

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры окна
WIDTH, HEIGHT = 300, 300

# Размеры ячейки
CELL_SIZE = WIDTH // 3

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

# Создание пустого игрового поля
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отображения текста на экране
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Функция для рисования игрового поля
def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i))
        pygame.draw.line(screen, BLACK, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT))

# Функция для определения победителя
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Функция для очистки игрового поля
def clear_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

# Основная функция игры
def game():
    current_player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if board[row][col] == ' ':
                    board[row][col] = current_player
                    if check_winner():
                        game_over = True
                    else:
                        current_player = 'X' if current_player == 'O' else 'O'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    clear_board()
                    current_player = 'X'
                    game_over = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        draw_board()

        for i in range(3):
            for j in range(3):
                if board[i][j] != ' ':
                    draw_text(board[i][j], pygame.font.Font(None, 80), BLACK, j * CELL_SIZE + 20, i * CELL_SIZE + 20)

        if game_over:
            winner = check_winner()
            draw_text(f"Игрок {winner} победил!", pygame.font.Font(None, 40), BLACK, 20, HEIGHT // 2)
            draw_text("Нажмите R для новой игры", pygame.font.Font(None, 20), BLACK, 20, HEIGHT // 2 + 50)

        pygame.display.update()

# Запуск игры
game()
