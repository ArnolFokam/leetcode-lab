#stack 

- We are given a list of characters in [reverse push notations](http://en.wikipedia.org/wiki/Reverse_Polish_notation)
- According to this notation, an operation is preceeded by two operand.
- The LIFO nature of the stack gives us the possibility to evaluate sub-operations on which outer operations depends.
- Since these sub-operations are enclosed by outer ones, we will need to evaluate and pop them out of the stack to evaluate the outer operations.
- Therefore, we push values into a stack, we know that when we encounter an operator the last two value in the stack will be the operands of the operator
- We can then evaluate the intermediate result and replace the operands with result
- Note: the problem says that 
*The answer and all the intermediate calculations can be represented in a 32-bit integer.*, 
- Therefore, we should cast the result (intermediate and final) without fear.