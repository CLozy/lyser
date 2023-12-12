## A text processing python package avalailable on PYPI


### How to install
`pip install text-analyzer`


### A class to perform text analysis on a given corpus.
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