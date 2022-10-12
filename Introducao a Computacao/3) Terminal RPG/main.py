from core.character import Character
from core.squad import Squad
from utilities import jneto_utility_methods
from utilities.jneto_string_builder import StringBuilder
from enum import Enum


class RoundPhase(Enum):
    ACTIVE = 0
    INITIATIVE = 1


class BattleWinner(Enum):
    UNDEFINED = 0
    PLAYER = 1
    ENEMY = 2


class InitiativePhase:
    pass

#todo IMPLEMENTAR a sgunda fase de aCTION
#todo solve draw cases in Action Order
class Round:

    _playerSquad: Squad
    _enemySquad: Squad
    # holds the current Turn phase (active or initiative)
    _currentRoundPhase: RoundPhase
    # holds the living characters in order to the action phase
    _actionPhaseOrder: list[Character] = []
    # holds a winner(player or enemy) or undefined value
    _battleWinner: BattleWinner = BattleWinner.UNDEFINED

    def __init__(self, player_squad: Squad, enemy_squad: Squad):

        self.playerSquad = player_squad
        self.enemySquad = enemy_squad

        # Inits Initiative phase
        self.set_current_round_phase(RoundPhase.INITIATIVE)
        self.print_initiative_phase_ui_header()
        self.clear_actionPhaseOrder_list()
        self.generate_action_phase_order_for_chars_in_squad_and_add_then_to_action_phase_order_list(self.playerSquad)
        self.generate_action_phase_order_for_chars_in_squad_and_add_then_to_action_phase_order_list(self.enemySquad)
        self.select_sort_actionPhaseOrder_list()
        self.print_initiative_phase_ui_results()

        # Inits Action Phase
        # self.set_current_round_phase(RoundPhase.ACTIVE)
        self.check_if_there_is_a_battle_winner()

    def clear_actionPhaseOrder_list(self):  # clears the action phase order list first, making sure it's empty
        self._actionPhaseOrder = []

    # basically checks if the character is alive, then set his/her currentActionPhaseOrder
    # then, adds the character to the _actionPhaseOrder, anf it sorts the list according to the action phase order
    def generate_action_phase_order_for_chars_in_squad_and_add_then_to_action_phase_order_list(self, squad: Squad):
        for char in squad.get_characterList():
            if char.get_if_is_alive_and_update_char_action_phase_order():
                d20: int = jneto_utility_methods.roll_dice(0, 20)
                char.set_currentActionPhaseOrder(char.initiative + d20)
                self._actionPhaseOrder.append(char)
                print(f"Name: {char.name} | Action Order => Initiative ({char.initiative}) + D20 ({d20})"
                      f" => {char.get_currentActionPhaseOrder()}")

    def select_sort_actionPhaseOrder_list(self):
        size = len(self._actionPhaseOrder)
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if self._actionPhaseOrder[i].get_currentActionPhaseOrder() > self._actionPhaseOrder[min_idx].get_currentActionPhaseOrder():
                    min_idx = i
            # put min at the correct position
            (self._actionPhaseOrder[step], self._actionPhaseOrder[min_idx]) = (self._actionPhaseOrder[min_idx], self._actionPhaseOrder[step])

    def print_initiative_phase_ui_header(self):
        jneto_utility_methods.draw_round_separator()
        print("Round phase: " + self.get_current_round_phase().name)
        print()
        print("Generating action order with alive characters:")

    def print_initiative_phase_ui_results(self):
        print()
        print("Action Order:" + jneto_utility_methods.list_to_str(self.get_actionPhaseOrder_list_as_string()))
        jneto_utility_methods.draw_squad_separator()

    def check_if_there_is_a_battle_winner(self) -> BattleWinner:
        are_all_player_chars_dead = True
        are_all_enemy_chars_dead = True
        # checks if all characters in each one of the squads are dead or not
        for enemy_char in self.enemySquad.get_characterList():
            if enemy_char.get_if_is_alive_and_update_char_action_phase_order():
                are_all_enemy_chars_dead = False
        for player_char in self.playerSquad.get_characterList():
            if player_char.get_if_is_alive_and_update_char_action_phase_order():
                are_all_player_chars_dead = False
        # if one of the two squads are completely dead, a winner is found
        if are_all_enemy_chars_dead:
            self._battleWinner = BattleWinner.PLAYER
        elif are_all_player_chars_dead:
            self._battleWinner = BattleWinner.ENEMY
        return self._battleWinner

    def get_current_round_phase(self) -> RoundPhase:
        return self._currentRoundPhase

    def set_current_round_phase(self, phase_state: RoundPhase):
        self._currentRoundPhase = phase_state

    def get_battle_winner(self) -> BattleWinner:
        return self._battleWinner

    def get_actionPhaseOrder_list_as_string(self) -> str:
        str_builder: StringBuilder = StringBuilder()
        for char in self._actionPhaseOrder:
            str_builder.append(" | " + char.name)
        str_builder.append(" | ")
        return str_builder.to_string()


class Battle:

    playerSquad: Squad
    enemySquad: Squad
    currentRound: Round

    # holds a winner(player or enemy) or undefined value
    battleWinner: BattleWinner = BattleWinner.UNDEFINED

    def __init__(self, player_squad: Squad, enemy_squad: Squad):
        self.playerSquad = player_squad
        self.enemySquad = enemy_squad

    def init_new_round(self):
        self.currentRound = Round(self.playerSquad, self.enemySquad)
        self.battleWinner = self.currentRound.get_battle_winner()


squadPlayer = Squad([Character("JNeto", 5, 10, 10, 10, 11), Character("Dani", 0, 10, 10, 10, 10)])
squadEnemy = Squad([Character("Bilu", 10, 10, 10, 10, 10), Character("Teteia", 10, 10, 10, 10, 12)])
battle1: Battle = Battle(squadPlayer, squadEnemy)
battle1.init_new_round()
battle1.init_new_round()

"""
battle1.init_new_round()
jneto_utility_methods.draw_round_separator()
print("Action Order:" + jneto_utility_methods.list_to_str(battle1.currentRound.get_actionPhaseOrder_list_as_string()))
print("Round phase:   " + battle1.currentRound.get_current_round_phase().name)
print("Battle winner: " + battle1.battleWinner.name)

jneto_utility_methods.draw_squad_separator()
print("Player Squad \n\n" + battle1.playerSquad.to_string())
jneto_utility_methods.draw_squad_separator()
print("Enemy  Squad \n\n" + battle1.enemySquad.to_string())
jneto_utility_methods.draw_squad_separator()
"""

