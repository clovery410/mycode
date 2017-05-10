"""
Given a string, write a funciton to check if it is a permutation of a palindrome
"""
#idea: basically, this question can be done by hashmap, just record each charaters' count, check whether there is at most one odd counts.
#but for this quesiton, we can also use bit manipulation to do it. Since we only need to know how many odd counts, no need to know the exact counts, so use 1 bit to toggle when a character appears, finally, check whether the binay number is 0 or whether there is only one bit of '1' in binay number.

def palindrome_permutation(s):
    bitVector = 0
    for c in s:
        idx = 1 << (ord(c) - ord('a'))
        if bitVector & idx == 0:
            bitVector |= idx
        else:
            bitVector &= ~idx
    return bitVector == 0 or (bitVector & (bitVector-1) == 0)

if __name__ == "__main__":
    print palindrome_permutation("charch")
