# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

# Your function also receives a third argument, a string, with the name of the fighter that attacks first.

# Example:

#   declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
#   Lew attacks Harry; Harry now has 3 health.
#   Harry attacks Lew; Lew now has 6 health.
#   Lew attacks Harry; Harry now has 1 health.
#   Harry attacks Lew; Lew now has 2 health.
#   Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    #round 1 if 1st_att = fighter1 then fighter2.health - fighter1.dmg else the reverse THEN if hurt fighter still has left flip attack and checkk health
    health1 = fighter1.health
    health2 = fighter2.health
    while health1 > 0 and health2 > 0:
        # print(fighter1, fighter1.name, fighter1.health, fighter1.damage_per_attack, fighter1.health-fighter2.damage_per_attack)
        if first_attacker == fighter1.name:
            health2 = health2 - fighter1.damage_per_attack
            if health2 <= 0:
                return fighter1.name
            else:
                health1 = health1 - fighter2.damage_per_attack
                if health1 <= 0:
                    return fighter2.name
            
                
        elif first_attacker == fighter2.name:
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            else:
                fighter2.health = fighter2.health - fighter1.damage_per_attack
                if fighter2.health <= 0:
                    return fighter1.name

print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry")) #, "Harald")
print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")) #lew
print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"))




# def declare_winner(fighter1, fighter2, first_attacker):
#     cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
#     while cur.health > 0:        
#         opp.health -= cur.damage_per_attack
#         cur, opp = opp, cur
#     return opp.name
# 2 similar code variations are grouped with this one
# Show Variations
# Best Practices133Clever227
#  14 ForkCompare with your solutionLink
# cmedina17, Zzzaaaiiikkk

# def declare_winner(fighter1, fighter2, first_attacker):
#     # Code your solution here
#     if(fighter1.name == first_attacker):
#         winner = fight(fighter1,fighter2)
#     elif(fighter2.name == first_attacker):
#         winner = fight(fighter2,fighter1)
#     return winner.name
    
# def fight(attacker,defender):
#     print('defender: ' + defender.name + ' current health: ' + str(defender.health))
#     print('attacker: ' + attacker.name + ' attacks for: ' + str(attacker.damage_per_attack))

#     defender.health = defender.health - attacker.damage_per_attack
#     print(defender.name + ' health after being attacked is: ' + str(defender.health))
    
#     if(defender.health <= 0):
#         print('\r\n')
#         print(defender.name + ' has been defeated')
#         print(attacker.name + ' is the winner!')
#         return attacker
#     else:
#         print('\r\n')
#         return fight(defender,attacker)
# Best Practices52Clever16
#  3 ForkCompare with your solutionLink
# zebulan, Chester2, Ceremonds, gongmingming, Not_tyan

# from math import ceil
# from operator import attrgetter


# def declare_winner(fighter1, fighter2, first_attacker):
#     fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
#     fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
#     if fighter1.turns == fighter2.turns:
#         return first_attacker
#     return max(fighter1, fighter2, key=attrgetter('turns')).name