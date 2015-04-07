

def load_list_from_text_file(file_name):
    '''
    Load file_name and return a list containing all lines from it.
    '''

    with open(file_name) as opened_file:
        lines = opened_file.read()
        lines = lines.split(" ")

    return lines


def trigrams(split_words):
    '''
    Find and return a dictionary of all space-separated
    words' trigrams from a file. Case sensitive.
    '''

    trigrams = {}

    for each_index, each_word in enumerate(split_words):

        # Preventing an index error, because we need three items at a time.
        if each_index >= (len(split_words) - 2):
            continue

        first_word = split_words[each_index]
        second_word = split_words[(each_index + 1)]
        third_word = split_words[(each_index + 2)]

        trigram_instance = (first_word, second_word, third_word)

        try:
            trigrams[trigram_instance] += 1
        except KeyError:
            trigrams[trigram_instance] = 1

    return trigrams


if __name__ == '__main__':

    the_list = load_list_from_text_file('marco-polo.txt')

    trigrams = trigrams(the_list)

    # Reference:
    # http://stackoverflow.com/
    #     questions/613183/sort-a-python-dictionary-by-value
    import operator
    for key, value in sorted(trigrams.items(), key=operator.itemgetter(1)):
        if value > 6:
            print('{}: {}'.format(key, value))
