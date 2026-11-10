from copy import deepcopy
from abc import ABC, abstractmethod

class Entry(ABC):
    def __init__(self, title: str, physical: bool, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._title = title
        self.is_physical = physical

    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, val: str) -> None:
        self._title = val.strip()


class BookEntry(Entry):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
