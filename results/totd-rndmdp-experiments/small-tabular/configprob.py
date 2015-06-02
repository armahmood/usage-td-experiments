
import numpy as np
import cPickle as pickle
  
def main():
  
  ns          = 10
  configs     = \
                   {
                   'algname'    : 'td',
                   'Gamma'      : 0.99*np.eye(ns),
                   'T'          : 100,
                   'N'          : 1,
                   'ns'         : ns,
                   'na'         : 1,
                   'b'          : 3,
                   'ftype'      : 'tabular',
                   'nf'         : ns,
                   'rtype'      :'normal', 
                   'rparam'     :1,
                   'Rstd'       : 0.1,
                   'initsdist'  : 'statezero',
                   }
  
  f = open('configprob.pkl', 'wb')
  
  pickle.dump(configs, f)
  
if __name__ == "__main__":
  main()  

