class Tablero:
    
    def __init__(self):
        self._modelo = [[0, 0, 0],[0,0,0],[0,0,0]]
        self._ganador = 0
    def __str__(self):
        return str(str(self._modelo[0][0])+"|"+str(self._modelo[0][1])+"|"+str(self._modelo[0][2])+"\n"\
                   +"-----"+"\n"\
                   +str(self._modelo[1][0])+"|"+str(self._modelo[1][1])+"|"+str(self._modelo[1][2])+"\n"\
                   +"-----"+"\n"\
                   +str(self._modelo[2][0])+"|"+str(self._modelo[2][1])+"|"+str(self._modelo[2][2]))
    def marcar(self,x,y,jugador):
        self._modelo[x][y] = jugador   
    def estaVacio(self,x,y):
        if self._modelo[x][y] == 0:
            return True
        else:
            return False
                
    def determinarGanador(self):
        for row in self._modelo:
            if row == [1,1,1]:
                self._ganador = 1
            if row == [2,2,2]:
                self._ganador = 2  
        for i in range(3):
            if self._modelo[0][i]== 1 and self._modelo[1][i] == 1 and self._modelo[2][i] ==1:
                self._ganador = 1
            if self._modelo[0][i]== 2 and self._modelo[1][i] == 2 and self._modelo[2][i] ==2:
                self._ganador = 2
        for i in range(1,3):
            if self._modelo[0][0] == i and self._modelo[1][1] == i and self._modelo[2][2] == i:
                self._ganador = i
            if self._modelo[2][0] == i and self._modelo[1][1] == i and self._modelo[2][0] == i:
                self._ganador = i
                
t = Tablero()
jugador = 2
print("Bienvenido al juego")
while t._ganador == 0:
    jugador = (jugador%2)+1
    x = int(input("Coordenadas x jugador "+ str(jugador)+"? "))
    y = int(input("Coordenadas y jugador "+ str(jugador)+"? ")) 
    if t.estaVacio(x,y) == False:
        print("Casilla ocupada")
        continue
    t.marcar(x,y,jugador)
    t.determinarGanador()
print("El ganador es el jugador ",jugador,"!!!!!!!!!!!!!!!!!!!!")    
            
    
                    
        
            
        
                
                
        
                 
