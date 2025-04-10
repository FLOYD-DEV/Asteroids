import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Destroy the current asteroid

        # If too small, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        # Scale up the velocities by 1.2
        new_velocity1 *= 1.2
        new_velocity2 *= 1.2

        # Compute the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities
        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2