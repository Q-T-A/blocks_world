from BlockWorldAgent import BlockWorldAgent
import time
def test():
    #This will test your BlockWorldAgent
	#with eight initial test cases.
    test_agent = BlockWorldAgent()

    initial_arrangement_1 = [["A", "B", "C"], ["D", "E"]]
    goal_arrangement_1 = [["A", "C"], ["D", "E", "B"]]
    goal_arrangement_2 = [["A", "B", "C", "D", "E"]]
    goal_arrangement_3 = [["D", "E", "A", "B", "C"]]
    goal_arrangement_4 = [["C", "D"], ["E", "A", "B"]]
    print(f'initial_arrangement: {initial_arrangement_1}')
    print(f'goal_arrangement: {goal_arrangement_1}')
    print(f'answer: {test_agent.solve(initial_arrangement_1, goal_arrangement_1)}')
    #print(test_agent.solve(initial_arrangement_1, goal_arrangement_2))
    #print(test_agent.solve(initial_arrangement_1, goal_arrangement_3))
    #print(test_agent.solve(initial_arrangement_1, goal_arrangement_4))

    initial_arrangement_2 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    goal_arrangement_5 = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
    goal_arrangement_6 = [["I", "H", "G", "F", "E", "D", "C", "B", "A"]]
    goal_arrangement_7 = [["H", "E", "F", "A", "C"], ["B", "D"], ["G", "I"]]
    goal_arrangement_8 = [["F", "D", "C", "I", "G", "A"], ["B", "E", "H"]]

   # print(test_agent.solve(initial_arrangement_2, goal_arrangement_5))
    #print(test_agent.solve(initial_arrangement_2, goal_arrangement_6))
    #print(test_agent.solve(initial_arrangement_2, goal_arrangement_7))
    #print(test_agent.solve(initial_arrangement_2, goal_arrangement_8))

    initial_arrangement_3 = [['O'], ['B', 'L', 'K', 'D'], ['A', 'F', 'G', 'J', 'E', 'C', 'H'], ['N'], ['I', 'M']]
    goal_arrangement_9 = [['B', 'K'], ['A', 'F', 'J', 'E', 'H', 'D'], ['O', 'L', 'M', 'G'], ['I'], ['N', 'C']]
    #print(test_agent.solve(initial_arrangement_3, goal_arrangement_9))
'''
    initial_arrangement_4 = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']]
    goal_arrangement_10 = [['Z', 'Y', 'X'], ['W', 'V', 'U'], ['T', 'S', 'R'], ['Q', 'P', 'O'], ['N', 'M', 'L'], ['K', 'J'], ['I', 'H', 'G'], ['F', 'E'], ['D', 'C', 'B', 'A']]
    start = time.time()
    print(test_agent.solve(initial_arrangement_4, goal_arrangement_10))
    end = time.time()
    print(start - end)'''
if __name__ == "__main__":
    test()