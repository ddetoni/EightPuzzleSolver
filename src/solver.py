class EightPuzzleSolver:
    b_state_list = None
    b_state_final = None

    def __init__(self, initial_state, final_state):
        self.b_state_list = [BoardState((initial_state), None, 0)]
        self.b_state_final = BoardState((final_state), None, 0)
        self.c = final_state

    def _contains_final_state(self, list_states):
        for b_state in list_states:
            if b_state.state == self.c:
                return b_state

        return None

    def start(self):
        list_of_movements = []
        solution_list = self.b_state_list #recebe o estado de entrada
        count = 1
        b_state_list = self.b_state_list
        final_state = None

        while(True):
            b_state_list = solution_list[count-1].get_next_states(count-1) #pega os possiveis proximos do estado atual

            final_state = self._contains_final_state(b_state_list)

            if final_state != None:
                father = final_state.index_father#pega indice do pai da solucao
                break
            else:
                solution_list.extend(b_state_list)#concatena no fim da lista

            count=count+1

    def _print_movements(self, index):
        movements = []
        while(self.b_state_list[index].index_father != None):
            movements.append(index)
            index = self.b_state_list[index].index_father

        movements.append(index)
        movements.reverse()

        for num in movements:
            self.b_state_list[num].print_board()

    def _is_solution(self, b_state):
        if b_state.state == self.b_state_final.state:
            return 1
        else:
            return 0

    def start_depth(self, max_level):

        while(self.b_state_list):
            last = len(self.b_state_list)-1 #Last position on array
            b_state = self.b_state_list[last]

            if self._is_solution(b_state):
                self._print_movements(last)
                break

            if not b_state.visited and b_state.level < max_level:
                b_state.visited = 1
                next_states = b_state.get_next_states(last)
                self.b_state_list.extend(next_states)
            else:
                del self.b_state_list[last]

        print "Max level hit."

class BoardState:
    state = None
    index_father = None
    level = None
    visited = 0

    def __init__(self, state, index, level):
        self.state = state
        self.index_father = index
        self.level = level

    def _empty_position(self):
        for i in range(len(self.state)):
            if self.state[i] == 0:
                return i

    def _change_position(self, pos1, pos2, index_father):
        b_state = BoardState(self.state[:], index_father, self.level+1)

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
            state_list.append(self._change_position(8, 7, index_father))
            state_list.append(self._change_position(8, 5, index_father))
            return state_list

    def print_board(self):
        print "|%s %s %s|\n|%s %s %s|\n|%s %s %s|\n" % (self.state[0], self.state[1], self.state[2],
                                                        self.state[3], self.state[4], self.state[5],
                                                        self.state[6], self.state[7], self.state[8]
                                                        )



if __name__ == '__main__':
    puzzle = EightPuzzleSolver([8,7,6,5,4,3,2,1,0],[0,1,2,3,4,5,6,7,8])
    puzzle.start_depth(30)
