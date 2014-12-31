# -*- coding: utf-8 -*-


class Stack(list):

    def push(self, element):
        self.append(element)

    def pop(self):
        return super(Stack, self).pop()

