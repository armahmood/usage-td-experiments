
import numpy as np
import cPickle as pickle

  
initas    = 10**np.arange(-3, 3.1, 1.)
lms       = np.arange(0, 1.1, .1)
configs     = [
                 {
                 'inita'     : inita,
                 'lmbda'    : lm
                 }
                 for inita in initas
                 for lm in lms
              ]

f = open('configalg.pkl', 'wb')

pickle.dump(configs, f)
