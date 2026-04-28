class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #last in first out (stack), every bracket that goes in needs to come out
        #order they come in have to be order they come out of stack
        for char in s:
            if char == "{" or char == "[" or char == "(" or len(stack) == 0:
                stack.append(char)
                print(stack)
            elif char == "}":
                print("Ending char: " + str(char))
                if stack.pop() != "{":
                    return False
            elif char == "]":
                print("Ending char: " + str(char))
                if stack.pop() != "[":
                    return False
            elif char == ")":
                print("Ending char: " + str(char))
                if stack.pop() != "(":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False