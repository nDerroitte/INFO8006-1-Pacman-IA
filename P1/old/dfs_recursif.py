# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions

#Fonction de base à jamais remplir.

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.foodPos = []
        self.exploredNodes = []
        self.firstCall = True
        self.path = []

    def getPath(self,state):
        x,y = state.getPacmanPosition()
        self.exploredNodes.append(state.getPacmanPosition())
        if self.foodPos[x][y]:
            self.exploredNodes = []
            return True
        for succ in state.generatePacmanSuccessors():
            if succ[0].getPacmanPosition() in self.exploredNodes:
                continue
            if self.getPath(succ[0]):
                self.path.append(succ[1])
                return True
        return False

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """
        if  state.isWin():
            return Directions.STOP
        x,y = state.getPacmanPosition()
        if self.firstCall:
            self.foodPos = state.getFood()
            self.getPath(state)
            self.firstCall = False
        else :
            if self.foodPos[x][y]:
                self.foodPos = state.getFood()
                self.getPath(state)

        return self.path.pop()
