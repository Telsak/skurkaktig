'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................. classes.py ]   █
 █   [ Type .......................................... Character classes ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Jan 13, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
class Fighter:
    def __init__(self) -> None:
        self._name = 'Fighter'
        self._level = 1
        self._xp = 0
        self._hitdie = 10
        self._proficiency = {
                'saves': ['str','con'],
                'weapons': ['simple weapons', 'martial weapons'],
                'armor': ['All armor', 'shields'],
                'tools': [],
                'skills': {'Acrobatics': 'dex', 'Perception': 'wis'},
                'style': 'Defense'
                }

    @property
    def get_attacks(self) -> int:
        if 4 < self._level < 11:
            attacks = 2
        elif 10 < self._level < 20:
            attacks = 3
        elif self._level == 20:
            attacks = 4
        return attacks

    def __str__(self) -> str:
        return self._name
