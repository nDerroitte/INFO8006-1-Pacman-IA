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
        self.firstCall = True
        self.path = []
        self.statesToCheck = []

    def appendWithCost(self,list,elementToAdd):
        if len(list)==0:
            list.append(elementToAdd)
            return
        cost = elementToAdd[0]
        for i in range (len(list)):
            if cost <= list[i][0]:
                list.insert(i,elementToAdd)
                return
        list.append(elementToAdd)
        return

    def get_path(self,state):
        food_pos = state.getFood()
        priorityQueue = []
        discovered = []

        cost = 1
        self.appendWithCost(priorityQueue,(cost,(state,Directions.STOP),[]))
        while priorityQueue:
            curr_node = priorityQueue.pop(0)
            curr_pos = curr_node[1][0].getPacmanPosition()

            if food_pos[curr_pos[0]][curr_pos[1]]:
                curr_node[2].append(curr_node[1][1])
                return curr_node[2][1:]

            if curr_pos not in discovered:
                discovered.append(curr_pos)
                curr_node[2].append(curr_node[1][1])
                successors = curr_node[1][0].generatePacmanSuccessors()
                for successor in successors:
                    cost = len(curr_node[2])
                    self.appendWithCost(priorityQueue,(cost,successor,curr_node[2].copy()))
        return [Directions.STOP]

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

        if self.path:
            return self.path.pop(0)
        else:
            self.path = self.get_path(state)
            return self.path.pop(0)
