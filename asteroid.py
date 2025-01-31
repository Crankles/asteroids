import pygame # type: ignore
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            old_position = self.position
            old_velocity = self.velocity
            old_radius = self.radius
            self.kill()
            random_angle = random.uniform(20, 50)
            
            new_vec1 = old_velocity.rotate(random_angle)
            new_vec2 = old_velocity.rotate(-random_angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid2 = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid1.velocity = new_vec1 * 1.2
            new_asteroid2.velocity = new_vec2 * 1.2