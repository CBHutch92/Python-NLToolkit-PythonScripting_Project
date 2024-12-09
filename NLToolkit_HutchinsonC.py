# Assignment 6
# Casey Hutchinson
# ITEC 3100
# Due by 11/17/2024

import string
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def three_musketeers():
    # Step 1, loads "The Three Musketeers" txt file into Python
    local_file = open("The Three Musketeers.txt", encoding = 'utf-8')
    three_musks = local_file.read()
    three_musks = nltk.word_tokenize(three_musks)
    local_file.close()

    # Step 2, display the length of the text
    print("First lets look at the length of the text:")
    three_musks_length = len(three_musks)
    print(f"The length of The Three Musketeers file is {three_musks_length} words.")
    print("\n")

    # Step 3, filter the punctuation
    print("Now, let's filter out the punctuation and take a look at the length of the text without it.")
    print("These are all of the punctuation marks we will be filtering out:")
    print(string.punctuation)
    three_musks_words = []
    for word in three_musks:
        if word not in string.punctuation:
            three_musks_words.append(word)
    punc = len(three_musks) - len(three_musks_words)
    no_punc = len(three_musks_words)
    print(f"The total number of punctuation chracters in the text is: {punc}")

    # Step 4, display the length of the text with punctuation filtered out
    print(f"After filtering out the punctuation above, the length of The Three Musketeers file is {no_punc} words.")
    print("\n")

    # Step 5, filter the stop words
    print("Now that we've filtered out the punctuation, let's see what the length of the text is without any 'stop words'")
    print("Since there are dozens of stop words, I'm only going to show you the top 10. These are the top 10 stop words amongst many that we will be filtering out:")
    english_stopwords = stopwords.words('English')
    print(english_stopwords[:10])
    three_musks_stopwords = []
    for word in three_musks:
        if word in english_stopwords:
            three_musks_stopwords.append(word)
    just_stopwords = len(three_musks_stopwords)
    no_punc_stopwords = len(three_musks_words) - len(three_musks_stopwords)
    print(f"The total number of stopwords in the text is: {just_stopwords}")

    # Step 6, display the length of the text after filtering out the stop words
    print(f"After filtering out punctuation and stopwords, the length of The Three Musketeers file is {no_punc_stopwords} words.")
    print("\n")

    # Step 7, display the frequency of the 15 most common words
    print("Now let's take a look at the 15 most common words use in the The Three Musketeers file.")
    three_musks_main = []
    filtered_words = ['”', '“', '’', 'D', 'I']                                                                    # I created a filtered list mostly to filter out the curly versions of the single/double quotes - not sure why they kept making it through
    for word in three_musks:
        if word not in string.punctuation:
            if word not in english_stopwords:
                if word not in filtered_words:
                    three_musks_main.append(word)
    three_musks_dist = nltk.FreqDist(three_musks_main)
    for word, freq in three_musks_dist.most_common(15):
        print(f"'{word}': {freq}")
    print("\n")
    print("We can make this look a little neater by putting them in a table and a chart:")

    # Step 7, display using a table
    print(three_musks_dist.tabulate(15))
    print("\n")

    # Step 7, display using a chart
    three_musks_dist.plot(15)
    plt.xlabel('Word')                                                      
    plt.ylabel('Frequency')
    plt.title('Top 15 words and their frequency from The Three Musketeers file')
    plt.show()


def main():
    three_musketeers()

if __name__ == "__main__":
    main()