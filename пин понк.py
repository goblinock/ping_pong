from pygame import *
window = display.set_mode((700, 500))
display.set_caption('пинг-понг')
window.fill((12, 32, 45))
clock = time.Clock()
FPS = 60


score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


lost = 0
         

class Kirpich_player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed


 





kirpich1 = Kirpich_player('kirpich1.png', 615, 100, 15, 80, 150)
kirpich2 = Kirpich_player('kirpich2.png', 5, 100, 15, 80, 150)
kirpich3 = GameSprite('kirpich3.png', 250, 250, 15, 150, 150)



game = True
finish = False



   
# font.init()
# font1 = font.SysFont('Arial', 36)
# win = font1.render('YOU WIN!', True, (255, 255, 255))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))
# bullets = sprite.Group()

# rel_time = False

# num_fire = 0          

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

                



    if finish != True:
        # if move_right:
        #     platform.rect.x += 3
        # if move_left:
        #     platform.rect.x -= 3
        # ball.rect.x += speed_x
        # ball.rect.y += speed_y
        # if ball.rect.colliderect(platform.rect):
        #     speed_y *= -1
        # if ball.rect.y < 0:
        #     speed_y *= -1
        # if ball.rect.x < 0 or ball.rect.x > 450:
        #     speed_x *= -1
        # if ball.rect.y > 420:
        window.fill((12, 32, 45))
        kirpich1.reset()
        kirpich1.update()
    

        kirpich2.reset()
        kirpich2.update_l()


        kirpich3.reset()
        kirpich3.update()
#         text = font1.render('Счет:' + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))

#         text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))

#         
#         ship.reset()
#         monsters.draw(window)
#         bullets.draw(window)

#         if rel_time == True:
#             now_time = timer()

#             if now_time - last_time < 3:
#                 reload = font1.render('Wait, reload...', 1, (150, 0, 0))
#                 window.blit(reload, (260, 460))
#             else:
#                 num_fire = 0
#                 rel_time = False


#         sprites_list = sprite.groupcollide(monsters, bullets, True, True)
    

#         for c in sprites_list:
#             score = score + 1
#             monster = Enemy('ufo.png', randint(80, 620), -40, randint(1, 3), 80, 50)
#             monsters.add(monster)

#         if sprite.spritecollide(ship, monsters, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if sprite.spritecollide(ship, asteroids, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if score >= 10 :
#             finish = True
#             window.blit(win, (200, 200))

      
    clock.tick(FPS)
    display.update()