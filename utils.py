import random
import requests

from basic_word import BasicWord


def load_data(path):
    """
    :param path: путь к данным
    :return: данные
    """
    result = requests.get(path)
    result_status = result.status_code
    if result_status != 200:
        return []
    return result.json()


def load_random_word(path):
    """
    Возвращает случайное слово
    :param path: путь к данным
    :return: экземпляр BasicWord
    """
    list_of_words = load_data(path)
    if len(list_of_words) == 0:
        return None

    random_word = random.choice(list_of_words)

    word = random_word["word"]
    subwords = random_word["subwords"]

    basic_word = BasicWord(word, subwords)

    return basic_word
