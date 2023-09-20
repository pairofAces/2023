def minNumberOfCoinsForChange(n, denoms):
    # create an array with the max integer value that can be stored
    # for the length of the target input integer
    numOfCoins = [float('inf') for amount in range(n + 1)]
    numOfCoins[0] = 0

    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    
    return numOfCoins[n]


