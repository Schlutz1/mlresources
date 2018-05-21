
'''
ML-Core v2.0 HPO Implementation (Optunity test)

Last Modified: 05/01/2018
Author: Max Schultz

File Structure:

o wrapper.py (main):
	- provides main handler interface for Optunity solver
	- end point for ml-core integration

o optimisation_process.py
	- handles parameter space, get and try parameters for Hyperband

o load_data.py
	- imports sklearn and mnist data sets for unit testing

o save_data.py
	- saves data in splunk readable format

'''

# custom imports
from optimisation_process import train_model_mlp
from save_data import save_data

import optunity.metrics
import optunity

# standard imports
import numpy as np
import random
import time
import math
import csv


# lambda space defintion

space_classification = {'alpha': [0.001, 1],
		 'num_hidden_layers': {'one_layer': {'n_hidden_1': [1, 128]},
							   'two_layers': {'n_hidden_1': [1, 128], 'n_hidden_2': [1, 128]},
							   'three_layers': {'n_hidden_1': [1, 128], 'n_hidden_2': [1, 128], 'n_hidden_3': [1, 128]}
							   }
		 }

#main process
if __name__ == "__main__":

	#options are classification, regression and unsupervised learning
	#pmap=optunity.pmap
	hps, info, _2 = optunity.minimize_structured(train_model_mlp, space_classification, num_evals=5)

	print "optimised vals: ", hps  # results
	print "optimisation information: ", info.stats
	print "saving data..."
	save_data(hps, info)


	
