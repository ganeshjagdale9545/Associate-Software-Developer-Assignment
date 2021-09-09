import numpy as np
import keyboard

class Cell:
    def __init__(self):
        self.cells={}
    def accept_range(self):
        try:
            self.N=int(input("Enter range of cells(Range Should Be 3 to 10):"))
            if self.N<3 or self.N>10:
                self.accept_range()
        except:
            self.accept_range()

    def accept_cells(self):
        for i in range(0,int(self.N*self.N)):
            F=True
            while F==True:
                cell_name=input("Enter cell name:").strip()
                cell_value=input("Enter cell value(for live 1 and for dead 0):").strip()
                try:
                    if cell_name in self.cells.keys():
                        print("Cell name is exist")
                    elif len(cell_name)==0:
                        print("Cell name is too short")
                    elif int(cell_value)>1 or int(cell_value)<0:
                        print("Cell value invalid")
                    else:
                        F=False
                except:
                    print("Cell value invalid")
            self.cells[cell_name]=cell_value

    def show_cells(self):
        for i in range(1,int(self.N*self.N)+1):
            print(list(self.cells.keys())[i-1]+"="+list(self.cells.values())[i-1],end=" ")
            if i%self.N==0:
                print("")
                
    def search_cell(self,cell_name):
        if cell_name in self.cells.keys():
            print(cell_name+"="+self.cells[cell_name])
        else:
            print("cell does not exist")

    def reshape_cells(self):
        self.reshape_name=np.reshape(list(self.cells.keys()), (self.N, self.N))
        self.reshape_value=np.reshape(list(self.cells.values()), (self.N, self.N))

    def solve(self):
        for i in range(0,self.N):
            for j in range(0,self.N):
                if j==self.N-1 and i!=self.N-1:
                    neighbors_value=[self.reshape_value[i][j-1],self.reshape_value[i][0],self.reshape_value[i-1][j-1],self.reshape_value[i-1][j]
                    ,self.reshape_value[i-1][0],self.reshape_value[i+1][j-1],self.reshape_value[i+1][j],self.reshape_value[i+1][0]]
                elif i==self.N-1 and j!=self.N-1:
                    neighbors_value=[self.reshape_value[i][j-1],self.reshape_value[i][j+1],self.reshape_value[i-1][j-1],self.reshape_value[i-1][j]
                    ,self.reshape_value[i-1][j+1],self.reshape_value[0][j-1],self.reshape_value[0][j],self.reshape_value[0][j+1]]
                elif j==self.N-1 and i==self.N-1:
                    neighbors_value=[self.reshape_value[i][j-1],self.reshape_value[i][0],self.reshape_value[i-1][j-1],self.reshape_value[i-1][j]
                    ,self.reshape_value[i-1][0],self.reshape_value[0][j-1],self.reshape_value[0][j],self.reshape_value[0][0]]
                else:
                    neighbors_value=[self.reshape_value[i][j-1],self.reshape_value[i][j+1],self.reshape_value[i-1][j-1],self.reshape_value[i-1][j]
                    ,self.reshape_value[i-1][j+1],self.reshape_value[i+1][j-1],self.reshape_value[i+1][j],self.reshape_value[i+1][j+1]]
                if self.reshape_value[i][j]=='1' and neighbors_value.count('1')<2:
                    self.reshape_value[i][j]='0'
                elif self.reshape_value[i][j]=='1' and neighbors_value.count('1')>3:
                    self.reshape_value[i][j]='0'
                elif self.reshape_value[i][j]=='1' and neighbors_value.count('1')==2 or neighbors_value.count('1')==3 :
                    self.reshape_value[i][j]='1'
                elif self.reshape_value[i][j]=='0' and neighbors_value.count('1')==3:
                    self.reshape_value[i][j]='1'
                self.cells[self.reshape_name[i][j]]=self.reshape_value[i][j]
        

              
print(".....Start.....")
while True:
    obj=Cell()
    obj.accept_range()
    obj.accept_cells()
    print("Entered cells:")
    obj.show_cells()
    obj.reshape_cells()
    print(".....Solving.....")
    obj.solve()
    print("Output of Generation:")
    obj.show_cells()
    while True:
        print("Press s to search\nPress c to Continue\nPress q to exit")
        key_pressed=keyboard.read_key()
        if key_pressed=="q":
            exit()
        elif key_pressed=="s":
            obj.search_cell(input("Enter cell name:"))
        elif key_pressed=="c":
            break