#!/usr/bin/env python

def clean_rtable(rtable):
    for el in rtable:
        el[1].pop(2)
    return(rtable)
