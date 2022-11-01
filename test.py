import random,string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    """
    fp = open(filename, encoding='utf8')

    if skip_header:
        for line in fp:
            if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK HUCKLEBERRY FINN ***'):
                break

    strippables = string.punctuation + string.whitespace

    hist = {}
    for line in fp:
        if line.startswith('*** END OF THE PROJECT GUTENBERG EBOOK HUCKLEBERRY FINN ***'):
            break

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    fp.close()
    return hist


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs in descending order of frequency.
    """
    t = []

    stopwords = process_file('data/stopwords.txt', False)

    stopwords = list(stopwords.keys())

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def show_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    """
    t = most_common(hist)
    print(f'The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


def show_total_differ(hist):
    print(f'Total number of words:', sum(hist.values()))
    print(f'Number of different words:', len(hist))


def show_freq_word(hist):
    print(f'The most common words are:')
                      # [(freq,word),(freq,word)...]
    for freq, word in most_common(hist, False)[0:20]:
        print(word, '\t', freq)


def show_diff_one(hist):
    words = process_file('data/stopwords.txt', skip_header=False)
    diff = subtract(hist, words)
    print(f"The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')


def show_random_words(hist):
    print(f"\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


def tackle_hist(hist):
    '''show "Total number of words" and "Number of different words"'''
    show_total_differ(hist)

    '''show all frequency and words'''
    show_freq_word(hist)

    '''show most common words'''
    show_most_common(hist, 20)

    '''show the words in the book that aren't in the word list'''
    show_diff_one(hist)

    '''show some random words from the book'''
    show_random_words(hist)


def main():
    hist = process_file('data/huckfinn.txt', skip_header=True)
    tackle_hist(hist)


if __name__ == '__main__':
    main()