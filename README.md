 <H2>both_sides</H2>
 
Final Project for Writing Machines (Fall 2016)

*Purpose of the Code* 

Our code comes in three bundles aimed to analyze, classify, and generate "Trumpian" and "Hilliarian" speeches. Upon beginning this project, we wondered whether we could find and, if so, measure distinctions in rhetoric, diction, or syntax between each candidate's respective nomination acceptance speeches. We were also curious whether we could use such data to discuss how each candidate's ideological differences are reflected in his or her delivery. By connecting how each candidate argues with the argumentative stances each candidate proposes, we can better examine how each delivery differs in content and structure. In the analyze and generate functions, we encourage users to interact by uploading texts of their own choosing. Users can analyze pronoun usage of any two texts in compare_pronouns() and can generate sentences and groups of sentences from any existing text in generateSentence() and generateSpeech(), respectively. 

*Analyze* 

This function, called compare_pronouns(), uses regex to find and calculate the percentage of first person singular, first person plural, and third person plural pronouns in two different texts. While the function was developed with the ultimate goal of comparing speeches by Hillary Clinton and Donald Trump, it will accept any two .txt files as an argument, allowing the user to compare any two pieces of writing that they find interesting. Users must find and save .txt files, then upload those files to python notebook. 


*Classify* 

This function imports a Naive Bayes Classifier from the TextBlob library to classify any sentence given by the user as either more Hillarian or Trumpian in nature. It was trained using sentences from Clinton and Trump's Presidential Nomination Acceptance Speeches. Using cl.classify(), users submit their chosen sentence as a string, and the classifier returns either "Clinton" or "Trump" based on salient features of the text that the program determines through machine learning. 

*Generate* 

This section includes two seperate functions, generateSentence() and generateSpeech(). It uses the markovify library to create a Markov Text Chain generator. Like Analyze, it was originally developed using speeches from Clinton and Trump. but has been generalized to accept any .txt file as an argument. Users must find and save a .txt file, then upload that file to python notebook. generateSentence() will use that file to randomly generate a single sentence of text, while generateSpeech() will generate a 5 sentence mini-speech. 

*Sample Texts*

In addition to the functions above, sample texts for both Clinton and Trump's Presidential Nomination Acceptance speeches have been attached so that they might be used with the Generate code. Users should save eace speech as a .txt file and upload it to python notebook. 



