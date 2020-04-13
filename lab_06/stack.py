class stack_class():

    stack = list()

    def __init__(self, element):
        self.push(element)

    def pop(self):
        return self.stack.pop()

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return not len(self.stack)
