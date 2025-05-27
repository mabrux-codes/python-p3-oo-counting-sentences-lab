#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self.value = value  # use setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        parts = re.split(r'[.!?]', self._value)
        sentences = [s for s in parts if s.strip()]
        return len(sentences)