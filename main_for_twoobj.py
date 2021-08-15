import geatpy as ea # import geatpy
from MyProblem import MyProblem 

if __name__ == '__main__':
    """================================Create object==========================="""
    problem = MyProblem()     
    """==================================Set population==============================="""
    Encoding = 'RI'          
    NIND = 200                
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) 
    population = ea.Population(Encoding, Field, NIND) 
    """=================================Set parameters============================"""
    myAlgorithm = ea.moea_NSGA2_templet(problem, population) 
    myAlgorithm.MAXGEN = 50  
    """============================Evaluation======================"""
    NDSet = myAlgorithm.run() 
    NDSet.save()              
  
