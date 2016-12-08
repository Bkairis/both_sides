def compare_pronouns(text1, text2):#function calls the previously defined functions to identify the percentage of first person singular, first person plural, and third person plural pronouns in the texts
   
    import re
    
    def convert(textfile): #this takes an argument as a textfile and opens it. Any time the function is called, it treats the text file as an object (which can then be named within the function depending on its purpose)
        source = open(textfile)
        return source.read()
    
    def wordcount(text): #this function finds the total number of words in the a text
        text = convert(text)
        words = re.findall(' [A-Za-z]+', text)
        return len(words)
    
    def first_person_singular(text): #I, me, my, mine
        text = convert(text)
        fps = re.findall(' I ', text) #I is never lowercase, so no need to include
        fps1 = re.findall('"I ', text) #dialogue
        fps2 = re.findall(' me', text)#me does not begin sentences, so no need to include uppercase or dialogue. 
        fps3 = re.findall(' my ', text) #lowercase
        fps4 = re.findall(' My ', text) #uppercase
        fps5 = re.findall('"My ', text) #dialogue
        fps6 = re.findall(' mine ', text) #lowercase, doesn't begine sentences so no need to include uppercase or dialogue. 
        return (len(fps)) + (len(fps1)) + (len(fps2)) + (len(fps3)) + (len(fps4)) + (len(fps5)) + (len(fps6))
    
    def first_person_plural(text):  #we, us, our, ours
        text = convert(text)
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
    
    def third_person_plural(text):   #they, them, their, theirs, they're
        text = convert(text)
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
    
    
    text1_percent_fps = (first_person_singular(text1) / float(wordcount(text1))) * 100 #divides the number of first person singular pronouns by the number of words in the text and then multiplies by 100 to find the percentage
    text2_percent_fps = (first_person_singular(text2) / float(wordcount(text2))) * 100
    
    text1_percent_fpp = (first_person_plural(text1) / float(wordcount(text1))) * 100   #percentage of first person plural pronouns
    text2_percent_fpp = (first_person_plural(text2) / float(wordcount(text2))) * 100
    
    text1_percent_tpp = (third_person_plural(text1) / float(wordcount(text1))) * 100    #percentage of third person plural pronouns
    text2_percent_tpp = (third_person_plural(text2) / float(wordcount(text2))) * 100
    
    return 'Text 1 first person singular pronouns: ' + str(text1_percent_fps) + '%', 'Text 2 first person singular pronouns: ' + str(text2_percent_fps) + '%', 'Text 1 first person plural pronouns: ' + str(text1_percent_fpp) + '%', 'Text 2 first person plural pronouns: ' + str(text2_percent_fpp) + '%', 'Text 1 third person plural pronouns: ' + str(text1_percent_tpp) + '%', 'Text 2 third person plural pronouns: ' + str(text2_percent_tpp) + '%'                                                                       
