"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:
spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
spinWords("This is a test") => "This is a test"
spinWords("This is another test") => "This is rehtona test"

"""
import re

def spin_Words(sentence):
    """words = [word if len(list(word))<5 else ''.join(list(word)[::-1]) for word in sentence.split()]
    return ' '.join(words)"""

    return re.sub(r"\w{7,}", lambda w: w.group(0)[::-1], sentence)

print(spin_Words("Hey fellow warriors"))