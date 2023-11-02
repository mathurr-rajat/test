# Check perticular bit in number is 0 or 1(set)
def isKthBitSet(n, k):
    if n & (1 << k):
        print("SET")
    else:
        print("NOT SET")


# Driver code
if __name__ == "__main__":
    n = 0b10001111
    # n=8
    k = 4

    # Function call
    isKthBitSet(n, k)
