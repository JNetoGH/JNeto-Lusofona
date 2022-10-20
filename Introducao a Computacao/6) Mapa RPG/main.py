map = [["a", "b", "c"],
       ["d", "e", "f"],
       ["g", "h", "i"]]


def print_map():
    print("MAPA", end="")
    for i in range(0, len(map)):
        print("\n|", end="")
        for j in range(0, len(map[0])):
            print(f" {map[i][j]}", end=" |")
    print()


class Axis:
    HORIZONTAL: int = 1
    VERTICAL: int = 0

class Player:

    def __init__(self, initial_pos: list[int]):
        self.pos: list[int] = initial_pos
        print("initial ", end="")
        self.print_pos_status()

    def move(self, code):
        print_map()
        print("You tried to move: " + code)

        if code == "EAST" and self.pos[Axis.HORIZONTAL] + 1 < len(map[0]):
            self.pos[Axis.HORIZONTAL] += 1
            self.print_pos_status()
            return
        elif code == "WEST" and self.pos[1] - 1 >= 0:
            self.pos[Axis.HORIZONTAL] -= 1
            self.print_pos_status()
            return
        elif code == "SOUTH" and self.pos[Axis.VERTICAL] + 1 < len(map):
            self.pos[Axis.VERTICAL] += 1
            self.print_pos_status()
            return
        elif code == "NORTH" and self.pos[Axis.VERTICAL] - 1 >= 0:
            self.pos[Axis.VERTICAL] -= 1
            self.print_pos_status()
            return
        print("NOT VALID")

    def print_pos_status(self):
        print("pos: " + map[self.pos[Axis.VERTICAL]][self.pos[Axis.HORIZONTAL]])
        print(f"current index: [{self.pos[Axis.VERTICAL]}][{self.pos[Axis.HORIZONTAL]}]\n")


print_map()
joao = Player([0, 1])  # x, y
while True:
    value = input("choose a direction: ").upper()
    joao.move(value)
