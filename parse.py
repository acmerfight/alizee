# -*- coding: utf-8 -*-


class Tokenizer(object):

    def __init__(self, string):
        self.string = string
        self.index = 0
        self.__next()

    def __next(self):
        if self.index >= len(self.string):
            self.next_char = None
            return
        self.next_char = self.string[self.index]
        self.index += 1

    def get(self):
        this = self.next_char
        self.__next()
        return this
