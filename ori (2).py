import csv
import string
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK resources
tokenizer = TreebankWordTokenizer()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()

# Define a function to preprocess and analyze a text
def preprocess_and_analyze(text):
    # Tokenize the text into words
    words = tokenizer.tokenize(text)
    
    # Define translator for punctuation removal
    translator = str.maketrans('', '', string.punctuation)
    
    # Preprocess and filter words
    filtered_words = [lemmatizer.lemmatize(word.translate(translator)).lower() for word in words if word.lower() not in stop_words]
    
    # Perform part-of-speech tagging
    pos_tags = pos_tag(filtered_words)
    
    # Filter out adjectives and verbs
    selected_words = [word for word, pos in pos_tags if pos in ['JJ', 'JJR', 'JJS', 'RBR', 'RBS', 'VBD', 'VBN']]
    
    return selected_words

# Open the CSV file and iterate through rows
with open(r"D:\py\merix1.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        vader_scores_sum = 0
        for cell in row:
            if cell.strip():  # Check if the cell is not empty
                # Preprocess and analyze the review
                analyzed_words = preprocess_and_analyze(cell)
                
                # Perform sentiment analysis for the current cell
                vader_scores = [sia.polarity_scores(word)['compound'] for word in analyzed_words]
                
                # Sum the Vader scores for the current cell
                vader_scores_sum += sum(vader_scores)
        
        # Print the sum of Vader scores for the row
        
        print("Vader Scores Sum:", vader_scores_sum)
        print("\n")
