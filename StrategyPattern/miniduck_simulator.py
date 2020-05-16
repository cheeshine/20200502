#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/5 13:48
# @Author : zhixiang
# @File   : miniduck_simulator.py
import os
from duck import MallardDuck, ModelDuck


class MiniDuckSimulator(object):
    @staticmethod
    def main():
        mallard = MallardDuck()
        mallard.performQuack()
        mallard.performFly()

        model = ModelDuck()
        model.performQuack()
        model.performFly()


if __name__ == '__main__':
    MiniDuckSimulator.main()
