########################################################################################
WEBSITES = []

DOCUMENTS_DIR = './documents'
VECTOR_DB_DIR = './vector_db'
EMBEDDING_MODEL = 'nvidia/nv-embed-v1'
LLM = 'meta/llama3-8b-instruct'

NUM_RELEVANT_CHUNKS = 3
# QUERY = str
# QUERY = []
QUERY = None
########################################################################################


########################################################################################
# Loading API Keys
from dotenv import load_dotenv
load_dotenv()
########################################################################################


########################################################################################
# Scrape Websites
print('\n*****************')
print('SCRAPING WEBSITES')
print('*****************')
from src import scraper
scraper.scrape(WEBSITES, DOCUMENTS_DIR)
########################################################################################


########################################################################################
# Pre-Process Document Content
print('\n*********************')
print('Cleaning Website Data')
print('*********************')
from src import data_cleaner
data_cleaner.clean(DOCUMENTS_DIR)
########################################################################################


########################################################################################
# Chucking Documents
print('\n*************')
print('Chucking Data')
print('*************')
from src import chunker
chunks = chunker.chunk(DOCUMENTS_DIR)
print(f'Total Number of Chunks is {len(chunks)}')
########################################################################################


########################################################################################
# Initializing Embedding Model
print('\n**********************')
print('Loading Embedding Model')
print('***********************')
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
embedding_model = NVIDIAEmbeddings(model=EMBEDDING_MODEL)
print(f'Loaded {EMBEDDING_MODEL}')
########################################################################################


########################################################################################
# Creating Vector Database
print('\n***********************')
print('Creating Vector Database')
print('************************')

import sys
from src import vector_db_builder

vector_db = vector_db_builder.build(chunks, VECTOR_DB_DIR, embedding_model)

retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k" : NUM_RELEVANT_CHUNKS})

if isinstance(QUERY, str):
    relevant_docs = retriever.invoke(QUERY)

    print('\nRelevant Documents:')
    for i, doc in enumerate(relevant_docs):
        print(f'\n\nDocument {i}:\n{doc.page_content}\n')
        print(f"Webpage: {doc.metadata['Webpage']}")
        print(f"Section: {doc.metadata['Section']}")

    sys.exit(0)
########################################################################################


########################################################################################
# Initializing LLM
print('\n**********')
print('Loading LLM')
print('***********')
from langchain_nvidia_ai_endpoints import ChatNVIDIA
llm = ChatNVIDIA(model = LLM, temperature=0.1, max_tokens=500)
print(f'Loaded {LLM}')
########################################################################################

########################################################################################
# QA Chat
print('\n*******')
print('Q&A Chat')
print('********')

from src import qa_rag_chain
conversational_rag_chain = qa_rag_chain.build_chain(llm, retriever)

if isinstance(QUERY, list):
    for query in QUERY:

        print('\n\nUSER: ', query)

        result = conversational_rag_chain.invoke(
                        {"input": query},
                        config={
                            "configurable": {"session_id": "abc123"}
                        },
                    )

        print('LLM: ', result['answer'])
        print('Sources: ', '\n  -' + '\n  -'.join([f"Webpage: {doc.metadata['Webpage']}, Section: {doc.metadata['Section']}" for doc in result['context']]))

if QUERY is None:
    while True:
        query = input('\n\nUSER: ')
        if query == 'exit':
            break

        result = conversational_rag_chain.invoke(
                    {"input": query},
                    config={
                        "configurable": {"session_id": "abc123"}
                    },
                )
        
        print('LLM: ', result['answer'])
        print('Sources: ', '\n  -' + '\n  -'.join([f"Webpage: {doc.metadata['Webpage']}, Section: {doc.metadata['Section']}" for doc in result['context']]))
########################################################################################