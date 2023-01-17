#!/usr/bin/python3
def multiple_returns(sentence):
    str = ''.join(map(str, sentence))
    leng = len(str)
    fir = str[0]
    for i in leng:
        if i <= 0:
            return None
    return (leng, fir)
