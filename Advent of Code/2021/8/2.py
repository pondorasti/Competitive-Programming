with open('input.txt') as f:
    lines = f.readlines()


patterns = {
    "abefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
    "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9
}

ans = 0
for line in lines:
    keys = {}
    rKeys = {}
    input, output = line.split(" | ")
    words = [[] for _ in range(8)]

    for word in input.split():
        length = len(word)
        words[length].append(word)

    # print(line)
    for word in output.split():
        newWord = ""
        for char in word:
            newWord += keys[char]

        newWord = "".join(sorted(newWord))
        number = number * 10 + patterns[newWord]

    ans += number
print(ans)


# Junk

# # Stage 1 - a
# one = set(words[2][0])
# seven = set(words[3][0])
# diff = seven.difference(one)
# diff = diff.pop()
# keys[diff] = "a"
# rKeys["a"] = diff

# # Stage 2 - g
# fourSeven = set.union(set(words[4][0]), set(words[3][0]))
# nine = set()
# strNine = ""
# for word in words[6]:
#     diff = set(word).difference(fourSeven)
#     if len(diff) == 1:
#         diff = diff.pop()
#         keys[diff] = "g"
#         rKeys["g"] = diff
#         nine = set(word)
#         strNine = word

# # Stage 3 - d
# exOne = set(words[2][0])
# exOne.add(rKeys["a"])
# exOne.add(rKeys["g"])
# three = set()
# for word in words[5]:
#     diff = set(word).difference(exOne)
#     if len(diff) == 1:
#         diff = diff.pop()
#         keys[diff] = "d"
#         rKeys["d"] = diff
#         three = set(word)

# # Stage 4 - c
# four = set(words[4][0])
# for word in words[5]:
#     diff = nine.difference(set(word))
#     if len(diff) == 2:  # 2
#         diff = one.difference(diff)
#         diff = diff.pop()
#         keys[diff] = "c"
#         rKeys["c"] = diff

# # Stage 5 - f
# diff = three.difference(set(keys.keys()))
# diff = diff.pop()
# keys[diff] = "f"
# rKeys["f"] = diff

# # Stage 6 - b
# diff = four.difference(set([rKeys["c"], rKeys["d"], rKeys["f"]]))
# diff = diff.pop()
# keys[diff] = "b"
# rKeys["b"] = diff

# # Stage 7 - e
# eight = set(words[7][0])
# diff = eight.difference(set(keys.keys()))
# diff = diff.pop()
# keys[diff] = "e"
# rKeys["e"] = diff

# number = 0
# print(keys)
