from abc import ABC, abstractmethod

class Main(ABC):

    def __init__(self, name):
        self._name = name
        self._price = -1
        self._buns= []
        self._patties = [] 
        self._others = []
