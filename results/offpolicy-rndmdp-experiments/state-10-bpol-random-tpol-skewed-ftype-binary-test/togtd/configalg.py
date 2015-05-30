
import numpy as np
import cPickle as pickle

alphas    = 10**np.arange(-3, 0.1, 0.5)
betas     = np.array([0.0, 0.01, 0.1])
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
