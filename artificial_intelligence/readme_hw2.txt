The heuristic function has two dimensions.
First helper function (distance-heuristic) calculates the Manhattan Distance between the current state and the given goal. Which is just the x-coordinates offs plus y-coordinates offs.
Second helper function (direction-heuristic) calculates how many turnings need to make at least when going towards the given goal.

Then I incorporate another (heuristic-helper) function with inputs of map, goal-list and current state, to calculate the minimal heuristic values against all different goals in the goal-list, and return that value as the final heuristic value for the corresponding input state.

I implemented all three algorithms a*-tree, a*-graph and ida* in my code, input values are defined as required in the pdf, output is a whole list, which includs the path to the goal in front and the performance metric score at last.


