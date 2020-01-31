# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import sys
import experience
import marker
import sorting
import numpy as np

def compare (m1,m2):
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers 
    :type markers: Numpy array of String
    :param positive: The list of positive markers
    :type positive: Numpy array of String
    :return: The list of negative markers
    :rtype: Numpy array of String
    """
    global cpt
    negative = np.array([])
    lm = len(markers)
    lp = len(positive)
    found = False
    for i in range(lm):
        for j in range(lp):
            cpt = cpt + 1
            if markers[i].cmp(positive[j]) == 0:
                found = True
                break
        if not found:
            negative = np.append(negative, markers[i])
        found = False
    return negative

# STRATEGY 2
def negative_markers2(markers,positive):
    global cpt
    positiveS = sorting.merge_sort(positive, compare)
    negative = np.array([])
    lm = len(markers)
    lp = len(positive)
    ind = 0
    found = False
    for i in range(lm):
        while not found and ind < lp and (compare(markers[i], positiveS[ind])> -1):
            if markers[i].cmp(positiveS[ind]) == 0:
                found = True
            else:
                ind += 1
            cpt += 1
        if not found:
            negative = np.append(negative, markers[i])
        found = False
        ind = 0
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    negative = np.array([])
    return negative
        
if __name__ == "__main__":
    p = int(sys.argv[1])
    m = int(sys.argv[2])

    assert (m > 0), "The number of markers must be greater than 0"
    assert (p <= m), "The number of positive markers must be less or equal to the number of markers"
    
    exp = experience.Experience(p,m)
    markers = exp.get_markers()
    positive = exp.get_positive_markers()

    print("Markers: %s" % (markers))
    print("Positive markers: %s" % (positive))
    
    # test stategy 1
    cpt = 0
    print("Negative markers: %s" % (negative_markers1(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))

    # test stategy 2
    cpt = 0
    print("Negative markers: %s" % (negative_markers2(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))

    # test stategy 3
    cpt = 0
    print("Negative markers: %s" % (negative_markers3(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))
