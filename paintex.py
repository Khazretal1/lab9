import pygame, sys

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

color = RED
clock = pygame.time.Clock()
FPS = 60

wl, wh = 1001, 601
screen = pygame.display.set_mode((wl, wh))
screen.fill(WHITE)

pen = "mouse"
last_event = None
pre, cur = None, None
pre_e, cur_e = None, None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pen = "mouse"
            if event.key == pygame.K_w:
                pen = "rectangle"
            if event.key == pygame.K_e:
                pen = "circle"
            if event.key == pygame.K_r:
                pen = "Eraser"
            if event.key == pygame.K_t:
                pen = "square"
            if event.key == pygame.K_y:
                pen = "right_triangle"
            if event.key == pygame.K_u:
                pen = "equilateral_triangle"
            if event.key == pygame.K_i:
                pen = "rhombus"
            
            if event.key == pygame.K_a:
                color = RED
            if event.key == pygame.K_s:
                color = GREEN
            if event.key == pygame.K_d:
                color = BLUE
            if event.key == pygame.K_f:
                color = BLACK
        
        if pen == "mouse":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
            if pre:
                pygame.draw.line(screen, color, pre, cur, 10)
                pre = cur
            if event.type == pygame.MOUSEBUTTONUP:
                pre = None
        
        if pen == "rectangle" or pen == "square":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                if pen == "square":
                    side = min(abs(x1 - x), abs(y1 - y))
                    x1, y1 = x + side, y + side
                pygame.draw.rect(screen, color, (x, y, x1 - x, y1 - y), 5)
                last_event = None
        
        if pen == "circle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.circle(screen, color, (((x + x1) // 2), ((y + y1) // 2)), abs((x1 - x) // 2), 3)
                last_event = None
        
        if pen == "right_triangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.polygon(screen, color, [(x, y), (x, y1), (x1, y1)], 5)
                last_event = None
        
        if pen == "equilateral_triangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                side = abs(x1 - x)
                height = (3 ** 0.5 / 2) * side
                pygame.draw.polygon(screen, color, [(x, y1), (x + side, y1), (x + side // 2, y1 - height)], 5)
                last_event = None
        
        if pen == "rhombus":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                width = abs(x1 - x)
                height = abs(y1 - y)
                pygame.draw.polygon(screen, color, [(x, y + height // 2), (x + width // 2, y), (x + width, y + height // 2), (x + width // 2, y + height)], 5)
                last_event = None
        
        if pen == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre_e = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur_e = pygame.mouse.get_pos()
            if pre_e:
                pygame.draw.line(screen, WHITE, pre_e, cur_e, 10)
                pre_e = cur_e
            if event.type == pygame.MOUSEBUTTONUP:
                pre_e = None
    
    clock.tick(60)
    pygame.display.flip()
