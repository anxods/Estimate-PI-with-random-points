import random
import matplotlib.pyplot as plt
import numpy as np

class calcPI():

    def __init__(self,iterations):
        self.iterations = iterations

    def plot(self,xInside,yInside,xOutside,yOutside):
        x = np.linspace(-1.0, 1.0, 100)
        y = np.linspace(-1.0, 1.0, 100)
        X, Y = np.meshgrid(x,y)
        F = X**2 + Y**2 - 1
        plt.contour(X,Y,F,[0])
        plt.axis([0,1,0,1])
        plt.plot(xInside,yInside,'ro',color='green')
        plt.plot(xOutside,yOutside,'ro',color='red')
        plt.show()

    def plotPI(self):
        pCircle = 0
        pTotal = 0
        xInside = [] 
        yInside = []
        xOutside = [] 
        yOutside = []
        pi = calcPI(self.iterations)

        for _ in range(self.iterations):
            x = random.uniform(0,1)
            y = random.uniform(0,1)   
            dist = x**2 + y**2
            
            if dist <= 1:
                pCircle += 1
                xInside.append(x)
                yInside.append(y)
            else:
                xOutside.append(x)
                yOutside.append(y)
            
            pTotal+=1

        pi.plot(xInside,yInside,xOutside,yOutside)

    def calcPI(self, pr):
        pCircle = 0
        pTotal = 0

        for _ in range(self.iterations):
            x = random.uniform(0,1)
            y = random.uniform(0,1)
            dist = x**2 + y**2

            if dist <= 1:
                pCircle += 1
            pTotal += 1

        if pr == 1:
            print(4*pCircle/pTotal)

        return 4 * pCircle/pTotal