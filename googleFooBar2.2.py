#python 2.7

def solution(n,b):
    CYCLE = []
    
    def determineCycle():
        cycleSet = set()
        for x in range(25,len(CYCLE)):
            cycleSet.add(CYCLE[x])
        return len(cycleSet)
    
    def changeBase(i,b):
        s = []
        while i:
            s.append(int(i % b))
            i /= b
        return ''.join(map(str,s[::-1]))
                 
    def assignPrisoner(n,b):
        if int(n) <0 :
            raise ValueError("Minion ID must be positive")   
        length = len(n)
        CYCLE.append(n)
        b=int(b)
        tempyList = list(n)
        tempyList.sort(reverse=True)
        x=tempyList[:]
        tempyList.sort()
        y=tempyList[:]
        x=''.join(x)
        y=''.join(y)
        xInt = int(x,b) 
        yInt = int(y,b)
        zInt = xInt - yInt
        z=changeBase(zInt,b)
        if len(z) != length:
            z=z.zfill(length)
        if len(CYCLE) < 50:
            return assignPrisoner(z,b)
        if len(CYCLE) >= 50:
            return determineCycle()

    def checkArgs(n,b):    
      if not 2<= b <= 10:
        raise ValueError
      if type(n) != str:
        raise ValueError
      if len(n) <0 :
        raise ValueError
      else:
        return True
        
    if checkArgs(n,b):
      return assignPrisoner(n,b)

result = solution('210022',3)
print(result)