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

def termialTest(state):
    """
    Given a pacman game state, returns True if the state is terminal and False
    otherwise

    Arguments:
    ----------
    - `state`: the current game state.

    Return:
    -------
    -  True if the game is win or lose and False otherwise
    """
    if state.isWin() or state.isLose():
        return True
    return False

def utility(state):
    """
    Given a pacman game state, return the utility score which correspond to the
    game score for minimax.

    Arguments:
    ----------
    - `state`: the current game state.

    Return:
    -------
    -  The current game score has define in the pacman module
    """
    return state.getScore()

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
        self.first_call = True
        self.last_move = Directions.STOP

    def initVariable(self, state):
        """
        Given a pacman game state, initialise the class variables

        Arguments:
        ----------
        - `state`: the current game state.
        """
        self.nb_agent = state.getNumAgents()
        self.first_call = False

    def minimax(self, state, agent, parents_positions):
        """
        Given a pacman game state, the agent index and the positions already
        visited by the parents node, compute the minimax algortihm to estimate
        the score of the current situation.

        Arguments:
        ----------
        - `state`: the current game state.
        - `agent`: agent index. 0 is for Pacman, 1-... is for ghosts
        - `parents_positions`: is a list of string corresponding to the
                               positions already explored and therefore,
                               forbidden.

        Return:
        -------
        - The score of the current game state resulting of the minimax
          algortihm
        """
        if termialTest(state):
            return utility(state)
        return self.computeMinimaxScore(state, agent, parents_positions)


    def computeMinimaxScore(self, state, agent, parents_positions):
        """
        Function in charge computing the minimax score. This function is not in
        charge of applying a terminal test before computing the score.
        See self.terminalTest(state)

        Arguments:
        ----------
        - `state`: the current game state.
        - `agent`: agent index. 0 is for Pacman, 1-... is for ghosts
        - `parents_positions`: is a list of string corresponding to the
                               positions already explored and therefore,
                               forbidden.

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
                    # Recursive call
                    score = max(score,
                                self.minimax(child_state[0],
                                (agent+1)%self.nb_agent, new_parents_positions))
        else :
            # initialise the score to infinity
            score = math.inf
            for child_state in state.generateGhostSuccessors(agent):
                # Generating a explored state
                sub_state = (child_state[0].getPacmanPosition()
                            , child_state[0].getGhostPositions()
                            , child_state[0].getFood().asList())
                # Checking if the state was not already explorated
                if sub_state not in parents_positions:
                    new_parents_positions = parents_positions.copy()
                    new_parents_positions.append(sub_state)
                    # Recursive call
                    score = min(score,
                                self.minimax(child_state[0],
                                (agent+1)%self.nb_agent, new_parents_positions))
        return score

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

        # Start with Pacman as agent
        agent = PACMAN #0

        # Getting legal moves
        legal_moves = getLegalMovingActions(state, agent)

        # parents_positions correspond to a "explored states" kind of variable
        parents_positions = [(state.getPacmanPosition(),
                              state.getGhostPositions(),
                              state.getFood().asList())]
        moves_dict = {}
        # We associate with each legal move a score and place the pair in the
        # moves_dict dictionary
        for move in legal_moves:
            # Getting the score
            score = self.minimax(state.generateSuccessor(agent, move),
                                (agent+1)%self.nb_agent,
                                parents_positions)
            # Placing the pair in the dict
            moves_dict[score] = move
        # We take the move that has the maximum score
        return moves_dict[max(moves_dict)]
