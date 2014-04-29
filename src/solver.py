import sys

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

    def _print_movements(self, index):
        movements = []
        while(self.b_state_list[index].index_father != None):
            movements.append(index)
            index = self.b_state_list[index].index_father

        movements.append(index)
        movements.reverse()

        count_move = 0
        for num in movements:
            self.b_state_list[num].print_board(count_move)
            count_move += 1

    def _is_solution(self, b_state):
        if b_state.state == self.b_state_final.state:
            return 1
        else:
            return 0

    def start_depth(self, max_level):
        nodes_visited = 0
        while(self.b_state_list):
            last = len(self.b_state_list)-1 #Last position on array
            b_state = self.b_state_list[last]

            if self._is_solution(b_state):
                self._print_movements(last)
                print "Number of nodes visited: %s" % nodes_visited
                return 1

            if not b_state.visited and b_state.level < max_level:
                b_state.visited = 1
                nodes_visited += 1
                next_states = b_state.get_next_states(last)
                self.b_state_list.extend(next_states)
            else:
                del self.b_state_list[last]

        print "Max level hit."
        return 0

    def start_breadth(self, max_level):

        index = 0
        while(index < len(self.b_state_list)):
            b_state = self.b_state_list[index]

            if self._is_solution(b_state):
                self._print_movements(index)
                print "Number of visited nodes: %s" % index
                return 1

            if b_state.level < max_level:
                next_states = b_state.get_next_states(index)
                self.b_state_list.extend(next_states)

            index += 1

        print "Max level hit."
        return 0

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

    def print_board(self, index):
        print "|%s %s %s|\n|%s %s %s| ---> %s\n|%s %s %s|\n" % (self.state[0], self.state[1], self.state[2],
                                                                self.state[3], self.state[4], self.state[5], index,
                                                                self.state[6], self.state[7], self.state[8]
                                                                )



if __name__ == '__main__':

    search_type = sys.argv[1]

    max_level = int(sys.argv[2])

    initial_state = sys.argv[3][1:18].split(',')
    initial_state = [int(num) for num in initial_state]

    final_state = sys.argv[4][1:18].split(',')
    final_state = [int(num) for num in final_state]

    puzzle = EightPuzzleSolver(initial_state, final_state)

    if search_type == '-d':
        print "Depth-First Searching..."
        puzzle.start_depth(max_level)
    elif search_type == '-b':
        print "Breadth-First Searching..."
        puzzle.start_breadth(max_level)
