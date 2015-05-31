#!/bin/bash

pathprefix=./results/offpolicy-rndmdp-experiments/state-100-bpol-random-tpol-skewed-ftype-binary

#for alg in gtd togtd wtd wgtd wtogtd wislstd oislstd olstd2
for alg in gtd
do
for runseed in {1..1}
do
python pysrc/plot/plotdatasummarize.py $pathprefix/$alg/mdpseed_1000_runseed_$runseed.dat $pathprefix/$alg/mdpseed_1000_summarized_$runseed.dat 100

done
done
