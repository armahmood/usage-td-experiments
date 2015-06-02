
import numpy as np
import cPickle as pickle
  
def main():
  
  lmbdas      = np.concatenate((np.arange(0, .9, .1), \
                                     np.arange(.9, 1.01, .01)))
  alphas      = np.concatenate((10**np.arange(-3, -1, 0.2), \
                                     np.arange(.1, 2.1, .1)))
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

