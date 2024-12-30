from constant.path import BASE_PATH
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_experimental.text_splitter import SemanticChunker

file_paths = (
        BASE_PATH + "/resource/Mamba.pdf"
)
embeddings_model = HuggingFaceEmbeddings(model_name="TaylorAI/bge-micro-v2")


def load_resource():
    pages = list()
    # for file_path in file_paths:
    loader = PyPDFLoader(file_paths)
    for page in loader.lazy_load():
        pages.append(page)

    return pages


def resource_splitter():
    pages = load_resource()
    content = list()
    for page in pages:
        content.append(page.page_content)

    text_splitter = SemanticChunker(embeddings_model)
    chunks = text_splitter.create_documents(content)

    return chunks


# def do_embedding():
#     chunks = resource_splitter()
#     documents = list()
#     for chunk in chunks:
#         documents.append(chunk.page_content)
#
#     embed_document = embeddings_model.embed_documents(documents)
#
#     return embed_document


def stored_embedding():
    chunks = resource_splitter()

    db = Chroma.from_documents(chunks, embeddings_model)

    return db
