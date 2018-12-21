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

def cutoffTest(state, depth, MAX_DEPTH):
    if state.isWin() or state.isLose() or depth > MAX_DEPTH:
        return True
    return False

def eval(state):

    #print(state.getWalls().asList())

    food_list = state.getFood().asList()
    nb_foods =  len(food_list)
    ghost_list = state.getGhostPositions()
    nb_ghosts = len(ghost_list)
    pacman_pos = state.getPacmanPosition()
    #print("-----\nFood list : {}\nNumber of food: {}\nGhost list : {}\nNumber of ghost : {}\nPacman Pos {}\n-----".format(food_list,nb_foods,ghost_list,nb_ghosts,pacman_pos))

    #distance_closest_food = min(map(lambda x: manhattanDistance(pacman_pos, x), food_list))
    #print(distance_closest_food , distance_closest_food2)
    #print(distance_closest_food,distance_closest_food2)
    distance_closest_ghost = min(map(lambda x: manhattanDistance(pacman_pos, x), ghost_list))
    distance_closest_ghost +=1
    distance_closest_food2 = bfs(state)
    if distance_closest_food2 == None:
        distance_closest_food2 = distance_closest_ghost
    score = 1* state.getScore() -1.5 * distance_closest_food2 -2* (1./(distance_closest_ghost))  -4 * nb_foods
    #print(score)
    return score


def bfs(state):
    queue = []
    discovered = []
    cost = 0
    food_pos = state.getFood()

    queue.append((state, cost))
    while queue:
        curr_node = queue.pop(0)
        x, y = curr_node[0].getPacmanPosition()

        if food_pos[x][y] :
            return curr_node[1]

        if (x, y) not in discovered:
            discovered.append((x, y))
            successors = curr_node[0].generatePacmanSuccessors()
            for successor in successors:
                queue.append((successor[0], curr_node[1] +1))

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
        self.MAX_DEPTH = 0


    def initVariable(self, state):
        self.first_call = False
        self.nb_agent = state.getNumAgents()

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



    def minimax(self, state, depth, agent):
        if cutoffTest(state, depth, self.MAX_DEPTH):
            return eval(state)
        return self.computeMinimaxScore(state, depth, agent)


    def computeMinimaxScore(self, state, depth, agent):
        if agent == PACMAN:
            score = -math.inf
            for child_state in state.generatePacmanSuccessors():
                score = max(score,
                            self.minimax(child_state[0],
                            depth+1, (agent+1)%self.nb_agent))
        else :
            score = math.inf
            for child_state in state.generateGhostSuccessors(agent):
                score = min(score,
                            self.minimax(child_state[0],
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
