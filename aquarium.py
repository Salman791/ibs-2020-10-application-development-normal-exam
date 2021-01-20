from fish import Fish


class Aquarium:


    def __init__(self):
        # self.bigFish = False
        self.list_of_fish = []

    def add_fish(self, more_fish):
        for Fish in more_fish:
            if isinstance(Fish, Clown_fish):
                self.list_of_fish.append(Fish)
                print("%s is a Clown Fish!"
                      % (Fish.name)

            elif isinstance(Fish, Kong):
                self.list_of_fish.append(Fish)
                print("%s is a Kong Fish!")
                      % (Fish.name)
            else:
                self.list_of_fish.append(Fish)
                print("%s is a Tang Fish!")
                      % (Fish.name)




    def getstatus(self):
            has_short_term_memory_loss = []
            for Fish in self.list_of_fish:
                if Fish.has_short_term_memory_loss:
                    has_short_term_memory_loss.append(Fish.name)

            return getstatus()

    def add_fish(self):
        total_fish = 0

        for Fish in self.list_of_fish:
            total_fish += Fish.weigth

        return total_fish

    def feed(self):
        for Fish in self.list_of_fish:
            Fish.feed()

    def remove_fish(self):
        total_fish = 0

        for Fish in self.list_of_fish:
            total_fish -= Fish.weight
