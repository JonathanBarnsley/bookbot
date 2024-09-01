#import section
from collections import OrderedDict
import re

#main.py has functions to open a book text file and analyse it
def main(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return(file_contents)

#function to count the words in a string
def count_words(string):
    words = string.split()
    word_count = len(words)
    return(word_count)

#function to count the instances of a character
def count_characters(string):
    #convert to lower case
    lower_case_string = string.lower()
    #generate dictonary for each character
    character_count_list = sorted(OrderedDict.fromkeys(lower_case_string))
    character_count_dictonary = {}
    #iterate for each character and update the dictonary value
    for key in character_count_list:
        character_count_dictonary[key] = lower_case_string.count(key)
        print(f"The '{re.escape(key)}' character was found {character_count_dictonary[key]} times")

#test using frankenstein example
print("--- Begin report of books/frankenstein.txt ---\n")

frankenstein_book = main("books/frankenstein.txt")

count_words_result = count_words(frankenstein_book)

print(f"{count_words_result} words found in the document\n")

count_characters(frankenstein_book)