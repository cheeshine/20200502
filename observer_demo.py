#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time   : 2020/5/2 16:23
# @Author : zhixiang
# @File   : observer_demo.py
import os
from abc import ABCMeta, abstractmethod


# 观察者接口
class Observer(object, metaclass=ABCMeta):

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


# 主题接口
class Subject(object, metaclass=ABCMeta):

    @abstractmethod
    def addObserver(self, o: Observer):
        pass

    @abstractmethod
    def removeObserver(self, o: Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

    @abstractmethod
    def setChanged(self):
        """用来标记状态已经改变的事实"""
        pass


# 可观察者类，实现主题接口
class Observable(Subject):

    def __init__(self):
        self.__observers: set = set()
        self.__changed: bool = False

    def addObserver(self, o: Observer):
        self.__observers.add(o)

    def removeObserver(self, o: Observer):
        if o in self.__observers:
            self.__observers.remove(o)

    def notifyObservers(self, *args, **kwargs):
        if self.__changed:
            for o in self.__observers:
                o: Observer
                o.update(self, *args, **kwargs)
            self.__changed = False

    def setChanged(self):
        self.__changed = True


# 展示接口
class DisplayElement(object, metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass


class WeatherData(Observable):

    def __init__(self):
        super(WeatherData, self).__init__()
        self.__temperature: float = 0.0
        self.__humidity: float = 0.0
        self.__pressure: float = 0.0

    def measurementsChanged(self):
        self.setChanged()
        self.notifyObservers()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementsChanged()

    def getTemperature(self) -> float:
        return self.__temperature

    def getHumidity(self) -> float:
        return self.__humidity

    def getPressure(self) -> float:
        return self.__pressure

    # WeatherData的其他方法


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, observable: Observable):
        self.__observable = observable
        self.__temperature: float = 0.0
        self.__humidity: float = 0.0
        self.__observable.addObserver(self)

    def update(self, obs: Observable, *args, **kwargs):
        if isinstance(obs, WeatherData):
            weatherData = obs
            self.__temperature = weatherData.getTemperature()
            self.__humidity = weatherData.getHumidity()
            self.display()

    def display(self):
        print('Current conditions: {temperature}F degrees and {humidity}% humidity'
              ''.format(temperature=self.__temperature, humidity=self.__humidity))


class WeatherStation(object):

    @staticmethod
    def main():
        weatherData = WeatherData()
        currentConditionsDisplay = CurrentConditionsDisplay(weatherData)

        weatherData.setMeasurements(80, 65, 30.4)
        weatherData.setMeasurements(82, 70, 29.2)
        weatherData.setMeasurements(78, 90, 29.2)


def main():
    WeatherStation.main()


if __name__ == '__main__':
    main()
