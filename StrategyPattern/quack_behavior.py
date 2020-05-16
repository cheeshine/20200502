#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/5 13:07
# @Author : zhixiang
# @File   : quack_behavior.py
import os
from abc import ABCMeta, abstractmethod


class QuackBehavior(object, metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        # 实现鸭子呱呱叫
        print('Quack!')


class Squeak(QuackBehavior):

    def quack(self):
        # 橡皮鸭子吱吱叫
        print('Squeak!')


class MuteQuack(QuackBehavior):

    def quack(self):
        # 什么都不做,不会叫
        print('<< Slience >>')
