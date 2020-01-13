# put your code here.

def word_count(text):

    file = open(text)

    count_word = {}

    for line in file:
        line = line.rstrip()
        paragraph = line.split(" ")

        for word in paragraph:
            count_word[word] = count_word.get(word, 0) + 1

    return count_word

all_the_words = (word_count("twain.txt"))


def listing_word_count(dictionary):
    for key, value in dictionary.items():
        print(f"{key} {value}")

listing_word_count(all_the_words)
