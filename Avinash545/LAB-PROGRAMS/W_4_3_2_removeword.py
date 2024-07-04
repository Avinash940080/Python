def remove_word(string, word):
    return string.replace(word, '')


strin = input("Enter string")
rmv = input("Enter word to remove")
outstring = remove_word(strin,rmv)
print("modified string = "+outstring)