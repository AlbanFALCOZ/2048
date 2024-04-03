import pygame,math,random,time, copy
from Case import Case

BLOCK_WIDTH = 200
BLOCK_HEIGHT = 200
GRID_CORNER_LEFT_X = 500
GRID_CORNER_LEFT_Y = 100
GRID_GAP = 15

BUTTON_QUIT_X = 100
BUTTON_QUIT_Y = 900
BUTTON_QUIT_WIDTH = 200
BUTTON_QUIT_HEIGTH = 100

BUTTON_START_X = 100
BUTTON_START_Y = 700
BUTTON_START_WIDTH = 200
BUTTON_START_HEIGTH = 100

LISTE_COLOR = ["lightgrey","#eee4da","#ede0c8",'#f2b179',"#f59563","#f67c5f","#f65e3b","#edcf72","#edcc61","#edc850","#edc53f","#edc22e"]

pygame.init()
SIZE = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
SCREEN = pygame.display.set_mode(SIZE)

tab = [[Case(), Case(), Case(), Case()] for _ in range(4)]

tab_old = copy.deepcopy(tab)

def main():
    continue_game = True
    draw_grid()
    spaw_case()
    draw_buttons()
    update_grid()
    
    while continue_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_click_quit_button()
                check_click_start_button()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN :
                    tab_move_down()
                if event.key == pygame.K_RIGHT:
                    tab_move_right()
                if event.key == pygame.K_LEFT:
                    tab_move_left()
                if event.key == pygame.K_UP:
                    tab_move_up()
        
        pygame.display.flip()
        
    pygame.quit()


def draw_grid():
    SCREEN.fill("white")
    background_rect = pygame.Rect(GRID_CORNER_LEFT_X,GRID_CORNER_LEFT_Y,BLOCK_WIDTH*4+GRID_GAP*5,BLOCK_HEIGHT*4+GRID_GAP*5)
    pygame.draw.rect(SCREEN,"black",background_rect)
    for i in range(4):
        for j in range(4):
            tab[i][j].hasMerged = False
            rect = pygame.Rect(GRID_CORNER_LEFT_X+i*(BLOCK_WIDTH)+(i+1)*GRID_GAP,GRID_CORNER_LEFT_Y+j*(BLOCK_HEIGHT)+(j+1)*GRID_GAP,BLOCK_WIDTH,BLOCK_HEIGHT)
            pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(tab[i][j].val))],rect)


def update_grid():
    global tab_old
    print_tab()
    for i in range(4):
        for j in range(4):
            tab[i][j].hasMerged = False
            if (tab_old[i][j].val != tab[i][j].val):
                rect = pygame.Rect(GRID_CORNER_LEFT_X+i*(BLOCK_WIDTH)+(i+1)*GRID_GAP,GRID_CORNER_LEFT_Y+j*(BLOCK_HEIGHT)+(j+1)*GRID_GAP,BLOCK_WIDTH,BLOCK_HEIGHT)
                pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(tab[i][j].val))],rect)
                if (tab[i][j].val != 1):
                    font = pygame.font.SysFont("consolas",50)
                    text = font.render(str(tab[i][j].val), True, (0,0,0))
                    text_rect = text.get_rect(center=(GRID_CORNER_LEFT_X+(i+1/2)*(BLOCK_WIDTH)+(i+1)*GRID_GAP,GRID_CORNER_LEFT_Y+(j+1/2)*(BLOCK_HEIGHT)+(j+1)*GRID_GAP))
                    SCREEN.blit(text, text_rect)
                tab_old[i][j].val = tab[i][j].val
    pygame.display.flip()


def draw_buttons():
    font = pygame.font.Font(pygame.font.get_default_font(),36)

    background_rect_quit = pygame.Rect(BUTTON_QUIT_X,BUTTON_QUIT_Y,BUTTON_QUIT_WIDTH,BUTTON_QUIT_HEIGTH)
    pygame.draw.rect(SCREEN,"grey",background_rect_quit)
    text_surface_quit = font.render("Quit", True, (0, 0, 0))
    SCREEN.blit(text_surface_quit, dest=(BUTTON_QUIT_X+BUTTON_QUIT_WIDTH/3.3,BUTTON_QUIT_Y+BUTTON_QUIT_HEIGTH/3))

    background_rect_start = pygame.Rect(BUTTON_START_X,BUTTON_START_Y,BUTTON_START_WIDTH,BUTTON_START_HEIGTH)
    pygame.draw.rect(SCREEN,"grey",background_rect_start)
    text_surface_start = font.render("Start", True, (0, 0, 0))
    SCREEN.blit(text_surface_start, dest=(BUTTON_START_X+BUTTON_START_WIDTH/3.3,BUTTON_START_Y+BUTTON_START_HEIGTH/3))

