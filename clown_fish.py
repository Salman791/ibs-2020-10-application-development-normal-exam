from fish import Fish

class Clown_fish(Fish):

    def feed(self):
        self.weight += 1
        self.color += 1


    def has_short_term_memory_loss(self):
        self.has_short_term_memory_loss() = False