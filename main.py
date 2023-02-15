import os

STOPWORDS_DIRECTORY = 'StopWords'
MASTER_DICTIONARY_DIRECTORY = 'MasterDictionary'
TWEETS_FILENAME = 'tweets500.txt'


def load_stopwords():
    """Load stopwords from files in the stopwords directory."""
    stopwords = set()
    for filename in os.listdir(STOPWORDS_DIRECTORY):
        if filename.endswith('.txt'):
            with open(os.path.join(STOPWORDS_DIRECTORY, filename), 'r') as f:
                for line in f:
                    word = line.strip().split('|')[0].lower()
                    stopwords.add(word)
    return stopwords


def load_master_dictionary():
    """Load positive and negative words from files in the master dictionary directory."""
    master_dict = {'positive': set(), 'negative': set()}
    for filename in os.listdir(MASTER_DICTIONARY_DIRECTORY):
        with open(os.path.join(MASTER_DICTIONARY_DIRECTORY, filename), 'r') as f:
            if filename == 'positive-words.txt':
                master_dict['positive'].update(f.read().lower().split())
            elif filename == 'negative-words.txt':
                master_dict['negative'].update(f.read().lower().split())
    return master_dict


def clean_tweet(tweet, stopwords):
    """Clean a tweet by removing stopwords and converting all words to lowercase."""
    words = tweet.lower().split()
    return [w for w in words if w not in stopwords]


def calculate_polarity(tweet, master_dict, stopwords):
    """Calculate the polarity and subjectivity of a tweet using a master dictionary and a set of stopwords."""
    words = clean_tweet(tweet, stopwords)
    positive_score = sum(1 for w in words if w in master_dict['positive'])
    negative_score = sum(1 for w in words if w in master_dict['negative'])
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 1e-6)
    subjectivity_score = (positive_score + negative_score) / (len(words) + 1e-6)
    return {'tweet': tweet, 'polarity_score': polarity_score}


def analyze_tweets():
    """Analyze the sentiment of tweets in the tweets500.txt file using a master dictionary and a set of stopwords."""
    stopwords = load_stopwords()
    master_dict = load_master_dictionary()
    with open(TWEETS_FILENAME, 'r', encoding='utf-8') as f:
        for tweet in f:
            result = calculate_polarity(tweet, master_dict, stopwords)
            print(result)


if __name__ == '__main__':
    analyze_tweets()