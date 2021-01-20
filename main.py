from fish import Fish
from aquarium import Aquarium

Clown_fish = Fish("Bob", 12, "Blue", False)
Tang = Fish("Buddy", 13, "Orange", True)
Kong = Fish("Patrick", 14, "Red", False)


aquarium1 = Aquarium()
aquarium1.add_fish([Clown_fish])
aquarium1.add_fish([Tang])
aquarium1.add_fish([Kong])

aquarium2 = Aquarium()
aquarium2.add_fish([Clown_fish, Kong])


print(aquarium1.getstatus())
print(aquarium2.getstatus())
ship1.lastDayOnTheShip()

for i in range(len(aquarium1.list_of_fish)):
    print(aquarium1.list_of_fish[i].status())

for i in range(len(aquarium2.list_of_fish)):
    print(aquarium2.list_of_fish[i].status())