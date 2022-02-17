def main():

    infile = open("AI.txt", "r")

    import re

    string = open(
        "AI.txt",
    ).read()
    new_str = re.sub("[^a-zA-z0-9\n.]", " ", string)
    open("AI.txt", "w").write(new_str)

    word_frequency = {}

    for line in infile:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        line = line.rstrip

    for word in words:

        if word in word_frequency:
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1

    word_frequency[word]

    print(word_frequency)


main()
