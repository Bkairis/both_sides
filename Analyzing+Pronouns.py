
# coding: utf-8

# In[2]:

import re  #I still need to figure out a way to do this within the function itself. This section imports the library for Regex 

source = open('Clinton.txt') #These sections turn the text file into an object. I still need to adjust the functions to accept text files as arguments
Clinton = source.read()

source = open('Trump.txt') 
Trump = source.read()




# In[3]:

def wordcount(text): #this function finds the total number of words in the a text
  
    words = re.findall(' [A-Za-z]+', text)

    return len(words)


# In[12]:

wordcount(Clinton)


# In[13]:

wordcount(Trump)


# In[11]:

def first_person_singular(text): 
    #I, me, my, mine
    
    fps = re.findall(' I ', text) #I is never lowercase, so no need to include
    fps1 = re.findall('"I ', text) #dialogue
    fps2 = re.findall(' me', text)#me does not begin sentences, so no need to include uppercase or dialogue. 
    fps3 = re.findall(' my ', text) #lowercase
    fps4 = re.findall(' My ', text) #uppercase
    fps5 = re.findall('"My ', text) #dialogue
    fps6 = re.findall(' mine ', text) #lowercase, doesn't begine sentences so no need to include uppercase or dialogue. 
    
    return (len(fps)) + (len(fps1)) + (len(fps2)) + (len(fps3)) + (len(fps4)) + (len(fps5)) + (len(fps6))


# In[12]:

first_person_singular(Clinton)


# In[13]:

first_person_singular(Trump)


# In[14]:

def first_person_plural(text):  
    #we, us, our, ours
    
    fpp = re.findall(' we ', text) #lowercase
    fpp1 = re.findall(' We ', text) #uppercase
    fpp2 = re.findall('"We ', text) #dialogue 
    fpp3 = re.findall(' us ', text) #doesn't begin sentences, no uppercase or dialoguwe required 
    fpp4 = re.findall(' our ', text) #lowercase
    fpp5 = re.findall(' Our ', text) #uppercase
    fpp6 = re.findall('"Our ', text) #dialogue
    fpp7 = re.findall(' ours ', text) #lowercase
    fpp8 = re.findall(' Ours ', text) #uppercase
    fpp9 = re.findall('"Ours ', text) #dialogue
    
    return (len(fpp)) + (len(fpp1)) + (len(fpp2)) + (len(fpp3)) + (len(fpp4)) + (len(fpp5)) + (len(fpp6)) + (len(fpp7)) + (len(fpp8)) + (len(fpp9))
    


# In[15]:

first_person_plural(Clinton)


# In[16]:

first_person_plural(Trump)


# In[17]:

def third_person_plural(text):   
    #they, them, their, theirs, they're
    
    tpp = re.findall(' they ', text) #lowercase
    tpp1 = re.findall( ' They ', text) #uppercase
    tpp2 = re.findall('They ', text) #dialogue 
    tpp3 = re.findall(' them ', text) #doesn't begin sentences, no uppercase or dialogue required
    tpp4 = re.findall(' their ', text) #lowercase
    tpp5 = re.findall(' Their ', text) #uppercase
    tpp6 = re.findall('"Their ', text) #dialogue
    tpp7 = re.findall(' theirs ', text) #lowercase
    tpp8 = re.findall(' Theirs ', text) #uppercase
    tpp9 = re.findall('"Theirs ', text) #dialogue
    tpp10 = re.findall(" they're ", text) #lowercase
    tpp11 = re.findall(" They're ", text) #uppercase
    
    return (len(tpp)) + (len(tpp1)) + (len(tpp2)) + (len(tpp3)) + (len(tpp4)) + (len(tpp5)) + (len(tpp6)) + (len(tpp7)) + (len(tpp8)) + (len(tpp9)) + (len(tpp10)) + (len(tpp11)) 
    


# In[18]:

third_person_plural(Clinton) 


# In[19]:

third_person_plural(Trump)


# In[20]:

def compare_pronouns(text1, text2): #function calls the previously defined functions to identify the percentage of first person singular, first person plural, and third person plural pronouns in the texts
    
    text1_percent_fps = (first_person_singular(text1) / float(wordcount(text1))) * 100 #divides the number of first person singular pronouns by the number of words in the text and then multiplies by 100 to find the percentage
    text2_percent_fps = (first_person_singular(text2) / float(wordcount(text2))) * 100
    
    text1_percent_fpp = (first_person_plural(text1) / float(wordcount(text1))) * 100   #percentage of first person plural pronouns
    text2_percent_fpp = (first_person_plural(text2) / float(wordcount(text2))) * 100
    
    text1_percent_tpp = (third_person_plural(text1) / float(wordcount(text1))) * 100    #percentage of third person plural pronouns
    text2_percent_tpp = (third_person_plural(text2) / float(wordcount(text2))) * 100
    
    return 'first text first person singular pronouns: ' + str(text1_percent_fps) + '%', 'second text first person singular pronouns: ' + str(text2_percent_fps) + '%', 'first text first person plural pronouns: ' + str(text1_percent_fpp) + '%', 'second text first person plural pronouns: ' + str(text2_percent_fpp) + '%', 'first text third person plural pronouns: ' + str(text1_percent_tpp) + '%', 'second text third person plural pronouns: ' + str(text2_percent_tpp) + '%'                                                                       


# In[21]:

compare_pronouns(Clinton, Trump)


# In[ ]:



