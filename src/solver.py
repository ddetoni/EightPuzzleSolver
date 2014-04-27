class EightPuzzleSolver:
    b_state_list = None
    b_state_final = None

    def __init__(self, initial_state, final_state):
        self.b_state_list = [BoardState((initial_state), None)]
        self.b_state_final = [BoardState((initial_state), None)]
        self.c = final_state



			
    def start(self):
        solution_list = self.b_state_list #recebe o estado de entrada 
        count = 1
        i = 1 
        b_state_list = self.b_state_list
        print solution_list[count-1].state
        print self.c
        while(solution_list[count-1].state!=self.c):    
            b_state_list = solution_list[count-1].get_next_states(count-1) #pega os possiveis proximos do estado atual
            solution_list.extend(b_state_list)#concatena no fim da lista
            #solution_list[count-1].print_board()
            count=count+1
            #print count
        print "solution: "
        solution_list[count-1].print_board()
			
class BoardState:
    state = None
    index_father = None

    def __init__(self, state, index):
        self.state = state
        self.index_father = index

    def _empty_position(self):
        for i in range(len(self.state)):
            if self.state[i] == 0:
                return i

    def _change_position(self, pos1, pos2, index_father):
        b_state = BoardState(self.state[:], index_father)

        temp = b_state.state[pos1]
        b_state.state[pos1] = b_state.state[pos2]
        b_state.state[pos2] = temp

        return b_state

    def get_next_states(self, index_father):
        empty_pos = self._empty_position()
        state_list = []

        if empty_pos == 0:
            state_list.append(self._change_position(0, 3, index_father))
            state_list.append(self._change_position(0, 1, index_father))
            return state_list
        elif empty_pos == 1:
            state_list.append(self._change_position(1, 0, index_father))
            state_list.append(self._change_position(1, 2, index_father))
            state_list.append(self._change_position(1, 4, index_father))
            return state_list
        elif empty_pos == 2:
            state_list.append(self._change_position(2, 1, index_father))
            state_list.append(self._change_position(2, 5, index_father))
            return state_list
        elif empty_pos == 3:
            state_list.append(self._change_position(3, 0, index_father))
            state_list.append(self._change_position(3, 4, index_father))
            state_list.append(self._change_position(3, 6, index_father))
            return state_list
        elif empty_pos == 4:
            state_list.append(self._change_position(4, 1, index_father))
            state_list.append(self._change_position(4, 5, index_father))
            state_list.append(self._change_position(4, 7, index_father))
            state_list.append(self._change_position(4, 3, index_father))
            return state_list
        elif empty_pos == 5:
            state_list.append(self._change_position(5, 2, index_father))
            state_list.append(self._change_position(5, 8, index_father))
            state_list.append(self._change_position(5, 4, index_father))
            return state_list
        elif empty_pos == 6:
            state_list.append(self._change_position(6, 3, index_father))
            state_list.append(self._change_position(6, 7, index_father))
            return state_list
        elif empty_pos == 7:
            state_list.append(self._change_position(7, 6, index_father))
            state_list.append(self._change_position(7, 4, index_father))
            state_list.append(self._change_position(7, 8, index_father))
            return state_list
        elif empty_pos == 8:
            state_list.append(self._change_position(8, 5, index_father))
            state_list.append(self._change_position(8, 7, index_father))
            return state_list

    def print_board(self):
        print "|%s %s %s|\n|%s %s %s|\n|%s %s %s|\n" % (self.state[0], self.state[1], self.state[2],
                                                        self.state[3], self.state[4], self.state[5],
                                                        self.state[6], self.state[7], self.state[8]
                                                        )


		
if __name__ == '__main__':
    #b = BoardState([1,8,2,4,0,5,3,6,7], None)
    
    #puzzle = EightPuzzleSolver([1,0,8,2,4,7,5,3,6])
    #puzzle.start()
    b = BoardState([5,0,2,8,4,1,6,7,3], None)
    c = BoardState([0,1,2,3,4,5,6,7,8], None)
    puzzle = EightPuzzleSolver([7,1,2,3,4,5,6,0,8],[0,1,2,3,4,5,6,7,8])
    puzzle.start()
    #l = b.get_next_states(0)
    #l[0].print_board()
    #l[1].print_board()
    #l[2].print_board()
    #l[3].print_board()
