class Fish:

    def __init__(self, name, weight, color, has_short_term_memory_loss):
        self.name = name
        self.weight = weight
        self.color = color
        self.has_short_term_memory_loss = has_short_term_memory_loss

    def feed(self):
        self.weight += 1


    def status(self):
        if self.has_short_term_memory_loss:
            return (True)
        else:
            return (False)