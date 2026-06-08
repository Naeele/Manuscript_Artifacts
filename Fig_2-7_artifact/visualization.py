#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys


if len(sys.argv) > 1:
  file = sys.argv[1]
else:
  print("Usage: python3 visualization.py file.csv")
  exit(1)


data = np.genfromtxt(file,delimiter=' ', dtype = int)
n = len(list(data))
x = np.arange(0, n)
y1 = [row[0] if row[0] < 1000 else np.nan for row in data]
y2 = [row[1] if row[1] < 1000 else np.nan for row in data]


plt.plot(x,y1,'bo',label='multiply')
plt.plot(x,y2,'r+',label='square')
plt.legend()
plt.show()

