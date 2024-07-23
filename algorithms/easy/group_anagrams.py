def group_anagrams(list_of_strings):
    # create a dictionary to hold words with the same letters
    hm = {}

    for word in list_of_strings:
        # turn words into lists of letters
        letters = list(word)
        # sort letters
        letters.sort()
        # create a tuple from sorted letters
        key = tuple(letters)
        # use a tuple as a key in the dictionary
        if key in hm:
            hm[key].append(word)
        else:
            hm[key] = [word]
    # create a list of lists for words with the same letters
    strings = []
    for key in hm:
        strings.append(hm[key])
    return strings

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""