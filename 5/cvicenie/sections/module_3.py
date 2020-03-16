#
# Module 3. Simple exercises including I/O ( Input/Output )
#
# Simple exercises to use I/O functins and the `re` module.
# Documentation for input and output in python can be found in the following link.
# http://docs.python.org/2/tutorial/inputoutput.html
#
import re, time, random
# from module_1 import is_palindrome_advanced, char_freq


# 32. Find palidromes.
# Scans a file line by line findind palidromes in it
# and return an array with the palindromes found.
def find_palidromes( filename = 'data/palidromes-32.md' ):
    pass


# 33. Semordnilap.
# A semordnilap is a word that when spelled backwards, produces other word.
# E.G.
#
#   strssed -> desserts
#
# This function, gets all the words in a file and finds all the words
# that when spelled backwards, are equal to other words in the file.
#
def find_semordnilaps( filename = 'data/words-33.md' ):
    pass


# 34. Character frequency table.
# Prints a table showing how many characters of each
# charachter there are in a text file
def char_freq_table( filename = 'data/the-dream.md' ):
    pass


# 35. Speak ICAO
#
# Given a string, this function will translate it to ICAO
# giving a speach of each letter's corresponding tranlation according ICAO dictionary.
# The pause betweet each spoken translated letter and each word can be set.
#
#  ( 'Hello', 0, 1 ) -> Will speach -> 'hotel' `wait 0 seconds`,  'echo' `wait 0 seconds`, 'lima' `wait 0 seconds`,
#      'lima' `wait 0 seconds`, 'oscar' `wait 0 seconds` `and then wait 1 second`
#
# Note: In order for this function to work you should have available `pyttsx` package
# instructions and download can be found in the following link
# https://github.com/parente/pyttsx
#
def speak_ICAO( string, letter_pause, word_pause ):
    pass


# 36. Hapax legomenon
# Finds words that happen to be used only once in a text.
def find_hapax_legomenons( filename = 'data/the-dream.md' ):
    pass


# 37. Add line numbers.
# Given a text file, this function will create a new text file
# in which all the lines from the original file are numbered
# from 1 to n.
def copy_file_count_lines( filename = 'data/text.txt' ):
    pass


# 38. Average_word_length.
# Calculates the average word length in a text file
# passed by the user.
def average_word_length( filename = 'data/the-dream.md' ):
    pass


# 39. Guess the number game.
# Command line game that will randomly select a number from 1 to 20
# and will ask the user to guess it.
def guess_the_number_game():
    pass


# 40. Anagram
# Command line game that given a list of colours will pick one,
# make an Anagram with it and ask the user to decript it.
def anagram_game( words ):
    pass


# 41. Lingo function
# Given two words, this function will compare them and show
# clues on the second one, that may lead to guess the first one.
def lingo( word, guess ):
    pass


# 41 Lingo Game
# Lingo is a game for guessing a hidden 5 characters word.
# Users enter a word and it is compared with the one to guess
# and clues are show for the user to finally guess the word.
def lingo_game():
    pass

