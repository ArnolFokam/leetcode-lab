#stack #string #backtracking

 - We are asked to create valid combinations of parantheses given n pairs of parantheses
- Here are properties of a valid combination
	- It should always start with '('
	- the number of open parentheses must always be greater than the numberbof closed parantheses.
- There an appriopriate solution to this problem will leverage **backtracking** to branch through solution until it reaches a terminal state the represents the leave of the branch  (one valid combinations)
- So our backtracking algorithm will keep track of number of open and closed parathenses on each node of the branch. This is to determine if it must consider it as a valid combination or branch through different possible combinations:
- In this solution, we have 3 different branch conditions:
	- **If number used open and closed parantheses is equal to 0:** we found a combination (leaf state)
	- **If the number of used open parantheses is less than the available (n):** we can still open so, branch through the addition of another open parentheses
	- **If the number of used closed parantheses is less than the number of used open parantheses (n):** we can still close so, branch through the addition of another closed parantheses
- **Backtracking** can be implemented through **recursion**