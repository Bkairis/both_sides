
# coding: utf-8

# In[39]:

Example = [
    ('Friends, delegates and fellow Americans: I humbly and gratefully accept your nomination for the presidency of the United States.', 'Trump'),
    ('Together, we will lead our party back to the White House, and we will lead our country back to safety, prosperity, and peace.', 'Trump'),
    ('We will be a country of generosity and warmth.', 'Trump'),
    ('But we will also be a country of law and order.', 'Trump'),
    ('Our Convention occurs at a moment of crisis for our nation. ', 'Trump'),
    ('Thank you!', 'Clinton',
    ('Thank you all very much!', 'Clinton'),
    ('Thank you for that amazing welcome.', 'Clinton'),
    ('Thank you all for the great convention that we’ve had.', 'Clinton'),
    ('And Chelsea, thank you.', 'Clinton'),
]


# In[40]:

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(Example)


# In[6]:

import markovify


# In[11]:

with open('Trump.txt') as f:
    text = f.read()


# In[25]:

text_model = markovify.Text(text)


# In[26]:

for i in range(5):
    print(text_model.make_sentence())


# In[20]:

for i in range(5):
    print(text_model.make_sentence())


# In[82]:

def trumpSentence(text):  #trumpsentence
    import markovify
    with open(text) as f:
        text = f.read()
    text_model = markovify.Text(text)
    return(text_model.make_sentence())


# In[38]:

generate('Clinton.txt')


# In[52]:

from textblob import TextBlob


# In[72]:

example = [
    ("Friends, delegates and fellow Americans I humbly and gratefully accept your nomination for the presidency of the United States.", 'Trump'),
    ("Together, we will lead our party back to the White House, and we will lead our country back to safety, prosperity, and peace.", 'Trump'),
    ("We will be a country of generosity and warmth.", 'Trump'),
    ("But we will also be a country of law and order.", 'Trump'),
    ("Our Convention occurs at a moment of crisis for our nation.", 'Trump'),
    ("The attacks on our police, and the terrorism in our cities, threaten our very way of life.", 'Trump'),
    ("Any politician who does not grasp this danger is not fit to lead our country.", 'Trump'),
    ("Americans watching this address tonight have seen the recent images of violence in our streets and the chaos in our communities.", 'Trump'),
    ("Many have witnessed this violence personally, some have even been its victims.", 'Trump'),
    ("I have a message for all of you: the crime and violence that today afflicts our nation will soon come to an end.", 'Trump'),
    ("Thank you!", 'Clinton'),
    ("Thank you all very much!", 'Clinton'),
    ("Thank you for that amazing welcome.", 'Clinton'),
    ("Thank you all for the great convention that we’ve had.", 'Clinton'),
    ("And Chelsea, thank you.", 'Clinton'),
    ("I am so proud to be your mother and so proud of the woman you have become.", 'Clinton'),
    ("Thank you for bringing Marc into our family, and Charlotte and Aidan into the world.", 'Clinton'),
    ("And Bill, that conversation we started in the law library 45 years ago, it is still going strong.", 'Clinton'),
    ("Thank you all for the great convention that we’ve had.", 'Clinton'),
    ("You know that conversation has lasted through good times that filled us with joy, and hard times that tested us.", 'Clinton')
]


# In[73]:

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(example)


# In[75]:

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')


# In[76]:

example = [
    ("Friends, delegates and fellow Americans I humbly and gratefully accept your nomination for the presidency of the United States.", 'Trump'),
    ("Together, we will lead our party back to the White House, and we will lead our country back to safety, prosperity, and peace.", 'Trump'),
    ("We will be a country of generosity and warmth.", 'Trump'),
    ("But we will also be a country of law and order.", 'Trump'),
    ("Our Convention occurs at a moment of crisis for our nation.", 'Trump'),
    ("The attacks on our police, and the terrorism in our cities, threaten our very way of life.", 'Trump'),
    ("Any politician who does not grasp this danger is not fit to lead our country.", 'Trump'),
    ("Americans watching this address tonight have seen the recent images of violence in our streets and the chaos in our communities.", 'Trump'),
    ("Many have witnessed this violence personally, some have even been its victims.", 'Trump'),
    ("I have a message for all of you: the crime and violence that today afflicts our nation will soon come to an end.", 'Trump'),
    ("Thank you!", 'Clinton'),
    ("Thank you all very much!", 'Clinton'),
    ("Thank you for that amazing welcome.", 'Clinton'),
    ("Thank you all for the great convention that we’ve had.", 'Clinton'),
    ("And Chelsea, thank you.", 'Clinton'),
    ("I am so proud to be your mother and so proud of the woman you have become.", 'Clinton'),
    ("Thank you for bringing Marc into our family, and Charlotte and Aidan into the world.", 'Clinton'),
    ("And Bill, that conversation we started in the law library 45 years ago, it is still going strong.", 'Clinton'),
    ("Thank you all for the great convention that we’ve had.", 'Clinton'),
    ("You know that conversation has lasted through good times that filled us with joy, and hard times that tested us.", 'Clinton')
]


# In[77]:

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(example)


# In[78]:

cl.classify('We are in crisis.')


# In[79]:

cl.classify('Border crossers will attack our police.')


# In[80]:

cl.classify('Thank you.')


# In[81]:

cl.classify('We will be a country of generosity and warmth.')


# In[100]:

def randomClassify():
    sentence=trumpSentence('trump.txt')
    return cl.classify(sentence)


# In[111]:

randomClassify()


# In[ ]:




# In[ ]:



