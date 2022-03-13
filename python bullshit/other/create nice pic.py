import matplotlib.pyplot as plt
from samila import GenerativeImage
import random
import math
from samila import Projection


def f1(x, y):
    result = random.gauss(0, 1) * math.sin(y)+ (x + y) * random.uniform(-1, 1)
    return result


def f2(x, y):
    result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1)
    return result

g = GenerativeImage(f1, f2)
g.generate(start=-2*math.pi, step=0.01, stop=0)  # start=-2*math.pi, step=0.01, stop=0
g.plot(color="red", bgcolor="black", projection=Projection.POLAR)
g.save_image(file_adr="test.png")
plt.show()
