import math

# Slower version using string manipulation
def isValidCard(cardNumber):
    reverse = str(cardNumber)[::-1]
    total = 0
    for pos in range(len(reverse)):
        if not pos%2: total += int(reverse[pos])
        else: total += int(reverse[pos])*2 if int(reverse[pos])<5 else int(reverse[pos])*2-9
    return total%10==0

# Faster version using maths
def mathIsValidCard(cardNumber):
    total = 0
    for n in range(math.ceil(math.log10(cardNumber+1))):
        total += cardNumber%10 if not n%2 else ((cardNumber%10)*2 if cardNumber%10<5 else ((cardNumber%10)*2-9))
        cardNumber//=10
    return total%10==0

# Use string manipulation method
print("VALID" if isValidCard(int(input())) else "INVALID")

# Use math library method (~37% faster!!!)
print("VALID" if mathIsValidCard(int(input())) else "INVALID")
