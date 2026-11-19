from copy import deepcopy
from abc import ABC, abstractmethod

## TODO enum typów Entry

class EntryInfo():
    def __init__(self,
                 type: str, ## EntryType
                 description: str,
                 authors: str,
                 year_published: str,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs) #
        self.type = type
        self.description = description
        self.authors = authors
        self.year_published = year_published

class Entry(ABC):
    def __init__(self, info: EntryInfo, lent_to: bool = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.info = info.copy()
        self.lent_to = lent_to

    def is_lent(self) -> bool:
        return not (self.lent_to is None)

class PhysicalEntry(Entry):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class DigitalEntry(Entry):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs) #

