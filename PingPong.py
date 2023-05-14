from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, speed_y=0, speed_x=0, angle=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.angle = angle
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
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
    def move(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > win_height - self.size_y:
            self.speed_y *= -1
    def collide(self, player_racket1, player_racket2):
        if sprite.collide_rect(self, player_racket1) or sprite.collide_rect(self, player_racket2):
            self.speed_x *= -1


win_width, win_height = 800,600
window = display.set_mode((win_width, win_height))
display.set_caption('PingPong')
background = transform.scale(image.load ("field.jpg"), (win_width, win_height))
FPS = 60
clock = time.Clock()
run = True
racket1 = Player('platform.jpg', 0, 0, 25, 150, 5)
racket2 = Player('platform.jpg', win_width-25, 0, 25, 150, 5)
ball = Ball('ball.png', 350,250,50,50, 0, 3,3)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    racket1.draw(window)
    racket2.draw(window)
    ball.move(window)
    ball.collide(racket1,racket2)
    racket1.move_l()
    racket2.move_r()
    clock.tick(FPS)
    display.update()