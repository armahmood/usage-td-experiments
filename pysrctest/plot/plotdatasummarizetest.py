'''
Created on May 30, 2015

@author: A. Rupam Mahmood
'''
import unittest
import os
import sys
import pysrc.experiments.stdrwexp as stdrwexp
from pysrc.plot import plotdatasummarize
import cPickle as pickle
import numpy as np

class Test(unittest.TestCase):

  def testplotdatasummarize(self):
    T = 12
    N = 3
    dirpath  = "./pysrctest/plot/"
    dirpath = "" if not os.path.isdir(dirpath) else dirpath
    sys.argv = ["", "1", "StdRWSparseReward", dirpath]
    stdrwexp.main()
    
    sys.argv = ["", dirpath+"run_1.dat", dirpath+"run_1_1.dat", str(N)]
    plotdatasummarize.main()
    f1 = open(dirpath+"run_1.dat", "rb")
    f2 = open(dirpath+"run_1_1.dat", "rb")

    try:
      while True:
        d1  =  pickle.load(f1)
        d2  =  pickle.load(f2)
        for i in range(N):
          meanerror = np.mean(d1['error'][i*(T/N):(i+1)*(T/N)])
          assert(abs(meanerror-d2['error'][i])<10**-10)
    except EOFError:
      print("End of file reached")

if __name__ == "__main__":
  #import sys;sys.argv = ['', 'Test.testName']
  unittest.main()