#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/2 23:42
# @Author : zhixiang
# @File   : decorator_demo.py
import os
from abc import ABCMeta, abstractmethod


class Beverage(object, metaclass=ABCMeta):

    def __init__(self):
        self._description: str = 'Unknown Beverage'

    def getDescription(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage, metaclass=ABCMeta):

    @abstractmethod
    def getDescription(self) -> str:
        pass


class Espresso(Beverage):

    def __init__(self):
        super(Espresso, self).__init__()
        self._description: str = 'Espresso'

    def cost(self) -> float:
        return 1.99



def main():
    print(Espresso().getDescription())


if __name__ == '__main__':
    main()
