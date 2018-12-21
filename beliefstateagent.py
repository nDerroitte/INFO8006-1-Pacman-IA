# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions, GhostRules
import numpy as np
from pacman_module import util
import time


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
    def getAllPropPosition(self, evidence):
        prob_position = []
        for k in range(-self.w, self.w):
            position_to_add = (evidence[0]+k, evidence[1]+k)
            prob_position.append(position_to_add)

        print(prob_position)
        return prob_position

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
        #Variables init :
        walls = self.walls.asList()
        last_cell = max(walls)
        prob_matrixes = []
        #For each ghost :
        for i in range(len(evidences)):
            nb_legal_move = 0
            prob_position = self.getAllPropPosition(evidences[i])
            for pos in prob_position:
                x,y =pos
                prob_matrix = np.matrix(np.zeros((last_cell[0]+1,last_cell[1]+1)))
                position_to_set = [[x,y ]]
                if(not self.walls[x+1][y]):
                    nb_legal_move+=1
                    position_to_set.append([x+1, y])
                if(not self.walls[x][y-1]):
                    nb_legal_move+=1
                    position_to_set.append([x, y-1])
                if(not self.walls[x][y+1]):
                    nb_legal_move+=1
                    position_to_set.append([x, y+1])

                #East if a legal move
                if (not self.walls[x-1][y]):
                    nb_legal_move +=1
                    prob_matrix[x-1, y] = self.p

                for pos in position_to_set:
                    prob_matrix[pos[0], pos[1]] = 1/nb_legal_move
            prob_matrixes.append(prob_matrix)

        beliefStates = prob_matrixes
        #time.sleep(5)
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
