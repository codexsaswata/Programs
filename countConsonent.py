def count_consonants(text):
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in "aeiouAEIOU":
            count = count + 1
    return count
text = input("Enter a string: ")
print("Number of consonants:", count_consonants(text))