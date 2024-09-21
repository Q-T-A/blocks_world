import numpy as np
class BlockWorldAgent:


   def __init__(self):
       # If you want to do any initial processing, add it here.
       pass
   
   def tup(self, lists):
      return tuple(tuple(list) for list in lists)

   def move_to_table(self, states, block):
        state = [state[:] for state in states]
        for stack in state:
          if stack[-1] == block:
            if len(stack) == 1:
                continue
            stack.pop()
        state.append([block])
        return state
        '''initial_arrangement_1 = [["A", "B", "C"], ["D", "E"]]
          goal_arrangement_1 = [["A", "C"], ["D", "E", "B"]]'''
       
   def move_to_block(self, states, block, pairs):

       state = [state[:] for state in states]
       for stack in state:
          if stack[-1] == block:
            stack.pop()
            if len(stack) == 0:
                state.remove(stack)
            break
       for other_stack in state:
           if pairs[block] == 'Table':
               state.append([block])
               return state, 'Table'
           if stack!= other_stack and other_stack[-1] == pairs[block]:
               for i in range(len(other_stack)-1):
                   if pairs[other_stack[i+1]] != other_stack[i] or pairs[other_stack[0]] != 'Table':
                       return state, -1
               other_stack.append(block)
               return state, pairs[block]
       state.append([block])
       return state, -1 
               
   def solve(self, initial_arrangement, goal_arrangement):
       pairs = {}
       for i in range(len(goal_arrangement)):
           for j in range(len(goal_arrangement[i])-1):
               pairs[goal_arrangement[i][j+1]] = goal_arrangement[i][j]
           pairs[goal_arrangement[i][0]] = 'Table'
               
       q = []
       visited = set()
       q.append((initial_arrangement, []))
       visited.add(self.tup(initial_arrangement))
       while q:
            state, path = q.pop(0)
            print(state)
            if state == goal_arrangement:
                return path
            for stack in state:
                            x = stack[-1]
                            new, y = self.move_to_block(state, x, pairs)
                    
                            if self.tup(new) not in visited and y != -1:
                                visited.add(self.tup(new))
                                q.append((new, path + [x, y]))
                            
                            if len(stack) > 1:
                                #print(f'state: {state}')
                                new = self.move_to_table(state, x)
                                #print(f'new state: {new}')
                                if self.tup(new) not in visited:
                                    visited.add(self.tup(new))
                                    q.append((new, path + [x, 'Table']))
                            if len(stack) == 0:
                                state.remove(stack)
                            
       return []
           
           


           



       # Your code here


       #Add your code here! Your solve method should receive
       #as input two arrangements of blocks. The arrangements
       #will be given as lists of lists. The first item in each
       #list will be the bottom block on a stack, proceeding
       #upward. For example, this arrangement:
       #
       #[["A", "B", "C"], ["D", "E"]]
       #
       #...represents two stacks of blocks: one with B on top
       #of A and C on top of B, and one with E on top of D.
       #
       #Your goal is to return a list of moves that will convert
       #the initial arrangement into the goal arrangement.
       #Moves should be represented as 2-tuples where the first
       #item in the 2-tuple is what block to move, and the
       #second item is where to put it: either on top of another
       #block or on the table (represented by the string "Table").
       #
       #For example, these moves would represent moving block B
       #from the first stack to the second stack in the example
       #above:
       #
       #("C", "Table")
       #("B", "E")
       #("C", "A")
      







