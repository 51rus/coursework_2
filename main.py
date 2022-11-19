from player import Player
from url import URL
import utils


def main():
    print("Введите имя игрока: ")
    user_input = input()
    player = Player(user_input)
    print(f"Привет, {player.get_name()}!")

    # Собираем случайное слово
    basic_word = utils.load_random_word(URL)

    print(f"Составьте {basic_word.count_subwords()} слов из слова {basic_word.get_word().upper()}")
    print(f"Слова должны быть не короче 3 букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите 'cтоп' или 'stop'")
    print(f"Поехали, ваше первое слово?")

    # Играется, пока пользователь угадал меньше слов, чем было загадано
    while player.count_subwords_used() < basic_word.count_subwords():
        user_input = input().strip().lower()
        # выход по запросу пользователя
        if user_input in ["stop", "стоп"]:
            break

        # слово короче 3 букв
        elif len(user_input) < 3:
            print("Слишком короткое слово")

        # нет в списке допустимых у basic_word
        elif not basic_word.has_subwords(user_input):
            print("Такое слово нельзя составить")

        # слово еще не было угадано
        elif player.has_subword_used(user_input):
            print("Такое слово уже угадано")

        else:
            print("Верно!")
            player.add_subword(user_input)

    print(f"Игра завершена, вы угадали {player.count_subwords_used()} слов!")


main()
