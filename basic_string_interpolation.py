# Finish the uefaEuro2016() function so it return string just like in the examples below:

# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."


def uefa_euro_2016(teams, scores):
    if scores[0] == scores[1]:
        return f'At match {teams[0]} - {teams[1]}, teams played draw'
    else:
        return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!' if scores[0] > scores[1] else f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'



print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))




# def uefa_euro_2016(teams, scores):
#     return f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"
# 5 similar code variations are grouped with this one
# Show Variations
# def uefa_euro_2016(teams, scores):
#     if scores[0] == scores[1]:
#         return f'At match {teams[0]} - {teams[1]}, teams played draw.'
#     else:
#         return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!' if scores[0] > scores[1] else f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'
# Best Practices35Clever56
#  0 ForkCompare with your solutionLink
# bidouille

# def uefa_euro_2016(teams, scores):
#     s1, s2 = scores
#     result = "teams played draw." if s1 == s2 else f"{teams[s1 < s2]} won!"
#     return f"At match {teams[0]} - {teams[1]}, {result}"