
# coding: utf-8

# In[5]:

import re  #I still need to figure out a way to do this within the function itself. This section imports the library for Regex 

source = open('Clinton.txt') #These sections turn the text file into an object. I still need to adjust the functions to accept text files as arguments
Clinton = source.read()

source = open('Trump.txt') 
Trump = source.read()




# In[2]:

def len_indefinite(text): #this function identifies and counts all of the indefinite articles in the text, including both upper/lowercase and those that begin sections of dialogue
    
    indefinite = re.findall(' a ', text)
    indefinite2 = re.findall(' A ', text)
    indefinite3 = re.findall(' an ', text)
    indefinite4 = re.findall(' An ', text) 
    indefinite5 = re.findall('"A ', text)
    indefinite6 = re.findall('"An ', text)

    return (len(indefinite)) + (len(indefinite2)) + (len(indefinite3)) + (len(indefinite4)) + (len(indefinite5)) + (len(indefinite6))


# In[6]:

len_indefinite(Clinton)


# In[7]:

len_indefinite(Trump)


# In[8]:

def len_definite(text): #this function identifies and counts all of the definite articles in the text, including both upper/lowercase and those that begin sections of dialogue
    
    definite = re.findall(' the ', text)
    definite2 = re.findall(' The ', text)
    definite3 = re.findall('"The ', text)

    return (len(definite)) + (len(definite2)) + (len(definite3))


# In[9]:

len_definite(Clinton)


# In[10]:

len_definite(Trump)


# In[11]:

def wordcount(text): #this function finds the total number of words in the a text
  
    words = re.findall(' [A-Za-z]+', text)

    return len(words)


# In[12]:

wordcount(Clinton)


# In[13]:

wordcount(Trump)


# In[14]:

def compare_articles(text1, text2): #function calls the previously defined functions to identify the percentage of both definite/indefinite articles in each text
    
    text1_percent_indefinite = (len_indefinite(text1) / float(wordcount(text1))) * 100 #divides the number of indefinite articles by the number of words in the text and then multiplies by 100 to find the percentage
    text2_percent_indefinite = (len_indefinite(text2) / float(wordcount(text2))) * 100
    
    text1_percent_definite = (len_definite(text1) / float(wordcount(text1))) * 100 
    text2_percent_definite = (len_definite(text2) / float(wordcount(text2))) * 100
    
    return 'first text indefinite articles: ' + str(text1_percent_indefinite) + '%', 'second text indefinite articles: ' + str(text2_percent_indefinite) + '%', 'first text definite articles: ' + str(text1_percent_definite) + '%', 'second text definite articles: ' + str(text2_percent_definite) + '%'


# In[15]:

compare_articles(Clinton, Trump)


# In[ ]:



