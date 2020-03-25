# -*- coding: utf-8 -*-

""":mod:`test` module : Test module for bloomfilter analysis

:author: `FIL - Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""
import random
import bloomfilter

nb_hash_functions = 8
random_tab = [ 0 for i in range(128 * nb_hash_functions)]

def init_random_tab ():
    """
    Creates the hash functions.
    """
    global random_tab
    for i in range(128):
        for j in range(nb_hash_functions):
            random_tab[j * 128 + i] = random.randint(1,32000)

def code_of_string (str,n):
    """
    For a given string, returns the hash code for the n-th hashing function.
    
    :param str: The string to be hashed.
    :type str: string
    :param n: The function number.
    :type n: int
    :return: A hash code
    :rtype: int

    .. note:: 
       1 <= n <= nb_hash_functions
    """
    h = 0
    for char in str:
        h += random_tab[ord(char) + (n*128)]
    return h

def random_word ():
    """
    Returns a word with random letters whose length is between 4 and 7.

    :rtype: string
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str

if __name__ == "__main__":
    init_random_tab()
    """
    bf = bloomfilter.create(4,code_of_string,8)
    w = random_word()
    bloomfilter.add(bf,"timoleon")
    if bloomfilter.contains(bf,"timoleon"):
        print("%s est present" % ("timoleon"))
    if bloomfilter.contains(bf,w):
        print("%s est present" % (w))
    """
    listRandomWords = [random_word() for k in range(2**10)]
    for n in range(1, 9):
        cpTested = 0
        cpPositif = 0
        for t in range(10, 21):
            bf = bloomfilter.create(t, code_of_string, n)
            for i in range(2**10):
                bloomfilter.add(bf,listRandomWords[i])
            for k in range(2**14):
                u = random_word()
                if not (u in listRandomWords):
                    cpTested += 1
                    if bloomfilter.contains(bf, u):
                        cpPositif += 1
            print(t, end = " ")
            print(n, end = " ")
            print(cpTested, end = " ")
            print(cpPositif, end = " ")
            print(cpPositif/cpTested)
            cpTested = 0
            cpPositif = 0
        print("\n")

    

    











