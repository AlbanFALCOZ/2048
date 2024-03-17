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
    update_all()
    while continue_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_click_quit_button()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_DOWN :
                    tab_move_down()
                elif event.key == pygame.K_RIGHT:
                    tab_move_right()
                elif event.key == pygame.K_LEFT:
                    tab_move_left()
                elif event.key == pygame.K_UP:
                    tab_move_up()
        
        
        update_all()
        pygame.display.flip()

    pygame.quit()


def update_all():
    draw_grid()
    draw_quit_button()
    draw_case_value()


def draw_grid():
    SCREEN.fill("white")
    background_rect = pygame.Rect(GRID_CORNER_LEFT_X-15,GRID_CORNER_LEFT_y-15,BLOCK_WIDTH*4+15,BLOCK_HEIGHT*4+15)
    pygame.draw.rect(SCREEN,"black",background_rect)
    for i in range(4):
        for j in range(4):
            tab[i][j].hasMerged = False
            rect = pygame.Rect(GRID_CORNER_LEFT_X+i*BLOCK_WIDTH,GRID_CORNER_LEFT_y+j*BLOCK_HEIGHT,BLOCK_WIDTH*0.92,BLOCK_HEIGHT*0.92)
            pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(tab[i][j].val))],rect)



def draw_quit_button():
    background_rect = pygame.Rect(BUTTON_QUIT_X,BUTTON_QUIT_Y,BUTTON_QUIT_WIDTH,BUTTON_QUIT_HEIGTH)
    pygame.draw.rect(SCREEN,"grey",background_rect)
    font = pygame.font.Font(pygame.font.get_default_font(),36)
    text_surface = font.render("Quit", True, (0, 0, 0))
    SCREEN.blit(text_surface, dest=(BUTTON_QUIT_X+BUTTON_QUIT_WIDTH/3.3,BUTTON_QUIT_Y+BUTTON_QUIT_HEIGTH/3))


def draw_case_value():
    for i in range(4):
        for j in range(4):
            if tab[i][j].val != 1 :
                TEXT_GAP = -10*int(math.log10(tab[i][j].val))
                font = pygame.font.SysFont("consolas",40)
                value_grid = font.render(str(tab[i][j].val), True, (0,0,0))
                SCREEN.blit(value_grid, dest=(GRID_CORNER_LEFT_X+BLOCK_WIDTH/2.5+i*BLOCK_WIDTH+TEXT_GAP,GRID_CORNER_LEFT_y+BLOCK_HEIGHT/2.6+j*BLOCK_HEIGHT))

def spaw_case():
    if check_tab_full():
        return
    i, j = random.randint(0,3),random.randint(0,3)
    while (tab[i][j].val != 1):
        i, j = random.randint(0,3),random.randint(0,3)
    val = 2**random.randint(1,2)
    
    for k in range(40):
        rect = pygame.Rect(GRID_CORNER_LEFT_X+i*BLOCK_WIDTH-BLOCK_WIDTH/2*k/40+BLOCK_WIDTH/2,GRID_CORNER_LEFT_y+j*BLOCK_HEIGHT-BLOCK_HEIGHT/2*k/40+BLOCK_HEIGHT/2,(BLOCK_WIDTH*0.92)*k/40,(BLOCK_HEIGHT*0.92)*k/40)
        pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(val))],rect)
        draw_quit_button()
        draw_case_value()
        pygame.display.flip()
        time.sleep(0.0002)
    tab[i][j].val = val


def check_click_quit_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x >= BUTTON_QUIT_X and mouse_x <= (BUTTON_QUIT_X + BUTTON_QUIT_WIDTH) and mouse_y >= BUTTON_QUIT_Y and mouse_y <= (BUTTON_QUIT_Y + BUTTON_QUIT_HEIGTH)):
        pygame.quit()


def check_tab_full():
    for i in range(4):
        for j in range(4):
            if tab[i][j].val == 1 :
                return False
    return True



def tab_move_right():
    for i in range(2,-1,-1):
        for j in range(4):
            indice = i
            while indice < 3 :
                if tab[indice][j].can_merge(tab[indice+1][j]):
                    merge_two_cells(tab[indice][j],tab[indice+1][j])
                    indice = indice + 1
                elif tab[indice][j].val != 1 and tab[indice+1][j].val == 1:
                    tab[indice][j].val,tab[indice+1][j].val = tab[indice+1][j].val, tab[indice][j].val
                    indice = indice + 1
                else :
                    indice = 3
    
    draw_grid()
    spaw_case()

def tab_move_left():
    for i in range(1,4):
        for j in range(4):
            indice = i
            while indice >= 1 :
                if tab[indice][j].can_merge(tab[indice-1][j]):
                    merge_two_cells(tab[indice][j],tab[indice-1][j])
                    indice = indice - 1
                elif tab[indice][j].val != 1 and tab[indice-1][j].val == 1:
                    tab[indice][j].val,tab[indice-1][j].val = tab[indice-1][j].val, tab[indice][j].val
                    indice = indice - 1
                else :
                    indice = 0
    draw_grid()
    spaw_case()


def tab_move_up():
    for i in range(4):
        for j in range(3,-1,-1):
            indice = j
            while indice >= 1 :
                if tab[i][indice].can_merge(tab[i][indice-1]):
                    merge_two_cells(tab[i][indice],tab[i][indice-1])
                    indice = indice - 1
                elif tab[i][indice].val != 1 and tab[i][indice-1].val == 1:
                    tab[i][indice-1].val,tab[i][indice].val = tab[i][indice].val, tab[i][indice-1].val
                    indice = indice - 1
                else :
                    indice = 0
    draw_grid()
    spaw_case()


def tab_move_down():
    for i in range(4):
        for j in range(3):
            indice = j
            while indice < 3 :
                if tab[i][indice].can_merge(tab[i][indice+1]):
                    merge_two_cells(tab[i][indice],tab[i][indice+1])
                    indice = indice + 1
                elif tab[i][indice].val != 1 and tab[i][indice+1].val == 1:
                    tab[i][indice+1].val,tab[i][indice].val = tab[i][indice].val, tab[i][indice+1].val
                    indice = indice - 1
                else :
                    indice = 3
    draw_grid()
    spaw_case()


def merge_two_cells(cell,cell_dest):
    cell_dest.val = cell_dest.val * 2
    cell_dest.hasMerged = True
    cell.val = 1


def print_tab():
    for i in range(4):
        line = ""
        for j in range(4):
            line = line + " " + str(tab[j][i].val) + " "
        print(line)


if __name__ == "__main__":
    main()
