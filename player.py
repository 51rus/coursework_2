class Player:

    def __init__(self, name):
        self.name = name
        self.subwords_used = set()

    def __repr__(self):
        return f'Player({self.name}, {self.subwords_used})'

    def get_name(self):
        """
        Возвращает имя пользователя
        :return: имя
        """
        return self.name

    def count_subwords_used(self):
        """
        Возвращает количество использованных слов
        :return: количество слов
        """
        return len(self.subwords_used)

    def add_subword(self, subword):
        """
        Добавляет слово в список использованных игроком
        :param subword: слово для добавления
        :return: добавление в список
        """
        self.subwords_used.add(subword)

    def has_subword_used(self, subword):
        """
        Проверяет было ли использовано слово
        :param subword: слово для проверки
        :return: результат
        """
        return subword in self.subwords_used
