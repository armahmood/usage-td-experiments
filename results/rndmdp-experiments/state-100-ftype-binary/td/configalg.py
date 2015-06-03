
import numpy as np
import cPickle as pickle

alphas    = 10**np.arange(-3, 0.1, .25)
lms       = np.concatenate((np.arange(0, .9, .1), np.arange(.9, 1.01, .01)))
configs     = [
                 {
                 'alpha'     : alpha,
                 'lmbda'    : lm
                 }
                 for alpha in alphas
                 for lm in lms
              ]

f = open('configalg.pkl', 'wb')

pickle.dump(configs, f)
