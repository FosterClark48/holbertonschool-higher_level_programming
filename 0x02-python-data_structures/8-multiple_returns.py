#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    for i in str(length):
        if i == 0:
            return None
        return length
