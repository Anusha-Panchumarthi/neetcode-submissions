class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [] 
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                op2, op1 = stk.pop(), stk.pop()
                if token == '+':
                    stk.append(op1 + op2)
                elif token == '-':
                    stk.append(op1 - op2)
                elif token == '*':
                    stk.append(op1 * op2)
                else:
                    stk.append(int(op1 / op2))
            else:
                stk.append(int(token))

        return stk.pop()

