#!/usr/bin/env python3

import sys

"""
Given a string s, convert it to a palindrome by adding characters it.
Find the shortest palindrome you can find by performing this transformation.
If there are multiple shortest palindromes, use the lexicographically first one.
"""

def shortestPalindrome(word):
    indexA = 0;
    indexB = len(word) - 1
    palindromeStart = ""
    palindromeEnd = ""

    while indexA <= indexB:
        letter1 = word[indexA]
        letter2 = word[indexB]
        if indexA == indexB:
            palindromeStart = palindromeStart + letter1
            indexA += 1
        elif letter1 == letter2:
            palindromeStart = palindromeStart + letter1
            palindromeEnd = letter2 + palindromeEnd
            indexA += 1
            indexB -= 1
        elif letter1 < letter2:
            palindromeStart = palindromeStart + letter1
            palindromeEnd = letter1 + palindromeEnd
            indexA += 1
        else:
            palindromeEnd = letter2 + palindromeEnd
            palindromeStart = palindromeStart + letter2
            indexB -= 1

    return palindromeStart + palindromeEnd

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please give a single word to be converted into a palindrome")
    else:
        print(shortestPalindrome(sys.argv[1]))
