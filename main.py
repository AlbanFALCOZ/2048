import sys,pygame

BLOCK_WIDTH = 200
BLOCK_HEIGHT = 200
GRID_CORNER_LEFT_X = 500
GRID_CORNER_LEFT_y = 200

BUTTON_QUIT_X = 100
BUTTON_QUIT_Y = 900
BUTTON_QUIT_WIDTH = 200
BUTTON_QUIT_HEIGTH = 100

pygame.init()
size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)

def main():
    continue_game = True
    while continue_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_click_quit_button()

        draw_grid()
        draw_quit_button()
        pygame.display.flip()

    pygame.quit()





def draw_grid():
    screen.fill("white")
    background_rect = pygame.Rect(GRID_CORNER_LEFT_X-20,GRID_CORNER_LEFT_y-20,BLOCK_WIDTH*4+25,BLOCK_HEIGHT*4+25)
    pygame.draw.rect(screen,"black",background_rect)
    for i in range(4):
        for j in range(4):
            rect = pygame.Rect(GRID_CORNER_LEFT_X+i*BLOCK_WIDTH,GRID_CORNER_LEFT_y+j*BLOCK_HEIGHT,BLOCK_WIDTH*0.9,BLOCK_HEIGHT*0.9)
            pygame.draw.rect(screen,"grey",rect)



def draw_quit_button():
    background_rect = pygame.Rect(BUTTON_QUIT_X,BUTTON_QUIT_Y,BUTTON_QUIT_WIDTH,BUTTON_QUIT_HEIGTH)
    pygame.draw.rect(screen,"grey",background_rect)
    font = pygame.font.Font(pygame.font.get_default_font(),36)
    text_surface = font.render("Quit", True, (0, 0, 0))
    screen.blit(text_surface, dest=(BUTTON_QUIT_X+BUTTON_QUIT_WIDTH/3.3,BUTTON_QUIT_Y+BUTTON_QUIT_HEIGTH/3))


def check_click_quit_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x >= BUTTON_QUIT_X and mouse_x <= (BUTTON_QUIT_X + BUTTON_QUIT_WIDTH) and mouse_y >= BUTTON_QUIT_Y and mouse_y <= (BUTTON_QUIT_Y + BUTTON_QUIT_HEIGTH)):
        pygame.quit()




if __name__ == "__main__":
    main()
