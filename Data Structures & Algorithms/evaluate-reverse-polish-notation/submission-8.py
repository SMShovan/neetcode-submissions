class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        symbols = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in symbols:
                second = int(stack[-1])
                stack.pop()
                first = int(stack[-1])
                stack.pop()

                if token == "*":
                    res = first * second
                elif token == "/":
                    res = int (first / second)
                elif token == "+":
                    res = first + second
                elif token == "-":
                    res = first - second
                
                stack.append(res)

            else:
                stack.append(token)
        
        return int(stack[0])


# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         symbols = ["+", "-", "*", "/"]
#         res = 0
#         for token in tokens:
#             if token in symbols:
#                 top2 = int(stack[-1])
#                 top1 = int(stack[-2])
                
#                 if token == symbols[0]:
#                     res = top1 + top2
#                 elif token == symbols[1]:
#                     res = top1 - top2
#                 elif token == symbols[2]:
#                     res = top1 * top2
#                 elif token == symbols[3]:
#                     res = int(top1 / top2)
#                 stack.pop()
#                 stack.pop()
#                 stack.append(res)
#             else:
#                 stack.append(token)
        
#         return int(stack[0])
