# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
import math
import time

###############################################################################
#                               Constants                                     #
###############################################################################
PACMAN = 0
###############################################################################
#                               Functions                                     #
###############################################################################
def getLegalMovingActions(state,agent):
    """
    Given a pacman game state, returns the list of legal moves which does
    not contain `Stop`.

    Arguments:
    ----------
    - `state`: the current game state.

    Return:
    -------
    - A list of legal moves as defined in `game.Directions` which does not
      contain stop.
    """
    actions = state.getLegalActions(agent)
    # Removing 'Stop'
    if Directions.STOP in actions:
        actions.remove(Directions.STOP)
    return actions

def cutoffTest(state, depth, MAX_DEPTH):
    """
    Given a pacman game state, returns True if the algortihm should stop and
    False otherwise. In order to dertermine if the algortihm should be stopped,
    this function check is the game is win or lose and if the current depth is
    not higher then the maximal depth

    Arguments:
    ----------
    - `state`: the current game state.
    - `depth`: current depth of the h-minimax algortihm
    - `MAX_DEPTH`: maximum depth that our h-minimax algortihm allows.

    Return:
    -------
    -  True if the game is win, lose or if the depth is higher then the maximal
       depth.  False otherwise
    """
    if state.isWin() or state.isLose() or depth > MAX_DEPTH:
        return True
    return False

def eval(state):
    """
    Given a pacman game state, return the evaluation score. This score should
    be a relevent score of the current game state. This function use the
    Pacman position, ghosts position and number of food left to compute such
    a score

    Arguments:
    ----------
    - `state`: the current game state.

    Return:
    -------
    -  The evaluated game score of the current game state.
    """
    # initialisation of the different elements that influence the score
    food_list = state.getFood().asList()
    nb_foods =  len(food_list)
    ghost_list = state.getGhostPositions()
    nb_ghosts = len(ghost_list)
    pacman_pos = state.getPacmanPosition()

    # Distance with the closest ghost using the manhattan distance
    distance_closest_ghost = min(map(lambda x: manhattanDistance(pacman_pos, x)
                                    , ghost_list))
    # Since this distance should be as high as possible to have a good score,
    # we will take the inverse of this distance in the evaluated score.
    # In order to avoid division by 0 (case where ghost position = Pacman
    # position), we add 1 to the result. The distance range now will be inside
    # N_0. (Natural positif number)
    distance_closest_ghost +=1
    # In order to compute the distance with the closest food, we use a distance
    # computed with a BFS algortihm. The reasons will be developed in the
    # report
    distance_closest_food = bfsDistance(state)

    # If there is only one food left and the ghost is over it, we don't find
    # the distance to the food. We therefore use the distance with the ghost
    # which is equivalent.
    if distance_closest_food == None:
        distance_closest_food = distance_closest_ghost
    # Score evaluation heuristics
    score = state.getScore() - 4 * distance_closest_food \
            - 5* (1./(distance_closest_ghost))  - 10 * nb_foods
    return score


def bfsDistance(state):
    """
    Given a pacman game state, give the distance with from the ghost to the
    closest food using a BFS algortihm

    Arguments:
    ----------
    - `state`: the current game state.

    Return:
    -------
    -  The distance between Pacman and the closest food
    """
    # Variables initialisation
    queue = []
    # Discovered states (to avoid looping cases)
    discovered = []
    cost = 0
    food_pos = state.getFood()

    # Pushing the first state to explore in queue
    queue.append((state, cost))
    while queue:
        curr_node = queue.pop(0)
        x, y = curr_node[0].getPacmanPosition()

        # We found the closest found
        if food_pos[x][y] :
            # Return the distance
            return curr_node[1]

        if (x, y) not in discovered:
            discovered.append((x, y))
            # Generating the sucessors and adding them to the queue
            successors = curr_node[0].generatePacmanSuccessors()
            for successor in successors:
                # cost increases by one unit
                queue.append((successor[0], curr_node[1] +1))

