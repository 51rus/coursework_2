class BasicWord:
    """
    Класс для хранения базового слова и подслов
    """

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'BasicWord({self.word}, {self.subwords})'

    def get_word(self):
        """
        Возвращает исходное слово
        :return: слово
        """
        return self.word

    def count_subwords(self):
        """
        Возвращает общее количество подслов
        :return: количество подслов int
        """
        return len(self.subwords)

    def has_subwords(self, word_to_check):
        return word_to_check.strip().lower() in self.subwords
