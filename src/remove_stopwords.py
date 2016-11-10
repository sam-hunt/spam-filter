
from nltk.stem.porter import PorterStemmer

def parse(filename):

    punctuation= ['.',',','?',':',';','\n']
    
    #make stopwords a set for faster membership lookup later (using a large stopwords list)
    stopwords = set(open('../res/stopwords.txt', 'r').read().split())
    textwords = open(filename, 'r').read()
    
    #my extra couple of rules to reduce number of unnecessary inputs
    punctuation.extend(["'", '"', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    textwords = textwords.replace('-', ' ')
    textwords = textwords.replace('!', ' ! ')
    
    textwords = textwords.translate(None,''.join(punctuation))
    textwords = [t.strip() for t in textwords.split()]
    
    #porters algorithm inserted in here
    filteredtext = [parse.ps.stem_word(t.lower()) for t in textwords if t.lower() not in stopwords]
    
    print([t for t in filteredtext])
    fid = open('../res/emails-clean/'+filename+'.out',"w")
    for i in filteredtext:
        fid.write(i)
        fid.write(" ")
    fid.close()

#static class instance so a new instance is not constructed each time parse is called (600 times)
parse.ps = PorterStemmer()