# DERROITTE NATAN - TESTOURI MEHDI - IAI - DEADLINE1

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from queue import PriorityQueue

class PrioritizedNode:
    def __init__(self,priority,state,move,path):
        self.priority = priority
        self.state = state
        self.move = move
        self.path = path

    def __lt__(self,other):
        if isinstance(other,PrioritizedNode):
            return self.priority < other.priority
        return False

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """

        self.args = args
        self.path = []

    def cost(self,curr_p_node):
        """
        Arguments :
        -----------
        - 'curr_p_node' : the current prioritizedNode.
        Return:
        -------
        - The current cost of the path
        """
        return curr_p_node.priority + 1

    def get_path(self,state):
        """
        Arguments :
        -----------
        - 'state' : the current game state.
        Return:
        -------
        - the list of move to perfom in order to eat all the nodes.
        """
        priority_queue = PriorityQueue()
        discovered = []

        priority_queue.put(PrioritizedNode(0,state,Directions.STOP,[]))
        while not priority_queue.empty():
            curr_p_node = priority_queue.get()
            curr_hash = hash((curr_p_node.state.getPacmanPosition()
            ,curr_p_node.state.getFood()))

            if curr_p_node.state.isWin():
                curr_p_node.path.append(curr_p_node.move)
                return curr_p_node.path[1:]

            if curr_hash not in discovered:
                discovered.append(curr_hash)
                curr_p_node.path.append(curr_p_node.move)
                successors = curr_p_node.state.generatePacmanSuccessors()
                for successor in successors:
                    priority_queue.put(PrioritizedNode(
                        self.cost(curr_p_node)
                        ,successor[0],successor[1],curr_p_node.path.copy()))

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
