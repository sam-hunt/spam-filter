'''
Created on 12/09/2015

@author: Sam Hunt
'''

import numpy as np
import pcn
import save_perceptron as sp

emails = np.loadtxt('../res/emails_proc.data', delimiter=",")
print "../res/emails_proc.data loaded."

#will still compile if number of inputs changes 
nInputs = np.shape(emails)[1]

#Keep track of the overall highest success rate NN 
highest_overall_sr, best_nn = 0, None
#Keep track of the highest success rate NN with 0 false positives
highest_sr_nofp, best_nn_nofp = 0, None
 
#Train 100 NNs with various learning rates, numbers of training iterations, and shuffle subsets
for learning_rate in [0.1,0.25,0.5,0.75,1]:
    for training_iterations in [50,200,500,1000]:
        for shuffle_iterations in xrange(0,5):
            #shuffle the email data-set records
            np.random.shuffle(emails)
            
            #use the first half for training, second half for testing 
            trainin = emails[0:300,:nInputs-1]
            testin = emails[300:600,:nInputs-1]
            traintgt = emails[0:300,nInputs-1:nInputs]
            testtgt = emails[300:600,nInputs-1:nInputs]

            #create a new empty perceptron and train it
            p = None
            p = pcn.pcn(trainin, traintgt)
            p.pcntrain(trainin, traintgt, learning_rate, training_iterations)
            
            #test the trained perceptron and store the resulting confusion matrix and success rate
            cm, sr = p.confmat(testin, testtgt)
            
            print "LR: ", learning_rate, "    TI: ", training_iterations, "    SI: ", shuffle_iterations, "    SR: ", int(sr*100), "%    FP: ", cm[0][1]
            
            #commit to disk and log the networks and with the highest success rates
            if (sr > highest_overall_sr):
                sp.save(p, "highest_overall_sr_pcn", cm, sr, learning_rate, training_iterations, 0)
                highest_overall_sr, best_nn = sr, p
            if ((cm[0][1] == 0) and sr > highest_sr_nofp):
                sp.save(p, "highest_sr_no_false_positives_pcn", cm, sr, learning_rate, training_iterations, 0)
                highest_sr_nofp, best_nn_nofp = sr, p
