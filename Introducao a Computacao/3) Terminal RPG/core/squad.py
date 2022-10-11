from core.character import *
from utilities.string_builder import StringBuilder


class Squad:

    characterList: list[Character]

    def __init__(self, characters_list: list[Character]):
        self.characterList = characters_list

    def to_string(self) -> str:

        string_builder = StringBuilder()

        for i in range(0, len(self.characterList)):
            if i == len(self.characterList) - 1:
                string_builder.append("[" + str(i) + "] " + self.characterList[i].to_string())
            else:
                string_builder.append_line("[" + str(i) + "] " + self.characterList[i].to_string())
                string_builder.append_line("")

        return string_builder.to_string()
