# Random MDP experiments on usage-based step-size adaptation applied to TD


This project contains random MDP experiments evaluating the usage-based step-size adaptation idea (Mahmood & Sutton 2015) applied to true online TD (TOTD) (van Seijen & Sutton 2014) and TD with accumulating traces (TD) (Sutton & Barto 1998).

This project can be imported as an Eclipse Pydev project.

In order to run the experiment on the randomly generated MDP with 10 state and generate plot, execute `run-rndmdp-experiments10.sh`.

In order to run the experiment on the randomly generated MDP with 100 state and generate plot, execute `run-rndmdp-experiments100.sh`.


## Unit tests

Use the following from the root directory:

`python -m unittest discover --pattern=*.py`

## References

Mahmood, A. R., Sutton R. S. (2015). Off-policy learning based on weighted importance sampling with linear computational complexity. In *Proceedings of the 301st Conference on Uncertainty in Arti- ficial Intelligence* Amsterdam, Netherlands.

Sutton, R. S., Barto, A. G. (1998). *Reinforcement Learning: An Introduction*. MIT Press.

van Seijen, H., Sutton, R. S. (2014). True online TD(lambda). In *Proceedings of the 31st International Conference on Machine Learning*. JMLR W&CP 32(1):692-700.

