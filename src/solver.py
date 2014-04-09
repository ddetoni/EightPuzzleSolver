class EightPuzzleSolver:
    b_state_list = None
    
    def __init__(self, initial_state):
        self.b_state_list = [BoardState(initial_state, 0)]
    
    def start(self):
        print self.b_state_list[0].state
        
class BoardState:
    state = None
    index_father = None
    
    def __init__(self, state, index):
        self.state = state
        self.index_father = index    

if __name__ == '__main__':
    puzzle = EightPuzzleSolver([1,0,8,2,4,7,5,3,6])
    puzzle.start()
