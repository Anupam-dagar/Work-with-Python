def anti_vowel(text):
    result = ""
    for char in text:
        if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
            result = result
        else:
            result = result + char
    return result
