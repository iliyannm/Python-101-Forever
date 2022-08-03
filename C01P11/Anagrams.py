def anagrams(word1, word2):
    first_word = word1.replace(' ', '').lower()
    second_word = word2.replace(' ', '').lower()

    return sorted(first_word) == sorted(second_word)


tests = [
    (("listen", "silent"), True),
    (("LISTEN", "silent"), True),
    (("SiLeNt", "lIsTeN"), True),
    (("python", "ruby"), False),
    (("New York Times", "monkeys write"), True),
    (("snake", "sssnakee"), False),
    (("a gentleman", "elegant man"), True),
    (("eleven plus two", "twelve plus one"), True),
    (("William Shakespeare", "I am a weakish speller"), True),
    (("", ""), True),
]

for words, answer in tests:
    if answer == anagrams(words[0], words[1]):
        print(True)
    else:
        print(False)
