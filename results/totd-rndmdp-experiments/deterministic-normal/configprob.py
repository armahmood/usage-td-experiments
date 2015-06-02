
import numpy as np
import cPickle as pickle
  
def main():
  
  ns          = 100
  configs     = \
                   {
                   'algname'    : 'totd',
                   'Gamma'      : 0.99*np.eye(ns),
                   'T'          : 1000,
                   'N'          : 1,
                   'ns'         : ns,
                   'na'         : 1,
                   'nf'         : 5,
                   'b'          : 3,
                   'ftype'      : 'normal',
                   'nf'         : 5,
                   'rtype'      :'normal', 
                   'rparam'     :1,
                   'Rstd'       : 0.0,
                   'initsdist'  : 'statezero',
                   }
  
  f = open('configprob.pkl', 'wb')
  
  pickle.dump(configs, f)
  
if __name__ == "__main__":
  main()  

