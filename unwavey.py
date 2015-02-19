#! /usr/bin/env python3

import fileinput
import math

lines = []

x = 110;
y = 110;
z = 0;
e = 0;

for line in fileinput.input():
    line = line[:-1]
    if line == 'G92 E0':
        olde = e = 0
    if line[0:3] == 'G1 ':
        oldy = y
        oldx = x
        olde = e
        if 'E' in line:
            (pre, e) = line.split('E', 1)
            e += ' '
            (e, post) = e.replace(';',' ;').split(' ', 1)
            e = float(e)
            line = pre + post
        if 'X' in line:
            (pre, x) = line.split('X', 1)
            (x, post) = x.replace(';',' ;').split(' ', 1)
            x = float(x)
            line = pre + post
        if 'Y' in line:
            (pre, y) = line.split('Y', 1)
            (y, post) = y.replace(';',' ;').split(' ', 1)
            y = float(y)
            line = pre + post
        if 'Z' in line:
            (pre, z) = line.split('Z', 1)
            (z, post) = z.replace(';',' ;').split(' ', 1)
            z = float(z)
            line = pre + post
        len = math.hypot(x - oldx, y - oldy)
        steps = max(1, math.ceil(len))
        for i in range(steps):
            subx = oldx + (x - oldx) / steps * (i + 1)
            suby = oldy + (y - oldy) / steps * (i + 1)
            print(
                (line +
                " X%f Y%f Z%f E%f" % (
                    subx,
                    suby,
                    max(
                        0,
                        z +
                        math.sin((subx-110) * math.pi + math.pi/2) * .25 +
                        math.sin((suby-110) * math.pi + math.pi/2) * .25
                    ),
                    olde + (e - olde) / steps * (i + 1)
                )).replace('  ',' ')
            )
    else:
        print(line)
