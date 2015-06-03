'''
Created on May 12, 2015

@author: A. Rupam Mahmood
'''

import os
import sys
sys.path.insert(0, os.getcwd())
import numpy as np
import matplotlib.pyplot as ppl
from pysrc.plot import plotdataprocess 
import cPickle as pickle

def plotperfvslmbda(pathfileprefix, label, params):
  plotfilename      = pathfileprefix+"perfvs"+params[-1]+".plot"
  if not os.path.isfile(plotfilename):
    sys.argv  = params
    plotdataprocess.main()
  plotfile    = file(plotfilename, "rb")
  data        = pickle.load(plotfile)
  ppl.plot(data[:,0], data[:,1], label=label)
  ppl.ylim([0,1])

def main():
  path                = "./results/rndmdp-experiments/state-10-ftype-binary/"
  if not os.path.exists(path):
    path = "../."+path
  pathfileprefix      = path+"td/mdpseed_1000_runseed_"
  plotperfvslmbda(pathfileprefix, "TD", ["", "5", pathfileprefix, "2", "alpha", "lmbda", "1", "lmbda"])
  pathfileprefix      = path+"utd/mdpseed_1000_runseed_"
  plotperfvslmbda(pathfileprefix, "UTD", ["", "5", pathfileprefix, "3", "eta", "initd", "lmbda", "1", "lmbda"])
  pathfileprefix      = path+"totd/mdpseed_1000_runseed_"
  plotperfvslmbda(pathfileprefix, "TOTD", ["", "5", pathfileprefix, "2", "alpha", "lmbda", "1", "lmbda"])
  pathfileprefix      = path+"utotd/mdpseed_1000_runseed_"
  plotperfvslmbda(pathfileprefix, "UTOTD", ["", "5", pathfileprefix, "3", "eta", "initd", "lmbda", "1", "lmbda"])
  ppl.legend()

if __name__ == '__main__':
  main()
  ppl.show()
  