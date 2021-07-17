'''
Define a class that stores the entire game.
This class can be manually stepped or it can be (potentially) run
via some GameEngine.autorun(FPS) method but will need to work out how
inputs will work (especially coming from another program such as NEAT)

'''

class GameEngine:
    def __init__(self):
        self.running = False
        self.fitness = 0
        pass

    def start(self):
        self.running = True
        pass

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
        pass

    pass