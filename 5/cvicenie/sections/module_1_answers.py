# Section 1. Very simple exercises
#
# This selection of exercises is intended for developers
# to get a basic understanding of logical operators and loops in Python
#

import re

def max_num(a, b):
    if a > b:
        return a
    return b

def max_of_three(a, b, c):
    return max_num(max_num(a, b), c)

def str_len(lst):
    sum = 0
    for x in lst:
        sum += 1
    return sum

def is_vowel(x):
    string = "a e i o u y"
    pole = string.split(" ")
    return x in pole

def translate(lst):
    str = ""
    for x in lst:
        if not is_vowel(x) and x!= " ":
            str += x + "o" + x.lower()
        else:
            str += x
    return str

def sum(lst):
    temp = 0
    for i in lst:
        temp += i
    return temp

def multiply(lst):
    temp = 1
    for i in lst:
        temp*= i
    return temp

def reverse(str):
    temp=""
    for i in str:
        temp=i+temp
    return temp

def is_palindrome(str):
    temp=reverse(str)
    return str == temp

def is_member(x, lst):
    for i in lst:
        if i == x:
            return True

    return False

def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True

    return False

def generate_n_chars (n, c):
    return n * c

def historigram(lst):
    for i in lst:
        print(i*"*")


def max_in_list(lst):
    temp = lst[0]
    for i in lst:
        if i > temp:
            temp = i
    return temp

def map_words(lst):
    temp = []
    for i in lst:
        temp.append(str_len(i))
    return temp

def longest_word(lst):
    return max_in_list(map_words(lst))

def filter_long_words(lst, int):
    temp = []
    for i in lst:
        if str_len(i) >= int:
            temp.append(i)
    return temp

def is_palindrome_advanced(lst):
    temp =""
    lst2 = lst.lower()
    for i in lst2:
        if i >= "a" and i <= "z":
            temp += i
    return is_palindrome(temp)

def is_pangram(str):
    temp = set()
    str = str.lower()
    for i in str:
        if i >= "a" and i <= "z":
            temp.add(i)
    return len(temp) == 26

def sing_99_bottles_of_beer():
    x = 99
    while x > 0:
        print("%d bottles of beer on the wall, %d bottles of beer. Take one down, pass it around, %d bottles of beer on the wall." %(x,x,x-1))
        x = x-1

def translate2(lst):
    temp = { "merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar" }
    str = []
    for i in lst:
        str.append(temp[i])

    return str


def char_freq(str):
    dict = {}

    for x in str:
        if x in dict:
            dict[x] += 1
        else:
            dict[x]=1

    return dict


def rot_13_encrypt(str):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

    str2 =""
    for i in str:
        if i in key:
            str2 += key[i]
        else:
            str2+=i
    return str2

def rot_13_decrypt(str):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    key2={}
    for i in key:
        key2[key[i]]=i

    str2 =""
    for i in str:
        if i in key2:
            str2 += key2[i]
        else:
            str2+=i
    return str2

def correct(str):
    str2 = str.split(" ")
    str3 = []

    for i in str2:
        if i == "":
            continue

        str3.append(i)
    str4 = " ".join(str3)
    str4 = str4.replace(".",". ")
    str4 = str4.replace(".  ",". ")

    return str4[:-1]

# def make_3d_form()