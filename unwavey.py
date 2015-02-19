#! /usr/bin/env python3

import fileinput
import math

lines = []

X = 0;
Y = 0;
Z = 0;


for line in fileinput.input():
    line = line[:-1]
    if line[0:3] == 'G1 ':
        if 'X' in line:
            X = float(line.split('X')[1].replace(';', ' ').split(' ')[0])
        if 'Y' in line:
            Y = float(line.split('Y')[1].replace(';', ' ').split(' ')[0])
        if 'Z' in line:
            (pre, z) = line.split('Z')
            (z, post) = z.split(' ')
            Z = float(z)
            line = pre + post
        line += " Z%f" % (Z + math.sin((X-110) * math.pi + math.pi/2) * .25 + math.sin((Y-110) * math.pi + math.pi/2) * .25)
    print(line)
