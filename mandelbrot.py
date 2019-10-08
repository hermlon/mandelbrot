import pygame
import math

def draw_mandelbrot(x_pos, y_pos, zoom):
    max_iterations = 50
    for x in range(width):
        for y in range(height):
            a = (x / width + x_pos) / zoom
            b = (y / height + y_pos) / zoom
            iterations = 0
            last_length = 3
            f_a, f_b = 0, 0
            while iterations < max_iterations and last_length < 10**50:
                iterations += 1
                f_a, f_b = f_a**2 - f_b**2 + a, 2*f_a*f_b + b
                last_length = math.sqrt(f_a**2 + f_b**2)
            if last_length > 2:
                # farbig
                color = (0, 0, iterations / max_iterations * 255)
                pass
            else:
                # schwarz
                color = (0, 0, 0)
            screen.set_at((x, y), color)

pygame.init()

size = width, height = 400, 300
screen = pygame.display.set_mode(size)

screen.fill((255, 255, 255))

running = True

x = -0.5
y = -0.5
zoom = 0.25
draw_mandelbrot(x, y, zoom)
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            oldzoom = zoom
            if event.button == 1:
                zoom *= 1.2
            elif event.button == 3:
                zoom *= 0.8
            else:
                # other mouse buttons
                break

            pos = pygame.mouse.get_pos()

            # translates function so that the point where the user clicked
            # is in the center of the viewport
            x = x + (pos[0] - width / 2) / width
            y = y + (pos[1] - height / 2)  / height

            # adjusts the translation so that the point where the user clicked
            # is still at the same position (the center) although we use another
            # zoom factor
            x = zoom * (pos[0]/width + x)/oldzoom - pos[0]/width
            y = zoom * (pos[1]/height + y)/oldzoom - pos[1]/height

            draw_mandelbrot(x, y, zoom)
            pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
