# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions, GhostRules
import numpy as np
from pacman_module import util
import time
import math

def isAccessible(pos1, pos2):
    x1,y1 = pos1
    x2, y2 =pos2
    if x1 == x2 and y1 == y2 +1:
        return 1
    if x1 == x2 and y1 == y2 -1:
        return 1
    if x1 == x2-1 and y1 == y2:
        return 1
    if x1 == x2+1 and y1 == y2:
        return 1
    return 0

def normalize(matrix):
    """
    Arguments:
    ---------
    - `matrix : input matrix one wants to normalize

    Return:
    -------
    - The normalize matrix from the input matrix.
    """
    sum = matrix.sum()
    # Verification that the sum is !=0. Shouldn't never happen
    if not sum :
        return matrix
    alpha = 1/matrix.sum()
    return np.multiply(matrix, alpha)

class BeliefStateAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        """
            Variables to use in 'updateAndFetBeliefStates' method.
            Initialization occurs in 'get_action' method.
        """
        # Current list of belief states over ghost positions
        self.beliefGhostStates = None
        # Grid of walls (assigned with 'state.getWalls()' method)
        self.walls = None
        # Uniform distribution size parameter 'w'
        # for sensor noise (see instructions)
        self.w = self.args.w
        # Probability for 'leftturn' ghost to take 'EAST' action
        # when 'EAST' is legal (see instructions)
        self.p = self.args.p

    def getLayoutSize(self):
        """
        Get the size of the puzzle

        Return:
        --------
         - (x_max, y_max), a list containing the maximum index of the maze
        """
        walls = self.walls.asList()
        last_cell = max(walls)
        return last_cell[0]+1, last_cell[1]+1

    def getLegalPos(self, position):
        """
        Return a list of legal position from a current position

        Arguments:
        ----------
        - `position`: a list containing the (x,y) coordinate of the point

        Return:
        -------
        The list of legals position from `position
        """
        legal_moves = []
        x, y = position
        x_max, y_max = self.getLayoutSize()

        #West
        if(x-1 > 0 and not self.walls[x-1][y]):
            legal_moves.append((x-1, y))
        #South
        if(y-1 > 0 and not self.walls[x][y-1]):
            legal_moves.append((x, y-1))
        #North
        if(y+1 < y_max and not self.walls[x][y+1]):
            legal_moves.append((x, y+1))
        #East
        if (x+1 < x_max and not self.walls[x+1][y]):
            legal_moves.append((x+1, y))

        return legal_moves

    def getNbLegalMoves(self, position):
        """
        Get the number of legals move from a position

        Argument:
        --------
        -`position`: the current position

        Return:
        ------
        The number of legals move from the position
        """
        return len(self.getLegalPos(position))

    def transitionModel(self, ghost_position_t1, ghost_position_t):
        nb_legal_move = self.getNbLegalMoves(ghost_position_t)
        if not nb_legal_move:
            return 0

        x, y = ghost_position_t
        x1, y1 = ghost_position_t1

        if x == x1-1 and y == y1:
            return self.p + (1-self.p)/nb_legal_move
        else:
            if not self.walls[x+1][y]:
                return (1-self.p)/nb_legal_move
            else:
                return 1/nb_legal_move

    def sensorModel(self, evidence, ghost_position):
        max_x, max_y = self.getLayoutSize()
        x,y = ghost_position

        for i in range (-self.w, self.w +1):
            for j in range (-self.w, self.w+1 ):
                if x+i < 0 or x+i > max_x or y+j <0 or y+j > max_y:
                    continue
                if (x+i, y+j) == evidence:
                    return (1/(math.pow(2*self.w + 1, 2)))
        return 0

    def updateAndGetBeliefStates(self, evidences):
        """
        Given a list of (noised) distances from pacman to ghosts,
        returns a list of belief states about ghosts positions

        Arguments:
        ----------
        - `evidences`: list of (noised) ghost positions at state x_{t}
          where 't' is the current time step

        Return:
        -------
        - A list of Z belief states at state x_{t} about ghost positions
          as N*M numpy matrices of probabilities
          where N and M are respectively width and height
          of the maze layout and Z is the number of ghosts.

        N.B. : [0,0] is the bottom left corner of the maze
        """

        beliefStates = self.beliefGhostStates
        # Getting max size of the maze
        max_x, max_y = self.getLayoutSize()

        # List of the new beliefs we will create
        new_beliefs = []
        # Looping for each ghost
        for i in range(len(evidences)):
            # Init matrix
            new_belief = np.matrix(np.zeros((max_x, max_y)))
            # Looping through the matrix of position
            for x in range(max_x):
                for y in range(max_y):
                    # Getting the first term of the Bayes filter definition
                    term = self.sensorModel(evidences[i], (x, y))
                    # Getting the sum terms of the Bayes filter definition
                    sum = 0
                    for pos in self.getLegalPos((x, y)):
                        sum += (self.transitionModel((x, y), pos)
                            *beliefStates[i][pos[0], pos[1]])
                    # Computing the final value for pixel (x, y)
                    new_belief[x, y] = term*sum
            # Adding the matrix for the current ghost in the total matrix
            new_beliefs.append(normalize(new_belief))

        # Returning our newly computed matrix
        beliefStates = new_beliefs
        self.beliefGhostStates = beliefStates
        return beliefStates

    def _computeNoisyPositions(self, state):
        """
            Compute a noisy position from true ghosts positions.
            XXX: DO NOT MODIFY THAT FUNCTION !!!
            Doing so will result in a 0 grade.
        """
        positions = state.getGhostPositions()
        w = self.args.w
        w2 = 2*w+1
        div = float(w2 * w2)
        new_positions = []
        for p in positions:
            (x, y) = p
            dist = util.Counter()
            for i in range(x - w, x + w + 1):
                for j in range(y - w, y + w + 1):
                    dist[(i, j)] = 1.0 / div
            dist.normalize()
            new_positions.append(util.chooseFromDistribution(dist))
        return new_positions

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

        """
           XXX: DO NOT MODIFY THAT FUNCTION !!!
                Doing so will result in a 0 grade.
        """

        # XXX : You shouldn't care on what is going on below.
        # Variables are specified in constructor.
        if self.beliefGhostStates is None:
            self.beliefGhostStates = state.getGhostBeliefStates()
        if self.walls is None:
            self.walls = state.getWalls()
        return self.updateAndGetBeliefStates(
            self._computeNoisyPositions(state))
