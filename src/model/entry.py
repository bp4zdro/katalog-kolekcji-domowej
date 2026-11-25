from copy import copy, deepcopy
from abc import ABC, abstractmethod

## TODO enum typów Entry

class EntryInfo():
    def __init__(self,
                 type: str, ## EntryType
                 title: str,
                 description: str,
                 authors: str,
                 year_published: str,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs) #
        self.type = type
        self.title = title
        self.description = description
        self.authors = authors
        self.year_published = year_published

class Entry(ABC):
    def __init__(self, info: EntryInfo, lent_to: bool = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.info = copy(info)
        self.lent_to = lent_to

    def __str__(self):
        i = self.info
        s = ''

        if self.is_lent():
            s += '[LENT] '
        s += '('+i.year_published+' '+i.type+') '+i.authors+' - '+i.title 
        return s
    def is_lent(self) -> bool:
        return not (self.lent_to is None)

class PhysicalEntry(Entry):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()

class DigitalEntry(Entry):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()

