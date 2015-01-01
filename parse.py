# -*- coding: utf-8 -*-

from utils import Stack


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


class Parser(object):

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.tokens_stack = Stack()

    def parse(self):
        while 1:
            char = self.tokenizer.get()
            if char == "(":
                continue
            elif char in {'a', 'b'}:
                self.tokens_stack.push(char)
                continue
            elif char in {'*', '?', '+'}:
                self.tokens_stack.push(char)
                continue
