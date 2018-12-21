from pacman_module.game import Agent
from pacman_module.pacman import Directions
from math import inf

PACMAN = 0
GHOST = 1

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """

        self.args = args

    def minimax(self, state, discovered, player, alpha, beta):
        """
        Compute the next best move for pacman.

        Arguments:
        ----------
        - `state`: The current game state.
        - `discovered`: The list of already discovered nodes.
        - `player`: The currently moving player.
        - `alpha`: Alpha parameter for pruning.
        - `beta`: Beta parameter for pruning.

        Return:
        -------
        - The next best move for pacman.
        """

        # compute the sub state used to mark the discovered nodes
        sub_state = (state.getPacmanPosition(), state.getGhostPositions()
        , state.getFood())

        # terminal test and compute the utility value which is the score
        if state.isWin() or state.isLose():
            return state.getScore()

        # pacman is moving
        if player == PACMAN:

            # check if the node has already been explored
            if sub_state not in discovered:
                discovered.append(sub_state)
            else:
                return inf

            # generate the successors
            successors = state.generatePacmanSuccessors()
            score_max = -inf

            # a move has to be returned for the root call instead of a score
            if len(discovered) == 1:
                best_move = Directions.STOP

                # search for the best move in the successors of the root
                for successor in successors:
                    score = self.minimax(successor[0], discovered.copy(), GHOST
                    , alpha, beta)
                    if score > score_max:
                        score_max = score
                        best_move = successor[1]

                    # update the alpha value for the root call
                    alpha = max(alpha, score_max)
                return best_move

            # a score has to be returned if it is not the root call
            else:

                # search for the maximum score in the successors
                for successor in successors:
                    score = self.minimax(successor[0], discovered.copy(), GHOST
                    , alpha, beta)
                    score_max = max(score_max, score)

                    # prune the tree if no better solution can be obtained
                    alpha = max(alpha, score_max)
                    if beta <= alpha:
                        break
                return score_max

        # the ghost is moving
        else:

            # check if the node has already been explored
            if sub_state not in discovered:
                discovered.append(sub_state)
            else:
                return -inf

            # generate the successors
            successors = state.generateGhostSuccessors(1)
            score_min = inf

            # search for the minimum score in the successors
            for successor in successors:
                score = self.minimax(successor[0], discovered.copy()
                , PACMAN, alpha, beta)
                score_min = min(score_min, score)

                # prune the tree if no better solution can be obtained
                beta = min(beta, score_min)
                if beta <= alpha:
                    break
            return score_min

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

        return self.minimax(state, [], PACMAN, -inf, inf)
