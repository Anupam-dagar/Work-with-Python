#given a list "text",this function censors the "word".(file handling)
def censor(text,word):
    temp = text.split()
    result =""
    for i in range(len(temp)):
        if temp[i] == word:
            temp[i] = "*" * len(word)
    temp = " ".join(temp)
    return temp
