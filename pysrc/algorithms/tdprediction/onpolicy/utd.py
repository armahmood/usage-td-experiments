'''
Created on January, 2015

@author: A Rupam Mahmood
'''

import numpy as np
import pylab as pl
from pysrc.algorithms.tdprediction.tdprediction import TDPrediction

class UTD(TDPrediction):
  
  def __init__(self, config):
    
    self.nf = config['nf']
    self.th = np.zeros(self.nf)
    self.z = np.zeros(self.nf)
    self.eta    = config['eta']
    self.initd  = config['initd']
    self.d      = np.ones(self.nf)*self.initd
    self.v      = np.zeros(self.nf)
    
  def initepisode(self):
    self.z = np.zeros(self.nf)
    
  def step(self, params):
    phi=params['phi']; R=params['R']; phinext=params['phinext']
    g=params['g']; l=params['l']; gnext=params['gnext']
    
    self.d        = self.d - self.eta*phi*phi*self.d \
            + phi*phi 
    self.dtemp    = np.copy(self.d)
    self.dtemp[self.dtemp==0.0] = 1
    alpha         = 1/self.dtemp

    delta = R + gnext*np.dot(phinext,self.th) - np.dot(phi, self.th)
    self.z = g*l*self.z + phi
    self.th += delta*alpha*self.z


