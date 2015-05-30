'''
Created on Jan 25, 2015

@author: A. Rupam Mahmood

This program takes a .dat file located at 'pathfile1',
summarizes the error array by keeping only 'N' 
data points and saves it in 'pathfile2'. 

'''

import numpy as np
import cPickle as pickle
import sys
import os.path

def main():
  pathfile1    = sys.argv[1] # location of source .dat file
  pathfile2    = sys.argv[2] # location of destination .dat file
  N           = int(sys.argv[3]) # number of d points to keep
  f1           = open(pathfile1, "rb")
  data        = []
  try:
    while True:
      d            = pickle.load(f1)
      error        = d['error']
      T            = len(error)
      d['error']   = np.mean(np.reshape(error, (T/N, N), 1), 0)
      data.append(d)
  except EOFError:
    print 'End of file reached'
  f1.close()
  f2    = open(pathfile2, "wb")
  for i in range(len(data)):
    pickle.dump(data[i], f2)
  f2.close()

if __name__ == '__main__':
  main()
    
    
    
