import matplotlib.pyplot as plt 
import numpy as np
import math
import random
from matplotlib import colors 
class CellularAutomata():
    def __init__(self,height,width,infection_rate=0.1,death_rate=0.001,heal_rate=0.001):
        self.height=height+2
        self.width=width+2
        self.cells=np.zeros([self.height,self.width])
        self.cells[math.floor(self.height/2),math.floor(self.width/2)]=1
        self.infected=[(height/2,width/2)]
        self.infection_rate=infection_rate
        self.death_rate=death_rate
        self.heal_rate=heal_rate
    
    def update_once(self):
        for x in range(1,self.width-1):
            for y in range(1,self.width-1):
            # 周围的人
                if self.cells[x,y]==1:
                    if self.healDie(x,y):
                        continue
                    else:
                        self.infect(x,y)
    
    def infect(self,infectX,infectY):
        for x in range(infectX-1,infectX+2):
            for y in range(infectY-1,infectY+2):
                if self.cells[x,y]==0:
                    r=random.random()
                    if r<=self.infection_rate:
                        self.cells[x,y]=1

    def healDie(self,x,y):
        r=random.random()
        if(r<=self.death_rate):
            self.cells[x,y]=2
            return True
        elif(r>=1-self.heal_rate):
            self.cells[x,y]=0
            return True
        else:
            return False

    def update(self,time):
        cmap = colors.ListedColormap(['white','red','black'])
        bounds=[0,1,2,3]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        plt.ion()
        for _ in range(0,time):
            self.update_once()
            plt.imshow(self.cells,cmap=cmap,norm=norm)
            plt.pause(0.2)
        plt.ioff()

def main():
    cellularAutomata=CellularAutomata(100,100)
    cellularAutomata.update(50)
if __name__ == '__main__':
    main()