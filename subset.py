'''
Code generated with the help of ChatGPT

The code was generated after the following promts:

P1: I need an algorithm for a math problem:

    I have a number of different values and want to find out which sum of values (not all values have to be used) is closest to a target value

P2: Can you alter the code you provided to fit the following constraints:

    The sum of integers doesn't have to be equal to the target value, just as close as possible, but never higher

P3: This code returns [5,2,1] as the closets subset and 10 as the closest sum. But [5,2,1] doesn't sum up to 10
'''


def subset_sum_closest(values, target):
    n = len(values)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= values[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - values[i - 1]]

    closest_sum = 0
    for j in range(target, -1, -1):
        if dp[n][j]:
            closest_sum = j
            break

    subset = []
    remaining_sum = closest_sum
    for i in range(n, 0, -1):
        if remaining_sum >= values[i - 1] and dp[i - 1][remaining_sum - values[i - 1]]:
            subset.append(values[i - 1])
            remaining_sum -= values[i - 1]

    return subset, closest_sum
