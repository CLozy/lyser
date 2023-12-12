from nltk.parse.malt import MaltParser
from nltk.parse import DependencyGraph
from nltk.tag import pos_tag
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize


from nltk.corpus import reuters

# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Sample Data
# sample_text = reuters.raw(fileids=reuters.fileids(categories='crude')[0])
# print(sample_text)

class TextAnalyzer:
    def __init__(self, corpus=None):
        self.corpus  = corpus
        
    def pipeline(self):
        # TOKENIZATION
        # pst = PunktSentenceTokenizer()
        # print(pst.tokenize(self.corpus))
        tokens = word_tokenize(self.corpus)
       

        # STEMMING AND lEMMATIZATION
        # stemmer = PorterStemmer()
        # singles = [stemmer.stem(plural) for plural in tokens]     
        tokens = [WordNetLemmatizer().lemmatize(word) for word in tokens]
      

        #STOPWORD ANALYSIS 
        stop_words = set(stopwords.words('english'))
        tokens = [token.lower() for token in tokens if token.lower()
                not in stop_words and token not in string.punctuation]
       
        return tokens
    


    def pos_tagging(self):
        tagged_words = pos_tag(self.pipeline())
        return tagged_words


# dependency parsing
