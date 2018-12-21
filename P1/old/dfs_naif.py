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
        self.previousNodes = []
        self.firstCall = True

    def containFood(self,state):
        x,y = state.getPacmanPosition()
        self.exploredNodes.append(state.getPacmanPosition())

        if self.foodPos[x][y]:
            self.exploredNodes = []
            return True
        elif state.getPacmanPosition() in self.previousNodes :
            return False

        for succ in state.generatePacmanSuccessors():
            if succ[0].getPacmanPosition() in self.exploredNodes or succ[0].getPacmanPosition() in self.previousNodes:

                continue
            if self.containFood(succ[0]):
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
            self.firstCall = False

        else :
            if self.foodPos[x][y]:
                self.previousNodes= []
                self.foodPos = state.getFood()


        self.previousNodes.append(state.getPacmanPosition())

        for succ in state.generatePacmanSuccessors() :
            if self.containFood(succ[0]):
                return succ[1]


        #Should never happen
        return Directions.STOP
