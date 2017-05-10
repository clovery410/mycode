class Queue(object):
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def push(self, x):
        self.inputs.append(x)

    def pop(self):
        if not self.outputs:
            self.transferData()
        self.outputs.pop()

    def peek(self):
        if not self.outputs:
            self.transferData()
        return self.outputs[-1]

    def empty(self):
        return len(self.inputs) == 0 and len(self.outputs) == 0

    def transferData(self):
        inputs, outputs = self.inputs, self.outputs
        while inputs:
            outputs.append(inputs.pop())
