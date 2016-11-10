'''
Created on 13/09/2015

@author: Sam Hunt
'''
import glob
import remove_stopwords

def parse_all():
    '''Apply the remove_stopswords.parse() function to each email and produce the *.txt.out file'''
    for each_email in glob.glob("../res/emails/*.txt"):
        remove_stopwords.parse(each_email)

def load_strings(path_pattern):
    '''Returns the contents of all files matching the path pattern, as a list of strings'''
    contents = []
    for each_file in glob.glob(path_pattern):
        with open(each_file, "r") as current_file:
            contents.append(current_file.read())
    return contents

# Ensure all emails are parsed with latest version of stopwords.txt
parse_all()

# Load all of the parsed emails into RAM as arrays of words
# Want to keep these separate so we can append the right class variable later 
all_messages = [each_message.split() for each_message in load_strings("../res/emails/*-*.txt.out")]
all_spams = [each_message.split() for each_message in load_strings("../res/emails/spm*.txt.out")]

# Get a set of all of the unique words in all of the emails 
# These will be the inputs to perceptron so we must have an ordered list without duplicates
all_words = set([])
for each_message in all_messages:
    all_words = all_words | set(each_message)        
for each_spam in all_spams:
    all_words = all_words | set(each_spam)

# Order the set of all unique words
# Should sort these as there is no defined order in converting sets to lists, 
# And this may differ across python implementations causing issues for pickled
# Perceptron instances?
all_words = list(all_words)
all_words.sort()
print "Total number of perceptron inputs: " + str(len(all_words))

# Save the ordered list of inputs for the perceptron
with open('../res/inputs.names',"w") as fid:
    for each_word in all_words:
        fid.write(each_word)
        fid.write(",")

# Generate the data set with a record for each message
with open('../res/emails_proc.data', "w") as fid:
    for each_message in all_messages:
        message_words = set(each_message)
        for each_input in all_words:
            fid.write("1," if each_input in message_words else "0,")
        fid.write("0\n")
    for each_spam in all_spams:
        spam_words = set(each_spam)
        for each_input in all_words:
            fid.write("1," if each_input in spam_words else "0,")
        fid.write("1\n")
        