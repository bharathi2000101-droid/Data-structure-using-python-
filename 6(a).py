class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op in ('^'):
        return 3
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    postfix = []

    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char == ' ':
            continue

        if char.isalnum():
            postfix.append(char)

        elif char in ('(', '[', '{'):
            stack.push(char)
        elif char in (')', ']', '}'):
            target_open = matching_bracket[char]
            while not stack.is_empty() and stack.peek() != target_open:
                postfix.append(stack.pop())
            if not stack.is_empty():
                stack.pop()

        else:
            while (not stack.is_empty() and 
                   stack.peek() not in ('(', '[', '{') and 
                   precedence(stack.peek()) >= precedence(char)):
                postfix.append(stack.pop())
            
            stack.push(char)
          
    while not stack.is_empty():
        postfix.append(stack.pop())

    return "".join(postfix)


if __name__ == "__main__":
    test_expressions = [
        "A + B * C",
        "( A + B ) * C",
        "X + Y - Z",
        "A + ( B * C - ( D / E ^ F ) * G ) * H"
    ]

    for expr in test_expressions:
        result = infix_to_postfix(expr)
        print(f"Infix : {expr}")
        print(f"Postfix : {result}")
        print("-" * 35)

