from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, tokens: List[str]) -> int:
        """evaluates RPN expression

        Args:
            tokens (List[str]): RPN expression

        Returns:
            int: result of the evaluation
        """

        eval_stack = []

        for tok in tokens:

            if tok in ['*', '+', '-', '/']:
                
                op2 = eval_stack.pop()
                op1 = eval_stack.pop()

                if tok == '*':
                    eval_stack.append(int(op1 * op2))
                elif tok == '+':
                    eval_stack.append(int(op1 + op2))
                elif tok == '-':
                    eval_stack.append(int(op1 - op2))
                elif tok == '/':
                    eval_stack.append(int(op1 / op2))
            else:
                eval_stack.append(int(tok))


        return eval_stack[-1]