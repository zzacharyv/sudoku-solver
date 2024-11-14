import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def draw_board(screen, board, width, height):
    w = width
    h = height
    coleur = (129,82,82)

    screen.fill((234,219,167))

    for i in range(0, w, (int)(w/9)):
        if i % (int)(w/3) == 0 and i != 0:
            pygame.draw.line(screen, coleur, (i, 0), (i, h), 7)
        elif i != 0:
            pygame.draw.line(screen, coleur, (i, 0), (i, h), 2)

    for i in range(0, w, (int)(w/9)):
        if i % (int)(h/3) == 0 and i != 0:
            pygame.draw.line(screen, coleur, (0, i), (w, i), 7)
        elif i != 0:
            pygame.draw.line(screen, coleur, (0, i), (w, i), 2)

    pygame.font.init()
    font = pygame.font.SysFont('optima', 36)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] != 0):
                poo = font.render(str(board[i][j]), True, (52, 105, 91),None)
                screen.blit(poo, (i*56+23,j*56+16))
    pygame.display.update()
    pygame.display.flip()

def display_backtracking(board):
    import backtracking
    pygame.init()
    SCREEN_WIDTH = 504
    SCREEN_HEIGHT = 504

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((234,219,167))

    draw_board(screen, board, SCREEN_HEIGHT, SCREEN_WIDTH)      

    running = True
    finished = 1
    # Main loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

        if finished == 1:
            backtracking.solve_and_display(board,screen,0,0)
            finished = 2

def display_csp(board):
    import constraintSatisfactionProblem as csp
    pygame.init()
    SCREEN_WIDTH = 504
    SCREEN_HEIGHT = 504

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((234,219,167))

    draw_board(screen, board, SCREEN_HEIGHT, SCREEN_WIDTH)      

    running = True
    finished = 1
    # Main loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

        if finished == 1:
            csp.solve_and_display(board,screen)
            finished = 2

def display_game(board,algorithm):
    if algorithm == "backtracking":
        display_backtracking(board)
    else:
        display_csp(board)

def main():
    board = [[0, 0, 0, 6, 7, 8, 0, 1, 0], 
             [6, 7, 2, 0, 9, 5, 3, 0, 8], 
             [0, 0, 8, 3, 4, 2, 5, 6, 0], 
             [8, 5, 9, 0, 0, 1, 0, 0, 3], 
             [0, 0, 0, 0, 0, 0, 7, 9, 0], 
             [0, 0, 3, 0, 2, 0, 0, 0, 6], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [2, 0, 7, 0, 1, 0, 6, 3, 5], 
             [3, 4, 0, 2, 0, 0, 1, 0, 9]]
    display_game(board,"backtracking")
    # display_game(board,"csp")

if __name__ == '__main__':
    main()
