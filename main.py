'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ main.py ]   █
 █   [ Type .................................. main file for skurkaktigt ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Jan 13, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
from dice import Dice
from entity import Entity, Player, Monster
from classes import Fighter
from races import Dwarf

def main() -> None:
    stats = {'str':15,'dex':13,'con':14,'int':10,'wis':12,'cha':8}
    me = Player('Simon', stats, Fighter(), Dwarf('Mountain'))
    print(me)
    attack = {'type': 'Melee', 'to_hit': 3, 'damage': '1d6+1'}
    enemy = Monster('Giant Crab', 'Medium', 15, 13, 1/8, {'str':13,'dex':15,'con':11,'int':1,'wis':9,'cha':3}, attack)
    weapon = {'type': 'simple weapons', 'name': 'Longsword', 'damage': '1d8+0'}
    me.equip_weapon(weapon)
    while True:
        me.attack(enemy)
        if enemy.is_alive:
            enemy.attack(me)
            if not me.is_alive:
                print(f'{me._name} has died!')
                break
        else:
            print(f'The {enemy._name} is dead!')
            break
        input('Next round')

if __name__ == "__main__":
    main()
