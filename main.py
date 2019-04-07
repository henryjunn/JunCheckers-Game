import pygame

def draw_board():
    """ Draw the board for the checkers game """

    pygame.init()
    colors = [(245, 222, 179), (139, 69, 19)]    # Set up colors [saddlebrown, wheat]

    n = 10                     # 8x8 Board, so n = 8
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Loading the images
    black_checker = pygame.image.load("images/black_checker.png")
    white_checker = pygame.image.load("images/white_checker.png")
    black_king = pygame.image.load("images/black_king.png")
    white_king = pygame.image.load("images/white_king.png")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz - black_checker.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_index = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_index], the_square)
                # Now flip the color index for the next square
                c_index = (c_index + 1) % 2

        # Now that squares are drawn, draw the pieces.
        for col in range(0, 10, 2):
            for row in range(0, 4):
                if row % 2 == 0:
                    surface.blit(black_checker, (col * sq_sz + ball_offset + sq_sz, row * sq_sz + ball_offset))
                elif row % 2 == 1:
                    surface.blit(black_checker, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))

        for col in range(0, 10, 2):
            for row in range(6, 10):
                if row % 2 == 0:
                    surface.blit(white_checker, (col * sq_sz + ball_offset + sq_sz, row * sq_sz + ball_offset))
                elif row % 2 == 1:
                    surface.blit(white_checker, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    draw_board()
