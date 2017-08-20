# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    visited = []
    def dfs(point, visited,problem):
        visited.append(point)
        if problem.isGoalState(point):
            return True, []
        for pointCan,direction,_ in problem.getSuccessors(point):
            if pointCan not in visited:
                win,path=dfs(pointCan,visited,problem)
                if win:
                    path.append(direction)
                    return True,path
        return False,[]
    
    p = problem.getStartState()
    win,path=dfs(p, visited,problem)
    path.reverse()
    return path
    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    visited=[]
    def bfs(point,visited,problem):
        visited.append(point)
        if problem.isGoalState(point):
            return True,[]
        for pointNew,direction,_ in problem.getSuccessors(point):
            if pointNew not in visited:
                if problem.isGoalState(pointNew):
                    return True, [direction]
        for pointNew2,direction,_ in problem.getSuccessors(point):
            if pointNew2 not in visited: 
                win,path=bfs(pointNew2,visited,problem)
                if win:
                    path.append(direction)
                    return True, path
        return False, []
    point = problem.getStartState()
    win,path=bfs(point,visited,problem)
    path.reverse()
    return path
    
                    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # pathList [(point, [directions..], cost)..]
    from util import PriorityQueue
   
    def ucs(Plist,visited,problem):
        if Plist.isEmpty():
            return False,[]
        pointN,direction,cost = Plist.pop()
        if problem.isGoalState(pointN):
            return True,direction
        for pointN2,directionN2,costN2 in problem.getSuccessors(pointN):
            if pointN2 not in visited:
                visited.append(pointN2)
                DN = direction[:]
                DN.append(directionN2)
                cost=cost+costN2
                Plist.push((pointN2,DN,cost),cost)
        return ucs(Plist,visited,problem)
    point = problem.getStartState()
    Plist = PriorityQueue()
    Plist.push((point,[],0),0)
    visited = [point]
    Win,direction = ucs(Plist,visited,problem)
    return direction


       




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
   #util.raiseNotDefined()
    from util import PriorityQueue
    visited=[]
    def astar(Plist,visited,problem):
        '''if Plist.isEmpty():
            return False,[]'''
        point,direction,cost = Plist.pop()
        if problem.isGoalState(point):
            return point,direction,cost
        visited = [point]
        '''for pointN2,directionN2,costN2 in problem.getSuccessors(pointN):
            if pointN2 not in visited:
                DN2=direction[:]
                DN2.append(directionN2)
                cost=cost+costN2+heuristic(pointN2,problem)
                Plist.push((pointN2,DN2,cost),cost)
        return astar(Plist,visited,problem)'''
        costtemp = 0
        ####
        while not problem.isGoalState(point):
            #DisN2 = direction[:]
            for pointN2,directionN2,costN2 in problem.getSuccessors(point):
                if pointN2 not in visited:
                    visited.append(pointN2)
                    DisN2 = direction[:]
                    DisN2.append(directionN2)
                    costtemp=cost+costN2+heuristic(pointN2,problem)
                    Plist.push((pointN2,DisN2,costtemp),costtemp)
            point,direction,cost = Plist.pop()
        ####
        #point,direction,cost = Plist.pop()    
        print point,direction,cost
        return point,direction,cost 

                
    point = problem.getStartState()
    Plist = PriorityQueue()
    Plist.push((point,[],heuristic(point,problem)),heuristic(point,problem))
    point,direction,cost = astar(Plist,visited,problem)
    print point,direction,cost
    return direction
   




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
