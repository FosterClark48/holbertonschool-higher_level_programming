#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if len(sys.argv) == 0:
        print("{:d} arguments.".format(len(sys.argv)))
    elif len(sys.argv) == 1:
        print("{:d} argument:".format(len(sys.argv)))
    else:
        print("{:d} arguments:".format(len(sys.argv)))
    for i in range(arg):
        print("{:d}: {} ".format(i + 1, sys.argv[i + 1]))
