'''
Define a class that stores the entire game.
This class can be manually stepped or it can be (potentially) run
via some GameEngine.autorun(FPS) method but will need to work out how
inputs will work (especially coming from another program such as NEAT)

'''
SCREEN_SIZE = (500, 500)
X_LEFT_OFFSET_FROM_SCREEN = 10
X_RIGHT_OFFSET_FROM_SCREEN = 100
Y_UP_OFFSET_FROM_SCREEN = 10
Y_DOWN_OFFSET_FROM_SCREEN = 10

TARGET_FPS = 166

import math
import shapes
from shapes import CollisionDetector as cd
import random

class GameEngine:
    def __init__(self, user_input = True):
        self.running = False
        self.fitness = 0
        self.user_input = user_input
        pass

    def start(self):
        self.running = True
        self.rocket = Rocket()
        self.asteroids = []
        self.dead_asteroids = []
        self.projectiles = []
        self.dead_projectiles = []
        self.level = 1
        self.ASTEROID_REWARD = 1000
        self.FRAME_SURVIVE_REWARD = 1
        pass

    def updateAll(self, action):
        # action tuple (left, right, up, down, shoot)
        # Go through all player, projectiles and asteroids and check for collision
        for projectile in self.projectiles:
            projectile.update()
            if projectile.x > SCREEN_SIZE[0]:
                self.projectiles.remove(projectile)
                self.dead_projectiles.append(projectile)

        for asteroid in self.asteroids:
            asteroid.update()
            if asteroid.x + asteroid.r < 0:
                #if asteroid in self.asteroids:
                    #print(self.asteroids)
                    #print(asteroid)
                self.asteroids.remove(asteroid)
                self.dead_asteroids.append(asteroid)

        # Generate enough asteroids for given level
        while len(self.asteroids) < self.level:  # Repopulate asteroids
            self.asteroids.append(
                Asteroid(2 * SCREEN_SIZE[0], random.randint(0, SCREEN_SIZE[1]), random.randint(20, 40)))

        self.rocket.update(self, action)

        self.fitness += self.FRAME_SURVIVE_REWARD

    def checkCollisions(self):
        # Check if player collides with asteroids
        for asteroid in self.asteroids:
            if cd.collisionRectCircle(asteroid.getHitbox(), self.rocket.getHitbox()):
                self.running = False
            for projectile in self.projectiles:
                if cd.collisionRectCircle(asteroid.getHitbox(), projectile.getHitbox()):
                    projectile.alive = False
                    asteroid.alive = False
                    self.dead_projectiles.append(projectile)
                    self.projectiles.remove(projectile)
                    self.dead_asteroids.append(asteroid)
                    self.asteroids.remove(asteroid)
                    self.fitness += self.ASTEROID_REWARD


    def isRunning(self):
        return self.running

    def getFitness(self):
        return self.fitness

    # Return current state of game - This will be predominantly
    # used to assist with rendering the game via. Pygame.
    def getState(self):
        pass

    # Return the observables that the agent has access to -
    # This will probably just be the screen (either raw pixels or most likely some
    # array that more succinctly encapsulates the data)
    def getObervables(self):
        #observables = []
        #observables.append(self.rocket.x)
        #observables.append(self.rocket.y)
        #for asteroid in self.asteroids:
            #observables.append(asteroid.x)
            #observables.append(asteroid.y)
            #observables.append(asteroid.r)
        observables = [[0] * 50]*50 #Entire screen
        #Render rocket, then asteroid, then maybe laser
        #observables[self.rocket.y // 10 : (self.rocket.y + self.rocket.height) // 10][]

        return observables

        pass

    # Simulate the next frame given the action or player input
    def simulateTimeStep(self, action):
        #for each rocket, for each projectile (ie laser), for each asteroid
        #call update on that object
        # action will be a tuple of booleans
        # (moveLeft, moveRight, moveUp, moveDown, fire)
        if self.isRunning():
            self.updateAll(action)
            self.checkCollisions()

        # Now we compute the logic of the program
        # IE. If player shot, generate projectile entity with a certain speed
        # Check collisions between rocket and asteroids
        # Check collisions between projectiles and asteroids


        pass

class Entity:
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def getHitbox(self):
        pass

class Rocket(Entity):

    def __init__(self):
        self.width = 30
        self.height = 15
        #Define x and y from the top-left of the rocket shape
        self.x = X_LEFT_OFFSET_FROM_SCREEN
        self.y = SCREEN_SIZE[1] // 2 - self.height // 2
        self.HORIZONTAL_MOVE = SCREEN_SIZE[0] // TARGET_FPS  # Desired Rocket Speed / Frame Rate | (pixels/sec)*(sec / frames)
        self.VERTICAL_MOVE = SCREEN_SIZE[1] // TARGET_FPS  # Desired Rocket Speed / Frame Rate | (pixels/sec)*(sec / frames)
        self.holding_fire = False # We dont fire intially
    pass

    def getHitbox(self):
        return shapes.Rectangle(self.x, self.y, self.width, self.height)

    def fireLaser(self, game):
        projectile = LaserBeam(self.x + self.width, self.y)
        game.projectiles.append(projectile)

        pass

    def move(self, left = False, right = False, up = False, down = False):
        if left:
            self.x -= self.HORIZONTAL_MOVE
        if right:
            self.x += self.HORIZONTAL_MOVE
        if up:
            self.y -= self.VERTICAL_MOVE
        if down:
            self.y += self.VERTICAL_MOVE

        # Now check constraints on screen
        if (self.x < X_LEFT_OFFSET_FROM_SCREEN):
            self.x = X_LEFT_OFFSET_FROM_SCREEN

        if (self.x + self.width > SCREEN_SIZE[0] - X_RIGHT_OFFSET_FROM_SCREEN ):
            self.x = SCREEN_SIZE[0] - X_RIGHT_OFFSET_FROM_SCREEN - self.width

        if (self.y < Y_DOWN_OFFSET_FROM_SCREEN):
            self.y = Y_DOWN_OFFSET_FROM_SCREEN

        if (self.y + self.height > SCREEN_SIZE[1] - Y_UP_OFFSET_FROM_SCREEN):
            self.y = SCREEN_SIZE[1] - Y_UP_OFFSET_FROM_SCREEN - self.height

    def update(self, game, action):
        self.move(action[0], action[1], action[2], action[3])
        if action[4] and not self.holding_fire:
            self.fireLaser(game)
            self.holding_fire = True
        if not action[4]: self.holding_fire = False

class LaserBeam(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 5
        self.HORIZONTAL_MOVE = 2 * SCREEN_SIZE[0] // TARGET_FPS  # Desired Rocket Speed / Frame Rate | (pixels/sec)*(sec / frames)
        self.alive = True

    def move(self):
        self.x += self.HORIZONTAL_MOVE

    def update(self):
        self.move()


    def getHitbox(self):
        return shapes.Rectangle(self.x, self.y, self.width, self.height)

class Asteroid(Entity):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.alive = True
        self.HORIZONTAL_MOVE = SCREEN_SIZE[0] // TARGET_FPS  # Desired Rocket Speed / Frame Rate | (pixels/sec)*(sec / frames)
        pass

    def move(self):
        self.x -= self.HORIZONTAL_MOVE

    def update(self):
        self.move()

    def getHitbox(self):
        return shapes.Circle(self.x, self.y, self.r)

