# spam-filter

A simple spam filter using neural networks.

![image](/res/Untitled.png?raw=true "Visualisation of MLP accuracy as number of hidden nodes increases.")

The algorithm uses two supervised machine learning algorithms:
 - the single-layer-perceptron (SLP) and
 - the multi-layer-perception (MLP)

to generate black-box neural networks which can accurately classify email texts as spam or not spam, based on a set of sample emails 
which have already been classified.

Bitsets were generated for each word found, after applying the porter stemmer algorithm to group words with the same meaning. 
These were then used to train multiple networks by partitioning the data into training, testing, and validation sets, 
and then ranking network instances based on the number of correct classifications, false positives, and false negatives.

A more in-depth explanation, as well as sample resultsets, can be found in the [readme](/doc/README.pdf) file created for the assignment.
