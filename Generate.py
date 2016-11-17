
# coding: utf-8

# In[ ]:

def generate(text):
    import markovify
    with open(text) as f:
        text = f.read()

    text_model = markovify.Text(text)
    return(text_model.make_sentence())

