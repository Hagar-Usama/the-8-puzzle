
class Node():
    # state is list of list. Each list is a row
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.move
    
    def dfs(self, goal):
        '''
        dfs(initial_state, goal):
            returns Success or Failure

            frontier = Queue.new(initial_state)
            explored = Set.new()

            while not frontier.isEmpty():
                state = frontier.dequeue()
                explored.add(state)

                if goal(state):
                    return Success(state)
                
                # note: in a tree the neighbors of a state
                # are (parent, children)
                for neighbor in state.neighbors():
                    if neighbor not in frontier U explored:
                        frontier.enqueue(neighbor)
                    
            return Failure
        '''




        pass

    def bsf(self, goal):
        '''
        dfs(initial_state, goal):
            # returns Success or Failure

            frontier = stack.new(initial_state)
            explored = set.new()

            while not frontier.isEmpty():
                state = frontier.pop()
                explored.add(state)

                if goal(state):
                    return Success(state)
                
                # note: in a tree the neighbors of a state
                # are (parent, children)
                for neighbor in state.neighbors():
                    if neighbor not in frontier U explored:
                        frontier.push(neighbor)
                    
            return Failure
        '''

        pass

    def a_start(self, goal, heuristic):
        '''
        A*(initial_state, goal):
            # returns Success or Failure

            frontier = Heap.new(initial_state)
            explored = Set.new()

            while not frontier.isEmpty():
                state = forintier.deleteMin()
                explored.add(state)

                if goal(state):
                    return Success
                
                for neighbor in state.neighbors():
                    if neighbor not in frontier U explored:
                        frontier.decreaseKey(neighbor)
            
            return Failure

        '''

        pass
    
    def print_state(state):
        pass

    def traverse_tree(state):
        pass

def parse_input(state):
    pass

def parse_output(state):
    pass