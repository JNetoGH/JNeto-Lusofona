from utilities.string_builder import StringBuilder


class Character:

    def __init__(self, name: str, hp: int, mana: int, armor, weapon_dmg: int, initiative: int):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.weapon_dmg = weapon_dmg
        self.initiative = initiative

    def to_string(self) -> str:
        str_builder: StringBuilder = StringBuilder()
        str_builder.append_line("Name: " + str(self.name))
        str_builder.append("HP: " + str(self.hp))
        str_builder.append(" | Mana: " + str(self.mana))
        str_builder.append(" | Armor: " + str(self.armor))
        str_builder.append(" | Weapon Dmg: " + str(self.weapon_dmg))
        str_builder.append(" | Initiative: " + str(self.initiative))
        return str_builder.to_string()

    def is_alive(self):
        return self.hp > 0


