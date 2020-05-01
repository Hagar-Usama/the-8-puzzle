
import copy

# https://bluesock.org/~willkg/dev/ansi.html
ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"

def print_yellow(msg):
    print(f"{ANSI_YELLOW}{msg}{ANSI_RESET}")

def print_purple(msg):
    print(f"{ANSI_PURPLE}{msg}{ANSI_RESET}")

def print_blue(msg):
    print(f"{ANSI_BLUE}{msg}{ANSI_RESET}")


def print_red(msg):
    print(f"{ANSI_RED}{msg}{ANSI_RESET}")


def print_green(msg):
    print(f"{ANSI_GREEN}{msg}{ANSI_RESET}")



class Node():
    # state is list of list. Each list is a row
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.neighbors = []
        self.tileRow ,self.tileCol = get_empty_tile(self)
        
    
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
                # neighbors are left,right,up,down
                for neighbor in state.neighbors():
                    if neighbor not in frontier U explored:
                        frontier.push(neighbor)
                    
            return Failure
        '''

        frontier = [self]
        explored = []
        
        while frontier:
            current_node = frontier.pop(0)
            if current_node.state not in explored:
                print("adding current_node in explored")
                explored.append(current_node.state)
            #explored.add(current_node.state)

            print_yellow(f'current state: {current_node.state}')

            if current_node.state == goal:
                print_blue("Target found")
                return True
            
            status = self.try_move(current_node)
            print_blue(status)

            for i in range(0,len(status)):
                if status[i]:
                    new_state = self.move(i,current_node)
                    print_red(f'move {new_state}')

                    
                    if new_state not in explored:
                        print("state not in explored")
                        ns = Node(new_state, current_node)
                        frontier.append(ns)
                        current_node.neighbors.append(ns) 

            print(f'explored: {explored}')    


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
    
    def try_move(self, current_node):
        '''
        returns the status [left, right, up, down]
        
        '''

        status = [False, False, False, False]
        #tileX, tileY = get_empty_tile()
        
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3

        if current_node.tileCol == 0 :
            status[RIGHT] = True
        elif current_node.tileCol == 1:
            status[LEFT] = True
            status[RIGHT] = True
        elif current_node.tileCol == 2:
            status[LEFT] = True

        if current_node.tileRow == 0 :
            status[DOWN] = True
        elif current_node.tileRow == 1:
            status[UP] = True
            status[DOWN] = True
        elif current_node.tileRow == 2:
            status[UP] = True

        return status

    def get_empty_tile(self):

        EMPTY_TILE = 0

        for i, element in enumerate(self.state):
            #print_yellow(i)
            try:
                j = element.index(EMPTY_TILE)
            except ValueError:
                continue

            return i,j
                    
        return -1,-1

    def move(self, movement,my_node):
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3

        EMPTY_TILE = 0

        row = my_node.tileRow
        col = my_node.tileCol

        # list of list
        board = copy.deepcopy(my_node.state)
        #board = list(my_node.state)

        if movement == LEFT:
            target_tile = board[row][col-1]
            board[row][col] = target_tile
            board[row][col-1] = EMPTY_TILE
            # check seems wrong
            #self.tileCol = col-1

        elif movement == RIGHT:
            target_tile = board[row][col+1]
            board[row][col] = target_tile
            board[row][col+1] = EMPTY_TILE
            #self.tileCol = col+1
        
        elif movement == UP:
            target_tile = board[row-1][col]
            board[row][col] = target_tile
            board[row-1][col] = EMPTY_TILE
            #self.tileRow = row-1

        elif movement == DOWN:
            target_tile = board[row+1][col]
            board[row][col] = target_tile
            board[row+1][col] = EMPTY_TILE
            #self.tileRow = row+1

        #self.state = temp
        #print_red(state)
        #print_green(board)

        return board


    

        
    def print_state(state):
        pass

    def traverse_tree(state):
        pass

    def zip_node(self):
        '''
        returns node as a list of nodes
        '''
        l = []
        if isinstance(self.neighbors, list):

            for i in self.neighbors:
                print_red(type(i))
                l.append(i)
            for i in l:
                self = i
                i = self.zip_node()

        return l

        
    

def move(movement,my_node):
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3

        EMPTY_TILE = 0

        row = my_node.tileRow
        col = my_node.tileCol

    
        board = copy.deepcopy(my_node.state)

        if movement == LEFT:
            target_tile = board[row][col-1]
            board[row][col] = target_tile
            board[row][col-1] = EMPTY_TILE
            # check seems wrong
            #self.tileCol = col-1

        elif movement == RIGHT:
            target_tile = board[row][col+1]
            board[row][col] = target_tile
            board[row][col+1] = EMPTY_TILE
            #self.tileCol = col+1
        
        elif movement == UP:
            target_tile = board[row-1][col]
            board[row][col] = target_tile
            board[row-1][col] = EMPTY_TILE
            #self.tileRow = row-1

        elif movement == DOWN:
            target_tile = board[row+1][col]
            board[row][col] = target_tile
            board[row+1][col] = EMPTY_TILE
            #self.tileRow = row+1

        #self.state = temp
        #print_red(state)
        #print_green(board)

        return board
      

def get_empty_tile(my_node):

        EMPTY_TILE = 0

        for i, element in enumerate(my_node.state):
            #print_yellow(i)
            try:
                j = element.index(EMPTY_TILE)
            except ValueError:
                continue

            return i,j
                    
        return -1,-1    

def parse_input(state):
    pass

def parse_output(state):
    pass


def print_tree(tree_list, depth):

    if isinstance(tree_list, list):
        print_tree(tree_list[0],depth+1)

        for i in range(depth):
            print("\t")

        #print_yellow(tree_list)

        print_tree(tree_list[1],depth+1)

def zip_node(n):
        '''
        returns node as a list of nodes
        '''
        l = []
        m = []
        if isinstance(n.neighbors, list):

            for i in n.neighbors:
                print_red(type(i))
                l.append(i)
                m.append(i.state)

            print_blue(m)

            

            for i in l:
                i,m = zip_node(i)


        return l, m

        
def find(c, board):

    for i, element in enumerate(board):
        print_yellow(i)
        try:
            j = element.index(c)
        except ValueError:
            continue

        return i,j
                
    return -1,-1
    

def main():
    state1 = [[1,2,5],[3,4,0],[6,7,8]]
    state2 = [[0,1,2],[3,4,5],[6,7,8]]

    ln = Node(state1, None)
    print_blue(ln.bsf(state2))


if __name__ == "__main__":
    main()