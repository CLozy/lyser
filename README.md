## lyser
A python package that has classes that processes text and creates a rag chef chat agent that gives cooking tips and recipes. 


### How to install
`pip install lyser`


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

### A class to invoke Chef Chat
        Attributes:
            folder_path (str, pdf): path to folder_path with recipe files
            query (str): user input
            
            
        Methods:
            data_loader(): A function that loads the pdf books in a folder and returns a list of documents.
            Returns:
                list: A list of documents. Each document is a dictionary with a 'page_content' key and 'metadata' key.
            
            chat_summary():  A function that creates a chat summary 
            Returns:
                chat_memory: A AgentTokenBufferMemory chat summary memory.

            
            rag_agent(): A function that creates a rag agent that returns recipes of meals from cook pdf books 
            Returns:
                agent_result: A dictionary with the output of the rag agent.
            
            
        Example:
            # chef_chat = ChefChat(folder_path="data", query="How can i make pineapple chicken")
            print(chef_chat.rag_agent())