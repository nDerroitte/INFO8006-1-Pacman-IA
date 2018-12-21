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

def cutoffTest(state, depth):
    if state.isWin() or state.isLose() or depth >= 4:
        return True

def eval(state):
    if state.isWin():
        return 9999999
    elif state.isLose():
        return -99999999

    #print(state.getWalls().asList())

    food_list = state.getFood().asList()
    nb_foods =  len(food_list)
    ghost_list = state.getGhostPositions()
    nb_ghosts = len(ghost_list)
    pacman_pos = state.getPacmanPosition()
    #print("-----\nFood list : {}\nNumber of food: {}\nGhost list : {}\nNumber of ghost : {}\nPacman Pos {}\n-----".format(food_list,nb_foods,ghost_list,nb_ghosts,pacman_pos))

    distance_closest_food = min(map(lambda x: manhattanDistance(pacman_pos, x), food_list))
    #distance_closest_food2 = min(map(lambda x: dfs_recursif_distance(state, x, 0, []), food_list))
    #print(distance_closest_food,distance_closest_food2)
    distance_closest_ghost = min(map(lambda x: manhattanDistance(pacman_pos, x), ghost_list))
    score = 1* state.getScore() -1.5 * distance_closest_food -2* (1./distance_closest_ghost)  -4 * nb_foods
    #print(score)
    return score



def dfs_recursif_distance (state , pos2, cost, exploredNodes):
    exploredNodes.append(pos2)
    pacman_pos = state.getPacmanPosition()
    if pacman_pos == pos2:
        return (cost, True)
    for succ in state.generatePacmanSuccessors():
            if succ[0].getPacmanPosition() in exploredNodes:
                continue
            ret , cost = dfs_recursif_distance(succ[0], pos2, cost +1, exploredNodes)
            if ret:
                return (cost, True)
    return (False, 0)

def manhattanDistance(pos1,pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

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


    def initVariable(self, state):
        self.nb_agent = state.getNumAgents()

    def minimax(self, state, depth, agent):
        if cutoffTest(state, depth):
            return eval(state)
        return self.computeMinimaxScore(state, depth, agent)


    def computeMinimaxScore(self, state, depth, agent):
        legal_moves = getLegalMovingActions(state,agent)
        if agent == PACMAN:
            score = -math.inf
            for move in legal_moves:
                score = max(score,
                            self.minimax(state.generateSuccessor(agent, move),
                            depth+1, (agent+1)%self.nb_agent))
        else :
            score = math.inf
            for move in legal_moves:
                score = min(score,
                            self.minimax(state.generateSuccessor(agent, move),
                            depth+1, (agent+1)%self.nb_agent))
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
        if self.first_call :
            self.initVariable(state)
            self.first_call = False

        agent = PACMAN #0
        depth = 0

        legal_moves = getLegalMovingActions(state, agent)
        moves_dict = {}
        for move in legal_moves:
            score = self.minimax(state.generateSuccessor(agent, move), depth+1,
                                (agent+1)%self.nb_agent)
            moves_dict[score] = move
        return moves_dict[max(moves_dict)]
