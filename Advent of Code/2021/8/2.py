with open('input.txt') as f:
    lines = f.readlines()


patterns = {
    "abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
    "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9
}
permutations = []
defaultPermutation = "abcdefg"


def getPermutations(permutation):
    if len(permutation) == 7:
        keys = {}
        for index, char in enumerate(permutation):
            keys[defaultPermutation[index]] = char
        permutations.append(keys)
        return

    for char in defaultPermutation:
        if char not in permutation:
            getPermutations(permutation + [char])


def sortWord(word):
    return "".join(sorted(word))


def convert(word, keys):
    newWord = ""
    for char in word:
        newWord += keys[char]

    newWord = sortWord(newWord)
    if newWord in patterns:
        return patterns[newWord]
    return None


getPermutations([])
ans = 0
for line in lines:
    input, output = line.split(" | ")

    # Parse Input
    words = []
    for word in input.split():
        length = len(word)
        sortedWord = sortWord(word)
        words.append(sortedWord)

    # Find Permutation
    correctKeys = {}
    for keys in permutations:
        isValid = True
        for word in words:
            number = convert(word, keys)
            if number is None:
                isValid = False
                break

        if isValid:
            correctKeys = keys
            break

    # Parse Output
    number = 0
    for word in output.split():
        digit = convert(word, correctKeys)
        number = number * 10 + digit

    # Update Ans
    ans += number

print(ans)
