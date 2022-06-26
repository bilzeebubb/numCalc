alphabet = {
    "A": 1, "J": 1, "S": 1,
    "B": 2, "K": 2, "T": 2,
    "C": 3, "L": 3, "U": 3,
    "D": 4, "M": 4, "V": 4,
    "E": 5, "N": 5, "W": 5,
    "F": 6, "O": 6, "X": 6,
    "G": 7, "P": 7, "Y": 7,
    "H": 8, "Q": 8, "Z": 8,
    "I": 9, "R": 9, " ": 0
}

consonant = {
    "J": 1, "S": 1,
    "B": 2, "K": 2, "T": 2,
    "C": 3, "L": 3,
    "D": 4, "M": 4, "V": 4,
    "N": 5, "W": 5,
    "F": 6, "X": 6,
    "G": 7, "P": 7, "Y": 7,
    "H": 8, "Q": 8, "Z": 8,
    "R": 9, " ": 0
}

vowel = {
    "A": 1,
    "U": 3,
    "E": 5,
    "O": 6,
    "I": 9,
    " ": 0

}

# numerology method
print("This numerology calculator uses the Pythagorean Method. \n")

# destiny number
destiny = input("Enter Full Name For Destiny Number: ")


# list comprehension
# returns total of digits in string
def digitSum(n):
    return sum(int(digit) for digit in str(n))


# adds total of each letter/digit in alphabet as digits
def destinyNumber(destiny):
    total = 0
    for letter in destiny.upper():
        total = digitSum(total + alphabet[letter])
    return total


# prints total of letters as digit
print(destinyNumber(destiny))

# soul number
soul = input("Enter VOWELS of Full Name for Soul Number: ")


# adds total value each vowel in vowel list as digits
def soulNumber(soul):
    total = 0
    for letter in soul.upper():
        total = digitSum(total + vowel[letter])
    return total


# print total of vowels as digit
print(soulNumber(soul))

# personality number
personality = input("Enter CONSONANTS of Full Name for Personality Number: ")


# adds total value of consonants as digits
def personalityNumber(personality):
    total = 0
    for letter in personality.upper():
        total = digitSum(total + consonant[letter])
    return total


# print total of consonants as digit
print(personalityNumber(personality))
