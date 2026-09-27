def find_longest_word(text):
    words = []
    word = ""
    for ch in text:
        if ch != " ":
            word = word + ch
        else:
            if word != "":
                words.append(word)
                word = ""
    if word != "":
        words.append(word)

    longest = ""

    for w in words:
        if len(w) > len(longest):
            longest = w

    return longest
text = input("Enter a sentence: ")
print("Longest word:", find_longest_word(text))