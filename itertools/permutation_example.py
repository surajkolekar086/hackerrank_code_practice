from itertools import permutations

s = input().split()  # Example input: 'HACK 2'
word = s[0]
k = int(s[1])         # Convert the second input to integer

# Sort to get lexicographic order if needed
perm = permutations(sorted(word), k)

# Print each permutation as a joined string
for p in perm:
    print(''.join(p))

#Note; input().split() will return a list of strings split by space.

"""
Input:
    HACK 2
Output:
    AC
    AH
    AK
    CA
    CH
    CK
    HA
    HC
    HK
    KA
    KC
    KH


"""