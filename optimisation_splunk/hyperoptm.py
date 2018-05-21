
'''
ML-Core v3.0 HPOA (Optunity)
'''

# custom imports
#from hyperoptm_process import train_model
from load_data import load_data
from save_data import save_data

from threading import Timer

import optunity.metrics
import optunity

# standard imports
import numpy as np
import random
import time
import math
import csv
import os, sys

# splunk system

print("resp")

space_classification = {'alpha': [0.001, 1],
		 'num_hidden_layers': {'one_layer': {'n_hidden_1': [1, 128]},
							   'two_layers': {'n_hidden_1': [1, 128], 'n_hidden_2': [1, 128]},
							   'three_layers': {'n_hidden_1': [1, 128], 'n_hidden_2': [1, 128], 'n_hidden_3': [1, 128]}
							   }
		 }

splunk_path = os.environ['SPLUNK_HOME']
#splunk_path = "/Applications/Splunk"
filename = splunk_path+"/etc/apps/aiam-ml-core/lookups/"+sys.argv[2]
max_evals = int(sys.argv[3])

path_to_file = filename
x_train, x_test, y_train, y_test = load_data(
	path_to_file)

# optimisation process

@optunity.cross_validated(x=x_train, y=y_train, num_folds=2, num_iter=2)
def train_model(x_train, y_train, x_test, y_test, alpha=0, num_hidden_layers='one_layer', n_hidden_1=0, n_hidden_2=0, n_hidden_3=0):

	from sklearn.neural_network import MLPClassifier

	n_hidden_list = []
	n_hidden_list.append(int(n_hidden_1))
	if n_hidden_2 != None:
		n_hidden_list.append(int(n_hidden_2))
		if n_hidden_3 != None:
			n_hidden_list.append(int(n_hidden_3))

	# train and fit model
	model = MLPClassifier(solver='lbfgs', alpha=alpha,
								  hidden_layer_sizes=n_hidden_list, random_state=1)
	model.fit(x_train, y_train)
	score = model.score(x_test, y_test) #standard score model
			
	#print "Iteration Number: ", iteration_counter
	#print "score: ", score
	#print "params: ", alpha, n_hidden_1, n_hidden_2, n_hidden_3
	return score

#MAIN MODEL

try :
	hps, info, _2 = optunity.minimize_structured(train_model, space_classification, num_evals=max_evals, pmap=optunity.pmap)
	#hps = 1
	print("Hyperparameter Optimization Successful") 
	print("Convergence achieved in %d iterations") % max_evals
except Exception, e :
	print("Hyperparameter Optimization Failed: "), e
#print "saving data..."
save_data(hps, info)


	
