import re
import os

def process_content(text):
    # Heading 1
    text = re.sub(r'\n(.+)\n=+', r'\n# \1', text)
    # Heading 2
    text = re.sub(r'\n(.+)\n-+', r'\n## \1', text)
    # Codeblock
    text = re.sub(r'(\s)*`\[\]\(#__codelineno-\d+-\d+\)(.+)`', r'\n```\n\2\n\1```', text)
    # CodeLine
    text = re.sub(r'\[(|\d+)\]\(#__codelineno-\d+-\d+\)', '\n', text)
    # Table Codeblock
    text = re.sub(r'\|     \|     \|\n\| --- \| --- \|\n\| \n(<br>\n)* \| `(.+)` \|', r'\n```\n\2\n```', text)
    return text


def clean(documents_dir):
    for root, _, files in os.walk(os.path.join(documents_dir, 'raw')):
        for file in files:
            raw_document_path = os.path.join(root, file)
            processed_document_path = os.path.join(documents_dir, 'processed', os.path.relpath(root, os.path.join(documents_dir, 'raw')), file)

            if not os.path.exists(processed_document_path):

                with open(raw_document_path, 'r') as f:
                    text = f.read()

                text = process_content(text)

                os.makedirs(os.path.dirname(processed_document_path), exist_ok=True)
                with open(processed_document_path, 'w') as f:
                    f.write(text)

                print(f"Processed Content of {raw_document_path} and Saved to {processed_document_path}")

            else:
                print(f"{raw_document_path} already cleaned to {processed_document_path}")