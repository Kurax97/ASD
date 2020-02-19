# -*- coding: utf-8 -*-

"""
:mod:`sorting` module : sorting functions module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import copy
import random
import numpy as np
import element
import generate
import test
import sys

cpt = 0

def merge (t1,t2, cmp):
    """
    Given two sorted array, creates a fresh sorted array.
    
    :param t1: An array of objects
    :type t1: Array
    :param t2: An array of objects
    :type t1: Array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh array, sorted.
    :rtype: arrayfile.write(str(100)+" "+str(i)+ " ")
    
    .. note::
    
       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t1 = numpy.array([0,2,5,6])
    >>> t2 = numpy.array([1,3,4])
    >>> merge(t1,t2,cmp)
    array([0, 1, 2, 3, 4, 5, 6])
    """
    n1 = len(t1)
    n2 = len(t2)
    t = np.zeros(n1+n2,dtype=type(t1[0]))
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t


def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm
    
    :param t: A array of integers
    :type t: array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh array, sorted.
    :rtype: array

    .. note::
    
       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    >>> import generate
    >>> def cmp_element (x,y): 
    ...    return x.cmp(y)
    >>> t = generate.random_array(10)
    >>> merge_sort(t,cmp_element)
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)
    

def quicksort (t, w, cmp):
    """
    A sorting function implementing the quicksort algorithm
    
    :param t: An array of Element
    :type t: NumPy array
    :param rand: A boolean, True if we want a random pivot, False if we want the first element to be the pivot
    :type rand: boolean
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing

    .. note::
       *t* is modified during the sort process

    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> quicksort(t, True,cmp)
    >>> t
    array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    p = dict()
    p["data"] = t
    p["left"] = 0
    p["right"] = len(t) - 1
    return quicksort_slice (p, w,cmp)


def quicksort_slice (s, w, cmp):
    """
    A sorting function implementing the quicksort algorithm
    
    :param s: A slice of an array, that is a dictionary with 3 fields :
              data, left, right representing resp. an array of objects and left
              and right bounds of the slice.
    :type s: dict
    :param rand: A boolean, True if we want a random pivot, False if we want the first element to be the pivot
    :type rand: boolean
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing
    
    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    >>> quicksort_slice (p, True, cmp)
    >>> p
    {'left': 0, 'right': 8, 'data': array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)}
    >>> t
    array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    if w == 0:
        c = s["left"]
    elif w == 1:
        c = random_pivot(s)
    elif w == 2:
        c = pivot_optimal(s)
    else:
        c = pivot_optimal_cpt(s)
    t = s["data"]
    left = s["left"]
    right = s["right"]
    if left != right: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        s1, s2 = partition(s, c,cmp) 
        # Separately sort elements before 
        # partition and after partition 
        quicksort_slice(s1, w, cmp)
        quicksort_slice(s2, w, cmp)


def partition (s, c, cmp):
    """
    Creates two slices from *s* by selecting in the first slice all
    elements being less than the pivot and in the second one all other
    elements.

    :param s: A slice of is a dictionary with 3 fields :
              - data: the array of objects,
              - left: left bound of the slide (a position in the array),
              - right: right bound of the slice.
    :type s: dict
    :param c: The pivot
    :type c: int
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A couple of slices, the first slice contains all elements that are 
             less than the pivot, the second one contains all elements that are 
             greater than the pivot, the pivot does not belong to any slice.
    :rtype: tuple

    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    
    """
    global cpt
    t = s["data"]
    low = s["left"]
    hi = s["right"]
    p = c
    pivotValue = t[p]
    t[p], t[low] = t[low], t[p]
    border = low
    
    for i in range(low, hi+1):
        c = cmp(t[i], pivotValue)
        cpt += 1
        if c == -1:
            border += 1
            t[i], t[border] = t[border], t[i]
    t[low], t[border] = t[border], t[low]
    if border == low:
        border +=1
    s1 = { "data" : t, "left" : low, "right" : border-1 }
    s2 = { "data" : t, "left" : border, "right" : hi }
    return (s1,s2)   

def random_pivot(s):
    return random.randint(s["left"], s["right"])

def pivot_optimal(s):
    t = s["data"]
    low = s["left"]
    hi = s["right"]
    mid = (hi + low) // 2
    pivot = hi
    if test.cmp(t[low], t[mid]) == -1:
        if test.cmp(t[mid] ,t[hi]) == -1:
            pivot = mid
    elif test.cmp(t[low], t[hi]) == -1:
        pivot = low
    return pivot

def pivot_optimal_cpt(s):
    global cpt
    t = s["data"]
    low = s["left"]
    hi = s["right"]
    mid = (hi + low) // 2
    pivot = hi
    if test.cmp(t[low], t[mid]) == -1:
        cpt += 1
        if test.cmp(t[mid] ,t[hi]) == -1:
            cpt += 1
            pivot = mid
    elif test.cmp(t[low], t[hi]) == -1:
        cpt += 1
        pivot = low
    return pivot

if __name__ == "__main__":
    import doctest
    doctest.testmod()
#     cpt = 0
#     t = np.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
#     quicksort(t, 3, test.cmp)
#     print(cpt)
#     
    cpt = 0
    tables = int(sys.argv[1]) 
    i = 1
    file=open("results-first-rand-opt-cpt"+str(tables)+".dat","w+") 
    while i <= tables:
        file.write(str(100)+" "+str(i)+ " ")
        print (100,i, end=" ")
        #First experience with a pivot in the first position
        tab = generate.random_array(i) #Create a table whose size is from 1 to 100 (i vraiant de 1 à 100)
        quicksort(tab, 0,test.cmp) #Sort with a pivot in the first position (rand = False)
        print(cpt, end=" ")
        file.write(str(cpt)+" ")
        #Second experience with a random pivot
        cpt = 0 #Reset the counter
        tab = generate.random_array(i) #Create a table whose size is from 1 to 100 (i vraiant de 1 à 100)
        quicksort(tab, 1,test.cmp) #Sort with a pivot in the first position (rand = False)
        print(cpt, end=" ")
        file.write(str(cpt)+" ")
        #Third experience with a optimal pivot
        cpt = 0 #Reset the counter
        tab = generate.random_array(i) #Create a table whose size is from 1 to 100 (i vraiant de 1 à 100)
        quicksort(tab, 2,test.cmp) #Sort with a pivot in the first position (rand = False)
        print(cpt, end=" ")
        file.write(str(cpt)+" ")
        #Fourth experience with an optimal pivot and cpt of the optimal_pivot
        cpt = 0 #Reset the counter
        tab = generate.random_array(i) 
        quicksort(tab, 3,test.cmp) #Sort with a random pivot (rand = True)
        print(cpt, end=" ")
        file.write(str(cpt) + "\n")
        i = i + 1
    file.close()
        
         
        
        
        
        
        
        
        
        
        
        
    