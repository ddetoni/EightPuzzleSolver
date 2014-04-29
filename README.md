EightPuzzleSolver
Names: Douglas Detoni and Marlon Mahl
=================

Input
Number of arguments: 4

1st arguments: type of search
								-d = Deep First-Search
								-b = Breadh First-Search

2nd argument: deepth in the tree
								if 10, the tree will not go further than 10 levels in the tree

3rd argument: first state 	
								example: [1,2,3,0,4,5,6,7,8]
								- no blanks between the numbers
								
4th argument: final state (solution
								example: [0,1,2,3,4,5,6,7,8]
								- no blanks between the numbers
								
input example:
python solver.py -d 15 [1,2,3,0,4,5,6,7,8] [0,1,2,3,4,5,6,7,8]
