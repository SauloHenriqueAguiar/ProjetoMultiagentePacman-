# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
#implementação de classes agente Reflexo, minimax, alfabeta pruning e Expectminmax

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):

    depth = 0
    return self.get_max(gameState, depth)[1]
  # alpha = max best option
  # beta = min best
  def get_max(self, gameState, depth, agent = 0, alpha=float('-inf'), beta=float('inf')):
    actions = gameState.getLegalActions(agent)
    successorCost = alpha
    successorAction = Directions.STOP
    if not actions or gameState.isWin() or depth >= self.depth:
      return self.evaluationFunction(gameState), Directions.STOP

    for action in actions:
      successor = gameState.generateSuccessor(agent, action)

      cost = self.get_min(successor, depth, agent + 1, alpha=successorCost, beta=beta)[0]

      if cost > successorCost:
        successorCost = cost
        successorAction = action
        alpha = successorCost
      if successorCost >= beta: # PODA
        return successorCost, successorAction
  
    return successorCost, successorAction

  def get_min(self, gameState, depth, agent, alpha=float('-inf'), beta=float('inf')):
    actions = gameState.getLegalActions(agent)

    if not actions or gameState.isLose() or depth >= self.depth:
      return self.evaluationFunction(gameState), Directions.STOP

    successorCost = beta
    successorAction = Directions.STOP

    for action in actions:
      successor = gameState.generateSuccessor(agent, action)

      if agent == gameState.getNumAgents() - 1:
        cost = self.get_max(successor, depth + 1, alpha=alpha, beta=beta)[0]
      else:
        cost = self.get_min(successor, depth, agent + 1, alpha=alpha, beta=successorCost)[0]
      if cost < successorCost:
        successorCost = cost
        successorAction = action
        beta = successorCost
      if successorCost <= alpha: # PODA
        return successorCost, successorAction
    return successorCost, successorAction

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).
      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
