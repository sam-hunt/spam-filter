'''
Created on 13/09/2015

@author: Sam Hunt
'''

import numpy as np
import pylab as pl
import mlp
import save_perceptron as sp

emails = np.loadtxt('../res/emails_proc.data', delimiter=",")
print "../res/emails_proc.data loaded."

#will still compile if number of inputs changes 
nInputs = np.shape(emails)[1]

#Keep track of the overall highest success rate NN 
highest_overall_sr = 0
#Keep track of the highest success rate NN with 0 false positives
highest_sr_nofp = 0

#Train 125 NNs with various learning rates, numbers of training iterations, and shuffle subsets
for learning_rate in [0.1]:
    for hidden_nodes in [1, 2, 3]:
        #for iterations in [50, 100, 200, 300]:
        for shuffle_iterations in xrange(0,10):
            #shuffle the email data-set records
            np.random.shuffle(emails)
            
            #use the first half for training, second half for testing 
            trainin = emails[0:200,:nInputs-1]
            validin = emails[200:400,:nInputs-1]
            testin = emails[400:600,:nInputs-1]
            traintgt = emails[0:200,nInputs-1:nInputs]
            validtgt = emails[200:400,nInputs-1:nInputs]
            testtgt = emails[400:600,nInputs-1:nInputs]

            #create a new empty mlp and train it
            p = None
            p = mlp.mlp(trainin, traintgt, hidden_nodes)
            p.earlystopping(trainin, traintgt, validin, validtgt, learning_rate)
            #p.mlptrain(trainin, traintgt, learning_rate, iterations)
            
            #test the trained perceptron and store the resulting confusion matrix and success rate
            cm, sr = p.confmat(testin, testtgt)
            
            print "LR: ", learning_rate, "    HN: ", hidden_nodes, "    SR: ", int(sr*100), "%    FP: ", cm[0][1]
            pl.plot_date(hidden_nodes, sr)
            
            #commit to disk and log the networks and with the highest success rates
            if (sr > highest_overall_sr):
                sp.save(p, "highest_overall_sr_mlp", cm, sr, learning_rate, 0, hidden_nodes)
                highest_overall_sr, best_nn = sr, p
            if ((cm[0][1] == 0) and sr > highest_sr_nofp):
                sp.save(p, "highest_sr_no_false_positives_mlp", cm, sr, learning_rate, 0, hidden_nodes)
                highest_sr_nofp, best_nn_nofp = sr, p
pl.show()