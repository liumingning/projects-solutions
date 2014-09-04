def vowels_counter(string):
    '''
    Enter a string and the program counts the number of vowels in the text.
    For added complexity have it report a sum of each vowel found.
    >>> vowels_counter('alexandre')
    4
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = len(map(lambda x: True if x in vowels, list(string)))
    return total
