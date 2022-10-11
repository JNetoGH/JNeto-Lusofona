from core.character import Character
from core.squad import Squad

import random
from enum import Enum


class RoundPhase(Enum):
    ACTIVE = 0
    INITIATIVE = 1


class BattleWinner(Enum):
    UNDEFINED = 0
    PLAYER = 1
    ENEMY = 2


class Battle:

    playerSquad: Squad
    enemySquad: Squad

    # holds the current Turn phase (active or initiative)
    _currentRoundPhase: RoundPhase
    # holds the living characters in order to the action phase
    _actionPhaseOrder: list[Character] = []
    # holds a winner(player or enemy) or undefined value
    _battleWinner: BattleWinner

    def __init__(self, player_squad: Squad, enemy_squad: Squad):
        self.playerSquad = player_squad
        self.enemySquad = enemy_squad
        self.set_current_round_phase(RoundPhase.INITIATIVE)
        self._battleWinner = BattleWinner.UNDEFINED

    def set_current_round_phase(self, phase_state: RoundPhase):
        self._currentRoundPhase = phase_state

    def get_current_round_phase(self) -> RoundPhase:
        return self._currentRoundPhase

    def get_battle_winner(self) -> BattleWinner:

        are_all_player_chars_dead = True
        are_all_enemy_chars_dead = True

        # checks if all characters in each one of the squads are dead or not
        for enemy_char in self.enemySquad.characterList:
            if enemy_char.get_if_is_alive_and_update_char_action_phase_order():
                are_all_enemy_chars_dead = False
        for player_char in self.playerSquad.characterList:
            if player_char.get_if_is_alive_and_update_char_action_phase_order():
                are_all_player_chars_dead = False

        # if one of the two squads are completely dead, a winner is found
        if are_all_enemy_chars_dead:
            self._battleWinner = BattleWinner.PLAYER
        elif are_all_player_chars_dead:
            self._battleWinner = BattleWinner.ENEMY

        # returns the winner based on the BattleWinner enum
        return self._battleWinner

    # basically checks if the character is alive, then set his/her action phase order
    # then, adds the character to the _actionPhaseOrder, anf it sorts the list according to the action phase order
    def generate_action_phase_order_for_characters(self):

        for player_char in self.playerSquad.characterList:
            if player_char.get_if_is_alive_and_update_char_action_phase_order():
                d20: int = Battle.roll_dice(0, 20)
                player_char.currentActionPhaseOrder = player_char.initiative + d20
                self._actionPhaseOrder.append(player_char)

        for enemy_char in self.enemySquad.characterList:
            if enemy_char.get_if_is_alive_and_update_char_action_phase_order():
                d20: int = Battle.roll_dice(0, 20)
                enemy_char.currentActionPhaseOrder = enemy_char.initiative + d20
                self._actionPhaseOrder.append(enemy_char)

    @staticmethod
    def roll_dice(min_range: int, max_range: int) -> int:
        return random.randint(min_range, max_range)


squadPlayer = Squad([Character("JNeto", 5, 10, 10, 10, 11), Character("Dani", 0, 10, 10, 10, 10)])
squadEnemy = Squad([Character("Bilu", 10, 10, 10, 10, 10), Character("Teteia", 10, 10, 10, 10, 12)])


def draw_separator():
    print("\n" + "=" * 20 + "\n")


battle1: Battle = Battle(squadPlayer, squadEnemy)
battle1.generate_action_phase_order_for_characters()

draw_separator()
print("Player Squad \n\n" + battle1.playerSquad.to_string())
draw_separator()
print("Enemy  Squad \n\n" + battle1.enemySquad.to_string())
draw_separator()

print(battle1.get_current_round_phase().name)
print("Battle winner " + battle1.get_battle_winner().name)
