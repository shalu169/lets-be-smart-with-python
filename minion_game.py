'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.
'''

from itertools import combinations
test_str = input()

# printing original string
print("The original string is : " + str(test_str))

# Get all substrings of string
# Using itertools.combinations()
res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r=2)]
res=list(set(res))
print(type(res))
st = 0
ke = 0
'''for a in res:
    if a[0] in {'a','e','i','o','u','A','E','I','O','U'}:
        p = test_str.count(a)
        ke = ke + p
    else:
        q = test_str.count(a)
        st = st + q
print(ke, st)
'''
for c in res:
    count = 0
    for i in range(len(test_str)-len(c)+1):
        if test_str[i:len(c)+i] == c:
            count += 1
    if c[0] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
        ke = ke + count
    else:
        st = st + count
print(ke,st)