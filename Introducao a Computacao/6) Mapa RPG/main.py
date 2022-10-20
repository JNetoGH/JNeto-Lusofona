positions = ["a", "b", "c"]

def print_map():
    print("MAPA\n|", end="")
    for pos in positions:
        print(f" {pos}", end=" |")
    print()


class Player:
    def __init__(self, initial_pos):
        self.currentPos = initial_pos
        print("initial ", end="")
        self.print_current_pos()

    def move(self, move_code):
        print("You tried to move: " + move_code)
        if move_code == "EAST" and self.get_current_pos_as_index() + 1 < len(positions):
            self.currentPos = positions[self.get_current_pos_as_index() + 1]
            joao.print_current_pos()
            return
        elif move_code == "WEST" and self.get_current_pos_as_index() - 1 >= 0:
            self.currentPos = positions[self.get_current_pos_as_index() -1]
            joao.print_current_pos()
            return
        print("NOT VALID")
        joao.print_current_pos()


    def get_current_pos_as_index(self):
        for i in range(0, len(positions)):
            if positions[i] == self.currentPos:
                return i
        return -1

    def print_current_pos(self):
        print("pos: " + self.currentPos + "\n")

print_map()
joao = Player("b")
joao.move("EAST")
joao.move("EAST")
joao.move("WEST")
joao.move("WEST")
joao.move("WEST")

