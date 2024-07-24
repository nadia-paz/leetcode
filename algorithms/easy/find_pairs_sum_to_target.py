"""
You are given two lists of integers, arr1 and arr2, and a target integer value, target. 
Your task is to find all pairs of numbers (one from arr1 and one from arr2) 
whose sum equals target.
"""

def find_pairs(arr1, arr2, target):
    # doesn't preserve the order of pairs
    arr1 = set([target-x for x in arr1])
    arr2 = set(arr2)
    complements = arr1.intersection(arr2)
    
    return [(target - x, x) for x in complements]

def find_pairs1(arr1, arr2, target):
    # keeps the order
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)