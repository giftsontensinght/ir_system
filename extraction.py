# # Contains functions that deal with the extraction of documents from a text file (see PR01)

# import json

# from document import Document

# def extract_collection(source_file_path: str) -> list[Document]:
#     """
#     Loads a text file (aesopa10.txt) and extracts each of the listed fables/stories from the file.
#     :param source_file_name: File name of the file that contains the fables
#     :return: List of Document objects
#     """
#     catalog = []  # This dictionary will store the document raw_data.

#     # TODO: Implement this function. (PR02)
#     raise NotImplementedError('Not implemented yet!')

#     return catalog


# def save_collection_as_json(collection: list[Document], file_path: str) -> None:
#     """
#     Saves the collection to a JSON file.
#     :param collection: The collection to store (= a list of Document objects)
#     :param file_path: Path of the JSON file
#     """

#     serializable_collection = []
#     for document in collection:
#         serializable_collection += [{
#             'document_id': document.document_id,
#             'title': document.title,
#             'raw_text': document.raw_text,
#             'terms': document.terms,
#             'filtered_terms': document.filtered_terms,
#             'stemmed_terms': document.stemmed_terms
#         }]

#     with open(file_path, "w") as json_file:
#         json.dump(serializable_collection, json_file)


# def load_collection_from_json(file_path: str) -> list[Document]:
#     """
#     Loads the collection from a JSON file.
#     :param file_path: Path of the JSON file
#     :return: list of Document objects
#     """
#     try:
#         with open(file_path, "r") as json_file:
#             json_collection = json.load(json_file)

#         collection = []
#         for doc_dict in json_collection:
#             document = Document()
#             document.document_id = doc_dict.get('document_id')
#             document.title = doc_dict.get('title')
#             document.raw_text = doc_dict.get('raw_text')
#             document.terms = doc_dict.get('terms')
#             document.filtered_terms = doc_dict.get('filtered_terms')
#             document.stemmed_terms = doc_dict.get('stemmed_terms')
#             collection += [document]

#         return collection
#     except FileNotFoundError:
#         print('No collection was found. Creating empty one.')
#         return []



#duplicate


# Contains functions that deal with the extraction of documents from a text file (see PR01)

import json
import os

from document import Document

def remove_symbols(text):
    return ''.join(char for char in text if char.isalnum()).lower()

def extract_collection(source_file_path: str) -> list[Document]:
    """
    Loads a text file (aesopa10.txt) and extracts each of the listed fables/stories from the file.
    :param source_file_path: File path of the file that contains the fables
    :return: List of Document objects
    """
    catalog = []

    with open(source_file_path,'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = lines[306:]
        lines = "".join(lines)
    fables = lines.split('\n\n\n')
    doc_id = 1
    for index in range(0,len(fables),2):
        document = Document()
        document.raw_text=''
        document.document_id = doc_id
        if index<len(fables):
            document.title = fables[index].strip()
            fable_lines = fables[index+1].strip()
            text = fable_lines.split()
            document.terms = [remove_symbols(term) for term in text]
            document.raw_text = " ".join(text)
        catalog.append(document)
        doc_id+=1
    return catalog



def save_collection_as_json(collection: list[Document], file_path: str) -> None:
    """
    Saves the collection to a JSON file.
    :param collection: The collection to store (= a list of Document objects)
    :param file_path: Path of the JSON file
    """

    serializable_collection = []
    for document in collection:
        serializable_collection += [{
            'document_id': document.document_id,
            'title': document.title,
            'raw_text': document.raw_text,
            'terms': document.terms,
            'filtered_terms': document.filtered_terms,
            'stemmed_terms': document.stemmed_terms
        }]

    with open(file_path, "w", encoding='utf-8') as json_file:
        json.dump(serializable_collection, json_file)


def load_collection_from_json(file_path: str) -> list[Document]:
    """
    Loads the collection from a JSON file.
    :param file_path: Path of the JSON file
    :return: list of Document objects
    """
    try:
        with open(file_path, "r", encoding='utf-8') as json_file:
            json_collection = json.load(json_file)

        collection = []
        for doc_dict in json_collection:
            document = Document()
            document.document_id = doc_dict.get('document_id')
            document.title = doc_dict.get('title')
            document.raw_text = doc_dict.get('raw_text')
            document.terms = doc_dict.get('terms')
            document.filtered_terms = doc_dict.get('filtered_terms')
            document.stemmed_terms = doc_dict.get('stemmed_terms')
            collection += [document]

        return collection
    except FileNotFoundError:
        print('No collection was found. Creating empty one.')
        return []


