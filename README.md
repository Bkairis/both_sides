# both_sides
Final Project for Writing Machines (Fall 2016)

*Purpose of Code* 

*Analyze* 

This function, called compare_pronouns(), uses regex to find and calculate the percentage of first person singular, first person plural, and third person plural pronouns in two different texts. While the function was developed with the ultimate goal of comparing speeches by Hillary Clinton and Donald Trump, it will accept any two .txt files as an argument, allowing the user to compare any two pieces of writing that they find interesting. Users must find and save .txt files, then upload those files to python notebook. 


*Classify* 

This function imports a Naive Bayes Classifier from the TextBlob library to classify any sentence given by the user as either more Hillarian or Trumpian in nature. It was trained using sentences from Clinton and Trump's Presidential Nomination Acceptance Speeches. Users submit their chosen sentence as a string, and the classifier returns either "Clinton" or "Trump." 

*Generate* 

This section includes two seperate functions, generateSentence() and generateSpeech(). It uses the markovify library to create a Markov Text Chain generator. Like Analyze, it was originally developed using speeches from Clinton and Trump. but has been generalized to accept any .txt file as a text. Users must find and save a .txt file, then upload that file to python notebook. generateSentence() will use that file to randomly generate a single sentence of text, while generateSpeech() will generate a 5 sentence mini-speech. 

*Sample Texts*

In addition to the functions above, a sample .txt file for both Clinton and Trump's Presidential Nomination Acceptance speeches have been attached.
