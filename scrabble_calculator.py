
# Base Scrabble word calculator instructions
# Given the below scoring create a Scrabble word calculator
# that will provide the correct scores dependent on
# the string provided.
#
# Letter Value
# A, E, I, O, U, L, N, R, S, T  = 1
# D, G  = 2
# B, C, M, P =  3
# F, H, V, W, Y  = 4
# K  = 5
# J, X  = 8
# Q, Z  = 10

def score_calculator():

    def __init__(self):
        self.score_table = {
                **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
                **dict.fromkeys(['D', 'G'], 2),
                **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
                **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
                **dict.fromkeys(['K'], 5),
                **dict.fromkeys(['J', 'X'], 8),
                **dict.fromkeys(['Q', 'Z'], 10),
                }

    def score_word(self, word):
        if not isinstance(word, str):
            print('Not a word.')
            return
        total = 0
        for letter in word:
            value = self.score_table.get(letter.upper())
            total = total+value if value else total
        return total




