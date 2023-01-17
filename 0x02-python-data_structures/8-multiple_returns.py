#!/usr/bin/python3
def multiple_returns(sentence):
    st = ''.join(map(str, sentence))
    leng = len(st)
    fir = st[0]
    for i in range(leng):
        if i <= 0:
            return None
    return (st, fir)
