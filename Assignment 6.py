# Top-Down Approach
def knapsack(weights, values, n, capacity, memo):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # Check stored answer
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If item is too heavy
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack(
            weights, values, n - 1, capacity, memo
        )
    else:
        # Include item
        include = values[n - 1] + knapsack(
            weights, values, n - 1,
            capacity - weights[n - 1], memo
        )

        # Exclude item
        exclude = knapsack(
            weights, values, n - 1, capacity, memo
        )

        # Store maximum
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# Input
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5
n = len(weights)

# Create memo table
memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

# Find Top-Down result
top_down = knapsack(weights, values, n, capacity, memo)

print("Top-Down Maximum Value:", top_down)


# Bottom-Up Approach

# Create DP table
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

# Fill the table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        # Check if item fits
        if weights[i - 1] <= w:

            # Take item
            take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            # Don't take item
            not_take = dp[i - 1][w]

            # Store maximum
            dp[i][w] = max(take, not_take)

        else:
            # Item does not fit
            dp[i][w] = dp[i - 1][w]


# Find Bottom-Up result
bottom_up = dp[n][capacity]

print("Bottom-Up Maximum Value:", bottom_up)
