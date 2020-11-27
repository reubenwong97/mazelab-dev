from abc import ABC
from abc import abstractmethod

from collections import namedtuple
import numpy as np

from .object import Object
from copy import deepcopy

class BaseMaze(ABC):
    def __init__(self, **kwargs):
        objects = self.make_objects()
        assert all([isinstance(obj, Object) for obj in objects])
        self.objects = namedtuple('Objects', map(lambda x: x.name, objects), defaults=objects)()
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @property
    @abstractmethod
    def size(self):
        r"""Returns evironment shape"""
        pass

    @property
    @abstractmethod
    def inner_size(self):
        r"""Returns a height width pair"""
        pass

    @abstractmethod
    def make_objects(self):
        r"""Returns a list of defined objects. """
        pass
    
    def _convert(self, x, name):
        for obj in self.objects:
            pos = np.asarray(obj.positions)
            # Puts the corresponding value/rgb/impassable at the positions of objects
            x[pos[:, 0], pos[:, 1]] = getattr(obj, name, None)
        return x
    
    def _convert_specific(self, x, name, spec_type=None):
        cp_objects = deepcopy(self.objects)
        print(type(cp_objects))
        if spec_type == 'robber':
            cp_objects.remove(police1)
            cp_objects.remove(police2)
        elif spec_type == 'police':
            cp_objects.remove(goal)
        for obj in cp_objects:
            pos = np.asarray(obj.positions)
            x[pos[:, 0], pos[:, 1]] = getattr(obj, name, None)
        return x

    def to_name(self):
        x = np.empty(self.inner_size, dtype=object)
        return self._convert(x, 'name')
    
    def to_value(self):
        x = np.empty(self.inner_size, dtype=int)
        return self._convert(x, 'value')
    
    def to_specific_rgb(self, spec_type):
        x = np.empty((*self.inner_size, 3), dtype=int)
        return self._convert_specific(x, 'rgb', spec_type)

    def to_rgb(self):
        x = np.empty((*self.inner_size, 3), dtype=np.uint8)
        return self._convert(x, 'rgb')
    
    def to_impassable(self):
        x = np.empty(self.inner_size, dtype=bool)
        return self._convert(x, 'impassable')
    
    def __repr__(self):
        return f'{self.__class__.__name__}{self.size}'
