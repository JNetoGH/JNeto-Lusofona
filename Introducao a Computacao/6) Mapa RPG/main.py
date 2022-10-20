from enum import Enum

positions = [["a", "b", "c"],
             ["d", "e", "f"],
             ["g", "h", "i"]]


def print_map():
    print("MAPA", end="")
    for i in range(0, len(positions)):
        print("\n|", end="")
        for j in range(0, len(positions[0])):
            print(f" {positions[i][j]}", end=" |")
    print()


class AxisOP(Enum):
    Horizontal = 0,
    Vertical = 1

class Player:

    def __init__(self, initial_pos: list[int]):
        self.currentPosAsAxis: list[int] = initial_pos
        print("initial ", end="")
        self.print_current_pos()

    def move(self, move_code):
        print_map()
        print("You tried to move: " + move_code)

        if move_code == "EAST" and self.currentPosAsIndex(AxisOP.Horizontal) + 1 < len(positions[0]):
            self.currentPosAsAxis[1] = self.currentPosAsAxis[1] + 1
            self.print_current_pos()
            return
        elif move_code == "WEST" and self.currentPosAsIndex(AxisOP.Horizontal) - 1 >= 0:
            self.currentPosAsAxis[1] = self.currentPosAsAxis[1] - 1
            self.print_current_pos()
            return
        elif move_code == "SOUTH" and self.currentPosAsIndex(AxisOP.Vertical) + 1 < len(positions):
            self.currentPosAsAxis[0] = self.currentPosAsAxis[0] + 1
            self.print_current_pos()
            return
        elif move_code == "NORTH" and self.currentPosAsIndex(AxisOP.Vertical) -1 >= 0:
            self.currentPosAsAxis[0] = self.currentPosAsAxis[0] - 1
            self.print_current_pos()
            return

        print("NOT VALID")
        self.print_current_pos()

    def currentPosAsIndex(self, axis: AxisOP):
        for x in range(0, len(positions)):
            for y in range(0, len(positions[0])):
                if positions[x][y] == positions[self.currentPosAsAxis[0]][self.currentPosAsAxis[1]]:
                    if axis == AxisOP.Horizontal:
                        return y
                    elif axis == AxisOP.Vertical:
                        return x
        return -1

    def print_current_pos(self):
        print("pos: " + positions[self.currentPosAsAxis[0]][self.currentPosAsAxis[1]])
        print(f"current index: [{self.currentPosAsIndex(AxisOP.Vertical)}][{self.currentPosAsIndex(AxisOP.Horizontal)}]")
        print()


print_map()
joao = Player([0, 1])  # x, y

while True:
    value = input("choose a direction: ").upper()
    joao.move(value)


