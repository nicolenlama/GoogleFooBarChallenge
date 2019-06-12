# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:43:44 2019
Locating Bunny Prisoners
@author: nlama
"""
def solution(x,y):
    def transY(y): 
        seq1 = 1
        for i in range(y):
            seq1+=i
        return seq1
    
    def transX(s,y,x):
        end = x - 1
        i = y + 1
        j=0
        while j < end:
            s+=i
            j+=1
            i+=1
        return s
           
    def getID(x,y):
        if x > 100000 or y > 100000:
            raise ValueError("x or y Surpassed number of physical prison cells")
        seq1 = transY(y) #Get first number in sequence
        iD = transX(seq1,y,x) # get id 
        return str(iD)
    
    return getID(x,y)    

print(solution(3,2))