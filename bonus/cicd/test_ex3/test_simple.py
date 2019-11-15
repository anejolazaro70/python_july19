#!/usr/bin/env python

def my_add(a, b):
    c = a + b
    return c

def my_mul(a, b):
    c = a * b
    return c

def main():
    my_add(2, 3)
    my_mul(2, 3)

def test_my_add():
    c = my_add(2, 3)
    assert c == 5

def test_my_mul():
    c = my_mul(2, 3)
    assert c == 7

