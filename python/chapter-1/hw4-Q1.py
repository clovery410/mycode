def pig_latin_original(w, i=0):
    """Return the Pig Latin equivalent of a lowercase English word w.

    >>> pig_latin('pun')
    'unpay'
    >>> pig_latin('sphynx')
    'sphynxay'
    """
    if starts_with_a_vowel(w) or i == len(w):
        return w + 'ay'
    else:
        return pig_latin_original(rest(w) + first(w), i + 1)

def pig_latin(w):
    return pig_latin_original(w, i=0)

def first(s):
    """Return the first character of a string."""
    return s[0]

def rest(s):
    """Return all but the first character of a string."""
    return s[1:]

def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    c = first(w)
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

