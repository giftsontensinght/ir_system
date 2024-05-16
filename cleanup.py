# # Contains all functions that deal with stop word removal.

# from document import Document


# def remove_symbols(text_string: str) -> str:
#     """
#     Removes all punctuation marks and similar symbols from a given string.
#     Occurrences of "'s" are removed as well.
#     :param text:
#     :return:
#     """

#     #  : Implement this function. (PR02)
#     raise NotImplementedError('Not implemented yet!')


# def is_stop_word(term: str, stop_word_list: list[str]) -> bool:
#     """
#     Checks if a given term is a stop word.
#     :param stop_word_list: List of all considered stop words.
#     :param term: The term to be checked.
#     :return: True if the term is a stop word.
#     """
#     # Implement this function  (PR02)
#     raise NotImplementedError('Not implemented yet!')


# def remove_stop_words_from_term_list(term_list: list[str]) -> list[str]:
#     """
#     Takes a list of terms and removes all terms that are stop words.
#     :param term_list: List that contains the terms
#     :return: List of terms without stop words
#     """
#     # Hint:  Implement the functions remove_symbols() and is_stop_word() first and use them here.
#     #  : Implement this function. (PR02)
#     raise NotImplementedError('Not implemented yet!')


# def filter_collection(collection: list[Document]):
#     """
#     For each document in the given collection, this method takes the term list and filters out the stop words.
#     Warning: The result is NOT saved in the documents term list, but in an extra field called filtered_terms.
#     :param collection: Document collection to process
#     """
#     # Hint:  Implement remove_stop_words_from_term_list first and use it here.
#     #  : Implement this function. (PR02)
#     raise NotImplementedError('To be implemented in PR02')


# def load_stop_word_list(raw_file_path: str) -> list[str]:
#     """
#     Loads a text file that contains stop words and saves it as a list. The text file is expected to be formatted so that
#     each stop word is in a new line, e. g. like englishST.txt
#     :param raw_file_path: Path to the text file that contains the stop words
#     :return: List of stop words
#     """
#     #  : Implement this function. (PR02)
#     raise NotImplementedError('To be implemented in PR02')


# def create_stop_word_list_by_frequency(collection: list[Document]) -> list[str]:
#     """
#     Uses the method of J. C. Crouch (1990) to generate a stop word list by finding high and low frequency terms in the
#     provided collection.
#     :param collection: Collection to process
#     :return: List of stop words
#     """
#     #  : Implement this function. (PR02)
#     raise NotImplementedError('To be implemented in PR02')

#duplicate

import string
from document import Document

def remove_symbols(text_string: str) -> str:
    """
    Removes all punctuation marks and similar symbols from a given string.
    Occurrences of "'s" are removed as well.
    :param text_string: The input text string.
    :return: The text string with symbols removed.
    """
    # Remove punctuation marks
    text_string = text_string.translate(str.maketrans('', '', string.punctuation))
    # Remove "'s"
    text_string = text_string.replace("'s", "")
    return text_string


def is_stop_word(term: str, stop_word_list: list[str]) -> bool:
    """
    Checks if a given term is a stop word.
    :param term: The term to be checked.
    :param stop_word_list: List of all considered stop words.
    :return: True if the term is a stop word, False otherwise.
    """
    # Case-insensitive comparison
    term_lower = term.lower()
    return term_lower in stop_word_list


def remove_stop_words_from_term_list(term_list: list[str], stop_word_list: list[str]) -> list[str]:
    """
    Takes a list of terms and removes all terms that are stop words.
    :param term_list: List that contains the terms.
    :param stop_word_list: List of stop words.
    :return: List of terms without stop words.
    """
    filtered_terms = [term for term in term_list if not is_stop_word(term, stop_word_list)]
    return filtered_terms


def filter_collection(collection: list[Document], stop_word_list: list[str]) -> None:
    """
    For each document in the given collection, this method takes the term list and filters out the stop words.
    Warning: The result is NOT saved in the document's term list, but in an extra field called filtered_terms.
    :param collection: Document collection to process.
    :param stop_word_list: List of stop words.
    """
    for document in collection:
        document.filtered_terms = remove_stop_words_from_term_list(document.terms, stop_word_list)


def load_stop_word_list(raw_file_path: str) -> list[str]:
    """
    Loads a text file that contains stop words and saves it as a list. The text file is expected to be formatted so that
    each stop word is in a new line.
    :param raw_file_path: Path to the text file that contains the stop words.
    :return: List of stop words.
    """
    with open(raw_file_path, 'r') as file:
        stop_word_list = [line.strip().lower() for line in file.readlines()]
    return stop_word_list


def create_stop_word_list_by_frequency(collection: list[Document], high_freq_threshold: int, low_freq_threshold: int) -> list[str]:
    """
    Generates a stop word list by finding high and low frequency terms in the provided collection.
    :param collection: Collection to process.
    :param high_freq_threshold: Threshold for high frequency terms.
    :param low_freq_threshold: Threshold for low frequency terms.
    :return: List of stop words.
    """
    # Count term frequencies
    term_freq = {}
    for document in collection:
        for term in document.terms:
            term_lower = term.lower()
            term_freq[term_lower] = term_freq.get(term_lower, 0) + 1
    
    # Identify high and low frequency terms
    high_freq_terms = [term for term, freq in term_freq.items() if freq >= high_freq_threshold]
    low_freq_terms = [term for term, freq in term_freq.items() if freq <= low_freq_threshold]
    
    # Combine high and low frequency terms as stop words
    stop_word_list = set(high_freq_terms + low_freq_terms)
    
    return list(stop_word_list)
