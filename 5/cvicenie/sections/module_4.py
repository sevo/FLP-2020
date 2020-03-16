#
# Section 4: Somehow harder exercises
#
# This section covers regular expressions, input and output, the use of higher-
# order-functions and a little more advanced loops.
#
from collections import defaultdict
import random, re


# 42. Sentence Splitter
# Given a text file, this program separates its sentences based
# on a set of rules and then, returns the result.
def split_sentences( filename = 'data/text-42.md' ):
    pass


# 43 Helper: Load Words
# Returns an array of all the words in a file
def load_words( filename ):
    pass


# 43. Find Anagram
# Finds all the anagrams in a text file and returns a list
# with all the group of anagrams
# Adapted from answer at
# http://stackoverflow.com/questions/8286554/find-anagrams-for-a-list-of-words
def find_anagrams( filename = 'data/words-43.md' ):
    pass


# 44 Helper: Checks whether a set pairs of squared brackets
# is sintactically correct. This means, whether every opening bracket ( '[' )
# is closed.
# Example:
#    []        True
#    [][]      True
#    []][[]    False
#
def validate_brackets( string ):
    pass


# 44. Analyze backets
# This function generates a random string with `n` opening brackets ( '[' ) and `n`
# closing brackets ( ']' ) in a random order. After that, it checks to see whether
# the generated string is combrises for pairs of opening/closing brackets.
# After that, it print the output to the console like in this example.
# Example:
#
#    []        OK   ][        NOT OK
#    [][]      OK   ][][      NOT OK
#    [[][]]    OK   []][[]    NOT OK
#
def analyze_rand_brackets():
    pass


# 45 Helper:
# Checks whether the list has a word ending with
# a specific letter and return its position,
# returns false if there are no words that match
# the criteria.
def has_word_starting_with( letter, iterable ):
    pass


# 45. This function will generate a sequence with the
# highest possible list of pokemons in which the final letter
# of the name of the preceding one is the first letter of the
# following one
# Example:
#
#   banette -> emboar -> relicant -> tirtuga -> audino ...
#
def words_domino( filename = 'data/pokemons-list.md' ):
    pass


# 46. Anternade
# Given a word list, this function takes each word and tries to make two
# smaller words  using all the letters of that word.
# Example:
#
#   'board': makes 'bad' and 'or'
#   'waists': makes: 'wit' and 'ass'
#
def alternade( filename = 'data/words-43.md' ):
    pass

