import os
import sys

import matplotlib.pyplot as plt
import seaborn


ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(ROOT)
from utils import benchmark


data = [
    ("NonTemporal", [0, 1]),
    ("Threads", list(range(1, 9)))
]

frame = benchmark(data)

seaborn.barplot(data=frame, x="Threads", y="Time", hue="NonTemporal")
plt.show()
