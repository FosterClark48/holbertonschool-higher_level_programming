#!/usr/bin/python3
def multiple_returns(sentence):
    st = ''.join(map(str, sentence))
    print(st)
    leng = len(st)
    print(leng)
    fir = st[0]
    print(fir)
    for i in range(leng):
        if i <= 0:
            return None
    return (st, fir)
