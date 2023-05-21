"""
Q-1. Take any YouTube videos link and your task is to extract the comments from
that videos and store it in a csv file and then you need define what is most
demanding topic in that videos comment section.
"""

#Ans:


import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import configparser

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models


# Load API key from the configuration file
config = configparser.ConfigParser()
config.read('Natural Language Processing\Question 1\config.ini')
print(config.sections())  # Check if the 'API' section is present
DEVELOPER_KEY = config['API']['DEVELOPER_KEY']

# Set up YouTube client
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

def preprocess_text(text):
    """
    Preprocesses the text by tokenizing, lemmatizing, and removing stop words.
    """
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stop words and lemmatize tokens
    preprocessed_text = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stop_words]

    return preprocessed_text

def get_video_comments(video_id):
    """
    Retrieves the comments from a YouTube video given its video_id.
    """
    try:
        comments = []
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100
        ).execute()

        while results:
            for item in results['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

            if 'nextPageToken' in results:
                results = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText",
                    maxResults=100,
                    pageToken=results['nextPageToken']
                ).execute()
            else:
                break

        return comments

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
        return None

def save_comments_to_csv(comments, file_path):
    """
    Saves the comments to a CSV file.
    """
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Comment'])
            writer.writerows([[comment] for comment in comments])
        print(f"Comments saved to {file_path}")
    except IOError:
        print("I/O error")

def find_most_demanding_topic(comments):
    """
    Finds the most demanding topic in the comments using LDA topic modeling.
    """
    preprocessed_comments = [preprocess_text(comment) for comment in comments]

    # Create a dictionary from the preprocessed comments
    dictionary = corpora.Dictionary(preprocessed_comments)

    # Create a corpus from the preprocessed comments
    corpus = [dictionary.doc2bow(comment) for comment in preprocessed_comments]

    # Train the LDA model
    lda_model = models.LdaModel(corpus, num_topics=10, id2word=dictionary)

    # Get the most representative topic for each comment
    topics = topics = [sorted(lda_model[dictionary.doc2bow(comment)], key=lambda x: x[1], reverse=True)[0][0] for comment in corpus]

    return topics

# Replace 'YOUR_VIDEO_ID' with the actual video ID of the YouTube video you want to analyze
video_id = 'pRbW2G4rVrw'
comments = get_video_comments(video_id)

if comments:
    save_comments_to_csv(comments, 'comments.csv')

    most_demanding_topic = find_most_demanding_topic(comments)
    print(f"The most demanding topic in the comments is: {most_demanding_topic}")
else:
    print("Failed to retrieve comments.")
