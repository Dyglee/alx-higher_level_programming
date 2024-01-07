#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0]
    if lenght == 0:
        first = None
    mytuple = (lenght, first)
    return mytuple
