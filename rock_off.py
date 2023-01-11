# Alice and Bob have participated to a Rock Off with their bands. A jury of true metalheads rates the two challenges, awarding points to the bands on a scale from 1 to 50 for three categories: Song Heaviness, Originality, and Members' outfits.

# For each one of these 3 categories they are going to be awarded one point, should they get a better judgement from the jury. No point is awarded in case of an equal vote.

# You are going to receive two arrays, containing first the score of Alice's band and then those of Bob's. Your task is to find their total score by comparing them in a single line.

# Example:

# Alice's band plays a Nirvana inspired grunge and has been rated  20 for Heaviness,  32 for Originality and only  18 for Outfits. Bob listens to Slayer and has gotten a good  48 for Heaviness,  25 for Originality and a rather honest  40 for Outfits.

# The total score should be followed by a colon : and by one of the following quotes: if Alice's band wins: Alice made "Kurt" proud! if Bob's band wins: Bob made "Jeff" proud! if they end up with a draw: that looks like a "draw"! Rock on!

# The solution to the example above should therefore appear like  '1, 2: Bob made "Jeff" proud!'.
import unittest

def solve(a, b):
    a_score = 0
    b_score = 0
    for indx, score in enumerate(a):
        if score > b[indx]:
            a_score += 1
        elif score < b[indx]:
            b_score += 1
        
    if a_score == b_score:
        return f'{a_score}, {b_score}: that looks like a "draw"! Rock on!'
    
    if a_score > b_score:
        return f'{a_score}, {b_score}: Alice made "Kurt" proud!'

    if a_score < b_score:
        return f'{a_score}, {b_score}: Bob made "Jeff" proud!'



print(solve([47, 7, 2], [47, 7, 2]))
print(solve([47, 49, 22], [26, 47, 12]))
# test.assert_equals(solve([25, 50, 22], [34, 49, 50]),'1, 2: Bob made "Jeff" proud!')


# def solve(a, b):
#     alice = sum(i > j for i, j in zip(a, b))
#     bob = sum(j > i for i, j in zip(a, b))
    
#     if alice == bob:
#         words = 'that looks like a "draw"! Rock on!'
#     elif alice > bob:
#         words = 'Alice made "Kurt" proud!'
#     else:
#         words = 'Bob made "Jeff" proud!'
    
#     return '{}, {}: {}'.format(alice, bob, words) 
# Best Practices6Clever2
#  0 ForkCompare with your solutionLink
# crataegus

# def solve(a, b):
#     s, n = 0, 0
#     for x,y in zip(a, b):
#         if x>y: n+=1
#         elif x<y: s+=1
#     if s!=n:
#         return f'{n}, {s}: {"Alice" if s<n else "Bob"} made "{"Kurt" if s<n else "Jeff"}" proud!'
#     return f'{n}, {s}: that looks like a "draw"! Rock on!'