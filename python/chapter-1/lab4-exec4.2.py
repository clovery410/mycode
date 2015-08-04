def is_vowel(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

def first(word):
    return word[0]

def second(word):
    return word[1]

def rest(word):
    return word[1:]

def remove_vowels(word):
    """
    >>> remove_vowels("hi my name is mark")
    'h my nm s mrk'
    >>> remove_vowels("aeiou")
    ''
    >>> remove_vowels("is y a vowel?")
    's y  vwl?'
    """
    if len(word) <= 1:
        if is_vowel(word):
            return ''
        return word
    elif is_vowel(first(word)):
        return remove_vowels(rest(word))
    return first(word) + remove_vowels(rest(word))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
