"""MyProblem.py"""
import numpy as np
import geatpy as ea
class MyProblem(ea.Problem): 
    def __init__(self):
        name = 'MyProblem' 
        M = 1 
        maxormins = [1] 
        Dim = 6 
        varTypes = [1] * Dim 
        lb = [3,10,3,8,6,8] 
        ub = [4,12,3,10,10,10] 
        lbin = [1,1,1,1,1,1] 
        ubin = [1,1,1,1,1,1] 
        
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
    def aimFunc(self, pop): 
        Vars = pop.Phen 
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]
        x6 = Vars[:, [5]]

        #pop.ObjV = 7*(14*x1+20*x2+24*x3+14*x4+20*x5+20*x6) # None emergency
        pop.ObjV = 7*(14*x1+20*x2+24*x3+20*x6)+5*14*x4+5*20*x5  #Emergency
        # Using penalty function

        '''
        pop.CV = np.hstack([7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x4*(20*14)+x5*(14*20+25*6)+x6*(14*15+20*6))-130000,
                        -7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x4*(20*14)+x5*(14*20+25*6)+x6*(14*15+20*6))+100000,
                        -x1+3])
        '''
        
        #Removing Upper Limit
        '''
        a=[-7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x4*(20*14)+x5*(14*20+25*6)+x6*(14*15+20*6))+100000,-7*(14*x1+20*x2+24*x3+14*x4+20*x5+20*x6)+5000]
        pop.CV = np.hstack(a)
        '''
        
        #Emergency Requriement
        pop.CV = np.hstack([7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x6*(14*15+20*6))-300*x5-400*x5-130000,
                        -7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x6*(14*15+20*6))-300*x4-400*x5+100000])
        
    def calReferObjV(self): 
        referenceObjV = np.array([[2.5]])
        return referenceObjV
