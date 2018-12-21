# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
import math
import time


PACMAN = 0

def getLegalMovingActions(state,agent):
    actions = state.getLegalActions(agent)
    if Directions.STOP in actions:
        actions.remove(Directions.STOP)
    return actions

def termialTest(state):
    if state.isWin() or state.isLose():
        return utility(state)

def utility(state):
    """if state.isWin():
        return 1
    elif state.isLose():
        return -1"""

    return state.getScore()

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
        self.last_move = Directions.STOP


    def initVariable(self, state):
        self.nb_agent = state.getNumAgents()

    def minimax(self, state, agent, parents_positions):
        if termialTest(state):
            return utility(state)
        return self.computeMinimaxScore(state, agent, parents_positions)


    def computeMinimaxScore(self, state, agent, parents_positions):
        legal_moves = getLegalMovingActions(state,agent)
        if agent == PACMAN:
            score = -math.inf
            for move in legal_moves:
                child_state = state.generateSuccessor(agent, move)
                curr_hash = hash((child_state.getPacmanPosition(), child_state.getGhostPositions()[0]))
                if curr_hash not in parents_positions:
                    new_parents_positions = parents_positions.copy()
                    new_parents_positions.append(curr_hash)
                    score = max(score,
                                self.minimax(child_state,
                                (agent+1)%self.nb_agent, new_parents_positions))
        else :
            score = math.inf
            for move in legal_moves:
                child_state = state.generateSuccessor(agent, move)
                curr_hash = hash((child_state.getPacmanPosition(), child_state.getGhostPositions()[0]))
                if curr_hash not in parents_positions:
                    new_parents_positions = parents_positions.copy()
                    new_parents_positions.append(curr_hash)
                    score = min(score,
                                self.minimax(child_state,
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
        if self.first_call :
            self.initVariable(state)
            self.first_call = False

        agent = PACMAN #0

        legal_moves = getLegalMovingActions(state, agent)
        parents_positions = [hash((state.getPacmanPosition(), state.getGhostPositions()[0]))]
        moves_dict = {}
        for move in legal_moves:
            score = self.minimax(state.generateSuccessor(agent, move),
                                (agent+1)%self.nb_agent,
                                parents_positions)
            moves_dict[score] = move
        print(moves_dict)
        time.sleep(3)
        return moves_dict[max(moves_dict)]
