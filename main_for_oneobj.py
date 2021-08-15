import numpy as np
import geatpy as ea   # import geatpy
from MyProblem import MyProblem 

if __name__ == '__main__':
    """================================Create object==========================="""
    problem = MyProblem() 
    """==================================Set population==============================="""
    Encoding = 'RI'       
    NIND = 500        
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) 
    population = ea.Population(Encoding, Field, NIND) 
    """================================Set parameters============================="""
    myAlgorithm = ea.soea_DE_rand_1_L_templet(problem, population) 
    myAlgorithm.MAXGEN = 50
    myAlgorithm.mutOper.F = 0.5 
    myAlgorithm.recOper.XOVR = 0.7 
    """===========================Evaluation======================="""
    [population, obj_trace, var_trace] = myAlgorithm.run() 
    population.save() #save
    #Output
    best_gen = np.argmin(problem.maxormins * obj_trace[:, 1]) # Record
    best_ObjV = obj_trace[best_gen, 1]
   
