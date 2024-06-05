#!/usr/bin/env python3

# Using a list comprehension, write a function return_evens() that returns a list of all of the even elements of a sequence of integers.

def return_evens(num_list):
    return [n for n in num_list if n%2 == 0]

# Using a list comprehension, write a function make_exclamation() that takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end.

def make_exclamation(sentence_list):
    return [n + '!' for n in sentence_list]