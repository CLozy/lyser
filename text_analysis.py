from nltk.parse.malt import MaltParser
from nltk.parse import DependencyGraph
from nltk.tag import pos_tag

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize


from nltk.corpus import reuters

from wordcloud import WordCloud
import plotly.express as px
import string

# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Sample Data
# sample_text = reuters.raw(fileids=reuters.fileids(categories='crude')[0])
# print(sample_text)

class TextAnalyzer:
    """
        A class to perform text analysis on a given corpus.
        Attributes:
            corpus (str): The corpus to analyze.
            
        Methods:
            pipeline(): A function to perform text analysis on a given corpus.
            Returns a list of tokens.
            e.g. ['the', 'cat', 'sat', 'on', 'the', 'mat']
            
            pos_tagging(): A function to perform POS tagging on a given corpus.
            Returns a list of tuples containing the word and its POS tag.
            e.g. [('the', 'DT'), ('cat', 'NN'), ('sat', 'VB'), ('on', 'IN'), ('the', 'DT'), ('mat', 'NN')]
            
            visualize_word_cloud(): A function to visualize the word cloud of a given corpus.
            
        Example:
            analyzer = TextAnalyzer(corpus=sample_text)
            analyzer.pipeline()
            analyzer.pos_tagging()
            analyzer.visualize_word_cloud()
        
    """
   
    def __init__(self, corpus=None):
        self.corpus  = corpus
        
    def pipeline(self):
        """
            A function to perform text analysis on a given corpus.
            Returns a list of tokens.
            e.g. ['the', 'cat', 'sat', 'on', 'the', 'mat']
            
        """
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
    

    #pos tagging
    def pos_tagging(self):
        """
            A function to perform POS tagging on a given corpus.
            Returns a list of tuples containing the word and its POS tag.
            e.g. [('the', 'DT'), ('cat', 'NN'), ('sat', 'VB'), ('on', 'IN'), ('the', 'DT'), ('mat', 'NN')]
            
        """
        tagged_words = pos_tag(self.pipeline())
        return tagged_words


    #creating word_cloud
    def visualize_word_cloud(self):
        """
            A function to visualize the word cloud of a given corpus.
            Returns a Word Cloud visualization of the given corpus.
           
        """
        
        # Generate a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(self.corpus)

        # Get the word frequencies from the WordCloud object
        word_frequencies = wordcloud.words_

        # Create an interactive Word Cloud using plotly
        fig = px.imshow(wordcloud.to_array(), title='Word Cloud')

        # Customize the layout
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        # Display the interactive Word Cloud
        fig.show()



