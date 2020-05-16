#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/5 13:08
# @Author : zhixiang
# @File   : duck.py
import os
from abc import ABCMeta, abstractmethod

from fly_behavior import FlyBehavior, FlyNoWay, FlyWithWings, FlyRocketPowered
from quack_behavior import QuackBehavior, Quack, Squeak, MuteQuack


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
