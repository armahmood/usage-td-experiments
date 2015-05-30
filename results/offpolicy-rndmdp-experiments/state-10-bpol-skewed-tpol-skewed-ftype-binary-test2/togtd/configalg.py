
import numpy as np
import cPickle as pickle

alphas    = 10**np.arange(-5, 0.1, 1)
betas     = np.array([0.0])
lms       = np.arange(0, 1.1, .1)
configs     = [
                 {
                 'alpha'     : alpha,
                 'beta'      : beta,
                 'lmbda'    : lm
                 }
                 for alpha in alphas
                 for beta in betas
                 for lm in lms
              ]

f = open('configalg.pkl', 'wb')

pickle.dump(configs, f)
