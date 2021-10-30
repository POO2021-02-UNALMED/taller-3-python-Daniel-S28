class TV:
    _numTV=0
    def __init__ (self,marca,estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self.control=None
        TV._numTV+=1
    
    def setMarca(self,m):
        self._marca=m
    def getMarca(self):
        return self._marca
    
    def setEstado(self,est):
        self._estado=est
    def getEstado(self):
        return self._estado
    
    def setControl(self,ctrl):
        self._control=ctrl
    def getControl(self):
        return self._control
    
    def setPrecio(self,p):
        self._precio=p
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self,vol):
        self._volumen=vol
    def getVolumen(self):
        return self._volumen
    
    def setCanal(self,chan):
        if (chan>=1 and chan<=120 and self._estado==True):
            self._canal=chan
    def getCanal(self):
        return self._canal
    
    @classmethod
    def setNumTV(cls,n):
        cls._numTV=n
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    
    def canalUp(self):
        if (self._canal<120 and self._estado==True):
            self._canal+=1
    def canalDown(self):
        if (self._canal>1 and self._estado==True):
            self._canal-=1
    
    def volumenUp(self):
        if (self._volumen<7 and self._estado==True):
            self._volumen+=1
    def volumenDown(self):
        if (self._volumen>0 and self._estado==True):
            self._volumen-=1
    



