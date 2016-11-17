
# coding: utf-8

# In[1]:

def trumpSentence(text):  #trumpsentence
    import markovify
    with open(text) as f:
        text = f.read()
    text_model = markovify.Text(text)
    return(text_model.make_sentence())

save me


# In[ ]:



