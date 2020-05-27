# ====================================
# COMP90024 Cluster and Cloud Computing - Assignment 2
# Group 29
# Hongwei Yin 901012
# Cheng Sun 900806
# Xinyi Xu 900966
# Yiran Yao 1144268
# Xiaotao Tan 1032950
# ====================================

# this function takes single/multiple input and return following tags as sentimentation result:
# positive   : this tweet content represents a positive opinion
# negative   : this tweet content represents a negative opinion
# neutral    : this tweet content represents a neutral opinion


import pandas as pd
import string
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_wordnet_pos(pos_tag):
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


# this helper function is to clean the text
def clean_text(tweet):
    # lower tweets content
    tweet = tweet.lower()
    # tokenize tweets content and remove puncutation
    tweet = [word.strip(string.punctuation) for word in tweet.split(" ")]
    # remove words that contain numbers
    tweet = [word for word in tweet if not any(c.isdigit() for c in word)]
    # remove stop words
    stop = stopwords.words('english')
    tweet = [x for x in tweet if x not in stop]
    # remove empty tokens
    tweet = [t for t in tweet if len(t) > 0]
    # pos tag tweets content
    pos_tags = pos_tag(tweet)
    # lemmatize tweets content
    tweet = [WordNetLemmatizer().lemmatize(t[0], get_wordnet_pos(t[1])) for t in pos_tags]
    # remove words with only one letter
    tweet = [t for t in tweet if len(t) > 1]

    tweet = " ".join(tweet)
    return(tweet)

# This function takes the one single input of tweetter content or a list of tweetter content for analysis
# and retuns a list of analysis result
def sentiment_test(tweets, single_flag=1):
    if single_flag:
        text_list = [tweets]
    else:
        text_list = tweets

    # initialise the dataframe
    tweet_df = pd.DataFrame()
    tweet_df["tweet"] = text_list

    # clean the tweets
    tweet_df["tweet_clean"] = tweet_df["tweet"].apply(lambda x: clean_text(x))

    # initialise analyzer
    sid = SentimentIntensityAnalyzer()

    # append analyse results
    tweet_df["sentiments"] = tweet_df["tweet_clean"].apply(lambda x: sid.polarity_scores(x))
    tweet_df = pd.concat([tweet_df.drop(['sentiments'], axis=1), tweet_df['sentiments'].apply(pd.Series)], axis=1)

    # append result
    tweet_df["result"] = tweet_df['compound'].apply(lambda x: 'positive' if x >= 0.05 else 'negative' if x <= -0.05 else 'neutral')

    return tweet_df["result"].tolist()

    