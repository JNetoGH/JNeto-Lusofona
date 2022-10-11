from core.character import Character
from core.squad import Squad

from enum import Enum


class PhaseState(Enum):
    ACTIVE = 0
    INITIATIVE = 1


class RoundWinner(Enum):
    UNDEFINED = 0
    PLAYER = 1
    ENEMY = 2


class Round:
    playerSquad: Squad
    enemySquad: Squad
    _currentPhaseState: PhaseState
    _roundWinner: RoundWinner

    def __init__(self, player_squad: Squad, enemy_squad: Squad):
        self.playerSquad = player_squad
        self.enemySquad = enemy_squad
        self.set_current_phase_state(PhaseState.INITIATIVE)
        self._roundWinner = RoundWinner.UNDEFINED

    def set_current_phase_state(self, phase_state: PhaseState):
        self._currentPhaseState = phase_state

    def get_current_phase_state(self) -> PhaseState:
        return self._currentPhaseState

    def get_round_winner(self) -> RoundWinner:

        are_all_player_chars_dead = True
        are_all_enemy_chars_dead = True

        for enemy_char in self.enemySquad.characterList:
            if enemy_char.is_alive():
                are_all_enemy_chars_dead = False

        for player_char in self.playerSquad.characterList:
            if player_char.is_alive():
                are_all_player_chars_dead = False

        if are_all_enemy_chars_dead:
            self._roundWinner = RoundWinner.PLAYER
        elif are_all_player_chars_dead:
            self._roundWinner = RoundWinner.ENEMY

        return self._roundWinner


squadPlayer = Squad([Character("JNeto", 0, 10, 10, 10, 10), Character("Dani", 0, 10, 10, 10, 10)])
squadEnemy = Squad([Character("Bilu", 10, 10, 10, 10, 10), Character("Teteia", 10, 10, 10, 10, 10)])


def draw_separator():
    print("\n" + "=" * 20 + "\n")


ronda: Round = Round(squadPlayer, squadEnemy)
draw_separator()
print("Player Squad \n\n" + ronda.playerSquad.to_string())
draw_separator()
print("Enemy  Squad \n\n" + ronda.enemySquad.to_string())
draw_separator()
print(ronda.get_current_phase_state().name)
print("Round winner " + ronda.get_round_winner().name)
