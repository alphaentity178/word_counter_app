
with open("text.txt" , "r") as file :
    text = file.read().lower()


lst = ["python" , "c" , "oop" , "hello" , "java"]

words = text.split()


word_counter = {word: 0 for word in lst}

for word in words :
    if word in lst :
        if word in word_counter :
            word_counter[word] += 1
        else:
            word_counter[word] = 1

for word , count in word_counter.items() :
    print("{} -> {}".format(word , count))

