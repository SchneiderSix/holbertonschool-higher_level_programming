#!/usr/bin/python3
def best_score(a_dictionary):
    bs = max(a_dictionary, key = a_dictionary.get)
    return bs
