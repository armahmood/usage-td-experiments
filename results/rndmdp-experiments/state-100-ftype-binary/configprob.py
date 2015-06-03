
import numpy as np
import cPickle as pickle
  
def main():
  ns          = 100
  N           = 1000
  gamma       = 0.99
  configs     = \
                   {
                   'Gamma'      : gamma*np.eye(ns),
                   'T'          : N,
                   'N'          : N,
                   'ns'         : ns,
                   'na'         : 1,
                   'ftype'      : 'binary',
                   'nf'         : int(np.ceil(np.log(ns+1)/np.log(2))),
                   'b'          : 10,
                   'rtype'      :'uniform', 
                   'rparam'     : 1,
                   'Rstd'       : 0.0,
                   'initsdist'  : 'statezero',
                   }
  
  f = open('configprob.pkl', 'wb')
  
  pickle.dump(configs, f)
  
if __name__ == "__main__":
  main()  

