'''
Created on Sep 30, 2014

@author: A. Rupam Mahmood

This module instantiates an algorithm on a random MDP problem 
(see van Seijen, Sutton, Mahmood, Pilarski 2015, ewrl) and runs an experiment.

'''

import os
import sys
sys.path.insert(0, os.getcwd())
import argparse
import numpy as np
from pysrc.problems import mdp
from pysrc.problems import randommdp
from pysrc.algorithms.tdprediction.onpolicy import td, tdr, totd, utd, utotd, utdr
import copy
import pickle

def runoneconfig(config, prob, alg, perf):
  prob.initTrajectory(config['runseed'])
  for t in range(config['T']):
    probstep          = prob.step()
    probstep['l']     = config['lmbda']
    probstep['lnext'] = config['lmbda']
    alg.step(probstep)
    perf.calcMSPVE(alg, t)

def main():
  parser          = argparse.ArgumentParser()
  parser.add_argument("mdpseed", help="used as a seed to generate a random MDP", type=int)
  parser.add_argument("runseed", help="used as a seed of an independent run", type=int)
  parser.add_argument("path", help="location of the result folder")
  parser.add_argument("algname", help="name of the algorithm")
  args = parser.parse_args()
  
  configprobpathname  = args.path + "configprob.pkl"
  cf              = open(configprobpathname, 'rb')
  configprob      = pickle.load(cf)  

  configalgpathname  = args.path + args.algname + "/configalg.pkl"
  cf              = open(configalgpathname, 'rb')
  configsalg      = pickle.load(cf)
    
  filepathname  = args.path + args.algname   +\
                  "/mdpseed_"  + str(args.mdpseed)   + "_"\
                  "runseed_"  + str(args.runseed)   +\
                  ".dat"
  f             = open(filepathname, 'wb')
  
  algs  = {
           'td':td.TD,
           'totd':totd.TOTD,
           'tdr':tdr.TDR,
           'utd':utd.UTD,
           'utotd':utotd.UTOTD,
           'utdr':utdr.UTDR
           }
  configprob['mdpseed'] = args.mdpseed
  prob                  = randommdp.RandomMDP(configprob)
  print("Running algorithm " + args.algname + ", runseed: " + str(args.runseed) )
  for config in configsalg:
    perf      = mdp.PerformanceMeasure(configprob, prob)
    config.update(configprob)
    alg                   = algs[args.algname](config)
    config['runseed']     = args.runseed
    runoneconfig(config, prob, alg, perf)
    config['error']      = perf.getNormMSPVE()
    pickle.dump(config, f, -1)

if __name__ == '__main__':
    main()
    
