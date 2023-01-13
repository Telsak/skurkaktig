'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename .............................................. entity.py ]   █
 █   [ Type ............................... entity class for skurkaktigt ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Jan 13, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
from dice import Dice

class Entity:
    def __init__(self, name: str) -> None:
        self._name = name
        self._maxhp = 1
        self._hp = 1
        self._armor_class = 0
        self.Dice = Dice()

    def modifier(self, score: int) -> int:
        return (score - 10) // 2

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp += value

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

class Player(Entity):
    def __init__(self, name, stats, dndclass, race):
        super().__init__(name)
        self._class = dndclass
        self._stats = stats
        self._race = race
        self._hp = self._maxhp = self._class._hitdie + self.modifier(stats['con'])
        self._level = 1
        self._xp = 0
        self._inventory = []
        self._attack = []

    def equip_weapon(self, weapon):
        if len(self._attack) > 0:
            self._inventory.append(self._attack)
            self._attack = weapon
 
    def attack(self, target):
        d20 = self.Dice.roll_die(20)
        modifiers = self.proficient_roll('str', self._attack['type'] in self._class._proficiency['weapons'])
        if d20 != 1 and d20 + modifiers >= target.get_ac():
            print(f'{self._name} hit: {d20 + modifiers} hits {target._name}')
            damage = self.calculate_damage(d20)
            print(f'{self._name} does {damage} to {target._name}')
            target.hp(-damage)
        else:
            if d20 == 1:
                print(f'{self._name}: Critical miss!')
            else:
                print(f'{self._name} hit: {d20 + modifiers} misses {target._name} ac: {target.get_ac()}')
 
    def calculate_damage(self, d20):
        damage = self._attack['damage']
        dmg_die = compile(r"(\d+)d(\d+)\+(\d+)")
        match = dmg_die.match(damage)
        num, sides, add = [int(group) for group in match.groups()]
        damage = self.Dice.roll_dice(num, sides)
        if d20 == 20:
            print(f'{self._name}: Critical hit!')
            damage *= 2 + add
        else:
            damage += add
        return damage
 
    def get_score(self, attribute):
        if attribute in self._race._stats.keys():
            ra = self._race._stats[attribute]
        else:
            ra = 0
        return self._stats[attribute] + ra
 
    def proficient_level(self, level):
        return (level - 1) // 4 + 2
 
    def proficient_roll(self, stat, proficient):
        base, prof = self.Dice.roll_die(20) + self.modifier(self.get_score(stat)), 0
        if proficient:
            prof += self.proficient_level(self._level)
        return base + prof

    def ability_check(self, ability, dc):
        roll = self.proficient_roll(ability, False)
        print(ability, roll, dc)
        return roll >= dc

    def saving_throw(self, stat, dc):
        return self.proficient_roll(stat, stat in self._class._proficiency['saves']) >= dc

    def get_ac(self):
        return 10 + self.modifier(self.get_score('dex'))

    def __str__(self):
        return f'Name: {self._name} \nStr: {self.get_score("str")}\nWeapon: {self._attack}'
