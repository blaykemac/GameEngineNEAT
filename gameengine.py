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

TARGET_FPS = 60

class GameEngine:
    def __init__(self):
        self.running = False
        self.fitness = 0
        pass

    def start(self):
        self.running = True
        self.rocket = Rocket()
        self.asteroids = []
        self.projectiles = []
        #self.entities = []
        pass

    def updateAll(self):
        # Go through all player, projectiles and asteroids and check for collision
        for projectile in self.projectiles:
            projectile.update()

        for asteroid in self.asteroids:
            asteroid.update()

        self.rocket.update()

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
        pass

    # Simulate the next frame given the action or player input
    def simulateTimeStep(self, action):
        #for each rocket, for each projectile (ie laser), for each asteroid
        #call update on that object
        # action will be a tuple of booleans
        # (moveLeft, moveRight, moveUp, moveDown, fire)

        pass

class Entity:
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

class Rocket(Entity):

    def __init__(self):
        self.width = 30
        self.height = 15
        #Define x and y from the top-left of the rocket shape
        self.x = X_LEFT_OFFSET_FROM_SCREEN
        self.y = SCREEN_SIZE[1] // 2 - self.height // 2
        self.HORIZONTAL_MOVE = SCREEN_SIZE[0] / TARGET_FPS  # Desired Rocket Speed / Frame Rate | (pixels/sec)*(sec / frames)
        self.VERTICAL_MOVE = SCREEN_SIZE[1] / TARGET_FPS  # Desired Rocket Speed / Frame Rate | (pixels/sec)*(sec / frames)
    pass

    def fireLaser(self):
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




class Asteroid(Entity):
    def __init__(self):
        pass

