# Twitter Sentiment Analysis
This project aims to perform sentiment analysis on a dataset of tweets. The goal is to determine the profanity score in tweets.

# Problem Statement
Do read the following blog post before answering the questions https://medium.com/affinityanswers-tech/recruitment-how-not-to-answer-our-take-home-questions-57153d143447 Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python) - make any assumptions, but remember to state them. Please place the code in GitHub with proper documentation and share...

# Implementation
The project is implemented using Python programming language. The load_stopwords() function loads a set of stop words from the StopWords directory. The load_master_dictionary() function loads a master dictionary of positive and negative words from the MasterDictionary directory. The clean_tweet() function cleans the tweet by removing stop words and converting all words to lowercase. The calculate_polarity() function calculates the polarity and subjectivity scores of the tweet. The analyze_tweets() function reads each tweet from the tweets500.txt file and prints the result of sentiment analysis for each tweet.

# Methods
- load_stopwords(): Loads a set of stop words from the StopWords directory.
- load_master_dictionary(): Loads a master dictionary of positive and negative words from the MasterDictionary directory.
- clean_tweet(tweet, stopwords): Cleans the tweet by removing stop words and converting all words to lowercase.
- calculate_polarity(tweet, master_dict, stopwords): Calculates the polarity and subjectivity scores of the tweet.
- analyze_tweets(): Reads each tweet from the tweets500.txt file and prints the result of sentiment analysis for each tweet.

The sentiment analysis is based on a scoring system where positive words increase the positive score, negative words increase the negative score, and the polarity score is calculated as the difference between the positive and negative scores divided by their sum. The subjectivity score is calculated as the ratio of the sum of the positive and negative scores to the total number of words in the tweet.
