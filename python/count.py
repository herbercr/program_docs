#!/usr/bin/env python3

import sys
x = sys.argv[1]
i = sys.argv[2]
for x in range(int(i)):
	if x % 2 == 0:
		print(x)
