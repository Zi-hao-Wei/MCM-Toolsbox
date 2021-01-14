def get_neighbour(self):
    # x=one[0]
    # y=one[1]
    # x=self.width-1
    y=2
    x=0
    # y=0
    self.cells[x,y]=2
    self.cells[x+1,y+1]=3
    print(self.cells)

    if x==0 and y==0:
        #左上角
        neighbours=self.cells[0:2,0:2].reshape((-1,))
        neighbours=np.delete(neighbours,[0])
    elif x==0 and y==self.height-1:
        #右上角
        neighbours=self.cells[0:2,y-1:y+1].reshape((-1,))
        neighbours=np.delete(neighbours,[1])
    elif x==self.width-1 and y==0:
        #左下角
        neighbours=self.cells[x-1:x+1,0:2].reshape((-1,))
        neighbours=np.delete(neighbours,[2])
    elif x==self.width-1 and y==self.height-1:
        #右下角
        neighbours=self.cells[x-1:x+1,y-1:y+1].reshape((-1,))
        neighbours=np.delete(neighbours,[3])
    elif x==0:
        #上界
        neighbours=self.cells[0:2,y-1:y+2].reshape((-1,))
        neighbours=np.delete(neighbours,[1])
        print(neighbours)
