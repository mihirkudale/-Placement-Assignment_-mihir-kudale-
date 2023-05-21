import nltk

# Check if NLTK is installed
try:
    nltk.data.find('tokenizers/punkt')
    print("NLTK is installed")
except LookupError:
    print("NLTK is not installed")

# Check if stopwords corpus is available
try:
    stopwords = nltk.corpus.stopwords.words('english')
    print("Stopwords corpus is available")
except LookupError:
    print("Stopwords corpus is not available")
