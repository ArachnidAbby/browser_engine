'''PYOBE.engine

Defines the functionality for the `Engine` class who's primary purpose
is to be the entrance point into using the engine.
'''

__all__ = ['Engine']
__version__ = '0.1.0'
__authors__ = ['spidertyler2005']

from abc import ABC, abstractmethod
from dataclasses import dataclass
from queue import Queue
import threading


@dataclass
class _file:
    '''basic dataclass full of file information fetched from'''
    name: str
    url: str
    data: bytes
    filetype: str = 'HTML'


class Engine(ABC):
    '''Provides a starting point for developers to define functionality the engine will need.'''
    
    __slots__ = ['mouse_position', 'fetch_queue', 'data', 'resolution', 'img', '_lock']

    def __init__(self):
        self.mouse_position: tuple[int,int] = (0,0)
        self.fetch_queue = Queue()      
        self.data = list[_file]         # bytes

        self.resolution = tuple[int,int]

        #? could be useful to create an abstract Surface class
        #? may also be worth just storing things as a singlular byte string. We have all info required to index that.
        self.img = None         # formated as [[b'abc',b'abc',b'abc'],[b'abc',b'abc',b'abc'],[b'abc',b'abc',b'abc']] each byte corresponds to RGB

        self._lock = threading.Lock()


    
    @staticmethod
    @abstractmethod
    def fetch_data(url: str) -> bytes:
        '''implement fetching of data from a URL. This can be handled in a variety of ways'''
        ...

    def tick(self):
        '''Do all basic functions such as fetching data from the queue'''
        with self._lock:
            while not self.fetch_queue.empty:
                self.fetch_data()
    

    

