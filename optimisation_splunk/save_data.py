# save data
import logging

import time
import csv
import os


def save_data(hps, info):

    iteration, tmp, write_list = 1, [], []

    # unzips data from info object

    _time = str(time.time())
    trial = " parallel_testing"
    directory = "output_data/" + trial + "_"  + _time
    

    if not os.path.exists(directory):
    	os.makedirs(directory)

    for a, nh1, nh2, nh3, val in zip(info.call_log['args']['alpha'], info.call_log['args']['n_hidden_1'], info.call_log['args']['n_hidden_2'], info.call_log['args']['n_hidden_3'], info.call_log['values']):
        tmp.append(iteration)
        tmp.append(a)
        tmp.append(nh1)
        tmp.append(nh2)
        tmp.append(nh3)
        tmp.append(val)
        write_list.append(tmp)
        iteration += 1
        tmp = []

    # writes data from object to csv
    output_path = directory + "/" + trial + _time + ".csv"
    output_path_log = output_path[:-4] + ".log"
    header = ['iteration', 'alpha', 'n_hidden_1',
              'n_hidden_2', 'n_hidden_3', 'score']
    with open(output_path, 'wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(header)
        wr.writerows(write_list)

    logging.basicConfig(filename=output_path_log, level=logging.DEBUG)
    logging.info("Performance: ")
    logging.info(info.stats)
    logging.info("Tested Values: ")
    logging.info(info.call_log)