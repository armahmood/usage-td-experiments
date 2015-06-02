'''
Created on Jun 2, 2014

@author: ashique
'''

import numpy as np
import pylab as pl
from pysrc.algorithms.tdprediction.tdprediction import TDPrediction

class UTOTD(TDPrediction):
  
  def __init__(self, config):
    
    self.nf     = config['nf']
    self.eta    = config['eta']
    self.initd  = config['initd']
    self.th     = np.zeros(self.nf)
    self.z      = np.zeros(self.nf)
    self.d      = np.ones(self.nf)*self.initd
    self.predprev = 0.
    
  def initepisode(self):
    self.z = np.zeros(self.nf)
    self.u = np.zeros(self.nf)
    self.v = np.zeros(self.nf)
    
  def step(self, params):
    phi=params['phi']; R=params['R']; phinext=params['phinext']
    g=params['g']; l=params['l']; gnext=params['gnext']
    
    self.d        = self.d - self.eta*phi*phi*self.d \
            + phi*phi
    dtemp    = np.copy(self.d)
    dtemp[dtemp==0.0] = 1
    alpha         = 1/dtemp
    alphaphi      = alpha*phi
    
    prednext      = np.dot(phinext,self.th)
    self.z        = alphaphi \
            + g*l*(self.z - np.dot(phi,self.z)*alphaphi)
    self.th       = self.th + (R+gnext*prednext-self.predprev)*self.z \
            + (self.predprev-np.dot(self.th,phi))*alphaphi

    self.predprev = prednext
    


