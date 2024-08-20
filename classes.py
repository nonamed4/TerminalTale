from ast import Dict


class player:
    name = "name"
    def __init__(self, maxhp : int, hp : int, damage : int, name : str):
        """Create a player with maxhp, hp, damage and a name. (Bonus points for names from ut and dt)"""
        self.maxhp = maxhp
        self.hp = hp
        if hp > maxhp or hp < 1:
            self.hp = maxhp
        self.damage = damage
        self.name = name
    def __str__(self):
        return f"{self.name}"
"""
I thought it would be easier to use a custom type.
class double_list:
    \"\"\"Also known as a dict.\"\"\"
    l : list
    r : list
    def __init__(self, l : list, r : list):
        self.l = l
        self.r = r

    @classmethod
    def from_dict(cls, d: dict):
        for i in range(0, len(d)):
"""
            

