#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/2 15:29
# @Author : zhixiang
# @File   : interface.py
import os
from abc import ABCMeta, abstractmethod


class Payment(object, metaclass=ABCMeta):
    @abstractmethod  # 调用@abstractmethod规定子类必须有pay方法
    def pay(self, money):
        pass


class Wechatpay(Payment):
    def pay(self, money):
        print('微信支付了%s元' % money)


def main():
    obj = Wechatpay()
    obj.pay(10)  # 微信支付了10元


if __name__ == '__main__':
    main()
