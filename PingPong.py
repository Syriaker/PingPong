from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, angle):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.angle = angle
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, angle):
        super().__init__(player_image, player_x, player_y, size_x, size_y,  player_speed, angle)
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
class Ball(GameSprite):
    def move(self):
        pass

win_width, win_height = 800,600
window = display.set_mode((win_width, win_height))
display.set_caption('PingPong')
background = transform.scale(image.load ("field.jpg"), (win_width, win_height))
FPS = 60
clock = time.Clock()
run = True
racket1 = Player('platform.jpg', 0, 0, 25, 150, 5, None)
racket2 = Player('platform.jpg', win_width-25, 0, 25, 150, 5, None)
ball = Ball('ball.png', 350,250,50,50, 5, None)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    racket1.draw(window)
    racket2.draw(window)
    ball.draw(window)
    racket1.move_l()
    racket2.move_r()
    clock.tick(FPS)
    display.update()