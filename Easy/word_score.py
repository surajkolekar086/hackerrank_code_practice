
"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Consider that vowels in the alphabet are a, e, i, o, u and y.

Function score_words takes a list of lowercase words as an argument and returns a score as follows:

The score of a single word is  if the word contains an even number of vowels. Otherwise, the score of this word is . 
The score for the whole list of words is the sum of scores of all words in the list.

Debug the given function score_words such that it returns a correct score.

Your function will be tested on several cases by the locked template code.
not
"""

"""
Input: 
2
hacker book

Sample Output:
4

Sample Input 2:
3
programming is awesome

Sample Ouput: 
4 --> bcs proggraming has odd vowel so will get score 1 same for "is" and "awesome" will score 2 so sum of all --> 4
"""

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))