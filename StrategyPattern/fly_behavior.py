#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/5 13:05
# @Author : zhixiang
# @File   : fly_behavior.py
import os
from abc import ABCMeta, abstractmethod


class FlyBehavior(object, metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


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
