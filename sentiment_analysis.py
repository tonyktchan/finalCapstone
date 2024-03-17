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


#
#
#

def get_one_sentiment(reviews, number=0):
    '''
    this is a function to either accept free text review
    or based on the record number of the given amazon_product_reviews to give the sentiment of
    a specific review using polarity as criterion of evaluation
    '''
    # load the nlp model
    if number !=0:
        num = number - 1
        review = str(reviews.iloc[num]["reviews.text"])
    else:
        review = reviews

    nlp = spacy.load("en_core_web_sm")
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
    print("Reading from amazon_product_reviews.csv and perform pre-processing, please wait.")  
    df_reviews_raw = pd.read_csv("amazon_product_reviews.csv", usecols=['reviews.text'])
    df_reviews_1 = df_reviews_raw.drop_duplicates()
    df_reviews = df_reviews_1.dropna()
    
    # display the basics of dataframe
    print("Some basic information of the csv file is as follows")
    print(df_reviews.head())
    print(df_reviews.shape)
    print(df_reviews.info)
    print(df_reviews.count())
    print(df_reviews.index)

    # Ask user to select 2 records from the existing dataset
    # to evaluate the sentiment of the reviews
    # Then ask user to input a free text review
    # to evaluate the sentiment of the review
    index = len(df_reviews)    
    while True:
        string1 = input(f"Please give me a number of first test record which is less than or equal to {index}: ")
        try:
            test1 = int(string1)  # Convert input to an integer
            if 0 < test1 <= index:
                print("You entered a valid number:", test1)
                break  # Exit the loop since valid input was received
            else:
                print("You entered an invalid number. This program will exit")
                exit()
        except TypeError:
            print("Incorrect input type. This program will exit")
            exit()

    while True:
        string2 = input(f"Please give me a number of second test record which is less than {index}: ")
        try:
            test2 = int(string2)  # Convert input to an integer
            if 0 < test2 <= index:
                print("You entered a valid number:", test2)
                break  # Exit the loop since valid input was received
            else:
                print("You entered an invalid number. This program will exit")
                exit()
        except TypeError:
            print("Incorrect input type. This program will exit")
            exit()

    print(f"Evaluate the sentinment of {test1} record.")
    get_one_sentiment(df_reviews, test1)
    print(f"Evaluate the sentinment of {test2} record.")
    get_one_sentiment(df_reviews, test2)

    #get the free text review from user/input and evaluate the sentiment
    review = input("Please provide me a review in text: ")
    get_one_sentiment(review, 0)    
    
### this is the end of this python program ###
