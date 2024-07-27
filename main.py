########################################################################################
# CFX Docs
architecture = [
    'https://bot-docs.cloudfabrix.io/beginners_guide/architecture/'
]

guides = [
    'https://bot-docs.cloudfabrix.io/beginners_guide/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/data_control/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/data_ingestion/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/data_at_rest/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/data_in_motion/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/ml/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/dashboards/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/pipe_builder/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/adm/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/scheduled_pipelines/',
    'https://bot-docs.cloudfabrix.io/reference_guides/grok_patterns/',
    'https://bot-docs.cloudfabrix.io/reference_guides/cfxql/',
    'https://bot-docs.cloudfabrix.io/reference_guides/synthetic_fields/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/svc_blueprints_cli/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/aia_api/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/users_groups/',
    'https://bot-docs.cloudfabrix.io/beginners_guide/persistent_streams/'
]

integrations = [
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Check_MK/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Dell-EMC-Unity/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/dynatrace/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/elasticsearch/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Infoblox-NetMRI/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/kubernetes/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Linux-OS/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/ManageEngine-OpManager/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Microsoft-Windows-Server-OS/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Nagios-XI/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/NetApp-Clustered-ONTAP/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/NodePing/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/PRTG-Network-Monitor/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/VMware-vCenter/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/VMware-vRealize-Operations/',
    'https://bot-docs.cloudfabrix.io/Datasource_Integrations/Zabbix/'
]

installation = [
    'https://bot-docs.cloudfabrix.io/installation_guides/',
    'https://bot-docs.cloudfabrix.io/installation_guides/deployment/',
    'https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/',
    'https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/',
    'https://bot-docs.cloudfabrix.io/installation_guides/rdac/',
    'https://bot-docs.cloudfabrix.io/installation_guides/rdaf_start_stop_ops/',
    'https://bot-docs.cloudfabrix.io/installation_guides/oia_deployment/',
    'https://bot-docs.cloudfabrix.io/installation_guides/oia_management/',
    'https://bot-docs.cloudfabrix.io/rda_releases/',
    'https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_for_fso/',
    'https://bot-docs.cloudfabrix.io/installation_guides/rdaf_portal/'
]

example_data = [
    'https://bot-docs.cloudfabrix.io/Datasets/',
    'https://bot-docs.cloudfabrix.io/Formatting-Templates/'
]

developing_bots = [
    'https://bot-docs.cloudfabrix.io/beginners_guide/sdk/'
]
########################################################################################


########################################################################################
WEBSITES = architecture + guides + integrations + installation + example_data + developing_bots

DOCUMENTS_DIR = './documents'
VECTOR_DB_DIR = './vector_db'
EMBEDDING_MODEL = 'nvidia/nv-embed-v1'
LLM = 'meta/llama3-8b-instruct'

NUM_RELEVANT_CHUNKS = 3
QUERY = ['How to create a Dashboard?',
         'What are dashboard filters?',
         'How to configure a pie chart?']
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
llm = ChatNVIDIA(model = LLM, temperature=0.1, max_tokens=500, convert_system_message_to_human=True)
print(f'Loaded {LLM}')
########################################################################################

########################################################################################
# QA Chat
print('\n*******')
print('Q&A Chat')
print('********')

from src import qa_rag_chain
conversational_rag_chain = qa_rag_chain.build_chain(llm, retriever)

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
########################################################################################