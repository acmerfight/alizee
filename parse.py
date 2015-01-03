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


class MarkStruct(object):

    def __init__(self, atom_number=0, alt_number=0):
        self.atom_number = atom_number
        self.alt_number = alt_number


class ReParser(object):
    """
    将正则表达式转换为后缀表达式
    """

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.tokens_stack = Stack()
        self.alt_number = 0
        self.atom_number = 0
        self.mark_struct = MarkStruct()
        self.mark_list = []

    def re2post(self):
        while 1:
            char = self.tokenizer.get()
            if char is None:
                break
            elif char == "(":
                if self.atom_number > 1:
                    self.atom_number -= 1
                    self.tokens_stack.push(".")
                self.mark_struct.alt_number = self.alt_number
                self.mark_struct.atom_number = self.atom_number
                self.mark_list.append(self.mark_struct)
                self.mark_struct = MarkStruct()
                self.alt_number = 0
                self.atom_number = 0
                continue
            elif char == ")":
                while self.atom_number > 1:
                    self.tokens_stack.push(".")
                    self.atom_number -= 1
                while self.alt_number > 0:
                    self.tokens_stack.push("|")
                    self.alt_number -= 1
                mark_struct = self.mark_list.pop()
                self.alt_number = mark_struct.alt_number
                self.atom_number = mark_struct.atom_number
                self.atom_number += 1
                continue
            elif char == "|":
                while self.atom_number > 1:
                    self.tokens_stack.push(".")
                    self.atom_number -= 1
                self.alt_number += 1
                continue
            elif char in {"*", "+", "?"}:
                self.tokens_stack.push(char)
                continue
            else:
                if self.atom_number > 1:
                    self.atom_number -= 1
                    self.tokens_stack.push('.')
                self.tokens_stack.push(char)
                self.atom_number += 1
                continue
        while self.alt_number > 0:
            self.tokens_stack.push("|")
            self.alt_number -= 1
        return self.tokens_stack

tokenizer = Tokenizer("qx|(xab)")
post_stack = ReParser(tokenizer).re2post()
print post_stack