def spaw_case():
    update_grid()
    if check_tab_full():
        return
    i, j = random.randint(0,3),random.randint(0,3)
    while (tab[i][j].val != 1): 
        i, j = random.randint(0,3),random.randint(0,3)
    val = (4)if(random.randint(0,2) == 2)else(2)
    print("Val : ",val)
    for k in range(40):
        rect = pygame.Rect(GRID_CORNER_LEFT_X+(i+1/2)*(BLOCK_WIDTH)+(i+1)*GRID_GAP-BLOCK_WIDTH/2*k/40,GRID_CORNER_LEFT_Y+(j+1/2)*(BLOCK_HEIGHT)+(j+1)*GRID_GAP-BLOCK_HEIGHT/2*k/40,(BLOCK_WIDTH)*k/40,(BLOCK_HEIGHT)*k/40)
        pygame.draw.rect(SCREEN,LISTE_COLOR[int(math.log2(val))],rect)
        draw_buttons()
        pygame.display.flip()
    
    tab[i][j].val = val
    update_grid()


def check_click_quit_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x >= BUTTON_QUIT_X and mouse_x <= (BUTTON_QUIT_X + BUTTON_QUIT_WIDTH) and mouse_y >= BUTTON_QUIT_Y and mouse_y <= (BUTTON_QUIT_Y + BUTTON_QUIT_HEIGTH)):
        pygame.quit()

def check_click_start_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x >= BUTTON_START_X and mouse_x <= (BUTTON_START_X + BUTTON_START_WIDTH) and mouse_y >= BUTTON_START_Y and mouse_y <= (BUTTON_START_Y + BUTTON_START_HEIGTH)):
        clear_tab()
        draw_grid()
        spaw_case()

def clear_tab():
    for i in range(4):
        for j in range(4):
            tab[i][j].val = 1


def check_tab_full():
    for i in range(4):
        for j in range(4):
            if tab[i][j].val == 1 :
                return False
    return True



def tab_move_right():
    Test = False
    for i in range(2,-1,-1):
        for j in range(4):
            indice = i
            while indice < 3 :
                if tab[indice][j].can_merge(tab[indice+1][j]):
                    merge_two_cells(tab[indice][j],tab[indice+1][j])
                    indice = indice + 1
                    Test = True
                elif tab[indice][j].val != 1 and tab[indice+1][j].val == 1:
                    tab[indice][j].val,tab[indice+1][j].val = tab[indice+1][j].val, tab[indice][j].val
                    indice = indice + 1
                    Test = True
                else :
                    indice = 3
    if Test:
        spaw_case()

def tab_move_left():
    Test = False
    for i in range(1,4):
        for j in range(4):
            indice = i
            while indice >= 1 :
                if tab[indice][j].can_merge(tab[indice-1][j]):
                    merge_two_cells(tab[indice][j],tab[indice-1][j])
                    indice = indice - 1
                    Test = True
                elif tab[indice][j].val != 1 and tab[indice-1][j].val == 1:
                    tab[indice][j].val,tab[indice-1][j].val = tab[indice-1][j].val, tab[indice][j].val
                    indice = indice - 1
                    Test = True
                else :
                    indice = 0
    if Test:
        spaw_case()


def tab_move_up():
    Test = False
    for i in range(4):
        for j in range(1,4):
            indice = j
            while indice >= 1 :
                if tab[i][indice].can_merge(tab[i][indice-1]):
                    merge_two_cells(tab[i][indice],tab[i][indice-1])
                    indice = indice - 1
                    Test = True
                elif tab[i][indice].val != 1 and tab[i][indice-1].val == 1:
                    tab[i][indice-1].val,tab[i][indice].val = tab[i][indice].val, tab[i][indice-1].val
                    indice = indice - 1
                    Test = True
                else :
                    indice = 0
    if Test :
        spaw_case()


def tab_move_down():
    Test = False
    for i in range(4):
        for j in range(2,-1,-1):
            indice = j
            while indice < 3 :
                if tab[i][indice].can_merge(tab[i][indice+1]):
                    merge_two_cells(tab[i][indice],tab[i][indice+1])
                    indice = indice + 1
                    Test = True
                elif tab[i][indice].val != 1 and tab[i][indice+1].val == 1:
                    tab[i][indice+1].val,tab[i][indice].val = tab[i][indice].val, tab[i][indice+1].val
                    indice = indice + 1
                    Test = True
                else :
                    indice = 3
    if Test :
        spaw_case()


def merge_two_cells(cell,cell_dest):
    cell_dest.val = cell_dest.val * 2
    cell_dest.hasMerged = True
    cell.val = 1


def print_tab():
    print("Tab : ")
    for i in range(4):
        line = ""
        for j in range(4):
            line = line + " " + str(tab[j][i].val) + " "
        print(line)


if __name__ == "__main__":
    main()
