import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.stop = False

        self.head_up = pygame.image.load('.\\asset\\head_up.png').convert_alpha()
        self.head_down = pygame.image.load('.\\asset\\head_down.png').convert_alpha()
        self.head_right = pygame.image.load('.\\asset\\head_right.png').convert_alpha()
        self.head_left = pygame.image.load('.\\asset\\head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('.\\asset\\tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('.\\asset\\tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('.\\asset\\tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('.\\asset\\tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('.\\asset\\body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('.\\asset\\body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('.\\asset\\body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('.\\asset\\body_topleft.png').convert_alpha()
        self.body_br = pygame.image.load('.\\asset\\body_bottomright.png').convert_alpha()
        self.body_bl = pygame.image.load('.\\asset\\body_bottomleft.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)

            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(1, 0): self.head = self.head_left

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(1, 0): self.tail = self.tail_left

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        elif self.stop:
            self.body = self.body
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def stop_snake(self):
        self.stop = True

    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.stop_snake()
        self.final_score()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

    def final_score(self):
        gameover = "GAME OVER"
        score_text = "Score: " + str(len(self.snake.body) - 3)

        gameover_surface = game_font.render(gameover, True, (56, 74, 12))
        score_surface = game_font.render(score_text, True, (56, 74, 12))

        score_x = int((cell_number * cell_size) / 2)
        score_y = int((cell_number * cell_size) / 2)

        gameover_rect = gameover_surface.get_rect(center=(score_x, score_y))
        score_rect = score_surface.get_rect(center=(score_x, score_y + 50))

        pygame.draw.rect(screen, (167, 209, 61), gameover_rect)
        pygame.draw.rect(screen, (167, 209, 61), score_rect)

        screen.blit(gameover_surface, gameover_rect)
        screen.blit(score_surface, score_rect)

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, True, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
        return False

class STARTMENU:
    def __init__(self):
        self.start = True
        self.play_button = Button("Play", (cell_number * cell_size // 2 - 50, cell_number * cell_size // 2 - 50), 30)
        self.quit_button = Button("Quit", (cell_number * cell_size // 2 - 50, cell_number * cell_size // 2 + 10), 30)

    def draw_start_menu(self):
        self.play_button.show(screen)
        self.quit_button.show(screen)

    def handle_event(self, event):
        if self.play_button.click(event):
            self.start = False
        if self.quit_button.click(event):
            pygame.quit()
            sys.exit()

pygame.init()
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('.\\asset\\apple.png').convert_alpha()
game_font = pygame.font.SysFont('arial', 25)
#icon = pygame.image.load('./asset/sb.ico').convert_alpha()

#pygame.display.set_icon(icon)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
pygame.display.set_caption('Snake Byte')
start_menu = STARTMENU()
main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE and not start_menu.start:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
        start_menu.handle_event(event)

    if start_menu.start:
        screen.fill((175, 215, 70))
        start_menu.draw_start_menu()
    elif main_game.snake.stop == False:
        screen.fill((175, 215, 70))
        main_game.draw_elements()
    else:
        main_game.final_score()

    pygame.display.update()
    clock.tick(60)
