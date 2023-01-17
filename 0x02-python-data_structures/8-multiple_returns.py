#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        if i <= 0:
            return None
        return len(sentence)
