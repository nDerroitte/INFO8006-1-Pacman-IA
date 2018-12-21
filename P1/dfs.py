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
        """
        Arguments :
        -----------
        - 'state' : the current game state.
        Return:
        -------
        - the list of move to perfom in order to eat all the nodes.
        """

        stack = []
        discovered = []

        stack.append((state,Directions.STOP,[]))
        while stack:
            curr_node = stack.pop()
            curr_hash = hash((curr_node[0].getPacmanPosition()
            ,curr_node[0].getFood()))

            if curr_node[0].isWin() :
                curr_node[2].append(curr_node[1])
                return curr_node[2][1:]

            if curr_hash not in discovered:
                discovered.append(curr_hash)
                curr_node[2].append(curr_node[1])
                successors = curr_node[0].generatePacmanSuccessors()
                for successor in reversed(successors):
                    stack.append((successor[0],successor[1],curr_node[2].copy()))

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
