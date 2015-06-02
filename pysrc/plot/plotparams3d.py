'''
Created on Apr 8, 2015

@author: A. Rupam Mahmood
'''

import os
import sys
sys.path.insert(0, os.getcwd())
from pysrc.plot import plotdataprocess
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as ppl
import pickle
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D  # @UnresolvedImport
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def plotonealg(algname, nparams, params, nparamssub, paramssub):
  path = "./results/offpolicy-rndmdp-experiments/state-100-bpol-random-tpol-skewed-ftype-binary/"+algname+"/"
  if not os.path.exists(path):
    path = "../."+path
  pathfileprefix      = path+"mdpseed_1000_summarized100_"
  #plotfilesuffix      = "perfvs"+paramssub[-1]+".plot"
  middlestr = ""
  for i in range(len(paramssub)): middlestr+=paramssub[i]
  plotfilesuffix      = "perfvs"+middlestr+".plot"
  nruns               = 50
  #if not os.path.isfile(pathfileprefix+plotfilesuffix):
  plotdataprocess.main2(nruns, pathfileprefix, nparams, params, nparamssub, paramssub, 0)
  data   = pickle.load(file(pathfileprefix+plotfilesuffix))
  #ppl.errorbar(data[:,0].T, data[:,2].T, data[:,2].T, label=algname)
  fig   = ppl.figure()
  ax    = fig.gca(projection='3d')
  r     = len(np.unique(data[:,0]))
  c     = len(np.unique(data[:,1]))
  X     = np.reshape(data[:,0], (r, c))
  Y     = np.reshape(data[:,1], (r, c))
  X     = np.log(X)/np.log(10)
  Z     = np.reshape(data[:,2], (r, c))
  W     = np.reshape(data[:,3], (r, c))
  print Z[:,4]
  print W[:,4]
  Z[Z>0.5]= None
  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,  # @UndefinedVariable
        linewidth=0, antialiased=False, vmin = 0.2, vmax = 0.3)
  ax.set_zlim(0.1, 0.3)  
  ax.zaxis.set_major_locator(LinearLocator(10))
  ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
  
  fig.colorbar(surf, shrink=0.5, aspect=5)

  
def main():

#   plotonealg("gtd", 3, ["alpha", "beta", "lmbda"], 1, ["lmbda"])
#   plotonealg("togtd", 3, ["alpha", "beta", "lmbda"], 2, ["alpha", "lmbda"])
#    plotonealg("wtd", 3, ["eta", "initd", "lmbda"], 2, ["initd", "lmbda"])
#   plotonealg("wgtd", 4, ["eta", "initd", "beta", "lmbda"], 1, ["lmbda"])
#   plotonealg("wtogtd", 4, ["eta", "initd", "beta", "lmbda"], 1, ["lmbda"])
#   plotonealg("oislstd", 2, ["inita", "lmbda"], 1, ["lmbda"])
#   plotonealg("wislstd", 2, ["inita", "lmbda"], 2, ["inita", "lmbda"])
  plotonealg("olstd2", 2, ["inita", "lmbda"], 2, ["inita", "lmbda"])
  #ppl.ylim([0.1, .3])
  #ppl.yscale('log')
  #ppl.xscale('log')
  #ppl.legend()
  #ppl.savefig('tmp.png')
  
if __name__ == '__main__':
    main()
    #ppl.show()
