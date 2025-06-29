"""
Problem: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
    Both players are given the same string, .
    Both players have to make substrings using the letters of the string .
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings
"""


"""
Key Observations:
    We need to generate all possible substrings of the input string.

    But we don’t need to actually list them out.

    Each substring starting at position i contributes len(string) - i substrings.

    If the character at position i is a vowel, Kevin gets len(string) - i points.

    Otherwise, Stuart gets those points.
"""
def minion_game(s):
    s = s.upper()
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    str_len = len(s)

    for i in range(str_len):
        print(i)
        if s[i] in vowels:
            print(s[i])
            kevin_score += str_len - i
        else:
            print(s[i])
            stuart_score += str_len - i
        
    if kevin_score > stuart_score:
        print("kevin: ", kevin_score)
    elif kevin_score < stuart_score:
        print("stuart: ", stuart_score)
    else:
        print("Draw..")

s = "BANANA"
minion_game(s)