# Set bit to 1 at required position of any given number
a = 0b1001
bit_position = 2
a = bin(a | (1 << bit_position))
print(a)

# Set bit to 0 at required position of any given number
# clear a bit
a = 0b1001
bit_position = 0
a = bin(a & ~(1 << bit_position))
print(a)

# toggle bits
a = 0b1001
bit_position = 0
a = bin(a ^ (1 << bit_position))
print(a)
