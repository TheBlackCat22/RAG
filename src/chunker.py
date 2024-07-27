import os
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain.schema import Document

def chunk(documents_dir):

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"), ("###", "Header 4")],
        strip_headers=False
    )
    recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=4000, 
            chunk_overlap=200
        )

    processed_docs_dir = os.path.join(documents_dir, 'processed')

    chunks = []
    for root, _, files in os.walk(processed_docs_dir):
        for file in files:
            rel_path = os.path.relpath(root, processed_docs_dir)
            
            with open(os.path.join(processed_docs_dir, rel_path, file), 'r') as f:
                content = f.read()

            for item in markdown_splitter.split_text(content):
                chunks.append(Document(page_content=item.page_content, metadata={'Webpage': os.path.normpath(os.path.join('https://bot-docs.cloudfabrix.io/', rel_path, file[:-3])), 'Section' : ' -> '.join(item.metadata.values())}))

    chunks = recursive_splitter.split_documents(chunks)

    return chunks