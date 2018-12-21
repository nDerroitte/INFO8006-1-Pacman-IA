# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """

        self.args = args
        self.path = []

    def get_path(self,state):
        food_pos = state.getFood()
        stack = []
        discovered = []

        stack.append(((state,Directions.STOP),[]))
        while stack:
            curr_node = stack.pop()
            curr_pos = curr_node[0][0].getPacmanPosition()

            if food_pos[curr_pos[0]][curr_pos[1]]:
                curr_node[1].append(curr_node[0][1])
                return curr_node[1][1:]

            if curr_pos not in discovered:
                discovered.append(curr_pos)
                curr_node[1].append(curr_node[0][1])
                successors = curr_node[0][0].generatePacmanSuccessors()
                for successor in successors:
                    stack.append((successor,curr_node[1].copy()))
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
