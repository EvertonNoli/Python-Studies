word = str(input("Type a word: ")).upper().strip()
vowel = []

for w in word:
    if w in "AEIOU":
        vowel.append(w)

single_vowels = set(vowel)
print(vowel)
print(single_vowels)
print("Total vowels: ",len(vowel))
print("Total single vowels: ",len(single_vowels))