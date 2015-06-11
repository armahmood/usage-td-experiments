#!/bin/bash


for runseed in {1..50}
do
for alg in td tdr totd utd utdr utotd
do

echo '#!/bin/bash 
#PBS -S /bin/bash 
#PBS -M ashique@ualberta.ca
#PBS -m bea
#PBS -l walltime=01:00:00
#PBS 
cd $PBS_O_WORKDIR 
echo "Current working directory is `pwd`" 
module load application/python/2.7.3 

time python ./pysrc/experiments/rndmdpexp.py 1000 '$runseed'  ~/usage-td-experiments2/usage-td-experiments/results/rndmdp-experiments/state-100-ftype-binary/ '$alg' > '$alg'-'$runseed'.txt' > $alg-$runseed.pbs 

qsub $alg-$runseed.pbs

done

done

