import random
from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()

    if len(character) > 1:
        raise InvalidGuessedLetterException()

    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    answer = answer_word.lower()
    if character.lower() not in answer:
        return masked_word

    new_word = ''

    for answer_char, masked_char in zip(answer, masked_word):
        if character.lower() == answer_char:
            new_word += answer_char
        else:
            new_word += masked_char

    return new_word


def _is_game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()


def _is_game_lost(game):
    return game['remaining_misses'] <= 0


def _is_game_finished(game):
    return _is_game_lost(game) or _is_game_won(game)


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
