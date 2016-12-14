
# coding: utf-8

def generateSentence(text):   #generalized to accept any .txt file 
    import markovify  #imports Markov text chain generator 
    with open(text) as f:  
        text = f.read()  #converts .txt file to an object
    text_model = markovify.Text(text) #trains markovify using the text object
    return(text_model.make_sentence()) #returns a single newly-generated sentence


def generateSpeech(text): 
    import markovify
    with open(text) as f: 
        text = f.read()     
    text_model = markovify.Text(text)  
    for i in range(5): #produces a 5 sentence speech 
        print (text_model.make_sentence())



 


