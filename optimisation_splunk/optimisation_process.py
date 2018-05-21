# optimisation process

# algo imports
from load_data import load_data

from threading import Timer

import optunity
import os, sys

# load data
path_to_file = None
x_train, x_test, y_train, y_test = load_data(
	path_to_file)

iteration_counter = 0
timer_length = 15

def kms() :
	print "ended"
	sys.exit()


t = Timer(timer_length, kms)
t.start() 

#@optunity.cross_validated(x=x_train, y=y_train, num_folds=2, num_iter=2)
def train_model_mlp(alpha=0, num_hidden_layers='one_layer', n_hidden_1=0, n_hidden_2=0, n_hidden_3=0):

	from sklearn.neural_network import MLPClassifier
	global iteration_counter

	n_hidden_list = []
	n_hidden_list.append(int(n_hidden_1))
	if n_hidden_2 != None:
		n_hidden_list.append(int(n_hidden_2))
		if n_hidden_3 != None:
			n_hidden_list.append(int(n_hidden_3))

	# train and fit model
	model = MLPClassifier(solver='lbfgs', alpha=alpha,
						  hidden_layer_sizes=n_hidden_list, random_state=1)
	#model.fit(x_train, y_train)
	#score = model.score(x_test, y_test) #standard score model
	
	print "Iteration Number: ", iteration_counter
	#print "score: ", score
	print "params: ", alpha, n_hidden_1, n_hidden_2, n_hidden_3
	iteration_counter += 1
	return 0

def train_model_sgd() :
	
	from sklearn.linear_model import SGDClassifier
	return None

def train_model_rf() :
	return None