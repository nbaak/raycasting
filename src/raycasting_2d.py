import pygame
import math
import random


def create_walls(max_width:int, max_height:int, number_of_walls:int=10) -> list:
    walls = [tuple(pygame.Vector2(random.randrange(max_width), random.randrange(max_height)) for _ in range(2)) for _ in range(number_of_walls)]
    return walls


def draw_walls(surface:pygame.surface, walls:list, color:str="white", width:int=1) -> None:
    for start_pos, end_pos in walls:
        pygame.draw.line(surface, color, start_pos, end_pos, width)
        
        
def intersection(a:pygame.Vector2, b:pygame.Vector2, c:pygame.Vector2, d:pygame.Vector2):
    ab, cd, ac = a - b, c - d, a - c
    if not (denominator := ab.x * cd.y - ab.y * cd.x): return
    t = (ac.x * cd.y - ac.y * cd.x) / denominator
    u = -(ab.x * ac.y - ab.y * ac.x) / denominator
    if 0 <= t <= 1 and 0 <= u <= 1: return a.lerp(b, t)
    

def ray_casting(surface:pygame.surface, rays:list, walls:list, color:str="green", width=1) -> None:
    # Cursor Position
    cursor = pygame.Vector2(pygame.mouse.get_pos())
    
    # Draw Rays
    for ray in rays:
        beam = cursor + ray
        distances = [(cursor.distance_to(intersect), intersect) for a, b in walls if (intersect := intersection(a, b, cursor, beam))]
        if not distances: continue
        pygame.draw.line(surface, color, cursor, min(distances)[1], width)


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    window_size = width, height = 1800, 900
    surface = screen = pygame.display.set_mode(window_size)  # Creates a window of 800x600 pixels
    pygame.display.set_caption("Simple Pygame App")

    # Set up the clock for managing FPS
    clock = pygame.time.Clock()
    fps = 40
    beam_length = int(math.hypot(width, height))
    
    number_of_walls = 20
    walls = create_walls(width, height, number_of_walls)
    beams = [pygame.Vector2(beam_length, 0).rotate(angle) for angle in range(360)]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            # Check if the quit event is triggered
            if event.type == pygame.QUIT:
                running = False
            # Check for keypress event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Press "q" to quit
                    running = False
                elif event.key == pygame.K_w:
                    walls = create_walls(width, height, number_of_walls)

        # Fill the screen with black color
        surface.fill("black")
        
        # Draw Walls
        draw_walls(surface, walls, "white")
        
        # Raycasting
        ray_casting(surface, beams, walls)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
