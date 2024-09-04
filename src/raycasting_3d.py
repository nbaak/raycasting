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
    

def ray_casting(surface_2d:pygame.surface, surface_3d:pygame.surface, fov:int, direction:int, walls:list, window_size, color:str="green", beam_width=1) -> None:
    # Cursor Position
    cursor = pygame.Vector2(pygame.mouse.get_pos())
    width, height = window_size
    
    width_rect = width / 2 / fov
    # Draw Rays
    for i in range(fov):
        ray = pygame.Vector2(3000, 0).rotate(direction - fov / 2 + i)
        beam = cursor + ray
        distances = [(cursor.distance_to(intersect), intersect) for a, b in walls if (intersect := intersection(a, b, cursor, beam))]
        if not distances: continue
        
        distance, intersect = min(distances)
        
        distance *= math.cos(math.radians(i - fov / 2))
        wall_height = (10 / distance * 2500)  
        wall_color = [max(10, 255 - distance / 1.5)] * 3
        
        pygame.draw.line(surface_2d, color, cursor, intersect, beam_width)
        pygame.draw.rect(surface_3d, wall_color, (width_rect * i, height / 2 - wall_height / 2, width_rect, wall_height))


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    window_size = width, height = 1800, 900
    surface = screen = pygame.display.set_mode(window_size)  # Creates a window of 800x600 pixels
    
    surface_map = pygame.surface.SurfaceType((width // 2, height))  # 2d view
    surface_first_person = pygame.surface.SurfaceType((width // 2, height))  # 3d view
    
    pygame.display.set_caption("Simple Pygame App")
    pygame.key.set_repeat(10)

    # Set up the clock for managing FPS
    clock = pygame.time.Clock()
    fps = 40
    beam_length = int(math.hypot(width, height))
    
    number_of_walls = 20
    walls = create_walls(width, height, number_of_walls)
    beams = [pygame.Vector2(beam_length, 0).rotate(angle) for angle in range(360)]
    
    field_of_view = 60  # deg
    view_direction = 0  # right

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            # Check if the quit event is triggered
            if event.type == pygame.QUIT:
                running = False
            # Check for keypress event
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q: running = False
                    case pygame.K_w: walls = create_walls(width, height, number_of_walls)
                    case pygame.K_a: view_direction = (view_direction - 1) % 360
                    case pygame.K_d: view_direction = (view_direction + 1) % 360
                    
        print(view_direction)
                    
        # Fill the screen with black color
        surface_map.fill("black")
        pygame.draw.rect(surface_first_person, "blue", (0, 0, width // 2, height // 2))
        pygame.draw.rect(surface_first_person, "brown", (0, height // 2, width // 2, height // 2))
        
        # Draw Walls
        draw_walls(surface_map, walls, "white")
        
        # Raycasting
        ray_casting(surface_map, surface_first_person, field_of_view, view_direction, walls, window_size)
        
        # Put screen together
        screen.blit(surface_map, (0, 0))
        screen.blit(surface_first_person, (width // 2, 0))
        pygame.draw.line(surface, 'blue', (width // 2, 0), (width // 2, width), 5)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
