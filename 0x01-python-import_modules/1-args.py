#!/usr/bin/python3
import sys
if len(sys.argv) == 0:
    print("{:d} arguments.".format(len(sys.argv)))
if len(sys.argv) == 1:
    print("{:d} argument:".format(len(sys.argv)))
else:
    print("{:d} arguments:".format(len(sys.argv)))
for i in range(len(sys.argv)):
    print("{:d}: {:s} ".format(i + 1, sys.argv[i]))
