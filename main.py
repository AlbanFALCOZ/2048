import pygame,math,random,time
from Case import Case

BLOCK_WIDTH = 200
BLOCK_HEIGHT = 200
GRID_CORNER_LEFT_X = 500
GRID_CORNER_LEFT_y = 150

BUTTON_QUIT_X = 100
BUTTON_QUIT_Y = 900
BUTTON_QUIT_WIDTH = 200
BUTTON_QUIT_HEIGTH = 100

LISTE_COLOR = ["lightgrey","#eee4da","#ede0c8",'#f2b179',"#f59563","#f67c5f","#f65e3b","#edcf72","#edcc61","#edc850","#edc53f","#edc22e"]

pygame.init()
SIZE = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
SCREEN = pygame.display.set_mode(SIZE)

tab = [[Case(), Case(), Case(), Case()] for _ in range(4)]

def main():
    continue_game = True
    draw_grid()
    draw_quit_button()
    spaw_case()
    while continue_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_click_quit_button()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    spaw_case()
                    print("yolo")

        

        draw_grid()
        draw_quit_button()
        draw_case_value()


        pygame.display.flip()

    pygame.quit()





def draw_grid():
    SCREEN.fill("white")
    background_rect = pygame.Rect(GRID_CORNER_LEFT_X-15,GRID_CORNER_LEFT_y-15,BLOCK_WIDTH*4+15,BLOCK_HEIGHT*4+15)
    pygame.draw.rect(SCREEN,"black",background_rect)
    for i in range(4):
        for j in range(4):
            rect = pygame.Rect(GRID_CORNER_LEFT_X+i*BLOCK_WIDTH,GRID_CORNER_LEFT_y+j*BLOCK_HEIGHT,BLOCK_WIDTH*0.92,BLOCK_HEIGHT*0.92)
            pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(tab[i][j].val))],rect)



def draw_quit_button():
    background_rect = pygame.Rect(BUTTON_QUIT_X,BUTTON_QUIT_Y,BUTTON_QUIT_WIDTH,BUTTON_QUIT_HEIGTH)
    pygame.draw.rect(SCREEN,"grey",background_rect)
    font = pygame.font.Font(pygame.font.get_default_font(),36)
    text_surface = font.render("Quit", True, (0, 0, 0))
    SCREEN.blit(text_surface, dest=(BUTTON_QUIT_X+BUTTON_QUIT_WIDTH/3.3,BUTTON_QUIT_Y+BUTTON_QUIT_HEIGTH/3))


def check_click_quit_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x >= BUTTON_QUIT_X and mouse_x <= (BUTTON_QUIT_X + BUTTON_QUIT_WIDTH) and mouse_y >= BUTTON_QUIT_Y and mouse_y <= (BUTTON_QUIT_Y + BUTTON_QUIT_HEIGTH)):
        pygame.quit()

def draw_case_value():
    for i in range(4):
        for j in range(4):
            if tab[i][j].val != 1 :
                TEXT_GAP = -10*int(math.log10(tab[i][j].val))
                font = pygame.font.SysFont("consolas",40)
                value_grid = font.render(str(tab[i][j].val), True, (0,0,0))
                SCREEN.blit(value_grid, dest=(GRID_CORNER_LEFT_X+BLOCK_WIDTH/2.5+i*BLOCK_WIDTH+TEXT_GAP,GRID_CORNER_LEFT_y+BLOCK_HEIGHT/2.6+j*BLOCK_HEIGHT))

def spaw_case():
    i, j = random.randint(0,3),random.randint(0,3)
    val = 2**random.randint(1,11)
    tab[i][j].val = val
    for k in range(40):

        rect = pygame.Rect(GRID_CORNER_LEFT_X+i*BLOCK_WIDTH-BLOCK_WIDTH/2*k/40+BLOCK_WIDTH/2,GRID_CORNER_LEFT_y+j*BLOCK_HEIGHT-BLOCK_HEIGHT/2*k/40+BLOCK_HEIGHT/2,(BLOCK_WIDTH*0.92)*k/40,(BLOCK_HEIGHT*0.92)*k/40)
        pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(val))],rect)
        pygame.display.flip()
        time.sleep(0.005)
        




if __name__ == "__main__":
    main()