def manhattanDistance(pos1,pos2):
    """
    Given a pacman game state, give the manhattan distance with from the ghost
    to the closest food

    Arguments:
    ----------
    - `state`: the current game state.

    Return:
    -------
    -  The distance between Pacman and the closest food
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

###############################################################################
#                               PacmanAgent                                   #
###############################################################################
class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.actions_dict = {}
        self.first_call = True
        self.MAX_DEPTH = 0


    def initVariable(self, state):
        """
        Given a pacman game state, initialise the class variables

        Arguments:
        ----------
        - `state`: the current game state.
        """
        self.first_call = False
        self.nb_agent = state.getNumAgents()

        # Computing the MAX_DEPTH in respect with the size of the layout.
        # This is done in order to have good time perfomance, no matter the
        # size
        x = max(state.getWalls().asList())
        nb_cell = x[0]*x[1]

        if nb_cell <=20:
            self.MAX_DEPTH = 4
        elif 21 < nb_cell <=40:
            self.MAX_DEPTH = 3
        elif 41 < nb_cell <=60:
            self.MAX_DEPTH = 2
        else:
            self.MAX_DEPTH = 1



    def minimax(self, state, depth, agent, parents_positions, alpha, beta):
        """
        Given a pacman game state, the agent index and the positions already
        visited by the parents node, compute the h-minimax algortihm to
        estimate the score of the current situation.

        Arguments:
        ----------
        - `state`: the current game state.
        - `depth`: the current depth of the h-minimax algortihm
        - `agent`: agent index. 0 is for Pacman, 1-... is for ghosts
        - `parents_positions`: is a list of string corresponding to the
                               positions already explored and therefore,
                               forbidden.
        - `alpha`: Alpha parameter for pruning.
        - `beta`: Beta parameter for pruning.

        Return:
        -------
        - The score of the current game state resulting of the minimax
          algortihm
        """
        if cutoffTest(state, depth, self.MAX_DEPTH):
            return eval(state)
        return self.computeMinimaxScore(state, depth, agent, parents_positions,
                                        alpha, beta)


    def computeMinimaxScore(self, state, depth, agent, parents_positions,
                            alpha, beta):
        """
        Function in charge computing the minimax score. This function is not in
        charge of applying a cutoff test before computing the score.
        See self.cutoffTest(state)

        Arguments:
        ----------
        - `state`: the current game state.
        - `depth`: the current depth of the h-minimax algortihm
        - `agent`: agent index. 0 is for Pacman, 1-... is for ghosts
        - `parents_positions`: is a list of string corresponding to the
                               positions already explored and therefore,
                               forbidden.
        - `alpha`: Alpha parameter for pruning.
        - `beta`: Beta parameter for pruning.

        Return:
        -------
        - The minimax score of the current game state.
        """
        if agent == PACMAN:
            # initialise the score to - infinity
            score = -math.inf
            # Creating each successors and computing for each of them
            for child_state in state.generatePacmanSuccessors():
                # Generating a explored state
                sub_state = (child_state[0].getPacmanPosition()
                            , child_state[0].getGhostPositions()
                            , child_state[0].getFood().asList())
                # Checking if the state was not already explorated
                if sub_state not in parents_positions:
                    new_parents_positions = parents_positions.copy()
                    new_parents_positions.append(sub_state)
                    score = max(score,
                                self.minimax(child_state[0],
                                depth+1, (agent+1)%self.nb_agent,
                                new_parents_positions, alpha, beta))
                # Prune the tree if no better solution can be obtained
                alpha = max(alpha, score)
                if beta <= alpha:
                    break

        else :
            # initialise the score to infinity
            score = math.inf
            # Creating each successors and computing for each of them
            for child_state in state.generateGhostSuccessors(agent):
                # Generating a explored state
                sub_state = (child_state[0].getPacmanPosition()
                            , child_state[0].getGhostPositions()
                            , child_state[0].getFood().asList())
                # Checking if the state was not already explorated
                if sub_state not in parents_positions:
                    new_parents_positions = parents_positions.copy()
                    new_parents_positions.append(sub_state)
                score = min(score,
                            self.minimax(child_state[0],
                            depth+1, (agent+1)%self.nb_agent,
                            new_parents_positions, alpha, beta))
                # Prune the tree if no better solution can be obtained
                beta = min(beta, score)
                if beta <= alpha:
                    break

        return math.floor(score)

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
        # In case of firt call, we initialise the self variables.
        if self.first_call :
            self.initVariable(state)
            self.first_call = False

        # Variables initialisation
        agent = PACMAN #0
        depth = 0
        alpha = -math.inf
        beta = math.inf

        # Getting legal moves
        legal_moves = getLegalMovingActions(state, agent)
        moves_dict = {}

        # parents_positions correspond to a "explored states" kind of variable
        parents_positions = [(state.getPacmanPosition(),
                              state.getGhostPositions(),
                              state.getFood().asList())]
        # We associate with each legal move a score and place the pair in the
        # moves_dict dictionary
        for move in legal_moves:
            # Getting the score
            score = self.minimax(state.generateSuccessor(agent, move), depth+1,
                                (agent+1)%self.nb_agent, parents_positions,
                                alpha, beta)
            # Update the alpha value for the root call
            alpha = max(alpha, score)
            moves_dict[score] = move
        # Taking the moves that has the higher score
        return moves_dict[max(moves_dict)]
