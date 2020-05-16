#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/4 18:09
# @Author : zhixiang
# @File   : _demo.py
import os
from abc import ABCMeta, abstractmethod


class FlyBehavior(object, metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(object, metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Duck(object, metaclass=ABCMeta):

    def __init__(self):
        self._flyBehavior: FlyBehavior = None
        self._quackBehavior: QuackBehavior = None

    def performQuack(self):
        self._quackBehavior.quack()

    def performFly(self):
        self._flyBehavior.fly()

    def swim(self):
        print("All ducks float, even decoys!")

    @abstractmethod
    def display(self):
        pass

    def setFlyBehavior(self, fb: FlyBehavior):
        self._flyBehavior = fb

    def setQuackBehavior(self, qb: QuackBehavior):
        self._quackBehavior = qb


class FlyWithWings(FlyBehavior):

    def fly(self):
        # 实现鸭子飞行
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):

    def fly(self):
        # 什么都不做，不会飞
        print("I can't fly!")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


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


class MallardDuck(Duck):

    def __init__(self):
        super(MallardDuck, self).__init__()
        self._quackBehavior = Quack()
        self._flyBehavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):

    def __init__(self):
        super(ModelDuck, self).__init__()
        self._flyBehavior = FlyNoWay()
        self._quackBehavior = Quack()

    def display(self):
        print("I'm a model duck!")


class MiniDuckSimulator(object):
    @staticmethod
    def main():
        mallard = MallardDuck()
        mallard.performQuack()
        mallard.performFly()

        model = ModelDuck()
        model.performQuack()
        model.performFly()


def main():
    MiniDuckSimulator.main()


if __name__ == '__main__':
    # main()
    print(__name__)
    print(__file__)
    print(os.__file__)
    print(os.__doc__)
    import time
    print(time.__doc__)
    print(time.__all__)


