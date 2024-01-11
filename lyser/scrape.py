from langchain_openai import ChatOpenAI

from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer 

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains import create_extraction_chain

from dotenv import load_dotenv

import pprint

load_dotenv()



#Scraping with extraction of tuko news webpage
#LLM with function calling
#Using Function (e.g., OpenAI) with an extraction chain, we avoid having to change your code constantly when websites change.

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

#defibe a schema
#describes what kind of data you want to extract
#key names matter as they tell the LLM what kind of information they want.

#In this example, we want to scrape only news article’s name and summary from Tuko News website.
schema = {
    "properties": {
        "news_article_title": {"type": "string"},
        "news_article_summary": {"type": "string"},
    },
    "required": ["news_article_title", "news_article_summary"],
}


def extract(content: str, schema: dict):
    return create_extraction_chain(schema=schema, llm=llm).run(content)

#Run the web scraper w/ BeautifulSoup


def scrape_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        docs, tags_to_extract=["span"]
    )
    print("Extracting content with LLM")

    # Grab the first 1000 tokens of the site
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=0
    )
    splits = splitter.split_documents(docs_transformed)

    # Process the first split
    extracted_content = extract(schema=schema, content=splits[0].page_content)
    pprint.pprint(extracted_content)
    return extracted_content


urls = ["https://www.tuko.co.ke/"]
extracted_content = scrape_with_playwright(urls, schema=schema)

print(extracted_content)