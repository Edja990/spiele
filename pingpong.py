import sys
import pygame
import random
green = (0, 255, 0)
blue = (0, 0, 128)
counter = 0

x = 1000
y = 650

racket_width = 100
racket_height = 15

racket_x = x / 2
racket_y = y - 50

ball_x = int(x / 2)
ball_y = int(y / 2)
ball_radius = 15

ball_speed_x = 1
ball_speed_y = -2

live = 0
speed = 0
next_step_faster = 0
morespeed = 0
def main ():
    global counter, ball_x, ball_y , racket_x, racket_y
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(counter), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (x - 10, y - 10)
    pygame.display.set_caption('Ping Pong')
    screen = pygame.display.set_mode([x, y])
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius, 0)
    pygame.draw.rect(screen, (255, 40, 0), (racket_x, racket_y, racket_width, racket_height), 0)
    pygame.display.flip()
    def racket_block():
        global speed
        if racket_x <= 0 or racket_x >= x - racket_width:
            speed = 0


    def ball_movement():
        global ball_x, ball_y
        ball_x += ball_speed_x
        ball_y += ball_speed_y


    def reset():
        global live, ball_speed_x, ball_speed_y, ball_x, ball_y, speed, racket_y, racket_x , next_step_faster
        racket_x = x / 2
        racket_y = y - 50

        ball_x = int(x / 2)
        ball_y = int(y / 2)

        speed = 0

        ball_speed_x = random.randint(-3 , 3)
        if ball_speed_x == 0:
            ball_speed_x = 1
        if ball_x < 0:
            ball_speed_x - next_step_faster
        else:
            ball_speed_x + next_step_faster

        ball_speed_y = random.randint(-3, -1) - next_step_faster
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius, 0)
        pygame.draw.rect(screen, (255, 40, 0), (racket_x, racket_y, racket_width, racket_height), 0)
        pygame.display.flip()
        pygame.time.wait(1000)


    def ballblock():
        global ball_speed_x, ball_speed_y, live, counter
        if ball_x - ball_radius <= 0:
            ball_speed_x *= -1
        if ball_y - ball_radius <= 0:
            ball_speed_y *= -1
        if ball_x + ball_radius >= x:
            ball_speed_x *= -1
        if ball_y >= y-65 and ball_y <= y - 60:
            if ball_x >= racket_x - 15 and ball_x <= racket_x + racket_width:
                ball_speed_y *= -1
                counter += 1
            else:
                live -= 1
                reset()


    def racket_movement():
        global racket_x
        racket_x += speed

    def start():
            global speed, live , ball_speed_x , ball_speed_y, next_step_faster, morespeed
            live = 3
            nextstep = 10
            while live > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            speed = -2 - morespeed
                        if event.key == pygame.K_RIGHT:
                            speed = 2 + morespeed
                if counter % nextstep == 0 and counter != 0:
                    nextstep += 10
                    morespeed += 1
                    next_step_faster += 1
                    if ball_speed_x > 0:
                        ball_speed_x +=1
                    else:
                        ball_speed_x += -1
                    if ball_speed_y > 0:
                        ball_speed_y += 1
                    else:
                        ball_speed_y += -1

                screen.fill((0, 0, 0))
                racket_movement()
                racket_block()
                pygame.draw.rect(screen, (255, 40, 0), (racket_x, racket_y, racket_width, racket_height), 0)
                ball_movement()
                ballblock()
                text = font.render(str(counter), True, green, blue)
                screen.blit(text, textRect)
                pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius, 0)
                pygame.display.flip()
                pygame.time.wait(5)
            else:
                pygame.quit()

    start()
