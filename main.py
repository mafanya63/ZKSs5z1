# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
import os


def func(x):
    return - math.cos(x) * math.cos(math.pi) * math.exp(- (x - math.pi) ** 2)


if __name__ == '__main__':
    xmin = -100.0
    xmax = 100.0
    count = 500
    xlist = np.linspace(xmin, xmax, count)
    ylist = [func(x) for x in xlist]
    plt.plot(xlist, ylist)
    plt.show()

    data = ET.Element('data')
    xdata = ET.SubElement(data, 'xdata')
    ydata = ET.SubElement(data, 'ydata')
    for i in range(count):
        ET.SubElement(xdata, 'x').text = str(xlist[i])
        ET.SubElement(ydata, 'y').text = str(ylist[i])

    if not os.path.exists('results'):
        os.mkdir('results')
    os.chdir(os.path.join(os.getcwd(), 'results'))
    tree = ET.ElementTree(data)
    tree.write('results.xml')