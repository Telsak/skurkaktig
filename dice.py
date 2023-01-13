'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ dice.py ]   █
 █   [ Type ........................................... dicerolls module ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Jan 13, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
from random import randint

class Dice:
    def roll_die(self, sides: int, adv: bool = False, dis: bool = False) -> int:
        if adv == True:
            rolls = [randint(1, sides) for die in range(2)]
            return max(rolls)
        elif dis == True:
            rolls = [randint(1, sides) for die in range(2)]
            return min(rolls)
        else:
            return randint(1, sides)

    def roll_dice(self, num: int, sides: int) -> int:
        return sum([randint(1, sides) for die in range(num)])
