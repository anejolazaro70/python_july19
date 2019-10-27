#!/usr/bin/env python

list_diff = list()

def compare_lists(list_a, list_b):
    for el in list_a:
        if el not in list_b:
            list_diff.append(el)
    for el in list_b:
        if el not in list_a:
            list_diff.append(el)
    return(list_diff)
