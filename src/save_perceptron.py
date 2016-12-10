'''
Created on 13/09/2015

@author: Sam Hunt
'''

import pickle

def save(p_instance, filename, confmat, success_rate, learning_rate, training_iterations=0, hidden_nodes=0):
    '''save the serialised perceptron and log its settings/output'''
    with open("../out/" + filename + ".p", 'wb') as handle:
        pickle.dump(p_instance, handle)
    with open("../out/" + filename + ".txt", 'w') as handle:
        if (hidden_nodes>0):
            handle.write("hidden nodes: " + str(hidden_nodes) + '\n')
        if (training_iterations>0):
            handle.write("training iterations: " + str(training_iterations) + '\n')
        handle.write("\nlearning rate: " + str(learning_rate) + '\n')
        handle.write("\nconfusion matrix: \n" + str(confmat) + '\n')
        handle.write("\nsuccess rate: " + str(success_rate) + '\n')
        handle.write("\nfalse positives: " + str(confmat[0][1]) + '\n')
        handle.write("\nfalse negatives: " + str(confmat[1][0]) + '\n')
