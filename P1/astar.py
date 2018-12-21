# Complete this class for all parts of the project

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

    def sum_manhattan_distances(self,curr_pos,food_pos):
        """
        Arguments :
        -----------
        - 'curr_pos' : the current position.
        - 'food_pos' : the grid containing the food location
        Return:
        -------
        - The manhattan_distance with the farest food.
        """
        sum_md = 0
        for i in range(food_pos.width):
            for j in range(food_pos.height):
                if food_pos[i][j]:
                    sum_md += abs(curr_pos[0]-i)+abs(curr_pos[1]-j)
        return sum_md

    def cost(self,curr_p_node,successor):
        """
        Arguments :
        -----------
        - 'curr_p_node' : the current prioritizedNode.
        - 'sucessor'    : the following node where we want to evaluate the dist
        Return:
        -------
        - The current cost of the path going to the sucessor node
        """
        food_pos = curr_p_node.state.getFood()
        curr_pos = curr_p_node.state.getPacmanPosition()
        return curr_p_node.priority + 1 + self.sum_manhattan_distances(curr_pos
        ,food_pos)

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
            curr_pos = curr_p_node.state.getPacmanPosition()
            curr_hash = hash((curr_pos,curr_p_node.state.getFood()))

            if curr_p_node.state.isWin():
                curr_p_node.path.append(curr_p_node.move)
                return curr_p_node.path[1:]

            if curr_hash not in discovered:
                discovered.append(curr_hash)
                curr_p_node.path.append(curr_p_node.move)
                successors = curr_p_node.state.generatePacmanSuccessors()
                for successor in successors:
                    priority_queue.put(PrioritizedNode(
                        self.cost(curr_p_node,successor)
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
