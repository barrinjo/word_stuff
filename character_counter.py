from collections import Counter
from numpy.random import choice
import re


def copy_text_file(text_file):
    f = open(text_file, "r")
    if f.mode == 'r':
        return f.read()


def counter_dict(text_file):
    return Counter(character_list(copy_text_file(text_file)))


def number_of_characters(text_file):
    char_count = 0
    for _ in copy_text_file(text_file):
        char_count += 1
    return char_count


def character_list(text_file):
    characters = []
    for x in text_file:
        characters.append(x)
    return characters


def character_probability(dictionary):
    character_count = values_total(dictionary)
    character_dictionary = dictionary
    probability_dictionary = {}
    for x in character_dictionary:
        prob = (character_dictionary.get(x, 'none') / character_count)
        probability_dictionary[x] = prob
    return probability_dictionary


def probability_count(text_file):
    y = 0
    prob = character_probability(text_file)
    for x in prob:
        y = y + prob.get(x, 'none')
    return y


def select_weighted_character(count, text_file):
    prob_dict = character_probability(text_file)
    return choice(list(prob_dict.keys()), count, p=list(prob_dict.values()))


def build_next_character_list(char, text_file):
    prev_char = ''
    prev_list = []
    for x in copy_text_file(text_file):
        if prev_char == char:
            if prev_char == '':
                pass
            else:
                prev_list.append(x)
        prev_char = x
    return prev_list


def count_list(char_list):
    return Counter(char_list)


def build_mega_dict(text_file):
    mega_dict = {}
    for x in set(copy_text_file(text_file)):
        mega_dict[x] = character_probability(count_list(build_next_character_list(x, text_file)))
    return mega_dict


def values_total(dictionary):
    y = 0
    for x in dictionary:
        y = y + dictionary.get(x, 'none')
    return y


def pick_next_character(char, mega_dict):
    prob_dict = mega_dict.get(char, 'none')
    return ''.join(choice(list(prob_dict.keys()), 1, p=list(prob_dict.values())))


def weighted_contextual_chars(text_file):
    mega_dictionary = build_mega_dict(text_file)
    count = number_of_characters(text_file)
    char = ''.join(choice(character_list(text_file), 1))
    char_list = []
    for _ in range(count):
        char = pick_next_character(char, mega_dictionary)
        char_list.append(char)
    return ''.join(char_list)


def remove_punctuation(text_file):
    text = copy_text_file(text_file)
    for char in ':?;!\".,-\n\ufeff()':
        text = text.replace(char, ' ')
    return text


def split_text_into_words(text_file):
    text = re.split(" ", copy_text_file(text_file))
    return [x for x in text if x != ""]


def build_next_word_list(word, word_list):
    prev_char = ''
    prev_list = []
    for x in word_list:
        if prev_char == word:
            if prev_char == '':
                pass
            else:
                prev_list.append(x)
        prev_char = x
    if len(prev_list) == 0:
        prev_list.append("no")
    return prev_list


def build_mega_word_dict(text_file):
    text = split_text_into_words(text_file)
    mega_dict = {}
    for word in split_text_into_words(text_file):
        mega_dict[word] = character_probability(count_list(build_next_word_list(word, text)))
    return mega_dict


def words_weighted_contextual(text_file):
    mega_dictionary = build_mega_word_dict(text_file)
    count = len(split_text_into_words(text_file))
    # count = 1000
    char = "I"
    char_list = []
    for _ in range(count):
        char = pick_next_character(char, mega_dictionary)
        char_list.append(char)
    super_list = []
    for word in char_list:
        super_list.append(word)
        super_list.append(" ")
    return ''.join(super_list)


def word_pick(char, mega_dict):
    prob_dict = mega_dict.get(char, 'none')
    return choice(list(prob_dict.keys()), 1, p=list(prob_dict.values()))


# file = open("output.txt", "w")
# file.write(weighted_contextual_chars("character_counter.py"))
# file.close()

file = open("output.txt", "w")
file.write(words_weighted_contextual("repo/markymark.txt"))
file.close()
