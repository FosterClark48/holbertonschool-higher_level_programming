#!/usr/bin/python3
for num in range(100):
    if(num != 100):
        print("{:0=2d}".format(num), end=", ")
    else:
        print()
