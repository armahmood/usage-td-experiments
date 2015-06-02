
import numpy as np
import cPickle as pickle
  
def main():
  
  lmbdas      = np.array([0])
  alphas      = np.array([10**-3])
  configs     = [
                   {
                   'alpha'      : alpha,
                   'lmbda'      : lmbda
                   }
                   for alpha in alphas
                   for lmbda in lmbdas
                ]
  
  f = open('configalg.pkl', 'wb')
  
  pickle.dump(configs, f)
  
if __name__ == "__main__":
  main()  

