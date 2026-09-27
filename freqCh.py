def character_frequency(text, ch):
    frequency = 0
    for character in text:
        if character == ch:
            frequency = frequency + 1
    return frequency
text = input("Enter text: ")
ch = input("Enter character: ")
print("Frequency:", character_frequency(text, ch))