def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result = result + ch
    return result
text = input("Enter a string: ")
print("After removing spaces:", remove_spaces(text))