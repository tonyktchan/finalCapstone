'''
 This python program consists of reading Amazon user reviews: amazon_product_reviews.csv
 and based on the column 'reviews.text' to provide input to 
 call the function to generate a sentiment score based on polarity
'''
import textwrap
import re
import pandas as pd
import spacy
from textblob import TextBlob



def get_sentiment(reviews, index):
    '''
    this is the funciton using nlp from spacy with Textblob 
    to come up with polarity as evaluation of sentiment
    '''
    # load the nlp model
    nlp = spacy.load("en_core_web_sm")
    for i in index:
        if i < 100:
            review = str(reviews.iloc[i]["reviews.text"])
            review_nlp = nlp(review)
            review_tokens = [token.text for token in review_nlp if not token.is_stop]
            review_no_stopwords = ' '.join(review_tokens)
            review_string = textwrap.fill(review_no_stopwords, width=120)
            review_string = review_string.lower()
            review_string = re.sub(r"[^\w\s]", "", review_string)
            
            # print(review_for_nlp)
            print(f"For this review: {review_string}")


            # get polarity from sentiment using Textblob
            blob = TextBlob(review_string)
            sentiment_polarity = blob.sentiment.polarity
            print(f"The sentiment value is: {sentiment_polarity} \n")
            
            # apart from polarity, there is subjectivity under sentiment
            # uncomment the following 2 lines if sentiment(polarity, subjectivity) is preferred
            # sentiment_sentiment = blob.sentiment
            # print(f"The sentiment value is: {sentiment_sentiment} \n")        
            
    return


if __name__=="__main__":
    
    
    # read from csv file and extract the 'reviews.text' cloumn 
    # and perform pre-processing
    df_reviews_raw = pd.read_csv("amazon_product_reviews.csv", usecols=['reviews.text'])
    df_reviews_1 = df_reviews_raw.drop_duplicates()
    df_reviews = df_reviews_1.dropna()

    # display the basics of dataframe
    print(df_reviews.head())
    print(df_reviews.shape)
    print(df_reviews.info)
    print(df_reviews.count())
    print(df_reviews.index)

    # input the dataframe and evaluate the polarity/sentiment
    get_sentiment(df_reviews, df_reviews.index)
    
    
### this is the end of this python program ###