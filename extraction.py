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

from document import Document

def extract_collection(source_file_path: str) -> list[Document]:
    """
    Loads a text file (aesopa10.txt) and extracts each of the listed fables/stories from the file.
    :param source_file_path: File path of the file that contains the fables
    :return: List of Document objects
    """
    with open(source_file_path, 'r') as file:
        lines = file.readlines()

    catalog = []
    current_fable_lines = []
    current_fable_title = None
    in_fable = False

    # Iterate through each line in the file
    for line in lines:
        line = line.strip()

        # Check if the line contains "Aesop's Fables", indicating the start of a fable
        if line == "Aesop's Fables":
            in_fable = True
            continue

        # If in_fable is True, add the line to current_fable_lines
        if in_fable:
            # Check if the line starts with uppercase letters, indicating the title of a fable
            if line and line[0].isupper():
                # If it's a title, it indicates the start of a new fable
                if current_fable_title:
                    # Join the lines of the previous fable's text
                    fable_text = '\n'.join(current_fable_lines)
                    # Create a Document object for the previous fable
                    document = Document()
                    document.document_id = len(catalog)  # Assigning the current length of catalog as document_id
                    document.title = current_fable_title
                    document.raw_text = fable_text
                    document.terms = fable_text.split()  # Split text into terms
                    catalog.append(document)
                    # Reset current fable variables
                    current_fable_lines = []
                # Update the title for the new fable
                current_fable_title = line
            else:
                # If not a title, add the line to current_fable_lines
                current_fable_lines.append(line)

    # After the loop, add the last fable
    if current_fable_title and current_fable_lines:
        fable_text = '\n'.join(current_fable_lines)
        document = Document()
        document.document_id = len(catalog)
        document.title = current_fable_title
        document.raw_text = fable_text
        document.terms = fable_text.split()
        catalog.append(document)

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

    with open(file_path, "w") as json_file:
        json.dump(serializable_collection, json_file)


def load_collection_from_json(file_path: str) -> list[Document]:
    """
    Loads the collection from a JSON file.
    :param file_path: Path of the JSON file
    :return: list of Document objects
    """
    try:
        with open(file_path, "r") as json_file:
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


