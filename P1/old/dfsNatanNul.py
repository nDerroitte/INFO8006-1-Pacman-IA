# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from collections import deque


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
        self.firstCall = True
        self.path = []
        self.statesToCheck = []

    def getPath(self,state):

        self.statesToCheck.append((state,[],[state.getPacmanPosition()]))

        while  len(self.statesToCheck) != 0:
            currentState, currentPath, exploredNodes =  self.statesToCheck.pop()
            x,y = currentState.getPacmanPosition()
            if self.foodPos[x][y]:
                self.statesToCheck.clear()
                return currentPath
            successors = currentState.generatePacmanSuccessors()
            for succ in successors:
                if succ[0].getPacmanPosition() in exploredNodes:
                    continue
                tempList = exploredNodes[:]
                tempList.append(succ[0].getPacmanPosition())
                self.statesToCheck.append((succ[0], currentPath + [succ[1]],tempList))




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
            self.path = self.getPath(state)
            self.firstCall = False
        else :
            if self.foodPos[x][y]:
                self.foodPos = state.getFood()
                self.path= self.getPath(state)

        return self.path.pop(0)
