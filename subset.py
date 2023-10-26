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


# Example usage
values = [3, 6, 4, 2, 5]
target = 1
subset, closest_sum = subset_sum_closest(values, target)
print("Closest subset:", subset)
print("Sum of closest subset:", closest_sum)
