class Tablero:
    
    def __init__(self):
        self._modelo = [[0, 0, 0,],[0,0,0],[0,0,0]]
    def __str__(self):
        return str(str(self._modelo[0][0])+"|"+str(self._modelo[0][1])+"|"+str(self._modelo[0][2])+"\n"\
                   +"-----"+"\n"\
                   +str(self._modelo[1][0])+"|"+str(self._modelo[1][1])+"|"+str(self._modelo[1][2])+"\n"\
                   +"-----"+"\n"\
                   +str(self._modelo[2][0])+"|"+str(self._modelo[2][1])+"|"+str(self._modelo[2][2]))
    def marcar(self,x,y,jugador):
        self._modelo[x+1][y+1] = jugador   
t = Tablero()        
                
                
        
                 
