# -*- coding: utf-8 -*-

from random import randint


def random_string(l, alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Return a random string of length `l` using the provided alphabet."""
    alphabet_len = len(alphabet)
    new_string = ''
    for i in range(l):
        new_string += alphabet[randint(0, alphabet_len - 1)]
    return new_string
