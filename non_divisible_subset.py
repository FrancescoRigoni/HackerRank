#!/bin/python3

"""
Link: https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""


def nonDivisibleSubset(k, arr):
    remainders_counts = dict()

    # Compute all the remainders when dividing each element by K.
    # Store results in a dictionary (key=remainder, value=how many elements have this remainder)
    for a in arr:
        remainder = a % k
        if remainder not in remainders_counts:
            remainders_counts[remainder] = 1
        else:
            remainders_counts[remainder] += 1

    # We can only keep one element with value K in the subset, adding two Ks
    # creates a multiple of K.
    if 0 in remainders_counts:
        remainders_counts[0] = 1

    # Now for each remainder value, remove all the complementaries which appear less often.
    # For each entry in the dictionary look at the entry for (K-entry) and remove the entry
    # which has smaller value.
    for i in range(1, k):
        complementary = k - i
        # If one of the two is not in the dictionary we don't have to remove anything.
        if i in remainders_counts and complementary in remainders_counts:
            if complementary == i:
                # If the remainder is exactly half K then we will get
                # a multiple of K when adding the two numbers, therefore
                # we can only have one of those in the subset.
                remainders_counts[i] = 1
            else:
                if remainders_counts[complementary] > remainders_counts[i]:
                    remainders_counts[i] = 0
                else:
                    remainders_counts[complementary] = 0

    # Now just count the elements.
    subset_len = 0
    for i in remainders_counts:
        subset_len += remainders_counts[i]

    return subset_len


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)