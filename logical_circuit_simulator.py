'''
Created on Feb 24, 2016

@author: MADHUSUDAN
'''
class LogicGate(object):
    def __init__(self,n):
        self.lable =n
        self.output=None
    
    def getLable(self):
        return self.lable  
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output  
 

'''setNextPin is very important for making connections. We need to add this method to our
 gate classes so that each togate can choose the proper input line for the connection.

'''    
class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)
        self.pina = None
        self.pinb = None
    
    def getpinA(self):
        
        if self.pina is None:
            p="Enter the input for pin A "+str(self.getLable())+" --->"
            return int(raw_input(p))
        else:
            return self.pina.getFrom().getOutput()
    
    def getpinB(self):
        
        if self.pinb is None:
            p="Enter the input for pin B "+str(self.getLable())+" --->"
            return int(raw_input(p))
        else:
            return self.pinb.getFrom().getOutput()
 
    def setNextpin(self,source):
        if self.pina==None:
            self.pina=source
        
        elif self.pinb==None:
                self.pinb=source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
        
        
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin=None
    
    def getpin(self):
        if self.pin is None:
            p="Enter the input for pin "+str(self.getLable())+" --->"
            return int(raw_input(p))
        
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextpin(self,source):
        print source
        if self.pin==None:
            self.pin=source
        
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
        
class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):
        a= self.getpinA()
        b= self.getpinB()
        if a== 1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self): 
        a = self.getpinA()
        b = self.getpinB()
        
        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n) 
        
    def performGateLogic(self):
        g = self.getpin()
        if g == 1:
            return 0
        else:
            return 1 
        
'''REMEMBER this connector class contains the instances of the gate objects and 
inside togate.setnextpin() method is used to set the input for the togate object , this is like an interface'''        
class Connector: 
    def __init__(self,fgate,tgate):
        self.framGate= fgate
        self.toGate= tgate
        
        tgate.setNextpin(self) # here the object tget is passing the connector instance
    
    def getFrom(self):
        return self.framGate
    
    def getTo(self):
        return self.toGate
            
          
g1=NotGate("G1")
#print g1.getOutput()
#print g1.getLable()
#print g1.g

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
print g3.getOutput()
#c3 = Connector(g3,g4)
#print g4.getOutput()