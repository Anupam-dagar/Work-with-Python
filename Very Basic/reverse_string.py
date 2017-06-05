#reverse the entered string.
def reverse(text):
    length = len(text)
    result = ""
    while length > 0:
        result = result + text[length-1]
        length = length - 1
    return result
string = raw_input("enter a string:")
answer = reverse(string)
print answer