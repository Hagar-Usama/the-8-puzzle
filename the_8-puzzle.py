
import copy
import time
from tabulate import tabulate
import os
import sys

# https://bluesock.org/~willkg/dev/ansi.html
ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_ORANGE_BG = "\033[48;2;255;165;0m"
ANSI_DARK_CYAN = "\033[96m"

purple = "\033[95m"
cyan = "\033[96m"
darkcyan = "\033[36m"
blue = "\033[94m"
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
magenta = "\033[35m"
white = "\033[37m"
black = "\033[30m"

def print_dark_cyan(msg):
    print(f"{ANSI_DARK_CYAN}{msg}{ANSI_RESET}")

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
    def __init__(self, state, parent, depth=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.neighbors = []
        self.tileRow ,self.tileCol = get_empty_tile(self)
        self.h_cost = h_cost
        self.depth = depth
        self.total_cost = h_cost + depth
        self.node_path = None
        self.expanded_nodes = []
        self.elapsed_time = 0
        self.last_search = ""
    
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
        self.last_search = "DFS"
        frontier = [self]
        explored = []
        
        start_time = time.time()
        
        while frontier:
            # pop last one 
            current_node = frontier.pop(-1)
            if current_node.state not in explored:
                print_blue("[Steps] Add Current Node to explored")
                explored.append(current_node.state)
            #explored.add(current_node.state)

            print_yellow(f'[Steps] current state:')
            print_state(current_node.state)

            if current_node.state == goal:
                print_purple("[Steps] Target found")
                self.node_path = current_node
                self.expanded_nodes = explored

                self.elapsed_time = time.time() - start_time
        
                return True
            
            status = self.try_move(current_node)
            #moves_list = (map(lambda x: self.get_move_name(x), L))
            #moves = list(map(lambda x: x**2, L))
            #print_dark_cyan(f'Possible_Moves: {}')

            #print_dark_cyan(f'Possible_Moves: Left: {status[0]}, Right: {status[1]}, Up: {status[2]}, Down: {status[3]}')

            #print_blue(status)

            for i in range(0,len(status)):
                if status[i]:
                    new_state = self.move(i,current_node)
                    #print_red(f'move {new_state}')
                    print_blue(f'[Steps] Move {self.get_move_name(i)}')
                    print_state(new_state)
                    
                    if new_state not in explored:
                        #print("state not in explored")
                        print_blue("[Steps] Add Next Node to Frontier")
                        print_state(new_state)

                        ns = Node(new_state, current_node, depth=current_node.depth+1)
                        frontier.append(ns)
                        current_node.neighbors.append(ns) 

            #print(f'explored: {explored}') 

        elapsed_time = time.time() - start_time   


    def get_move_name(self,move_no):  
        
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3 

        if move_no == LEFT:
            return "Left"
        elif  move_no == RIGHT:
            return "Right"
        elif  move_no == UP:
            return "Up"
        elif move_no == DOWN:
            return "Down"


    def bfs(self, goal):
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
        self.last_search = "BFS"
        frontier = [self]
        explored = []
        
        #start_time = time.time()

        start_time = time.time()
        
        while frontier:
            current_node = frontier.pop(0)
            if current_node.state not in explored:
                print_blue("[Steps] Add Current Node to explored")
                explored.append(current_node.state)
            #explored.add(current_node.state)

            print_yellow(f'[Steps] current state:')
            print_state(current_node.state)

            if current_node.state == goal:
                print_purple("[Steps] Target found")
                self.node_path = current_node
                self.expanded_nodes = explored

                self.elapsed_time = time.time() - start_time 
        

                return True
            
            status = self.try_move(current_node)
            #print_blue(f'Possible_Moves: Left: {status[0]}, Right: {status[1]}, Up: {status[2]}, Down: {status[3]}')

            for i in range(0,len(status)):
                if status[i]:
                    new_state = self.move(i,current_node)
                    #print_red(f'MAKE  {new_state}')
                    print_blue(f'[Steps] Move {self.get_move_name(i)}')
                    print_state(new_state)
                    #time.sleep(0.5)
                    #os.system('clear')


                    
                    if new_state not in explored:
                        #print("state not in explored")
                        print_blue("[Steps] Add Next Node to Frontier")
                        print_state(new_state)
                        ns = Node(new_state, current_node, depth=current_node.depth+1)
                        frontier.append(ns)
                        current_node.neighbors.append(ns) 

            #print(f'explored: {explored}')

        #elapsed_time = time.time() - start_time   


    def a_star(self, goal, heuristic= 'Manhattan'):
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


            note: f(n) = g(n) + h(n)
            h(n) = hueristic cost
            g(n) = distance from current node to the root node
            g(n) = depth
            f(n) = total cost

        '''
        
        self.last_search = "A* " + heuristic
        frontier = [self]
        explored = []

        start_time = time.time()
        
        while frontier:
            frontier = sorted(frontier, key= lambda c:c.total_cost)
            current_node = frontier.pop(0)
            if current_node.state not in explored:
                print_blue("[Steps] Add Current Node to explored")
                #print("adding current_node in explored")
                explored.append(current_node.state)


            print_yellow(f'[Steps] current state:')
            print_state(current_node.state)

            if current_node.state == goal:
                print_purple("[Steps] Target found")
                self.node_path = current_node
                self.expanded_nodes = explored

                self.elapsed_time = time.time() - start_time 
                return True

            status = self.try_move(current_node)
            #print_blue(f'Possible_Moves: Left: {status[0]}, Right: {status[1]}, Up: {status[2]}, Down: {status[3]}')

            for i in range(0,len(status)):
                if status[i]:
                    # mind node depth (has to be changed)

                    new_state = self.move(i,current_node)
                    #print_red(f'move {new_state}')
                    print_blue(f'[Steps] Move {self.get_move_name(i)}')


                    
                    if new_state not in explored:
                        print_blue("[Steps] Add Next Node to Frontier")
                        print_state(new_state)
                        depth = current_node.depth + 1
                        h_cost = get_heuristic_val(new_state, goal, option=heuristic)
                        total_cost = h_cost + depth


                        ns = Node(new_state, current_node, depth=depth, h_cost=h_cost)
                        frontier.append(ns)
                        current_node.neighbors.append(ns) 

            #print(f'explored: {explored}')
            


        
            
    
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

    def print_path(self):

        path_stack = []
        #path_list = []

        n = copy.deepcopy(self.node_path)
        #print_green(n)

        while (n != None):
            #print_purple(n.state)
            path_stack.append(n.state)
            n = n.parent
        
        while path_stack:
            #printing path
            #path_list.append(path_stack.pop(-1)
            temp = path_stack.pop(-1)
            #print(temp)
            time.sleep(0.25)
            os.system('clear')
            print_state(temp)
        

    def print_path_cost(self):
        print(f"{ANSI_GREEN}Cost of path :{self.node_path.depth} {ANSI_RESET}")
    
    def show_node_expanded(self):
        print(f"{ANSI_GREEN}# Nodes Expanded :{len(self.expanded_nodes)} {ANSI_RESET}")
        for i in self.expanded_nodes:
            print_state(i)
    
    def show_search_depth(self):
        ''' 
        a) search depth: the level of the goal
        b) max search depth: the deepest level reach during the search.
        It is greater than or equal to searxh depth.
        
        '''
        print_green(f"#Search Depth :{self.node_path.depth}")
        print_green(f"#MaX Search Depth [implement me]!!!:{self.node_path.depth}")

    def print_elapsed_time(self):
        print(f"{ANSI_GREEN}Time Elapsed :{self.elapsed_time} {ANSI_RESET}")

    def print_title(self):
        os.system("clear")
        print('*'*20)
        print_yellow(self.last_search)
        print('*'*20)
    


    
    def print_details(self):
        
        # cost of path
        self.print_path_cost()

        # nodes expanded
        self.show_node_expanded()

        # search depth
        self.show_search_depth()

        #running time
        self.print_elapsed_time()
        
        time.sleep(3)
        os.system('clear')
        # path to goal
        self.print_path()



        # -- path to goal
        # root.print_path()
        # root.print_path_cost()
        # -- consider not printing
        #root.show_node_expanded()
        #root.print_elapsed_time()
        #root.show_search_depth()
    

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

        
def print_state(state):

        EMPTY_TILE = 0

        for i in state:
            for j in i:
                if j == EMPTY_TILE:
                    print(f"{ANSI_ORANGE_BG} _ {ANSI_RESET}",end="|")
                else:
                    print(f" {j} ",end="|")
                    
            print('\n')
            print('-'*12)

        print("="*12)
        


def get_heuristic_val(state, goal_state, option='Manhattan' ):
    h = []
    row_mat = []
    col_mat = []

    EMPTY_TILE = 0
    # Assumption: 8-puzzle has no duplicates ever
    if option == 'Manhattan':
        for i in state:
            for j in i:
                if j != EMPTY_TILE:
                    row1,col1 =  get_tile_coodrinates(state, j)
                    row2,col2 =  get_tile_coodrinates(goal_state, j)
                    h_tile_cost = abs(row1 - row2) + abs(col1 - col2)
                    #print_green(f'({row1-row2},{col1-col2})')
                    h.append(h_tile_cost)
        
    elif option == 'Euclidean':
         for i in state:
            for j in i:
                if j != EMPTY_TILE:
                    row1,col1 =  get_tile_coodrinates(state, j)
                    row2,col2 =  get_tile_coodrinates(goal_state, j)
                    h_tile_cost = (row1 - row2)**2 + (col1 - col2)**2
                    h.append(h_tile_cost)
    
    print_yellow(h)
    return sum(h)
        
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

def get_tile_coodrinates(state, tile_key):

    ''' takes a state list and key and returns rol and col'''

    for i, element in enumerate(state):
        #print_yellow(i)
        try:
            j = element.index(tile_key)
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

def get_arg(param_index, default=None):
    """
        Gets a command line argument by index (note: index starts from 1)
        If the argument is not supplies, it tries to use a default value.

        If a default value isn't supplied, an error message is printed
        and terminates the program.
    """
    try:
        return sys.argv[param_index]
    except IndexError as e:
        if default:
            return default
        else:
            print(e)
            print(
                f"[FATAL] The comand-line argument #[{param_index}] is missing")
            exit(-1)  # Program execution failed.
   

def main():

    # getting args
    default_state = [[1,2,5],[3,4,0],[6,7,8]]
    default_goal = [[0,1,2],[3,4,5],[6,7,8]]
    initial_state = get_arg(1,default_state)
    goal_state = get_arg(2, default_goal)
    #print(initial_state,goal_state)

    root = Node(initial_state,None)

    root.print_title()
    time.sleep(1)

    # BFS
    root.bfs(goal_state)
    root.print_details()
    
    os.system("clear")
    print('*'*20)
    print_yellow("DFS")
    print('*'*20)

    root.print_title()
    time.sleep(1)

    # DFS
    root.dfs(goal_state)
    root.print_details()

    

    root.print_title()
    time.sleep(1)

    # A* Manhattan
    root.a_star(goal_state)
    root.print_details()


    root.print_title()
    time.sleep(1)
        
    # A* Euclidean
    root.a_star(goal_state, 'Euclidean')
    root.print_details()
       
    
if __name__ == "__main__":
    main()