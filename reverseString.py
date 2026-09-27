def reverse_string_loop(text):
    reverse = ""
    for ch in text:
        reverse = ch + reverse
    return reverse
text = input("Enter a string: ")
print("Reverse:", reverse_string_loop(text))