sentence = input("Enter your sentence:\n").lower()
words = sentence.split()
sentence_new = []
for word in words:
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        word += "way"
        sentence_new.append(word)
    else:
        word += (word[0] + "ay")
        word = word[1:]
        sentence_new.append(word)
sentence_new_str = ""
for word in sentence_new:
    sentence_new_str += (word + " ")
print(sentence_new_str)
