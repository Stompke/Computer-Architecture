#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

filename = None
if len(sys.argv) > 1:
    filename = sys.argv[1]
clean_file = []

if filename:
    with open(filename) as f:
        for address, line in enumerate(f):
            line = line.split('#')

            try:
                v = int(line[0])
                clean_file.append(v)
            except ValueError:
                continue
            # memory[address] = v
            print(v)

cpu = CPU()
# print('clean file', clean_file)
cpu.load()
print(cpu.ram)
cpu.run()
sys.exit(0)