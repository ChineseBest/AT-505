
import numpy as np
import geatpy as ea
class MyProblem(ea.Problem): 
    def __init__(self, M = 2):
        name = 'MyProblem' 
        M = 1 
        maxormins = [1] 
        Dim = 6 
        varTypes = [1] * Dim 
        lb = [2,10,3,8,6,8] 
        ub = [4,12,3,10,10,10] 
        lbin = [1,1,1,1,1,1] 
        ubin = [1,1,1,1,1,1] 
        
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
    def aimFunc(self, pop): 
        Vars = pop.Phen #Get matrix
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]
        x6 = Vars[:, [5]]
        
        f1=x2+x3+x4
        f2=7*(14*x1+20*x2+24*x3+14*x4+20*x5+20*x6)
        
        exIdx1 = np.where(7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x4*(20*14)+x5*(14*20+25*6)+x6*(14*15+20*6))>130000)[0] # 因为约束条件之一是x1不能为10，这里把x1等于10的个体找到
        exIdx2 = np.where(7*(x1*(50*14)+x2*(30*14+25*6)+x3*(25*18+30*6)+x4*(20*14)+x5*(14*20+25*6)+x6*(14*15+20*6))<100000)[0] # 因为约束条件之一是x1不能为10，这里把x1等于10的个体找到
        f1[exIdx1] = f1[exIdx1]+np.max(f1) - np.min(f1)
        f2[exIdx1] = f2[exIdx1]+np.max(f2) - np.min(f2)
        
        f1[exIdx2] = f1[exIdx2]+np.max(f1) - np.min(f1)
        f2[exIdx2] = f2[exIdx2]+np.max(f2) - np.min(f2)
        
        pop.ObjV = np.hstack([f1, f2]) 
    