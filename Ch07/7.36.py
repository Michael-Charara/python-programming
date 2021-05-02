def reverse(sentence):
    print(sentence)
    # just split sentence wih space as delimiter
    new_sent = sentence.split(" ")
    for x in range(len(new_sent)):  # loop till each word in splitted sentence
        sentence_rev = " ".join(reversed(new_sent))
    print(sentence_rev)


words = input("please enter a sentence\n")
print("Entered String", words)
reverse(words)
