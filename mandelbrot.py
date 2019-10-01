import pygame
import math

def draw_mandelbrot(x_pos, y_pos, zoom):
    max_iterations = 50
    for x in range(width):
        for y in range(height):
            # c = a + bi
            a = (x / width * 4 - 2 + x_pos) / zoom
            b = (y / height * 4 - 2 + y_pos) / zoom
            iterations = 0
            last_length = 3
            f_a, f_b = 0, 0
            while iterations < max_iterations and last_length < 10**50:
                iterations += 1
                f_a, f_b = f_a**2 - f_b**2 + a, 2*f_a*f_b + b
                last_length = math.sqrt(f_a**2 + f_b**2)
                #print(last_length)
            if last_length > 2:
                # farbig
                color = (0, 0, iterations / max_iterations * 255)
                pass
            else:
                # schwarz
                color = (0, 0, 0)
            screen.set_at((x, y), color)

pygame.init()

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)

screen.fill((255, 255, 255))

running = True

x = 0
y = 0
zoom = 1
draw_mandelbrot(x, y, zoom)
while running:
    print("Bitte Brot aus dem Ofen entnehmen!")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                zoom *= 1.2
            if event.button == 3:
                zoom *= 0.8
            pos = pygame.mouse.get_pos()
            x = (width / 2 - pos[0]) * 4 / width
            y = (height / 2 - pos[1]) * 4 / height
            draw_mandelbrot(-x, -y, zoom)
        if event.type == pygame.QUIT:
            running = False
